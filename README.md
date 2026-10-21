# 🤖 Evangelion Unit-01 Cyberpunk HUD — Turing Smart Screen 3.5"

Tema funcional de alta performance e estética mecha cyberpunk inspirado no **EVA-01 de Neon Genesis Evangelion**, desenvolvido especificamente para displays secundários USB **Turing Smart Screen de 3.5 polegadas** (resolução nativa de **480×320** em modo horizontal e **320×480** em modo vertical) gerenciados pelo software `UsbMonitor.exe`.

---

## 📸 Imagens das Telas (Pré-visualizações)

### Modo Horizontal (Landscape — 480 × 320 px)
> *Orientação recomendada para suporte de mesa padrão.*

![EVA-01 Cyberpunk Landscape Preview](./preview_landscape.png)

### Modo Vertical (Portrait — 320 × 480 px)
> *Orientação para displays verticais.*

![EVA-01 Cyberpunk Portrait Preview](./preview_portrait.png)

---

## ⚙️ Métricas de Telemetria Mapeadas em Tempo Real

| Módulo | Métrica | Identificador no Software | Formato & Cor |
| :--- | :--- | :--- | :--- |
| **CPU** | Carga de Uso (%) | `CpuLoad` | Dígitos em Verde Neon (`#39FF14`) + Barra Dinâmica LED HUD |
| **CPU** | Temperatura (°C) | `CpuTemp` | Dígitos em Âmbar NERV Alert (`#FFAA00`) |
| **CPU** | Frequência de Clock (GHz) | `CpuFreq` | Dígitos em Verde Neon |
| **GPU** | Carga de Uso (%) | `GpuLoad` | Dígitos em Verde Neon + Barra Dinâmica LED HUD |
| **GPU** | Temperatura (°C) | `GpuTemp` | Dígitos em Âmbar NERV Alert |
| **GPU** | Memória VRAM (MB) | `GpuRam` | Dígitos em Verde Neon com sufixo nativo |
| **RAM** | Uso da Memória (%) | `RamLoad` | Dígitos em Verde Neon + Barra Dinâmica LED HUD |
| **Drive C:** | Uso do Armazenamento (%) | `HDDLoad` | Dígitos em Âmbar NERV Alert + Barra Dinâmica LED HUD |
| **Rede** | Taxa de Download (MB/s) | `InternetDown` | Dígitos em Verde Neon com indicador `DL [v]` |
| **Rede** | Taxa de Upload (MB/s) | `InternetUp` | Dígitos em Roxo Elétrico (`#C878FF`) com indicador `UL [^]` |
| **Relógio** | Horário Atual | `Time` | Sincronizado no card superior direito sem sobreposição |

---

## 🎨 Paleta de Cores & Design Mecha

- **Verde Neon Fluorescente (`#00FF66` / `#39FF14`)**: Destaque para taxas de clock, carga de uso, download e status nominal do EVA-01.
- **Roxo Mecha Profundo (`#8C28DC` / `#2E0854`)**: Molduras táticas chanfradas no estilo cockpit, cantoneiras e trilhos de medição.
- **Laranja/Âmbar NERV Alert (`#FFAA00`)**: Temperaturas críticas, advertências de emergência e capacidade do Drive C:.
- **Textura Carbon Hex Cyberpunk (`#0A0810`)**: Fundo escuro fosco de alto contraste que realça os displays sob luz ambiente e destaca o holograma central aramado do EVA-01.

---

## 📁 Estrutura do Repositório

```text
tss/
├── assets/
│   ├── eva_center_crop.png             # Holograma EVA-01 para orientação horizontal
│   └── eva_portrait_crop.png           # Holograma EVA-01 para orientação vertical
│
├── build_theme_images.py               # Gerador procedural de backgrounds HUD via Pillow
├── build_theme_data.ps1                # Compilador binário de temas (.data) via .NET Reflection
├── eva_cyberpunk_landscape.png         # Imagem de fundo 480x320 gerada
├── eva_cyberpunk_portrait.png          # Imagem de fundo 320x480 gerada
├── preview_landscape.png               # Imagem demonstrativa de telemetria horizontal
├── preview_portrait.png                # Imagem demonstrativa de telemetria vertical
├── A EVA 01 Cyberpunk Land.data        # Arquivo de tema pronto para o UsbMonitor (Horizontal)
├── A EVA 01 Cyberpunk Port.data        # Arquivo de tema pronto para o UsbMonitor (Vertical)
└── README.md                           # Documentação oficial do projeto
```

---

## 🚀 Como Instalar e Ativar

### 1. Local dos Arquivos
Os temas e fundos devem estar nas respectivas pastas do seu software (ex: `C:\Users\bruno\Downloads\35inchENG\35inchENG`):
- Temas `.data`: pasta `config\`
- Imagens de fundo `.png`: pasta `3.5\`

### 2. Ativação no Software
1. Abra a janela principal do **UsbMonitor**.
2. No menu suspenso de temas (**Theme**), selecione:
   - **`A EVA 01 Cyberpunk Land`** (modo horizontal)
   - ou **`A EVA 01 Cyberpunk Port`** (modo vertical)
3. Clique em **Run**. O visor de 3.5 polegadas atualizará na hora com a telemetria do Evangelion.

---

## 🔖 Versionamento (Changelog)

### [v1.2.0] - 2026-10-21
- **Card RAM & Drive C:**: Redistribuição vertical dos elementos, novo alinhamento horizontal em `X = 392` e linha divisória entre RAM e Drive C:, eliminando sobreposição com o texto "DRIVE C:".
- **Card de Horário**: Ampliação do card de tempo (`Y = 3..25`) e inserção com margem interna de 4px, resolvendo o corte na linha superior da borda.
- **Cards CPU e GPU**: Temperaturas posicionadas com 13px de respiro abaixo das barras de LED, sem sobreposição.

### [v1.1.0] - 2026-10-21
- **Eliminação de camada OSD residual**: Remoção dos círculos e textos antigos herdados de modelos legados.
- **Estabilidade USB**: Correção de buffer no firmware de 3.5", evitando estouro de memória e desconexões do dispositivo.
- **Ajuste de VRAM**: Correção da sobreposição do indicador de unidade.

### [v1.0.0] - 2026-10-21
- Lançamento inicial do tema Evangelion Unit-01 Cyberpunk com suporte a orientações Landscape e Portrait.
