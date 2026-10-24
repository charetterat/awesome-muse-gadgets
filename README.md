<div align="center">

# 🎛️ Awesome Muse Gadgets
### The community-maintained index of boards, skills, ports, and projects for Meta's open-source Muse Gadget SDK

[![CI Sources Verified](https://img.shields.io/badge/CI-Sources%20Verified%20100%25-brightgreen)](scripts/verify_sources.py)
[![Boards](https://img.shields.io/badge/Boards-24-blue)](facebookincubator/muse-gadget-sdk)
[![Skills](https://img.shields.io/badge/Skills-43-violet)](facebookincubator/muse-gadget-sdk)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/facebookincubator/muse-gadget-sdk/blob/main/LICENSE)
[![Last updated](https://img.shields.io/badge/Last%20updated-2026-10-24-green)]()

Meta's open-source SDK lets any ESP32 board or Linux box pair with [Muse](https://gadgets.muse.ai) and act as a **gadget** — screen, button, sensor, or full UI.
This list tracks every supported board, every official skill, and every community port.

[Quickstart](#-quickstart) • [Boards](#-officially-supported-boards-24) • [Skills](#-official-skill-catalog-43-active) • [Community](#-community-ports--integrations) • [Verification](#-source-verification)

</div>

---

## 🚀 Quickstart

```bash
# Clone the official SDK
git clone https://github.com/facebookincubator/muse-gadget-sdk.git
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
curl -fsSL https://raw.githubusercontent.com/facebookincubator/muse-gadget-sdk/main/linux/install.sh -o install.sh
less install.sh                             # always read first
bash install.sh --sdk-token mgst_…
```

### Muse Code CLI (the official build agent)

```bash
curl -fsSL https://dev.meta.ai/install.sh | sh
```

> 🔑 Every gadget — even one you build for yourself — needs an SDK token from [`gadgets.muse.ai/settings/sdk-tokens`](https://gadgets.muse.ai/settings/sdk-tokens). Read the [Gadget SDK Terms](https://gadgets.muse.ai/sdk-terms) before you use one.

---

## 🪛 Officially supported boards (24)

Each entry is verified against the [`esp32/README.md`](https://github.com/facebookincubator/muse-gadget-sdk/blob/main/esp32/README.md) and [`esp32/devices/README.md`](https://github.com/facebookincubator/muse-gadget-sdk/blob/main/esp32/devices/README.md) of the official SDK. Tier means what the firmware can do on that board:

| Tier | What you get |
|---|---|
| **minimal** | RGB status light + BOOT button |
| **status** | Status screen, sometimes images |
| **full-ui** | Animated avatar, push-to-talk, settings, images (and touch where the panel supports it) |

| Board | Chip | Display | Tier | Build / Setup | Reference |
| --- | --- | --- | --- | --- | --- |
| **ESP32-C5 DevKitC-1** | ESP32-C5 | RGB status light | minimal | idf.py build | [link](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c5/esp32-c5-devkitc-1/index.html) |
| **ESP32-C6 devkit (no PSRAM)** | ESP32-C6 | RGB status light | minimal | tools/board.sh c6-nopsram build | [link](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitc-1/user_guide.html) |
| **Espressif ESP32-S3-DevKitC-1** | ESP32-S3 | RGB status light | minimal | tools/board.sh espressif-s3-devkitc-1 build | [link](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html) |
| **ideaspark ESP32 with 1.9" display** | ESP32 | 1.9" 170×320 LCD | status | tools/board.sh ideaspark build | — |
| **Waveshare ESP32-C6-LCD-1.47** | ESP32-C6 | 1.47" 172×320 LCD | status | tools/board.sh waveshare-c6-lcd-147 build | [link](https://www.waveshare.com/wiki/ESP32-C6-LCD-1.47) |
| **Seeed SenseCAP Indicator** | ESP32-S3 | 4" 480×480 LCD | status | tools/board.sh sensecap-indicator build | [link](https://wiki.seeedstudio.com/SenseCAP_Indicator_Get_Started/) |
| **Seeed reTerminal E1001** | ESP32-S3 | 7.5" 800×480 e-paper B/W | status | tools/board.sh reterminal-e1001 build | [link](https://wiki.seeedstudio.com/getting_started_with_reterminal_e1001/) |
| **Seeed reTerminal E1002** | ESP32-S3 | 7.3" 800×480 e-paper Spectra 6 | status | tools/board.sh reterminal-e1002 build | [link](https://wiki.seeedstudio.com/reterminal_e10xx_with_esphome/) |
| **Home Assistant Voice Preview Edition** | ESP32-S3 | 12-LED ring | status | tools/board.sh home-assistant-voice build | [link](https://www.home-assistant.io/voice-pe/) |
| **Seeed reSpeaker Lite (XIAO ESP32-S3)** | ESP32-S3 | single RGB LED | experimental | See devices/seeed-respeaker-lite.md | — |
| **Waveshare ESP32-S3-Touch-AMOLED-1.75C** | ESP32-S3 | 1.75" 466×466 round AMOLED, touch | full-ui | — | [link](https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-1.75C) |
| **Waveshare ESP32-S3-Touch-AMOLED-1.75** | ESP32-S3 | 1.75" 466×466 round AMOLED, touch | full-ui | — | [link](https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-1.75) |
| **Espressif ESP32-S3-BOX-3** | ESP32-S3 | 2.4" 320×240 LCD, touch | full-ui | — | [link](https://github.com/espressif/esp-box) |
| **AIPI Lite** | ESP32-S3 | 128×128 LCD | full-ui | — | [link](https://github.com/78/xiaozhi-esp32/tree/main/main/boards/xorigin/aipi-lite) |
| **Waveshare ESP32-C6-Touch-AMOLED-1.8** | ESP32-C6 | 1.8" 368×448 AMOLED, touch | full-ui | — | [link](https://docs.waveshare.com/ESP32-C6-Touch-AMOLED-1.8) |
| **Seeed SenseCAP Watcher** | ESP32-S3 | 1.45" 412×412 round LCD, touch | full-ui | — | [link](https://wiki.seeedstudio.com/watcher/) |
| **M5Stack Cardputer ADV** | ESP32-S3 | 1.14" 240×135 LCD | full-ui 🧪 | tools/muse/board.sh build cardputer-adv | — |
| **M5Stack StickS3** | ESP32-S3 | 1.14" 135×240 LCD | full-ui | — | — |
| **M5Stack StopWatch** | ESP32-S3 | 1.75" 466×466 round AMOLED, touch | full-ui | — | — |
| **M5Stack CoreS3** | ESP32-S3 | 2" 320×240 LCD, touch | full-ui | — | — |
| **Guition JC3248W535** | ESP32-S3 | 3.5" 320×480 IPS, touch | full-ui | tools/muse/board.sh build jc3248w535 | — |
| **M5Stack StickC Plus2** | ESP32 | 1.14" 135×240 LCD | full-ui | — | — |
| **M5Stack Core2 v1.0** | ESP32 | 2.0" 320×240 touch LCD | full-ui | tools/muse/board.sh build core2 | — |
| **Freenove FNK0104B** | ESP32-S3 | 2.8" 240×320 touch LCD | full-ui | tools/muse/board.sh build fnk0104b | — |

---

## 🧩 Official skill catalog (43 active)

Every skill listed in [`skills/CATALOG.md`](https://github.com/facebookincubator/muse-gadget-sdk/blob/main/skills/CATALOG.md) of the SDK. Each one turns the gadget into a local control point for an existing device on your network — no cloud round-trip required.

| Skill | Kind |
| --- | --- |
| [Google Cast](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-google-cast) | shared protocol |
| [Lutron Smart Bridges](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-lutron-smart-bridges) | lights |
| [Shelly Gen 4 plugs](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-shelly-plugs) | plugs |
| [Philips Hue bridges](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-philips-hue-bridges) | lights |
| [Elgato Key Light](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-elgato-key-light) | lights |
| [Meross smart plugs](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-meross-smart-plugs) | plugs |
| [TP-Link Kasa EP10](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-tplink-kasa-ep10) | plugs |
| [TP-Link Kasa EP25](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-tplink-kasa-ep25) | plugs |
| [Apple HomePod mini](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-apple-homepod-mini) | speaker |
| [Apple TV 4K](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-apple-tv-4k) | tv |
| [Freebox Player Pop](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-freebox-player-pop) | tv |
| [Google Home](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-google-home-speaker) | speaker |
| [Google Home Max](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-google-home-max) | speaker |
| [Google Nest Audio](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-google-nest-audio) | speaker |
| [Google Nest Hub](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-google-nest-hub) | display |
| [Google Nest Hub Max](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-google-nest-hub-max) | display |
| [Google Nest Mini](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-google-nest-mini) | speaker |
| [Google Pixel Tablet](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-google-pixel-tablet) | display |
| [Google TV Streamer](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-google-tv-streamer) | tv |
| [LG webOS TVs](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-lg-webos-tvs) | tv |
| [Logitech Squeezebox](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-logitech-squeezebox) | speaker |
| [Samsung Tizen TVs](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-samsung-tizen-tvs) | tv |
| [Sonos speakers](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-sonos-speakers) | speaker |
| [VIZIO D40f-G9](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-vizio-d40f-g9) | tv |
| [Brother printers](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-brother-printers) | printer |
| [Epson printers](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-epson-printers) | printer |
| [HP Color LaserJet Pro M254dw](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-hp-color-laserjet-pro-m254dw) | printer |
| [Dyson Pure Hot+Cool HP04](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-dyson-pure-hot-cool-hp04) | appliance |
| [Miele G7566 dishwasher](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-miele-g7566-dishwasher) | appliance |
| [iRobot Roomba/Braava](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-irobot-roomba-braava) | vacuum |
| [Roborock vacuums](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-roborock-vacuums) | vacuum |
| [Eufy RoboVac (Tuya)](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-eufy-robovac-tuya) | vacuum |
| [Moonraker 3D printers](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-moonraker-3d-printers) | printer |
| [ratgdo v3.2 garage door](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-ratgdo-v32-garage-door) | garage |
| [Sonoff RF Bridge](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-sonoff-rf-bridge) | rf |
| [ESPHome devices](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-esphome-devices) | generic |
| [ESP-Somfy-RTS](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-espsomfy-rts) | blinds |
| [Velux KLF200](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-velux-klf200) | blinds |
| [Tuya WiFi devices](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-tuya-wifi-devices) | generic |
| [UniFi network consoles](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-unifi-network-consoles) | network |
| [Zigbee2MQTT gateways](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-zigbee2mqtt-gateways) | zigbee |
| [Wyze RTSP cameras](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-wyze-rtsp-cameras) | camera |
| [Yi-Hack cameras](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/skills/gadget-yi-hack-cameras) | camera |

> **Note:** Boards without PSRAM (e.g. classic ESP32, ESP32-C6) run without the home-network tunnel. Muse can still reach and control the device — just not poke at devices on your LAN through it.

---

## 🔌 Community ports & integrations

Third-party projects that adapt, wrap, or extend the SDK. Quality varies — check stars, last commit, and the linked issue tracker before relying on one in production.

| Project | Author | Kind | Purpose |
| --- | --- | --- | --- |
| [Muse Code ACP adapter](https://github.com/bex-co/muse-code-acp) | bex-co | agent-protocol | Unofficial ACP adapter so Muse Code works inside Zed |
| [Muse Code OpenRouter](https://github.com/xhluca/muse-code-openrouter) | xhluca | backend | Plug OpenRouter keys and any model into Muse Code |
| [Muse Code in OpenCode](https://github.com/swalker326/opencode-muse-code) | swalker326 | agent-protocol | Reuse a Muse Code subscription in OpenCode |
| [Muse Code Sandboxes kit](https://github.com/shelajev/muse-code-sbx-kit) | shelajev | infra | Docker sandboxes for Muse Code CLI |
| [Muse Code Helicon UI](https://github.com/HarjjotSinghh/helicon) | HarjjotSinghh | frontend | Open-source desktop/web UI for Muse Code |
| [muse-gadget-psp](https://github.com/wobsoriano/muse-gadget-psp) | wobsoriano | port | Run Muse Gadget SDK natively on Sony PSP |
| [muse-gadget-sdk (alt fork)](https://github.com/ledienbien-ai/muse-gadget-sdk) | ledienbien-ai | fork | — |
| [Waveshare Muse Gadget SDK](https://github.com/wupsbr/waveshare-muse-gadget-sdk) | wupsbr | board-port | Waveshare ESP32-S3 boards (1.75/1.75C) |
| [muse-r1 (Rabbit r1 home launcher)](https://github.com/cameronapak/muse-r1) | cameronapak | device-mod | Native Android HOME app: turn Rabbit r1 into a Muse Gadget host |
| [muse-arr](https://github.com/vocino/muse-arr) | vocino | skill-extension | Control Sonarr/Radarr from Muse |
| [muse-gadget (Waveshare status report)](https://github.com/az9713/muse-gadget) | az9713 | board-port | Waveshare ESP32-S3-Touch-AMOLED-1.75C |
| [muse-gadget-xiaozhi](https://github.com/moerdowo/muse-gadget-xiaozhi) | moerdowo | firmware-port | Muse UI (pixel character, push-to-talk, captioned display) for xiaozhi-esp32 |
| [luci-muse-gadget](https://github.com/burndown/luci-muse-gadget) | burndown | router-port | Run the SDK on OpenWrt with a LuCI page and BLE |
| [muse-ai-passport](https://github.com/timzenxia/muse-ai-passport) | timzenxia | port | Unofficial firmware port of Muse Gadget SDK |
| [aipets-muse](https://github.com/veiovi/aipets-muse) | veiovi | animation-pack | Portable AI Pets animation packs for Muse ESP32 SDK |
| [muse-web](https://github.com/shreyaskarnik/muse-web) | shreyaskarnik | firmware-port | Browser installer for Muse Gadget SDK ESP32 firmware |
| [muse-tamagotchi](https://github.com/ameyarya/muse-tamagotchi) | ameyarya | hardware-project | DIY ESP32 Muse handheld Tamagotchi-like device |
| [muse-gadget-c6-n16](https://github.com/assix/muse-gadget-c6-n16) | assix | board-port | Bring Muse SDK to generic ESP32-C6-N16 |
| [smktec-154-muse-port](https://github.com/ousiaresearch/smktec-154-muse-port) | ousiaresearch | board-port | SMKTelec ESP32-S3 1.54" port |
| [mute-gadget-sdk](https://github.com/mfiumara/mute-gadget-sdk) | mfiumara | fork | Open-source gadgets on ESP32 + Linux with your own AI backend |
| [R1-jot](https://github.com/sussman/R1-jot) | sussman | experiment | Connect Rabbit R1 to a persistent Muse gadget |
| [GenPark Ambient Vision Anchor](https://github.com/Alpha-Park/genpark-ambient-vision-anchor-skill) | Alpha-Park | skill | Multimodal ambient vision Muse skill |

---

## 🐇 Open-source Rabbit R1 alternatives

If you came for the Muse Gadget SDK **because** you want a small AI gadget in your pocket, these are open-source spin-offs that pair with the same Muse app:

| Project | Purpose |
| --- | --- |
| [S1-app (Rabbit R1 alternative)](https://github.com/Foqsee/S1-app) | Open-source alternative to Rabbit R1 |
| [hamster-h1 (Rabbit R1 alternative)](https://github.com/harigovind511/hamster-h1) | OS alternative aiming at parity with Rabbit R1 |

---

## ✅ Source verification

Every board, skill, and project on this list is verified against a live upstream source through the 19001 HK proxy:

```bash
python3 scripts/verify_sources.py
```

- 📦 [Official Muse Gadget SDK](https://github.com/facebookincubator/muse-gadget-sdk)
- 🌐 [Muse Gadgets homepage](https://gadgets.muse.ai)
- 📜 [Gadget SDK Terms](https://gadgets.muse.ai/sdk-terms)

---

<div align="center">
<sub>Maintained by the open-source community. Not affiliated with Meta Platforms. PRs welcome — add a board, a port, or a skill, and the CI will re-verify the upstream.</sub>
</div>
