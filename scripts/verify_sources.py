#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify all referenced sources in data/projects.json are live and contain expected tokens.

Runs through the 19001 HK proxy. Used as a CI gate so a stale README is impossible.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

PROXY = os.environ.get("CLOAK_PROXY", "http://127.0.0.1:19001")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "projects.json")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


def opener():
    return urllib.request.build_opener(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))


def check(op, url, expected_token):
    """Fetch a URL and confirm `expected_token` is present in the body."""
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    try:
        with op.open(req, timeout=40) as r:
            text = r.read().decode("utf-8", "replace")
            clean = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text))
            if expected_token.lower() in clean.lower():
                return r.status, "OK"
            return r.status, "STALE"
    except urllib.error.HTTPError as e:
        return e.code, "HTTP_ERROR"
    except Exception as e:
        return 0, f"ERR: {e}"


def main():
    op = opener()
    d = json.load(open(DATA, encoding="utf-8"))
    sources = d.get("verification_sources", [])
    failed = False
    for s in sources:
        status, res = check(op, s["url"], s["expected_token"])
        marker = "✅" if res == "OK" else "🔴"
        print(f"{marker} [{res:<5}] {status:<3} | {s['name'][:38]:<40} | {s['url']}")
        if res != "OK":
            failed = True
    if failed:
        sys.exit(1)
    # 🔴 报出**源数**（2026-10-15 加）：原来只印一句「verified successfully」，
    #    下游无法从这个绿里读出"验了几个" ⇒ 空清单也能印出一模一样的绿。
    #    ⚠️ 实况：轮动核验器 2026-10-15 把本仓列为「绿但报不出源数」——
    #       那不是它误报，是**这句话当时确实不可核对**。
    if not sources:
        sys.exit("No sources found — an empty list is a pass that proves nothing. Failing.")
    print(f"\nAll {len(sources)} sources verified successfully.")


if __name__ == "__main__":
    main()