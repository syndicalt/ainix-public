#!/usr/bin/env python3
"""Render the 5:2 X header for the "From Theater to First Blood" article.

Generated diagram, not a screenshot. Run: python3 scripts/render-first-blood-header.py
Requires: cairosvg
"""
import html
import os

import cairosvg

W, H = 1500, 600  # 5:2
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "press", "first-blood-x-header.png")

BG0, BG1 = "#0a1020", "#10182e"
TITLE = "#f2f5fb"
SUB = "#9aa6c0"
MUTE = "#aab4cc"
STROKE = "#243049"
CYAN, INDIGO, GREEN, AMBER, PINK = "#36c5d6", "#7c8cf0", "#3fcf8e", "#e0a13a", "#e06a9c"


def esc(s):
    return html.escape(str(s), quote=True)


def stars(n=90):
    out, x, y = [], 7919, 104729
    for i in range(n):
        x = (x * 1103515245 + 12345) & 0x7FFFFFFF
        y = (y * 1103515245 + 54321) & 0x7FFFFFFF
        px, py = x % W, y % H
        r = 0.5 + (i % 3) * 0.5
        op = 0.10 + (i % 5) * 0.05
        out.append(f'<circle cx="{px}" cy="{py}" r="{r:.1f}" fill="#cfe0ff" opacity="{op:.2f}"/>')
    return "\n".join(out)


# Provenance chain — the real dogfood sequence.
CHAIN = [
    ("intent", CYAN),
    ("inference", INDIGO),
    ("proposal", AMBER),
    ("approval", PINK),
    ("apply", GREEN),
]


def chain_svg(cy):
    margin = 250
    span = W - 2 * margin
    n = len(CHAIN)
    xs = [margin + span * i / (n - 1) for i in range(n)]
    parts = []
    # connecting line
    for i in range(n - 1):
        parts.append(
            f'<line x1="{xs[i]+16:.0f}" y1="{cy}" x2="{xs[i+1]-16:.0f}" y2="{cy}" '
            f'stroke="{STROKE}" stroke-width="2"/>'
        )
        # arrowhead
        mx = (xs[i] + xs[i + 1]) / 2
        parts.append(
            f'<path d="M{mx-4:.0f},{cy-5} L{mx+5:.0f},{cy} L{mx-4:.0f},{cy+5}" '
            f'fill="none" stroke="{SUB}" stroke-width="2" opacity="0.7"/>'
        )
    for (label, color), x in zip(CHAIN, xs):
        filled = label == "apply"
        parts.append(
            f'<circle cx="{x:.0f}" cy="{cy}" r="13" fill="{color if filled else "#0c1426"}" '
            f'stroke="{color}" stroke-width="2"/>'
        )
        if filled:
            parts.append(
                f'<path d="M{x-5:.0f},{cy} l3,4 l6,-7" fill="none" stroke="#0a1020" '
                f'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
            )
        parts.append(
            f'<text x="{x:.0f}" y="{cy+38}" fill="{MUTE}" font-size="20" '
            f'font-family="Arial, sans-serif" text-anchor="middle">{esc(label)}</text>'
        )
    return "\n".join(parts)


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="bg" cx="32%" cy="18%" r="120%">
      <stop offset="0%" stop-color="{BG1}"/><stop offset="100%" stop-color="{BG0}"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  {stars()}
  <rect x="22" y="22" width="{W-44}" height="{H-44}" rx="22" fill="none" stroke="{STROKE}" stroke-opacity="0.7"/>

  <text x="92" y="120" fill="{CYAN}" font-size="19" letter-spacing="3.5"
        font-family="Arial, sans-serif">A I N I X &#8201;&#183;&#8201; TOWARD AN AGENT-NATIVE OS</text>

  <text x="88" y="232" fill="{TITLE}" font-size="74" font-weight="800"
        font-family="Arial, sans-serif">From Theater to First Blood</text>

  <text x="92" y="288" fill="{SUB}" font-size="27" font-family="Arial, sans-serif">
        How a system stopped describing readiness — and started earning it.</text>

  <text x="92" y="392" fill="{MUTE}" font-size="20" font-family="Arial, sans-serif">
        One real local agent loop — authority-scoped, cited, traceable to the source bytes.</text>

  {chain_svg(465)}
</svg>'''

if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT, output_width=W, output_height=H)
    print("wrote", os.path.relpath(OUT, os.path.join(os.path.dirname(__file__), "..")))
