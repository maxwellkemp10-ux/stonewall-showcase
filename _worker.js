export default {
  async fetch(request, env) {
    const assetResponse = await env.ASSETS.fetch(request);
    if (assetResponse.status === 404) {
      const url = new URL(request.url);
      url.pathname = "/";
      return env.ASSETS.fetch(new Request(url.toString(), request));
    }
    return assetResponse;
  },
};
