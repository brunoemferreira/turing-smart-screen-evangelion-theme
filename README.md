# <p align="center"><img src="./assets/icons/bot.svg" width="42" height="42" valign="middle" /> Evangelion Unit-01 (EVA-01) HUD <img src="./assets/icons/activity.svg" width="42" height="42" valign="middle" /></p>

<p align="center">
  <strong>High-performance mecha telemetry theme inspired by Evangelion Unit-01 for 3.5-inch Turing Smart Screen displays.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Evangelion-EVA--01-8C28DC?style=for-the-badge&logoColor=white" alt="Evangelion EVA-01" />
  <img src="https://img.shields.io/badge/Display-Turing%20Smart%20Screen%203.5%22-00FF66?style=for-the-badge&logoColor=black" alt="Turing 3.5" />
  <img src="https://img.shields.io/badge/App-UsbMonitor.exe-107C41?style=for-the-badge&logo=windows&logoColor=white" alt="UsbMonitor" />
  <img src="https://img.shields.io/badge/Resolution-480x320%20%7C%20320x480-007ACC?style=for-the-badge" alt="Resolution" />
  <img src="https://img.shields.io/badge/Python-3.10%2B%20%7C%20Pillow-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PowerShell-.NET%20Reflection-5391FE?style=for-the-badge&logo=powershell&logoColor=white" alt="PowerShell" />
  <img src="https://img.shields.io/badge/Version-v1.3.1-FFAA00?style=for-the-badge" alt="v1.3.1" />
  <img src="https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge&logo=gnu&logoColor=white" alt="GPL-3.0 License" />
</p>

---

## <img src="./assets/icons/explore.svg" width="24" height="24" valign="middle" /> Table of Contents

- [Overview](#-overview)
- [Visual Demonstration](#-visual-demonstration)
- [Telemetry Mapping](#-telemetry-mapping)
- [Repository Structure](#-repository-structure)
- [How to Compile the Files](#-how-to-compile-the-files)
- [How to Install and Activate on the Display](#-how-to-install-and-activate-on-the-display)
- [Useful Links & Downloads](#-useful-links--downloads)
- [Version History](#-version-history)
- [License](#-license)

---

## <img src="./assets/icons/explore.svg" width="24" height="24" valign="middle" /> Overview

This project provides a real-time hardware telemetry monitoring theme for the secondary USB display **Turing Smart Screen 3.5-inch** (native resolutions: **480×320** in horizontal mode and **320×480** in vertical mode).

The layout is inspired by the tactical cockpit aesthetics and interface of **NERV's MAGI System**, featuring the official color palette of the **Evangelion Unit-01 (EVA-01)**:
- **Deep Mecha Purple (`#8C28DC` / `#2E0854`)**: Chamfered bezels, structural rails, and corner brackets.
- **Fluorescent Acid Neon Green (`#00FF66` / `#39FF14`)**: Clock speeds, usage loads, download bandwidth, and sync status (`SYNC: 100%`).
- **NERV Warning Amber (`#FFAA00`)**: Critical temperatures, emergency indicators, and Drive C: storage usage.
- **Carbon Hex Texture**: High-contrast, anti-reflective matte dark background that eliminates glare and highlights the central wireframe hologram of EVA-01.

---

## <img src="./assets/icons/target.svg" width="24" height="24" valign="middle" /> Visual Demonstration

### Horizontal Mode (Landscape — 480 × 320 px)
> *Ideal for standard desktop landscape docks and stands.*

![EVA-01 Landscape Preview](./preview_landscape.png)

### Vertical Mode (Portrait — 320 × 480 px)
> *Ideal for vertical PC chassis mounts or upright stands.*

![EVA-01 Portrait Preview](./preview_portrait.png)

---

## <img src="./assets/icons/activity.svg" width="24" height="24" valign="middle" /> Telemetry Mapping

All metrics are updated in real time by the software without text collisions or bar overlaps:

| Module | Metric | Software Identifier | Format & Styling |
| :--- | :--- | :--- | :--- |
| **CPU** | Usage Load (%) | `CpuLoad` | Neon Green digits (`#39FF14`) + Dynamic HUD LED bar |
| **CPU** | Temperature (°C) | `CpuTemp` | Amber NERV Alert digits (`#FFAA00`) with 13px breathing room |
| **CPU** | Clock Frequency (GHz) | `CpuFreq` | Neon Green digits |
| **GPU** | Usage Load (%) | `GpuLoad` | Neon Green digits + Dynamic HUD LED bar |
| **GPU** | Temperature (°C) | `GpuTemp` | Amber NERV Alert digits with 13px breathing room |
| **GPU** | VRAM Memory (MB) | `GpuRam` | Neon Green digits with native suffix |
| **RAM** | Memory Usage (%) | `RamLoad` | Neon Green digits (`X = 392` column) + Dynamic HUD bar |
| **Drive C:** | Storage Usage (%) | `HDDLoad` | Amber NERV digits (`X = 392` column) + Dynamic HUD bar |
| **Network** | Download Speed (MB/s) | `InternetDown` | Neon Green digits with `DL [v]` indicator |
| **Network** | Upload Speed (MB/s) | `InternetUp` | Electric Purple digits (`#C878FF`) with `UL [^]` indicator |
| **Clock** | Current Time | `Time` | Synchronized top-right with 4px internal margin |

---

## <img src="./assets/icons/architecture.svg" width="24" height="24" valign="middle" /> Repository Structure

```text
tss/
├── assets/
│   ├── icons/                          # SVG icons for project documentation
│   ├── eva_center_crop.png             # EVA-01 Hologram (Landscape)
│   └── eva_portrait_crop.png           # EVA-01 Hologram (Portrait)
│
├── build_theme_images.py               # Procedural HUD background generator (Pillow)
├── build_theme_data.ps1                # Binary theme compiler (.data via .NET Reflection)
├── eva_01_landscape.png                # Generated background 480x320
├── eva_01_portrait.png                 # Generated background 320x480
├── preview_landscape.png               # Horizontal demonstration preview
├── preview_portrait.png                # Vertical demonstration preview
├── A EVA 01 Evangelion Land.data       # Horizontal binary theme package
├── A EVA 01 Evangelion Port.data       # Vertical binary theme package
├── .gitignore                          # Git ignore rules
├── LICENSE                             # GNU General Public License v3.0 (GPL-3.0)
└── README.md                           # Official project documentation
```

---

## <img src="./assets/icons/tools.svg" width="24" height="24" valign="middle" /> How to Compile the Files

The compilation pipeline consists of two stages: procedural high-definition visual generation and binary serialization compatible with the `.NET` architecture of Turing Smart Screen.

### Prerequisites:
- **Python 3.10+** with the Pillow library:
  ```bash
  pip install pillow
  ```
- **PowerShell 5.1 or 7+** (with script execution permissions).

### Step 1: Generate Background Images (PNG)
Run the Python script to draw the HUD panels, hexagonal grids, mecha frames, and composite the holograms:
```bash
python build_theme_images.py
```
*Output:* Generates `eva_01_landscape.png` (480x320) and `eva_01_portrait.png` (320x480).

### Step 2: Compile Binary Theme Files (`.data`)
Run the PowerShell script to serialize the themes with `BinaryFormatter`, inject font tables, neon colors, absolute coordinates, and transparent OSD layers:
```powershell
powershell -ExecutionPolicy Bypass -File build_theme_data.ps1
```
*Output:* Compiles `A EVA 01 Evangelion Land.data` and `A EVA 01 Evangelion Port.data`, automatically deploying them into your UsbMonitor directory.

---

## <img src="./assets/icons/backend.svg" width="24" height="24" valign="middle" /> How to Install and Activate on the Display

If you want to manually deploy to another machine or directory:

1. **Copy the theme files into the `config\` folder:**
   - Copy `A EVA 01 Evangelion Land.data` and `A EVA 01 Evangelion Port.data` to `C:\...\35inchENG\config\`
2. **Copy the background images into the `3.5\` folder:**
   - Copy `eva_01_landscape.png` and `eva_01_portrait.png` to `C:\...\35inchENG\3.5\`
3. **Activate in the UsbMonitor interface:**
   - Open **UsbMonitor.exe**.
   - In the **Theme** dropdown, select:
     - **`A EVA 01 Evangelion Land`** (for horizontal display)
     - or **`A EVA 01 Evangelion Port`** (for vertical display)
   - Click the **Run** button. The screen will update immediately.

---

## <img src="./assets/icons/connect.svg" width="24" height="24" valign="middle" /> Useful Links & Downloads

Official downloads and community resources for the **Turing Smart Screen 3.5"** management application (`UsbMonitor.exe`), drivers, and firmwares:

| Resource | Description | Access Link |
| :--- | :--- | :--- |
| **Turing 3.5" App Direct Download** | Official direct download page for 3.5" packages (`35inchENG.rar` / `UsbMonitor.exe`) | [Turzx 3.5" Direct Download](https://www.turzx.com/2023/03/02/%E7%9B%B4%E9%93%BE%E4%B8%8B%E8%BD%BDdirectdownload/) |
| **Official Manufacturer Portal (Turzx)** | Official Turzx website with documentation, updates, and user guides | [https://www.turzx.com/](https://www.turzx.com/) |
| **Turzx Software & Drivers Center** | Central driver repository, default themes, and firmware releases | [Turzx Software Center](https://www.turzx.com/2021/11/02/download/) |
| **Turing Smart Screen Python (Open Source)** | Community-driven open-source Python driver and library for Turing displays | [GitHub - mathoudebine/turing-smart-screen-python](https://github.com/mathoudebine/turing-smart-screen-python) |

---

## <img src="./assets/icons/code.svg" width="24" height="24" valign="middle" /> Version History

### [v1.3.1] - 2026-10-21
- **Drive C: (HDDLoad) Bounding Box & Height Fix**: Enforced explicit `W=14, H=18, interval=14` font metrics for size 24 font, fixing cropped percentage digits on the physical display.
- **Global FontConfig Standardization**: Automated strict configuration of `W`, `H`, `offsetX`, `offsetY`, and `interval` for all font sizes (18, 24, 30, 40) in both Landscape and Portrait themes.
- **GPL-3.0 License & English Localization**: Switched project license to GNU GPL v3.0 and converted documentation to English.

### [v1.3.0] - 2026-10-21
- **Evangelion Naming Standardization**: 100% exclusive focus on Evangelion Unit-01 / NERV MAGI theme.
- **New README SVG Icons**: Integrated clean SVG icons for section titles and ecosystem badges.
- **Compilation Guide & Download Links**: Added comprehensive build pipeline documentation and direct links to official Turzx software.

### [v1.2.0] - 2026-10-21
- **RAM & Drive C: Card**: Restructured layout vertically aligned at `X = 392` with divider line, resolving label collisions.
- **Time Card**: Expanded time card (`Y = 3..25`) with 4px internal margin, preventing top border overlap.
- **CPU & GPU Cards**: Realigned temperatures with 13px spacing below the LED bars.

### [v1.1.0] - 2026-10-21
- **Legacy OSD Cleanup**: Removed residual `osdImg` gauge graphics and overlay layers.
- **USB Firmware Stability**: Resolved watchdog timer resets and disconnection issues over USB HID.

### [v1.0.0] - 2026-10-21
- Initial release of the Evangelion Unit-01 themes for 3.5" Turing Smart Screen displays (Landscape & Portrait).

---

## <img src="./assets/icons/briefcase.svg" width="24" height="24" valign="middle" /> License

This project is licensed under the [GNU General Public License v3.0 (GPL-3.0)](LICENSE).
