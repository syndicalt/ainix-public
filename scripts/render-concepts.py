#!/usr/bin/env python3
"""Render the Ainix concept diagrams to PNG.

These are *generated diagrams*, not screenshots of the runtime. The script is
committed alongside the PNGs so the assets are reproducible and honestly
labeled. Run:  python3 scripts/render-concepts.py

Requires: cairosvg  (pip install cairosvg)
"""
import html
import os

import cairosvg

W, H = 1600, 900
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "concept-renders")

# Palette ------------------------------------------------------------------
BG0, BG1 = "#0a1020", "#10182e"
PANEL = "#0e1426"
PANEL_STROKE = "#243049"
TITLE = "#f2f5fb"
SUB = "#8d9ab5"
MUTE = "#aab4cc"
ACCENTS = ["#36c5d6", "#7c8cf0", "#3fcf8e", "#e0a13a", "#e06a9c"]
GREEN = "#3fcf8e"


def esc(s):
    return html.escape(str(s), quote=True)


def stars(seed=1, n=70):
    # deterministic pseudo-stars (no RNG, so output is stable across runs)
    out = []
    x, y = seed * 97 + 13, seed * 57 + 31
    for i in range(n):
        x = (x * 1103515245 + 12345) & 0x7FFFFFFF
        y = (y * 1103515245 + 54321) & 0x7FFFFFFF
        px, py = x % W, y % H
        r = 0.6 + (i % 3) * 0.5
        op = 0.12 + (i % 5) * 0.05
        out.append(f'<circle cx="{px}" cy="{py}" r="{r:.1f}" fill="#cfe0ff" opacity="{op:.2f}"/>')
    return "\n".join(out)


def frame(inner, badges=None):
    badge_svg = ""
    if badges:
        bx = W - 60
        for label in reversed(badges):
            bw = 22 + len(label) * 8.4
            bx -= bw
            badge_svg += (
                f'<rect x="{bx:.0f}" y="64" width="{bw:.0f}" height="30" rx="15" '
                f'fill="none" stroke="{PANEL_STROKE}"/>'
                f'<text x="{bx + bw/2:.0f}" y="84" fill="{MUTE}" font-size="13" '
                f'font-family="Arial, sans-serif" letter-spacing="1.5" text-anchor="middle">{esc(label)}</text>'
            )
            bx -= 12
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="bg" cx="35%" cy="20%" r="120%">
      <stop offset="0%" stop-color="{BG1}"/>
      <stop offset="100%" stop-color="{BG0}"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  {stars()}
  <rect x="40" y="40" width="{W-80}" height="{H-80}" rx="26" fill="{PANEL}" fill-opacity="0.55" stroke="{PANEL_STROKE}"/>
  {badge_svg}
  {inner}
</svg>'''


def header(title, subtitle):
    return (
        f'<text x="72" y="96" fill="{TITLE}" font-size="40" font-weight="700" '
        f'font-family="Arial, sans-serif">{esc(title)}</text>'
        f'<text x="74" y="128" fill="{SUB}" font-size="19" '
        f'font-family="Arial, sans-serif">{esc(subtitle)}</text>'
    )


# 01 — What's real today ---------------------------------------------------
def render_today():
    inner = [header("Ainix today", "Hosted runtime substrate — every exposed command does real work.")]
    # terminal card
    cx, cy, cw, ch = 72, 168, 900, 600
    inner.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="16" fill="#0b1striped" />')
    inner.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="16" fill="#080d1a" stroke="{PANEL_STROKE}"/>')
    for i, c in enumerate(("#e0625e", "#e0b03a", "#3fcf8e")):
        inner.append(f'<circle cx="{cx+34+i*26}" cy="{cy+34}" r="7" fill="{c}"/>')
    rows = [
        ("$ cargo test --workspace --locked", "ok — workspace verified"),
        ("$ cargo clippy --workspace -- -D warnings", "clean — zero warnings"),
        ("$ ainix lattice import <path>", "canonical blocks + provenance event"),
        ("$ ainix extension execute --nonce …", "brokered · replay-guarded · audited"),
        ("$ ainix shell-demo run --input <path>", "import → context → proposal → approve"),
    ]
    y = cy + 92
    for cmd, res in rows:
        inner.append(f'<text x="{cx+34}" y="{y}" fill="#cdd6ea" font-size="20" font-family="monospace">{esc(cmd)}</text>')
        inner.append(f'<text x="{cx+52}" y="{y+30}" fill="{GREEN}" font-size="19" font-family="monospace">{esc(res)}</text>')
        y += 96
    # side cards
    sx, sw = 1012, 470
    cards = [
        ("IDENTITY", "capability-scoped authority"),
        ("EVENT LOG", "append-only, tamper-evident"),
        ("SURFACE", "honest — no gate-record theater"),
    ]
    sy = cy + 6
    for i, (k, v) in enumerate(cards):
        a = ACCENTS[i]
        inner.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="120" rx="14" fill="#0b1striped"/>')
        inner.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="120" rx="14" fill="#0c1striped"/>')
        inner.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="120" rx="14" fill="{PANEL}" stroke="{a}" stroke-opacity="0.6"/>')
        inner.append(f'<text x="{sx+28}" y="{sy+44}" fill="{a}" font-size="14" letter-spacing="2" font-family="Arial, sans-serif">{esc(k)}</text>')
        inner.append(f'<text x="{sx+28}" y="{sy+80}" fill="{TITLE}" font-size="22" font-weight="600" font-family="Arial, sans-serif">{esc(v)}</text>')
        sy += 142
    inner.append(f'<text x="72" y="{cy+ch+44}" fill="{SUB}" font-size="18" font-family="Arial, sans-serif">'
                 'Runs on today’s operating systems. The substrate is designed to move lower in the stack later.</text>')
    return frame("\n".join(inner), badges=["LOCAL-FIRST", "CAPABILITY-SCOPED", "AUDITABLE"])


# 02 — Architecture --------------------------------------------------------
def render_architecture():
    inner = [header("Ainix architecture", "A hosted semantic-OS substrate with a native-OS trajectory.")]
    layers = [
        ("Control surfaces", "CLI, local API, canvas shell, touch, AR/VR", 0),
        ("System brokers", "capabilities, policy, agents, extensions, intent", 1),
        ("Semantic substrate", "identity, event log, lattice, provenance, sync", 2),
        ("Host adapters — today", "Windows, Linux, macOS, files, sockets", 3),
        ("Native layer — later", "session manager, shell, IPC, storage, kernel boundary", 4),
    ]
    x, w = 96, W - 192
    y = 196
    rh, gap = 96, 18
    for name, detail, i in layers:
        a = ACCENTS[i]
        inner.append(f'<rect x="{x}" y="{y}" width="{w}" height="{rh}" rx="12" fill="{PANEL}" stroke="{a}" stroke-opacity="0.65"/>')
        inner.append(f'<text x="{x+34}" y="{y+rh/2+8:.0f}" fill="{TITLE}" font-size="25" font-weight="600" font-family="Arial, sans-serif">{esc(name)}</text>')
        inner.append(f'<text x="{x+430}" y="{y+rh/2+7:.0f}" fill="{MUTE}" font-size="19" font-family="Arial, sans-serif">{esc(detail)}</text>')
        y += rh + gap
    return frame("\n".join(inner), badges=["LOCAL-FIRST", "AUDITABLE", "COMPOSABLE"])


# 03 — Future canvas -------------------------------------------------------
def render_canvas():
    inner = [header("Future Ainix canvas — concept", "Everyday control surface for people, agents, tools, and knowledge.")]
    cxh, cyh = W/2, 470
    nodes = [
        ("work package", "Q3 board deck", 320, 300, 0),
        ("policy gate", "approval needed", W-540, 300, 3),
        ("source graph", "plan lattice", 300, 600, 2),
        ("provenance", "audit + replay", cxh-110, 650, 4),
        ("agent team", "delegated tasks", W-540, 600, 1),
    ]
    for _t, _s, nx, ny, i in nodes:
        a = ACCENTS[i]
        inner.append(f'<line x1="{cxh}" y1="{cyh}" x2="{nx+110}" y2="{ny+34}" stroke="{a}" stroke-opacity="0.55" stroke-width="2"/>')
    # hub
    inner.append(f'<circle cx="{cxh}" cy="{cyh}" r="64" fill="#161f3a" stroke="{ACCENTS[1]}" stroke-opacity="0.8"/>')
    inner.append(f'<text x="{cxh}" y="{cyh-2}" fill="{TITLE}" font-size="24" font-weight="700" text-anchor="middle" font-family="Arial, sans-serif">intent</text>')
    inner.append(f'<text x="{cxh}" y="{cyh+22}" fill="{SUB}" font-size="14" text-anchor="middle" font-family="Arial, sans-serif">delegated work</text>')
    for title, sub, nx, ny, i in nodes:
        a = ACCENTS[i]
        inner.append(f'<rect x="{nx}" y="{ny}" width="220" height="72" rx="12" fill="{PANEL}" stroke="{a}" stroke-opacity="0.6"/>')
        inner.append(f'<text x="{nx+22}" y="{ny+34}" fill="{TITLE}" font-size="20" font-weight="600" font-family="Arial, sans-serif">{esc(title)}</text>')
        inner.append(f'<text x="{nx+22}" y="{ny+57}" fill="{SUB}" font-size="15" font-family="Arial, sans-serif">{esc(sub)}</text>')
    inner.append(f'<text x="72" y="{H-72}" fill="{SUB}" font-size="18" font-family="Arial, sans-serif">'
                 'Concept of the long-term interface: an infinite semantic canvas, not a static admin dashboard. Not current software.</text>')
    return frame("\n".join(inner), badges=["screen", "touch", "AR", "VR"])


# 04 — Roadmap -------------------------------------------------------------
def render_roadmap():
    inner = [header("Ainix roadmap", "Prove the model on today’s OS first; move lower only where it earns it.")]
    steps = [
        ("NOW", "Hosted runtime", "identity, capabilities, events, lattice, extensions", 0),
        ("NEXT", "First real agent", "one local model, cited proposals, human approval", 1),
        ("THEN", "Supervised OS", "sandboxed sessions, async supervisor, real storage", 2),
        ("LATER", "Canvas + native", "canvas shell, then native shell / session / kernel work", 4),
    ]
    n = len(steps)
    margin = 240
    span = W - 2 * margin
    cy_line = 300
    xs = [margin + span * i / (n - 1) for i in range(n)]
    for i in range(n - 1):
        inner.append(f'<line x1="{xs[i]+34}" y1="{cy_line}" x2="{xs[i+1]-34}" y2="{cy_line}" stroke="{PANEL_STROKE}" stroke-width="3"/>')
    for i, (tag, title, detail, ai) in enumerate(steps):
        a = ACCENTS[ai]
        x = xs[i]
        inner.append(f'<circle cx="{x}" cy="{cy_line}" r="30" fill="#0c1striped"/>')
        inner.append(f'<circle cx="{x}" cy="{cy_line}" r="30" fill="{PANEL}" stroke="{a}"/>')
        inner.append(f'<text x="{x}" y="{cy_line+8}" fill="{TITLE}" font-size="26" font-weight="700" text-anchor="middle" font-family="Arial, sans-serif">{i+1}</text>')
        # card
        cw = 290
        cx = x - cw / 2
        cyc = cy_line + 80
        inner.append(f'<rect x="{cx}" y="{cyc}" width="{cw}" height="170" rx="14" fill="{PANEL}" stroke="{PANEL_STROKE}"/>')
        tagw = 30 + len(tag) * 9
        inner.append(f'<rect x="{cx+24}" y="{cyc+22}" width="{tagw}" height="26" rx="13" fill="none" stroke="{a}" stroke-opacity="0.7"/>')
        inner.append(f'<text x="{cx+24+tagw/2}" y="{cyc+39}" fill="{a}" font-size="13" letter-spacing="1.5" text-anchor="middle" font-family="Arial, sans-serif">{esc(tag)}</text>')
        inner.append(f'<text x="{cx+24}" y="{cyc+82}" fill="{TITLE}" font-size="23" font-weight="700" font-family="Arial, sans-serif">{esc(title)}</text>')
        # wrap detail
        words, line, ly = detail.split(), "", cyc + 112
        for wd in words:
            if len(line) + len(wd) + 1 > 34:
                inner.append(f'<text x="{cx+24}" y="{ly}" fill="{MUTE}" font-size="16" font-family="Arial, sans-serif">{esc(line)}</text>')
                line, ly = wd, ly + 22
            else:
                line = (line + " " + wd).strip()
        inner.append(f'<text x="{cx+24}" y="{ly}" fill="{MUTE}" font-size="16" font-family="Arial, sans-serif">{esc(line)}</text>')
    inner.append(f'<text x="72" y="{H-66}" fill="{SUB}" font-size="18" font-family="Arial, sans-serif">'
                 'Let existing platforms host the agent-native layer while Ainix proves which primitives deserve native treatment.</text>')
    return frame("\n".join(inner), badges=["hosted now", "native later"])


TARGETS = {
    "01-runtime-today.png": render_today,
    "02-ainix-architecture.png": render_architecture,
    "03-future-canvas-control-surface.png": render_canvas,
    "04-hosted-to-native-roadmap.png": render_roadmap,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in TARGETS.items():
        svg = fn().replace("#0b1striped", PANEL).replace("#0c1striped", "#0c1426")
        cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT, name),
                         output_width=W, output_height=H)
        print("wrote", name)
