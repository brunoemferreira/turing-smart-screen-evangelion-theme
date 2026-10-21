param(
    [string]$UsbMonitorDir = "C:\Users\bruno\Downloads\35inchENG\35inchENG",
    [string]$ProjectDir = "e:\Dev\03-laboratorios\tss"
)

Add-Type -AssemblyName System.Drawing

# Load UsbMonitor .NET Assembly
$asmPath = Join-Path $UsbMonitorDir "UsbMonitor.exe"
if (-not (Test-Path $asmPath)) {
    Write-Error "UsbMonitor.exe not found at $asmPath"
    exit 1
}

$asm = [System.Reflection.Assembly]::LoadFrom($asmPath)
$formatter = New-Object System.Runtime.Serialization.Formatters.Binary.BinaryFormatter

function Configure-Font($item, $fontName, $fontSize, $color) {
    if ($item.fontType -eq $null) {
        $item.fontType = New-Object usb_hid.FontConfig
    }
    $item.fontType.name = $fontName
    $item.fontType.size = $fontSize
    $item.fontType.color = $color
    switch ($fontSize) {
        18 { $item.fontType.offsetX = 5; $item.fontType.offsetY = 8; $item.fontType.interval = 10 }
        24 { $item.fontType.offsetX = 7; $item.fontType.offsetY = 11; $item.fontType.interval = 12 }
        30 { $item.fontType.offsetX = 8; $item.fontType.offsetY = 13; $item.fontType.interval = 16 }
        40 { $item.fontType.offsetX = 11; $item.fontType.offsetY = 17; $item.fontType.interval = 22 }
    }
}

# Evangelion Colors
$colGreen = [System.Drawing.Color]::FromArgb(255, 57, 255, 20)      # Neon Lime (#39FF14)
$colAmber = [System.Drawing.Color]::FromArgb(255, 255, 170, 0)     # Neon Amber (#FFAA00)
$colPurple = [System.Drawing.Color]::FromArgb(255, 200, 120, 255)  # Neon Purple (#C878FF)
$colWhite = [System.Drawing.Color]::FromArgb(255, 255, 255, 255)   # White

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "COMPILING REDISTRIBUTED EVA-01 THEMES" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

# ---------------------------------------------------------
# 1. LANDSCAPE THEME (480x320)
# ---------------------------------------------------------
Write-Host "`n[1/2] Building Landscape Theme (480x320)..." -ForegroundColor Yellow
$msiPath = Join-Path $UsbMonitorDir "config\msi.data"
$stream = [System.IO.File]::OpenRead($msiPath)
$landTheme = $formatter.Deserialize($stream)
$stream.Close()

$landTheme.name = "A EVA 01 Cyberpunk Land"
$landTheme.isLanscape = $true
$landTheme.needRereshArch = $false

# 100% clean transparent OSD bitmaps
$landTheme.osdImg = New-Object System.Drawing.Bitmap(480, 320, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$landTheme.osdWithFontBack = New-Object System.Drawing.Bitmap(480, 320, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$landTheme.enbaleOsdWithFontBack = $false
$landTheme.useOsdWithFontBack = $false

# Load clean landscape background
$landImgPath = Join-Path $ProjectDir "eva_cyberpunk_landscape.png"
$landBmp = [System.Drawing.Bitmap]::FromFile($landImgPath)
$landTheme.backImg = New-Object System.Drawing.Bitmap($landBmp)
$landBmp.Dispose()

# Disable all firmware bars and archs for maximum stability (no disconnects)
foreach ($a in $landTheme.archList) {
    $a.enabled = $false
}
foreach ($b in $landTheme.barList) {
    $b.enabled = $false
}

# Configure Item Positions in groupList
foreach ($g in $landTheme.groupList) {
    $g.backImg = $null
    foreach ($item in $g.itemList) {
        $item.enabled = $false
        
        # CPU Items (Generous spacing: Load Y=52, Temp Y=93, Freq Y=117)
        if ($item.itemName -eq "CpuLoad") {
            $item.posX = 68; $item.posY = 52; $item.enabled = $true
            Configure-Font $item "24" 24 $colGreen
        }
        elseif ($item.itemName -eq "CpuTemp") {
            # 13px below bar (bar ends at Y=80). Zero collision!
            $item.posX = 68; $item.posY = 93; $item.enabled = $true
            Configure-Font $item "18" 18 $colAmber
        }
        elseif ($item.itemName -eq "CpuFreq") {
            $item.posX = 68; $item.posY = 117; $item.enabled = $true
            Configure-Font $item "18" 18 $colGreen
        }
        # GPU Items (Load Y=52, Temp Y=93, VRAM Y=117)
        elseif ($item.itemName -eq "GpuLoad") {
            $item.posX = 388; $item.posY = 52; $item.enabled = $true
            Configure-Font $item "24" 24 $colGreen
        }
        elseif ($item.itemName -eq "GpuTemp") {
            # 13px below bar (bar ends at Y=80). Zero collision!
            $item.posX = 388; $item.posY = 93; $item.enabled = $true
            Configure-Font $item "18" 18 $colAmber
        }
        elseif ($item.itemName -eq "GpuRam") {
            $item.posX = 384; $item.posY = 117; $item.enabled = $true
            Configure-Font $item "18" 18 $colGreen
        }
        # RAM Items (X=392, Y=193)
        elseif ($item.itemName -eq "RamLoad") {
            $item.posX = 392; $item.posY = 193; $item.enabled = $true
            Configure-Font $item "24" 24 $colGreen
        }
        # HDD / Drive C: Items (X=392, Y=241)
        elseif ($item.itemName -eq "HDDLoad") {
            $item.posX = 392; $item.posY = 241; $item.enabled = $true
            Configure-Font $item "24" 24 $colAmber
        }
        # Network Items
        elseif ($item.itemName -eq "InternetDown") {
            $item.posX = 56; $item.posY = 194; $item.enabled = $true
            Configure-Font $item "18" 18 $colGreen
        }
        elseif ($item.itemName -eq "InternetUp") {
            $item.posX = 56; $item.posY = 222; $item.enabled = $true
            Configure-Font $item "18" 18 $colPurple
        }
        # Time Item (Y=7, card border is at Y=3, leaves 4px padding so no overlap with top line!)
        elseif ($item.itemName -eq "Time") {
            $item.posX = 396; $item.posY = 7; $item.enabled = $true
            Configure-Font $item "18" 18 $colGreen
        }
    }
}

# Save Landscape theme to local and UsbMonitor config
$landOutLocal = Join-Path $ProjectDir "A EVA 01 Cyberpunk Land.data"
$landOutTarget = Join-Path $UsbMonitorDir "config\A EVA 01 Cyberpunk Land.data"

$streamOut = [System.IO.File]::Create($landOutLocal)
$formatter.Serialize($streamOut, $landTheme)
$streamOut.Close()
Copy-Item $landOutLocal $landOutTarget -Force
Write-Host " -> Saved Landscape Theme: $landOutTarget" -ForegroundColor Green

# ---------------------------------------------------------
# 2. PORTRAIT THEME (320x480)
# ---------------------------------------------------------
Write-Host "`n[2/2] Building Portrait Theme (320x480)..." -ForegroundColor Yellow
$cyberPath = Join-Path $UsbMonitorDir "config\Cyberpunk2077.data"
$streamPort = [System.IO.File]::OpenRead($cyberPath)
$portTheme = $formatter.Deserialize($streamPort)
$streamPort.Close()

$portTheme.name = "A EVA 01 Cyberpunk Port"
$portTheme.isLanscape = $false
$portTheme.needRereshArch = $false

# Clean OSD bitmaps
$portTheme.osdImg = New-Object System.Drawing.Bitmap(320, 480, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$portTheme.osdWithFontBack = New-Object System.Drawing.Bitmap(320, 480, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$portTheme.enbaleOsdWithFontBack = $false
$portTheme.useOsdWithFontBack = $false

# Load clean portrait background
$portImgPath = Join-Path $ProjectDir "eva_cyberpunk_portrait.png"
$portBmp = [System.Drawing.Bitmap]::FromFile($portImgPath)
$portTheme.backImg = New-Object System.Drawing.Bitmap($portBmp)
$portBmp.Dispose()

# Disable all bars and archs for 100% stability
foreach ($a in $portTheme.archList) {
    $a.enabled = $false
}
foreach ($b in $portTheme.barList) {
    $b.enabled = $false
}

# Configure Text Item Positions in groupList
foreach ($g in $portTheme.groupList) {
    $g.backImg = $null
    foreach ($item in $g.itemList) {
        $item.enabled = $false
        
        # CPU
        if ($item.itemName -eq "CpuLoad") {
            $item.posX = 52; $item.posY = 178; $item.enabled = $true
            Configure-Font $item "24" 24 $colGreen
        }
        elseif ($item.itemName -eq "CpuTemp") {
            $item.posX = 150; $item.posY = 178; $item.enabled = $true
            Configure-Font $item "24" 24 $colAmber
        }
        elseif ($item.itemName -eq "CpuFreq") {
            $item.posX = 250; $item.posY = 178; $item.enabled = $true
            Configure-Font $item "24" 24 $colGreen
        }
        # GPU
        elseif ($item.itemName -eq "GpuLoad") {
            $item.posX = 52; $item.posY = 257; $item.enabled = $true
            Configure-Font $item "24" 24 $colGreen
        }
        elseif ($item.itemName -eq "GpuTemp") {
            $item.posX = 150; $item.posY = 257; $item.enabled = $true
            Configure-Font $item "24" 24 $colAmber
        }
        elseif ($item.itemName -eq "GpuRam") {
            $item.posX = 250; $item.posY = 257; $item.enabled = $true
            Configure-Font $item "18" 18 $colGreen
        }
        # RAM
        elseif ($item.itemName -eq "RamLoad") {
            $item.posX = 56; $item.posY = 336; $item.enabled = $true
            Configure-Font $item "24" 24 $colGreen
        }
        # Drive C:
        elseif ($item.itemName -eq "HDDLoad") {
            $item.posX = 220; $item.posY = 336; $item.enabled = $true
            Configure-Font $item "24" 24 $colAmber
        }
        # Network
        elseif ($item.itemName -eq "InternetDown") {
            $item.posX = 56; $item.posY = 417; $item.enabled = $true
            Configure-Font $item "18" 18 $colGreen
        }
        elseif ($item.itemName -eq "InternetUp") {
            $item.posX = 200; $item.posY = 417; $item.enabled = $true
            Configure-Font $item "18" 18 $colPurple
        }
        # Time
        elseif ($item.itemName -eq "Time") {
            $item.posX = 56; $item.posY = 447; $item.enabled = $true
            Configure-Font $item "18" 18 $colGreen
        }
    }
}

# Save Portrait theme
$portOutLocal = Join-Path $ProjectDir "A EVA 01 Cyberpunk Port.data"
$portOutTarget = Join-Path $UsbMonitorDir "config\A EVA 01 Cyberpunk Port.data"

$streamPortOut = [System.IO.File]::Create($portOutLocal)
$formatter.Serialize($streamPortOut, $portTheme)
$streamPortOut.Close()
Copy-Item $portOutLocal $portOutTarget -Force
Write-Host " -> Saved Portrait Theme: $portOutTarget" -ForegroundColor Green

# Copy background PNGs to UsbMonitor 3.5 folder
Copy-Item (Join-Path $ProjectDir "eva_cyberpunk_landscape.png") (Join-Path $UsbMonitorDir "3.5\eva_cyberpunk_landscape.png") -Force
Copy-Item (Join-Path $ProjectDir "eva_cyberpunk_portrait.png") (Join-Path $UsbMonitorDir "3.5\eva_cyberpunk_portrait.png") -Force

Write-Host "`nSUCCESS! Themes updated with zero overlap and redistributed spacing." -ForegroundColor Cyan
