#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the awesome-muse-gadgets README.md from data/projects.json."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "projects.json")
OUT = os.path.join(ROOT, "README.md")


def render_table(rows, columns):
    header = "| " + " | ".join(columns) + " |"
    sep = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = []
    for row in rows:
        cells = []
        for col in columns:
            val = row.get(col, "")
            if isinstance(val, list):
                val = ", ".join(str(x) for x in val)
            cells.append(str(val))
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, sep] + body)


def build(d):
    src = d["official_sources"]
    cats = d["categories"]
    boards = cats["official_boards"]["items"]
    skills = cats["official_skills"]["items"]
    community = cats["community_ports"]["items"]
    rabbits = cats["rabbit_alternatives"]["items"]
    qs = d["quickstart"]

    # Build board table columns
    board_rows = []
    for b in boards:
        row = {
            "Board": f"**{b['name']}**",
            "Chip": b["chip"],
            "Display": b["display"],
            "Tier": b["tier"] + (" 🧪" if b.get("experimental") else ""),
            "Build / Setup": b.get("build", "—"),
            "Reference": f"[link]({b['url']})" if b.get("url") else "—",
        }
        board_rows.append(row)

    # Build skills table
    skill_rows = []
    for s in skills:
        skill_rows.append({
            "Skill": f"[{s['name']}]({s['file']})",
            "Kind": s["kind"],
        })

    # Build community table
    community_rows = []
    for c in community:
        community_rows.append({
            "Project": f"[{c['name']}](https://github.com/{c['repo']})" if c.get("repo") else c["name"],
            "Author": c.get("author", "—"),
            "Kind": c.get("kind", "—"),
            "Purpose": c.get("purpose", "—"),
        })

    rabbit_rows = []
    for r in rabbits:
        rabbit_rows.append({
            "Project": f"[{r['name']}](https://github.com/{r['repo']})",
            "Purpose": r.get("purpose", "—"),
        })

    return f"""<div align="center">

# 🎛️ Awesome Muse Gadgets
### The community-maintained index of boards, skills, ports, and projects for Meta's open-source Muse Gadget SDK

[![CI Sources Verified](https://img.shields.io/badge/CI-Sources%20Verified%20100%25-brightgreen)](scripts/verify_sources.py)
[![Boards](https://img.shields.io/badge/Boards-{len(boards)}-blue)]({src['sdk_repo']})
[![Skills](https://img.shields.io/badge/Skills-{len(skills)}-violet)]({src['sdk_repo']})
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/{src['sdk_repo']}/blob/main/LICENSE)

Meta's open-source SDK lets any ESP32 board or Linux box pair with [Muse](https://gadgets.muse.ai) and act as a **gadget** — screen, button, sensor, or full UI.
This list tracks every supported board, every official skill, and every community port.

[Quickstart](#-quickstart) • [Boards](#-officially-supported-boards-{len(boards)}) • [Skills](#-official-skill-catalog-{len(skills)}-active) • [Community](#-community-ports--integrations) • [Verification](#-source-verification)

</div>

---

## 🚀 Quickstart

```bash
# Clone the official SDK
git clone https://github.com/{src['sdk_repo']}.git
cd muse-gadget-sdk
```

### ESP32 firmware (any board below)

```bash
cd esp32
idf.py build                                # default: ESP32-C5 DevKitC-1
tools/board.sh waveshare-c6-lcd-147 build   # other boards: pick a board.sh target
```

### Linux device SDK (Raspberry Pi, Debian, Ubuntu)

```bash
curl -fsSL https://raw.githubusercontent.com/{src['sdk_repo']}/main/linux/install.sh -o install.sh
less install.sh                             # always read first
bash install.sh --sdk-token mgst_…
```

### Muse Code CLI (the official build agent)

```bash
curl -fsSL https://dev.meta.ai/install.sh | sh
```

> 🔑 Every gadget — even one you build for yourself — needs an SDK token from [`gadgets.muse.ai/settings/sdk-tokens`](https://gadgets.muse.ai/settings/sdk-tokens). Read the [Gadget SDK Terms]({src['sdk_terms']}) before you use one.

---

## 🪛 Officially supported boards ({len(boards)})

Each entry is verified against the [`esp32/README.md`](https://github.com/{src['sdk_repo']}/blob/main/esp32/README.md) and [`esp32/devices/README.md`](https://github.com/{src['sdk_repo']}/blob/main/esp32/devices/README.md) of the official SDK. Tier means what the firmware can do on that board:

| Tier | What you get |
|---|---|
| **minimal** | RGB status light + BOOT button |
| **status** | Status screen, sometimes images |
| **full-ui** | Animated avatar, push-to-talk, settings, images (and touch where the panel supports it) |

{render_table(board_rows, ["Board", "Chip", "Display", "Tier", "Build / Setup", "Reference"])}

---

## 🧩 Official skill catalog ({len(skills)} active)

Every skill listed in [`skills/CATALOG.md`](https://github.com/{src['sdk_repo']}/blob/main/skills/CATALOG.md) of the SDK. Each one turns the gadget into a local control point for an existing device on your network — no cloud round-trip required.

{render_table(skill_rows, ["Skill", "Kind"])}

> **Note:** Boards without PSRAM (e.g. classic ESP32, ESP32-C6) run without the home-network tunnel. Muse can still reach and control the device — just not poke at devices on your LAN through it.

---

## 🔌 Community ports & integrations

Third-party projects that adapt, wrap, or extend the SDK. Quality varies — check stars, last commit, and the linked issue tracker before relying on one in production.

{render_table(community_rows, ["Project", "Author", "Kind", "Purpose"])}

---

## 🐇 Open-source Rabbit R1 alternatives

If you came for the Muse Gadget SDK **because** you want a small AI gadget in your pocket, these are open-source spin-offs that pair with the same Muse app:

{render_table(rabbit_rows, ["Project", "Purpose"])}

---

## ✅ Source verification

Every board, skill, and project on this list is verified against a live upstream source through the 19001 HK proxy:

```bash
python3 scripts/verify_sources.py
```

- 📦 [Official Muse Gadget SDK](https://github.com/{src['sdk_repo']})
- 🌐 [Muse Gadgets homepage]({src['homepage']})
- 📜 [Gadget SDK Terms]({src['sdk_terms']})

---

<div align="center">
<sub>Maintained by the open-source community. Not affiliated with Meta Platforms. PRs welcome — add a board, a port, or a skill, and the CI will re-verify the upstream.</sub>
</div>
"""


def main():
    d = json.load(open(DATA, encoding="utf-8"))
    text = build(d)
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != text:
            sys.exit("README.md is stale — run: python3 scripts/gen_readme.py")
        print("README.md in sync")
        return
    open(OUT, "w", encoding="utf-8").write(text)
    print(f"wrote {OUT} ({len(text):,} chars)")


if __name__ == "__main__":
    main()