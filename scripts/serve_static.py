#!/usr/bin/env python3
"""Serve static Stonewall web surfaces from a target directory."""

from __future__ import annotations

import argparse
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Serve static Stonewall surfaces.")
    parser.add_argument("--directory", default="docs", help="Directory to serve (default: docs)")
    parser.add_argument("--host", default="0.0.0.0", help="Bind host (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="Default port when PORT env is unset.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    directory = Path(args.directory).resolve()
    if not directory.exists() or not directory.is_dir():
        raise SystemExit(f"Static directory not found: {directory}")

    port = int(os.environ.get("PORT", args.port))
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    server = ThreadingHTTPServer((args.host, port), handler)

    print(f"Serving {directory} on http://{args.host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
