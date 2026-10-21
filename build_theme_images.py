"""
Evangelion Unit-01 Cyberpunk Theme Background Generator (v3)
- Expanded vertical layout in CPU & GPU cards:
  * Clean separation between LOAD, Progress Bar, TEMP, and CLOCK
  * Temperature has 14px of breathing room below the bar (zero collision!)
- Upgraded Time Card:
  * Taller header bar with deep chamfered card (Y=3..25)
  * Time digits sit comfortably at Y=7 with 4px padding below the top border (zero collision!)
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont

# Palette EVA-01 Cyberpunk
BG_DARK = (10, 8, 16)           # Deep dark tech carbon
BG_PANEL = (16, 12, 26)         # Dark purple-grey panel background
BORDER_PURPLE = (140, 40, 220)  # Vivid EVA-01 mecha purple
BORDER_GREEN = (0, 255, 102)    # Fluorescent Acid Neon Green
ACCENT_GREEN = (57, 255, 20)    # Hyper-bright Lime
ACCENT_AMBER = (255, 160, 0)    # NERV Warning Amber
TEXT_WHITE = (240, 245, 255)
TEXT_MUTED = (140, 150, 175)
TEXT_PURPLE = (190, 120, 255)
TRACK_BG = (24, 16, 38)         # Recessed bar track background

def get_font(size, bold=False):
    font_paths = [
        "C:/Windows/Fonts/bahnschrift.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/arial.ttf"
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

def draw_hex_pattern(draw, width, height, step=22):
    """Draw subtle dark hexagonal cyberpunk carbon grid in background"""
    color = (20, 15, 32)
    r = step / math.sqrt(3)
    for y in range(0, height + int(step), int(step * 0.75)):
        row = int(y / (step * 0.75))
        offset = (step / 2) if (row % 2 == 1) else 0
        for x in range(0, width + int(step), int(step)):
            cx = x + offset
            cy = y
            points = []
            for i in range(6):
                angle = math.radians(60 * i + 30)
                px = cx + r * 0.45 * math.cos(angle)
                py = cy + r * 0.45 * math.sin(angle)
                points.append((px, py))
            draw.polygon(points, outline=color)

def draw_chamfer_box(draw, x, y, w, h, chamfer=6, fill=None, outline=None, width=1):
    """Draws a cyberpunk chamfered-corner rectangle"""
    pts = [
        (x + chamfer, y),
        (x + w - chamfer, y),
        (x + w, y + chamfer),
        (x + w, y + h - chamfer),
        (x + w - chamfer, y + h),
        (x + chamfer, y + h),
        (x, y + h - chamfer),
        (x, y + chamfer)
    ]
    if fill:
        draw.polygon(pts, fill=fill)
    if outline:
        draw.polygon(pts, outline=outline)

def draw_tech_brackets(draw, x, y, w, h, bracket_len=8, color=BORDER_GREEN, width=2):
    """Draw tactical HUD corner brackets"""
    draw.line([(x, y + bracket_len), (x, y), (x + bracket_len, y)], fill=color, width=width)
    draw.line([(x + w - bracket_len, y), (x + w, y), (x + w, y + bracket_len)], fill=color, width=width)
    draw.line([(x, y + h - bracket_len), (x, y + h), (x + bracket_len, y + h)], fill=color, width=width)
    draw.line([(x + w - bracket_len, y + h), (x + w, y + h), (x + w, y + h - bracket_len)], fill=color, width=width)

def draw_hazard_stripes(draw, x, y, w, h, color1=(20, 16, 28), color2=ACCENT_AMBER):
    """Draw classic Evangelion NERV hazard warning stripes"""
    draw.rectangle([x, y, x + w, y + h], fill=color1)
    stripe_w = 6
    for sx in range(x - h, x + w, stripe_w * 2):
        pts = [
            (max(x, sx), y),
            (min(x + w, sx + stripe_w), y),
            (min(x + w, sx + stripe_w + h), y + h),
            (max(x, sx + h), y + h)
        ]
        if pts[0][0] < pts[1][0] and pts[3][0] < pts[2][0]:
            draw.polygon(pts, fill=color2)

def draw_segmented_bar(draw, x, y, w, h, num_segments=16, lit_segments=10, lit_color=BORDER_GREEN, dim_color=(35, 25, 50)):
    """Draws a permanent high-tech segmented HUD bar meter"""
    seg_w = (w - (num_segments - 1) * 2) / num_segments
    for i in range(num_segments):
        sx = int(x + i * (seg_w + 2))
        ex = int(sx + seg_w)
        c = lit_color if i < lit_segments else dim_color
        draw.rectangle([sx, y, ex, y + h], fill=c)

def generate_landscape():
    width, height = 480, 320
    im = Image.new("RGBA", (width, height), BG_DARK)
    draw = ImageDraw.Draw(im)

    # 1. Subtle Cyberpunk Hex Grid
    draw_hex_pattern(draw, width, height, step=22)

    # 2. Top Header Bar (Y=0 to 28)
    draw.rectangle([0, 0, width, 28], fill=(16, 11, 26))
    draw.line([(0, 28), (width, 28)], fill=BORDER_PURPLE, width=1)
    draw.line([(0, 29), (width, 29)], fill=(0, 255, 102, 180), width=1)

    f_badge = get_font(9, bold=True)
    f_label = get_font(10, bold=True)
    f_unit = get_font(9, bold=False)
    f_tiny = get_font(8, bold=False)

    # Header Left: EVA-01 Badge
    draw_chamfer_box(draw, 6, 4, 116, 20, chamfer=3, fill=(35, 15, 55), outline=BORDER_GREEN)
    draw.text((12, 7), "EVA-01 TEST TYPE", font=f_badge, fill=ACCENT_GREEN)

    # Header Center: NERV Magi Sync Badge
    draw_chamfer_box(draw, 128, 4, 168, 20, chamfer=3, fill=(20, 12, 36), outline=BORDER_PURPLE)
    draw.text((136, 7), "NERV MAGI HUD // SYNC: 100%", font=f_badge, fill=TEXT_WHITE)

    # Hazard stripe decor
    draw_hazard_stripes(draw, 302, 7, 38, 14, color1=(25, 15, 38), color2=(255, 140, 0))

    # Header Right: TIME Card (Y=3..25, H=22, generous vertical clearance)
    draw_chamfer_box(draw, 346, 3, 128, 22, chamfer=3, fill=(16, 12, 28), outline=BORDER_GREEN)
    draw.text((354, 7), "TIME:", font=f_label, fill=TEXT_MUTED)
    # Digits for Time will be placed at X=396, Y=7 (leaving 4px below top border Y=3)

    # 3. Center Cockpit / Hologram Panel (X=162, Y=31, W=156, H=283)
    cx, cy, cw, ch = 162, 31, 156, 283
    draw_chamfer_box(draw, cx, cy, cw, ch, chamfer=8, fill=(14, 10, 22), outline=BORDER_PURPLE, width=1)
    draw_tech_brackets(draw, cx, cy, cw, ch, bracket_len=12, color=BORDER_GREEN, width=2)

    # Header in center
    draw.rectangle([cx + 12, cy + 5, cx + cw - 12, cy + 18], fill=(30, 16, 48))
    draw.text((cx + 20, cy + 6), "MECHA CORE // EVA-01", font=f_tiny, fill=BORDER_GREEN)

    # Composite EVA-01 wireframe crop into center
    crop_path = "e:/Dev/03-laboratorios/tss/assets/eva_center_crop.png"
    if os.path.exists(crop_path):
        eva_crop = Image.open(crop_path).convert("RGBA")
        target_w = 142
        target_h = int(eva_crop.height * (target_w / eva_crop.width))
        if target_h > 185:
            target_h = 185
            target_w = int(eva_crop.width * (target_h / eva_crop.height))
        eva_crop = eva_crop.resize((target_w, target_h), Image.Resampling.LANCZOS)
        paste_x = cx + (cw - target_w) // 2
        paste_y = cy + 24
        im.paste(eva_crop, (paste_x, paste_y), eva_crop)

    # Radar/Targeting crosshairs overlay
    rcx = cx + cw // 2
    rcy = cy + 115
    draw.ellipse([rcx - 45, rcy - 45, rcx + 45, rcy + 45], outline=(0, 255, 102, 60), width=1)
    draw.ellipse([rcx - 22, rcy - 22, rcx + 22, rcy + 22], outline=(140, 40, 220, 80), width=1)
    draw.line([(rcx - 55, rcy), (rcx - 30, rcy)], fill=ACCENT_GREEN, width=1)
    draw.line([(rcx + 30, rcy), (rcx + 55, rcy)], fill=ACCENT_GREEN, width=1)
    draw.line([(rcx, rcy - 55), (rcx, rcy - 30)], fill=ACCENT_GREEN, width=1)
    draw.line([(rcx, rcy + 30), (rcx, rcy + 55)], fill=ACCENT_GREEN, width=1)

    # Tactical Status at bottom of center panel
    draw_hazard_stripes(draw, cx + 10, cy + ch - 62, cw - 20, 8, color1=(20, 14, 30), color2=ACCENT_AMBER)
    draw_chamfer_box(draw, cx + 8, cy + ch - 50, cw - 16, 42, chamfer=4, fill=(22, 15, 36), outline=BORDER_PURPLE)
    draw.text((cx + 14, cy + ch - 47), "STATUS: SYNCHRONIZED", font=f_tiny, fill=BORDER_GREEN)
    draw.text((cx + 14, cy + ch - 35), "PILOT: SHINJI IKARI", font=f_tiny, fill=TEXT_MUTED)
    draw.text((cx + 14, cy + ch - 23), "INTERNAL BATTERY: 100%", font=f_tiny, fill=ACCENT_AMBER)

    # 4. Left Panel 1 - CPU Telemetry (X=8, Y=31, W=146, H=135)
    px, py, pw, ph = 8, 31, 146, 135
    draw_chamfer_box(draw, px, py, pw, ph, chamfer=6, fill=BG_PANEL, outline=BORDER_PURPLE)
    draw_tech_brackets(draw, px, py, pw, ph, bracket_len=8, color=BORDER_GREEN)
    draw.rectangle([px + 8, py + 4, px + pw - 8, py + 18], fill=(32, 16, 52))
    draw.text((px + 12, py + 5), "// CPU TELEMETRY", font=f_label, fill=BORDER_GREEN)

    # Row 1: LOAD (Y=54)
    # CpuLoad digits rendered at posX=68, posY=52 (Font 24)
    draw.text((px + 10, 54), "LOAD:", font=f_label, fill=TEXT_WHITE)
    draw.text((px + 126, 54), "%", font=f_label, fill=BORDER_GREEN)

    # Row 2: SEGMENTED BAR (Y=74..80)
    draw_segmented_bar(draw, px + 10, 74, pw - 20, 6, num_segments=16, lit_segments=10, lit_color=BORDER_GREEN)

    # Row 3: TEMP (Y=95) -> 15px gap below bar! Zero collision!
    # CpuTemp digits rendered at posX=68, posY=93 (Font 18)
    draw.text((px + 10, 95), "TEMP:", font=f_label, fill=TEXT_WHITE)
    draw.text((px + 122, 95), "°C", font=f_label, fill=ACCENT_AMBER)

    # Row 4: CLOCK (Y=119) -> 24px gap below Temp!
    # CpuFreq digits rendered at posX=68, posY=117 (Font 18)
    draw.text((px + 10, 119), "CLOCK:", font=f_label, fill=TEXT_WHITE)
    draw.text((px + 120, 119), "GHz", font=f_label, fill=BORDER_GREEN)

    # Row 5: Tactical Status Line (Y=143)
    draw.line([(px + 8, 143), (px + pw - 8, 143)], fill=(45, 25, 65), width=1)
    draw.text((px + 10, 147), "CORES: ALL OPTIMAL", font=f_tiny, fill=TEXT_MUTED)

    # 5. Left Panel 2 - Network Telemetry (X=8, Y=172, W=146, H=142)
    nx, ny, nw, nh = 8, 172, 146, 142
    draw_chamfer_box(draw, nx, ny, nw, nh, chamfer=6, fill=BG_PANEL, outline=BORDER_PURPLE)
    draw_tech_brackets(draw, nx, ny, nw, nh, bracket_len=8, color=BORDER_GREEN)
    draw.rectangle([nx + 8, ny + 4, nx + nw - 8, ny + 18], fill=(32, 16, 52))
    draw.text((nx + 12, ny + 5), "// NETWORK UPLINK", font=f_label, fill=BORDER_GREEN)

    # InternetDown: Digit at posX=56, posY=195
    draw.text((nx + 10, ny + 24), "DL [v]:", font=f_label, fill=BORDER_GREEN)
    draw.text((nx + 116, ny + 25), "MB/s", font=f_unit, fill=TEXT_MUTED)

    # InternetUp: Digit at posX=56, posY=223
    draw.text((nx + 10, ny + 52), "UL [^]:", font=f_label, fill=TEXT_PURPLE)
    draw.text((nx + 116, ny + 53), "MB/s", font=f_unit, fill=TEXT_MUTED)

    # Network Decor
    draw.line([(nx + 8, ny + 80), (nx + nw - 8, ny + 80)], fill=BORDER_PURPLE, width=1)
    draw.text((nx + 10, ny + 86), "INTERFACE: ETHERNET", font=f_tiny, fill=TEXT_MUTED)
    draw.text((nx + 10, ny + 100), "STATUS: ONLINE 1Gbps", font=f_tiny, fill=BORDER_GREEN)
    # Signal bars
    for bi in range(6):
        bh = 4 + bi * 3
        draw.rectangle([nx + 10 + bi * 8, ny + 130 - bh, nx + 15 + bi * 8, ny + 130], fill=BORDER_GREEN)

    # 6. Right Panel 1 - GPU Telemetry (X=326, Y=31, W=146, H=135)
    gx, gy, gw, gh = 326, 31, 146, 135
    draw_chamfer_box(draw, gx, gy, gw, gh, chamfer=6, fill=BG_PANEL, outline=BORDER_PURPLE)
    draw_tech_brackets(draw, gx, gy, gw, gh, bracket_len=8, color=BORDER_GREEN)
    draw.rectangle([gx + 8, gy + 4, gx + gw - 8, gy + 18], fill=(32, 16, 52))
    draw.text((gx + 12, gy + 5), "// GPU TELEMETRY", font=f_label, fill=BORDER_GREEN)

    # Row 1: LOAD (Y=54)
    # GpuLoad digits rendered at posX=388, posY=52 (Font 24)
    draw.text((gx + 10, 54), "LOAD:", font=f_label, fill=TEXT_WHITE)
    draw.text((gx + 126, 54), "%", font=f_label, fill=BORDER_GREEN)

    # Row 2: SEGMENTED BAR (Y=74..80)
    draw_segmented_bar(draw, gx + 10, 74, gw - 20, 6, num_segments=16, lit_segments=11, lit_color=BORDER_GREEN)

    # Row 3: TEMP (Y=95) -> 15px gap below bar! Zero collision!
    # GpuTemp digits rendered at posX=388, posY=93 (Font 18)
    draw.text((gx + 10, 95), "TEMP:", font=f_label, fill=TEXT_WHITE)
    draw.text((gx + 122, 95), "°C", font=f_label, fill=ACCENT_AMBER)

    # Row 4: VRAM (Y=119) -> 24px gap below Temp!
    # GpuRam digits rendered at posX=384, posY=117 (Font 18, outputs '8136MB')
    draw.text((gx + 10, 119), "VRAM:", font=f_label, fill=TEXT_WHITE)

    # Row 5: Tactical Status Line (Y=143)
    draw.line([(gx + 8, 143), (gx + gw - 8, 143)], fill=(45, 25, 65), width=1)
    draw.text((gx + 10, 147), "PCIE LINK: ACTIVE", font=f_tiny, fill=TEXT_MUTED)

    # 7. Right Panel 2 - RAM & Drive C: Telemetry (X=326, Y=172, W=146, H=142)
    rx, ry, rw, rh = 326, 172, 146, 142
    draw_chamfer_box(draw, rx, ry, rw, rh, chamfer=6, fill=BG_PANEL, outline=BORDER_PURPLE)
    draw_tech_brackets(draw, rx, ry, rw, rh, bracket_len=8, color=BORDER_GREEN)
    draw.rectangle([rx + 8, ry + 4, rx + rw - 8, ry + 18], fill=(32, 16, 52))
    draw.text((rx + 12, ry + 5), "// MEMORY & STORAGE", font=f_label, fill=BORDER_GREEN)

    # Section 1: RAM (Row 1 at Y=195, Bar at Y=217)
    # RamLoad digits rendered at posX=392, posY=193 (Font 24)
    draw.text((rx + 8, 195), "RAM:", font=f_label, fill=TEXT_WHITE)
    draw.text((rx + 124, 195), "%", font=f_label, fill=BORDER_GREEN)
    draw_segmented_bar(draw, rx + 8, 217, rw - 16, 6, num_segments=16, lit_segments=6, lit_color=BORDER_GREEN)

    # Subtle divider line between RAM and Drive C:
    draw.line([(rx + 8, 231), (rx + rw - 8, 231)], fill=(40, 24, 58), width=1)

    # Section 2: DRIVE C: (Row 2 at Y=243, Bar at Y=267)
    # HDDLoad digits rendered at posX=392, posY=241 (Font 24)
    draw.text((rx + 8, 243), "DRIVE C:", font=f_label, fill=BORDER_GREEN)
    draw.text((rx + 124, 243), "%", font=f_label, fill=ACCENT_AMBER)
    draw_segmented_bar(draw, rx + 8, 267, rw - 16, 6, num_segments=16, lit_segments=9, lit_color=ACCENT_AMBER)

    # Footer
    draw.line([(rx + 8, 285), (rx + rw - 8, 285)], fill=(40, 24, 58), width=1)
    draw.text((rx + 10, 289), "SYSTEM NVMe STORAGE", font=f_tiny, fill=TEXT_MUTED)

    out_file = "e:/Dev/03-laboratorios/tss/eva_cyberpunk_landscape.png"
    im.save(out_file, "PNG")
    print(f"Landscape background saved to {out_file} ({width}x{height})")
    return out_file

def generate_portrait():
    width, height = 320, 480
    im = Image.new("RGBA", (width, height), BG_DARK)
    draw = ImageDraw.Draw(im)

    draw_hex_pattern(draw, width, height, step=22)

    f_badge = get_font(9, bold=True)
    f_label = get_font(10, bold=True)
    f_unit = get_font(9, bold=False)
    f_tiny = get_font(8, bold=False)

    # Top Header (Y=0 to 28)
    draw.rectangle([0, 0, width, 28], fill=(16, 11, 26))
    draw.line([(0, 28), (width, 28)], fill=BORDER_PURPLE, width=1)
    draw.line([(0, 29), (width, 29)], fill=(0, 255, 102, 180), width=1)

    draw_chamfer_box(draw, 6, 4, 150, 20, chamfer=3, fill=(35, 15, 55), outline=BORDER_GREEN)
    draw.text((12, 7), "EVA-01 TEST TYPE", font=f_badge, fill=ACCENT_GREEN)

    draw_chamfer_box(draw, 164, 4, 150, 20, chamfer=3, fill=(20, 12, 36), outline=BORDER_PURPLE)
    draw.text((170, 7), "NERV MAGI // SYNC 100%", font=f_badge, fill=TEXT_WHITE)

    # Top Section: EVA-01 Hologram (X=8, Y=33, W=304, H=120)
    hx, hy, hw, hh = 8, 33, 304, 120
    draw_chamfer_box(draw, hx, hy, hw, hh, chamfer=6, fill=(14, 10, 22), outline=BORDER_PURPLE)
    draw_tech_brackets(draw, hx, hy, hw, hh, bracket_len=10, color=BORDER_GREEN)

    crop_path = "e:/Dev/03-laboratorios/tss/assets/eva_portrait_crop.png"
    if os.path.exists(crop_path):
        eva_crop = Image.open(crop_path).convert("RGBA")
        target_h = 110
        target_w = int(eva_crop.width * (target_h / eva_crop.height))
        eva_crop = eva_crop.resize((target_w, target_h), Image.Resampling.LANCZOS)
        im.paste(eva_crop, (hx + 12, hy + 5), eva_crop)

    draw_chamfer_box(draw, hx + 130, hy + 12, 160, 24, chamfer=3, fill=(26, 16, 42), outline=BORDER_GREEN)
    draw.text((hx + 138, hy + 17), "STATUS: ACTIVE", font=f_badge, fill=ACCENT_GREEN)

    draw_chamfer_box(draw, hx + 130, hy + 42, 160, 24, chamfer=3, fill=(20, 14, 32), outline=BORDER_PURPLE)
    draw.text((hx + 138, hy + 47), "PILOT: SHINJI IKARI", font=f_badge, fill=TEXT_WHITE)

    draw_hazard_stripes(draw, hx + 130, hy + 72, 160, 14, color1=(20, 14, 30), color2=ACCENT_AMBER)
    draw.text((hx + 135, hy + 92), "NERV TACTICAL HUD SYSTEM", font=f_tiny, fill=TEXT_MUTED)

    # Section 1: CPU (X=8, Y=158, W=304, H=74)
    cx, cy, cw, ch = 8, 158, 304, 74
    draw_chamfer_box(draw, cx, cy, cw, ch, chamfer=6, fill=BG_PANEL, outline=BORDER_PURPLE)
    draw_tech_brackets(draw, cx, cy, cw, ch, bracket_len=6, color=BORDER_GREEN)
    draw.text((cx + 10, cy + 4), "// CPU TELEMETRY", font=f_label, fill=BORDER_GREEN)

    draw.text((cx + 12, cy + 22), "LOAD:", font=f_label, fill=TEXT_WHITE)
    draw.text((cx + 80, cy + 23), "%", font=f_unit, fill=BORDER_GREEN)

    draw.text((cx + 110, cy + 22), "TEMP:", font=f_label, fill=TEXT_WHITE)
    draw.text((cx + 178, cy + 23), "°C", font=f_unit, fill=ACCENT_AMBER)

    draw.text((cx + 208, cy + 22), "CLOCK:", font=f_label, fill=TEXT_WHITE)
    draw.text((cx + 280, cy + 23), "GHz", font=f_unit, fill=BORDER_GREEN)

    draw_segmented_bar(draw, cx + 12, cy + 52, cw - 24, 6, num_segments=24, lit_segments=12, lit_color=BORDER_GREEN)

    # Section 2: GPU (X=8, Y=237, W=304, H=74)
    gx, gy, gw, gh = 8, 237, 304, 74
    draw_chamfer_box(draw, gx, gy, gw, gh, chamfer=6, fill=BG_PANEL, outline=BORDER_PURPLE)
    draw_tech_brackets(draw, gx, gy, gw, gh, bracket_len=6, color=BORDER_GREEN)
    draw.text((gx + 10, gy + 4), "// GPU TELEMETRY", font=f_label, fill=BORDER_GREEN)

    draw.text((gx + 12, gy + 22), "LOAD:", font=f_label, fill=TEXT_WHITE)
    draw.text((gx + 80, gy + 23), "%", font=f_unit, fill=BORDER_GREEN)

    draw.text((gx + 110, gy + 22), "TEMP:", font=f_label, fill=TEXT_WHITE)
    draw.text((gx + 178, gy + 23), "°C", font=f_unit, fill=ACCENT_AMBER)

    draw.text((gx + 208, gy + 22), "VRAM:", font=f_label, fill=TEXT_WHITE)

    draw_segmented_bar(draw, gx + 12, gy + 52, gw - 24, 6, num_segments=24, lit_segments=16, lit_color=BORDER_GREEN)

    # Section 3: RAM & DRIVE C: (X=8, Y=316, W=304, H=74)
    rx, ry, rw, rh = 8, 316, 304, 74
    draw_chamfer_box(draw, rx, ry, rw, rh, chamfer=6, fill=BG_PANEL, outline=BORDER_PURPLE)
    draw_tech_brackets(draw, rx, ry, rw, rh, bracket_len=6, color=BORDER_GREEN)
    draw.text((rx + 10, ry + 4), "// MEMORY & STORAGE", font=f_label, fill=BORDER_GREEN)

    draw.text((rx + 12, ry + 22), "RAM:", font=f_label, fill=TEXT_WHITE)
    draw.text((rx + 125, ry + 23), "%", font=f_unit, fill=BORDER_GREEN)
    draw_segmented_bar(draw, rx + 12, ry + 52, 130, 5, num_segments=10, lit_segments=4, lit_color=BORDER_GREEN)

    draw.text((rx + 155, ry + 22), "DRIVE C:", font=f_label, fill=TEXT_WHITE)
    draw.text((rx + 280, ry + 23), "%", font=f_unit, fill=ACCENT_AMBER)
    draw_segmented_bar(draw, rx + 155, ry + 52, 130, 5, num_segments=10, lit_segments=6, lit_color=ACCENT_AMBER)

    # Section 4: NETWORK & TIME (X=8, Y=395, W=304, H=78)
    nx, ny, nw, nh = 8, 395, 304, 78
    draw_chamfer_box(draw, nx, ny, nw, nh, chamfer=6, fill=BG_PANEL, outline=BORDER_PURPLE)
    draw_tech_brackets(draw, nx, ny, nw, nh, bracket_len=6, color=BORDER_GREEN)
    draw.text((nx + 10, ny + 4), "// NETWORK & TIME", font=f_label, fill=BORDER_GREEN)

    draw.text((nx + 12, ny + 24), "DL [v]:", font=f_label, fill=BORDER_GREEN)
    draw.text((nx + 115, ny + 25), "MB/s", font=f_unit, fill=TEXT_MUTED)

    draw.text((nx + 155, ny + 24), "UL [^]:", font=f_label, fill=TEXT_PURPLE)
    draw.text((nx + 255, ny + 25), "MB/s", font=f_unit, fill=TEXT_MUTED)

    draw.line([(nx + 8, ny + 48), (nx + nw - 8, ny + 48)], fill=BORDER_PURPLE, width=1)
    draw.text((nx + 12, ny + 54), "TIME:", font=f_tiny, fill=TEXT_MUTED)

    out_file = "e:/Dev/03-laboratorios/tss/eva_cyberpunk_portrait.png"
    im.save(out_file, "PNG")
    print(f"Portrait background saved to {out_file} ({width}x{height})")
    return out_file

if __name__ == "__main__":
    generate_landscape()
    generate_portrait()
