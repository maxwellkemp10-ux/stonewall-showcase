/**
 * QB1 Command Portal — static demo with local preferences (localStorage).
 */

const STORAGE_KEY = "stonewall_portal_settings_v1";

const defaultSettings = () => ({
  hourlyRate: 200,
  currency: "USD",
  density: "comfortable",
  showMatterIds: true,
  showRunwayBadges: true,
  reducedMotion: false,
});

function loadSettings() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultSettings();
    const parsed = JSON.parse(raw);
    return { ...defaultSettings(), ...parsed };
  } catch {
    return defaultSettings();
  }
}

function saveSettings(settings) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(settings));
}

function formatMoney(amount, currency) {
  try {
    return new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: currency || "USD",
      maximumFractionDigits: 0,
    }).format(amount);
  } catch {
    return `$${Math.round(amount)}`;
  }
}

function formatNumber(n) {
  return new Intl.NumberFormat("en-US").format(n);
}

const state = {
  settings: loadSettings(),
  data: {},
};

function applyGlobalSettings() {
  const { density, reducedMotion } = state.settings;
  document.body.classList.toggle("density-compact", density === "compact");
  document.body.classList.toggle("reduce-motion", reducedMotion);
  if (reducedMotion) {
    document.documentElement.style.scrollBehavior = "auto";
  }
}

function showToast(message) {
  let el = document.getElementById("portal-toast");
  if (!el) {
    el = document.createElement("div");
    el.id = "portal-toast";
    el.className = "toast";
    document.body.appendChild(el);
  }
  el.textContent = message;
  el.classList.add("is-visible");
  window.clearTimeout(showToast._t);
  showToast._t = window.setTimeout(() => el.classList.remove("is-visible"), 2200);
}

function node(tagName, options = {}, children = []) {
  const el = document.createElement(tagName);
  if (options.className) el.className = options.className;
  if (options.text !== undefined) el.textContent = String(options.text);
  const childList = Array.isArray(children) ? children : [children];
  childList.forEach((child) => {
    el.appendChild(typeof child === "string" ? document.createTextNode(child) : child);
  });
  return el;
}

function metric(value, label) {
  return node("article", { className: "metric" }, [
    node("strong", { text: value }),
    node("span", { text: label }),
  ]);
}

function tableRow(cells) {
  const tr = node("tr");
  cells.forEach((cell) => {
    const td = node("td", { className: cell.className || "" });
    if (cell.child) td.appendChild(cell.child);
    else td.textContent = String(cell.text ?? "");
    tr.appendChild(td);
  });
  return tr;
}

async function loadData() {
  const files = [
    "metrics.json",
    "cases.json",
    "deadlines.json",
    "artifacts.json",
    "playbooks.json",
    "patterns.json",
    "cast.json",
    "billing.json",
  ];
  const base = new URL("data/", window.location.href);
  const out = {};
  await Promise.all(
    files.map(async (name) => {
      const res = await fetch(new URL(name, base), { cache: "no-store" });
      if (!res.ok) throw new Error(`Failed to load ${name}`);
      out[name.replace(".json", "")] = await res.json();
    }),
  );
  state.data = out;
}

function renderDashboard() {
  const m = state.data.metrics || {};
  const root = document.getElementById("dash-metrics");
  if (!root) return;
  root.replaceChildren(
    metric(formatNumber(m.cataloged_artifacts ?? 0), "cataloged artifacts"),
    metric(formatNumber(m.active_matters ?? 0), "active matters"),
    metric(formatNumber(m.pattern_tags ?? 0), "pattern tags"),
    metric(formatNumber(m.artifact_classes ?? 0), "artifact classes"),
  );

  const glance = document.getElementById("dash-glance");
  if (glance) {
    glance.replaceChildren(
      glanceItem(
        `${m.urgent_runway ?? 0} matters inside urgent runway`,
        "Deposition prep, mediation staging, and deadline confirmation surfaced in the board.",
      ),
      glanceItem(
        `${m.packets_ready ?? 0} report packets nearly ready`,
        "Chronology aligned, records pulled, and damages notes staged for downstream workflow.",
      ),
      glanceItem(
        `${m.live_threads ?? 0} live witness-prep thread active`,
        "Prior statements, chronology gaps, and issue clusters stay query-ready.",
      ),
    );
  }
}

function glanceItem(title, description) {
  return node("li", {}, [
    node("strong", { text: title }),
    node("br"),
    node("span", { text: description }),
  ]);
}

function renderCases() {
  const tbody = document.querySelector("#cases-table tbody");
  if (!tbody) return;
  const matters = state.data.cases?.matters || [];
  const { showMatterIds } = state.settings;
  tbody.replaceChildren(
    ...matters.map((row) =>
      tableRow([
        { className: "mono", text: showMatterIds ? row.id : "—" },
        { text: row.label },
        { text: row.posture },
        { text: row.runway },
        { child: node("span", { className: "chip", text: row.status }) },
      ]),
    ),
  );
}

function renderDeadlines() {
  const tbody = document.querySelector("#deadlines-table tbody");
  if (!tbody) return;
  const items = state.data.deadlines?.items || [];
  const { showMatterIds, showRunwayBadges } = state.settings;
  tbody.replaceChildren(
    ...items.map((row) => {
      const matter = showMatterIds ? row.matter : "Matter";
      const band = showRunwayBadges ? row.band : "scheduled";
      const chipClass =
        band === "urgent" ? "chip chip--urgent" : band === "soon" ? "chip chip--soon" : "chip chip--planned";
      return tableRow([
        { className: "mono", text: row.date },
        { className: "mono", text: matter },
        { text: row.label },
        { child: node("span", { className: chipClass, text: band }) },
      ]);
    }),
  );
}

function renderArtifacts() {
  const tbody = document.querySelector("#artifacts-table tbody");
  if (!tbody) return;
  const arts = state.data.artifacts?.artifacts || [];
  const { showMatterIds } = state.settings;
  tbody.replaceChildren(
    ...arts.map((a) =>
      tableRow([
        { className: "mono", text: a.id },
        { text: a.type },
        { className: "mono", text: showMatterIds ? a.matter : "—" },
        { text: a.summary },
        { className: "mono", text: a.date },
      ]),
    ),
  );
}

function renderPatterns() {
  const root = document.getElementById("pattern-list");
  if (!root) return;
  const patterns = state.data.patterns?.patterns || [];
  root.replaceChildren(
    ...patterns.map((p) => {
      const meta = node("p", { text: `${p.band} · ${formatNumber(p.hits)} hits` });
      meta.style.margin = "8px 0 0";
      meta.style.fontSize = "13px";
      meta.style.color = "var(--muted)";
      return node("article", { className: "pattern-card" }, [
        node("code", { text: p.code }),
        meta,
      ]);
    }),
  );
}

function renderPlaybooks() {
  const playbooks = state.data.playbooks || {};
  const modules = Array.isArray(playbooks.modules) ? playbooks.modules : [];
  const pipeline = Array.isArray(playbooks.pipeline) ? playbooks.pipeline : [];
  const qc = Array.isArray(playbooks.qc_checks) ? playbooks.qc_checks : [];
  const readiness = Array.isArray(playbooks.readiness_lanes) ? playbooks.readiness_lanes : [];

  const modulesRoot = document.getElementById("playbook-modules");
  if (modulesRoot) {
    modulesRoot.replaceChildren(
      ...modules.map((m) =>
        node("article", { className: "playbook-card" }, [
          node("div", { className: "playbook-card__head" }, [
            node("span", { className: "playbook-layer", text: m.layer || "Layer" }),
            node("span", { className: "chip", text: m.status || "active" }),
          ]),
          node("h3", { text: m.title || "Untitled module" }),
          node("p", { text: m.summary || "" }),
          node("code", { className: "playbook-signal", text: m.signal || "" }),
        ]),
      ),
    );
  }

  const pipeRoot = document.getElementById("playbook-pipeline");
  if (pipeRoot) {
    pipeRoot.replaceChildren(
      ...pipeline.map((step, idx) => {
        if (typeof step === "string") {
          return node("li", { className: "pipeline-step" }, [
            node("strong", { text: `Step ${idx + 1}` }),
            node("span", { text: step }),
          ]);
        }
        return node("li", { className: "pipeline-step" }, [
          node("strong", { text: step.step || `Step ${idx + 1}` }),
          node("span", { text: step.outcome || "" }),
        ]);
      }),
    );
  }

  const qcRoot = document.getElementById("playbook-qc");
  if (qcRoot) {
    qcRoot.replaceChildren(
      ...qc.map((item) => {
        const title = item.check || item.name || "Check";
        const desc = item.note || item.description || "";
        return node("li", {}, [
          node("strong", { text: title }),
          node("br"),
          node("span", { text: desc }),
        ]);
      }),
    );
  }

  const readinessRoot = document.getElementById("playbook-readiness");
  if (readinessRoot) {
    readinessRoot.replaceChildren(
      ...readiness.map((item) => {
        const title = item.lane || item.name || "Lane";
        const desc = item.value || item.description || "";
        return node("li", {}, [
          node("strong", { text: title }),
          node("br"),
          node("span", { text: desc }),
        ]);
      }),
    );
  }
}

function renderCast() {
  const root = document.getElementById("cast-list");
  if (!root) return;
  const chars = state.data.cast?.characters || [];
  root.replaceChildren(
    ...chars.map((c) => {
      const note = node("p", { text: c.note });
      note.style.margin = "6px 0 0";
      note.style.fontSize = "14px";
      note.style.color = "var(--muted)";
      const matters = node("p");
      matters.style.margin = "10px 0 0";
      matters.style.fontSize = "13px";
      matters.appendChild(node("span", { className: "chip", text: `${formatNumber(c.matters)} matters` }));
      return node("article", { className: "cast-card" }, [
        node("div", { className: "cast-meta", text: c.role }),
        node("h3", { text: c.alias }),
        note,
        matters,
      ]);
    }),
  );
}

function renderBilling() {
  const b = state.data.billing || {};
  const rate = Number(state.settings.hourlyRate) || Number(b.default_hourly) || 200;
  const currency = state.settings.currency || b.currency || "USD";
  const lineItems = b.line_items || [];
  const tbody = document.querySelector("#billing-table tbody");
  const totalHours = lineItems.reduce((s, row) => s + (Number(row.hours) || 0), 0);
  const totalAmt = totalHours * rate;

  const rateDisplay = document.getElementById("settings-rate-display");
  if (rateDisplay) rateDisplay.textContent = `${formatMoney(rate, currency)}/hr`;

  const billRateEl = document.getElementById("billing-rate-display");
  if (billRateEl) billRateEl.textContent = `${formatMoney(rate, currency)}/hr`;

  const summary = document.getElementById("billing-summary");
  if (summary) {
    summary.replaceChildren(
      node("p", { className: "billing-total", text: formatMoney(totalAmt, currency) }),
      node(
        "p",
        {
          className: "billing-note",
          text: `${formatNumber(totalHours)} billable hours × ${formatMoney(rate, currency)}/hr (demo math — preferences only)`,
        },
      ),
    );
  }

  if (tbody) {
    tbody.replaceChildren(
      ...lineItems.map((row) =>
        tableRow([
          { className: "mono", text: state.settings.showMatterIds ? row.matter : "Matter" },
          { text: row.phase },
          { className: "mono", text: row.hours },
          { className: "mono", text: formatMoney(row.hours * rate, currency) },
        ]),
      ),
    );
  }
}

function populateSettingsForm() {
  const s = state.settings;
  const hourly = document.getElementById("set-hourly");
  const currency = document.getElementById("set-currency");
  const density = document.getElementById("set-density");
  const matterIds = document.getElementById("set-matter-ids");
  const runway = document.getElementById("set-runway");
  const motion = document.getElementById("set-motion");

  if (hourly) hourly.value = String(s.hourlyRate);
  if (currency) currency.value = s.currency;
  if (density) density.value = s.density;
  if (matterIds) matterIds.checked = !!s.showMatterIds;
  if (runway) runway.checked = !!s.showRunwayBadges;
  if (motion) motion.checked = !!s.reducedMotion;
}

function bindSettingsForm() {
  const form = document.getElementById("settings-form");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const hourly = document.getElementById("set-hourly");
    const currency = document.getElementById("set-currency");
    const density = document.getElementById("set-density");
    const matterIds = document.getElementById("set-matter-ids");
    const runway = document.getElementById("set-runway");
    const motion = document.getElementById("set-motion");

    state.settings = {
      ...state.settings,
      hourlyRate: Math.max(0, Number(hourly?.value) || 0),
      currency: currency?.value || "USD",
      density: density?.value || "comfortable",
      showMatterIds: !!matterIds?.checked,
      showRunwayBadges: !!runway?.checked,
      reducedMotion: !!motion?.checked,
    };
    saveSettings(state.settings);
    applyGlobalSettings();
    renderCases();
    renderDeadlines();
    renderArtifacts();
    renderBilling();
    populateSettingsForm();
    showToast("Preferences saved locally in this browser.");
  });

  document.getElementById("settings-reset")?.addEventListener("click", () => {
    state.settings = defaultSettings();
    saveSettings(state.settings);
    applyGlobalSettings();
    populateSettingsForm();
    renderCases();
    renderDeadlines();
    renderArtifacts();
    renderBilling();
    showToast("Reset to defaults.");
  });

  document.getElementById("settings-export")?.addEventListener("click", () => {
    const blob = new Blob([JSON.stringify(state.settings, null, 2)], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "stonewall-portal-settings.json";
    a.click();
    URL.revokeObjectURL(a.href);
    showToast("Downloaded settings JSON.");
  });
}

function switchPage(name) {
  document.querySelectorAll(".page").forEach((p) => {
    p.classList.toggle("is-visible", p.id === `page-${name}`);
  });
  document.querySelectorAll(".portal-nav button[data-page]").forEach((btn) => {
    btn.classList.toggle("is-active", btn.dataset.page === name);
  });
  if (name === "billing" || name === "dashboard") renderBilling();
  if (name === "playbooks") renderPlaybooks();
}

function bindNav() {
  document.querySelectorAll(".portal-nav button[data-page]").forEach((btn) => {
    btn.addEventListener("click", () => switchPage(btn.dataset.page));
  });
}

async function init() {
  applyGlobalSettings();
  bindNav();
  bindSettingsForm();

  try {
    await loadData();
  } catch (err) {
    console.error(err);
    showToast("Could not load portal data JSON.");
    return;
  }

  renderDashboard();
  renderCases();
  renderDeadlines();
  renderArtifacts();
  renderPlaybooks();
  renderPatterns();
  renderCast();
  renderBilling();
  populateSettingsForm();

  const initial = new URLSearchParams(window.location.search).get("page");
  const allowed = [
    "dashboard",
    "cases",
    "deadlines",
    "artifacts",
    "playbooks",
    "patterns",
    "characters",
    "billing",
    "settings",
  ];
  switchPage(allowed.includes(initial) ? initial : "dashboard");
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
