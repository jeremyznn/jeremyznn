from pathlib import Path
from datetime import datetime, timezone

OUT = Path("assets/generated")
OUT.mkdir(parents=True, exist_ok=True)
STAMP = datetime.now(timezone.utc).strftime("%Y.%m.%d")

def hero(theme):
    dark = theme == "dark"
    bg0 = "#070A12" if dark else "#F7F8FC"
    bg1 = "#121027" if dark else "#ECEAF8"
    panel = "#111522" if dark else "#FFFFFF"
    fg = "#F7F8FF" if dark else "#171821"
    muted = "#9CA4BC" if dark else "#62677B"
    grid = "#6158A8" if dark else "#948CC3"
    violet = "#8B5CF6" if dark else "#6D4DE0"
    cyan = "#22D3EE" if dark else "#0891B2"
    line = "#2C3150" if dark else "#D8DAE8"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="846" height="330" viewBox="0 0 846 330" role="img" aria-label="Jérémy — Full-Stack Engineer at SKOLEOM PLATFORM INC.">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg0}"/><stop offset="1" stop-color="{bg1}"/></linearGradient>
    <radialGradient id="glowV"><stop offset="0" stop-color="{violet}" stop-opacity=".34"/><stop offset="1" stop-color="{violet}" stop-opacity="0"/></radialGradient>
    <radialGradient id="glowC"><stop offset="0" stop-color="{cyan}" stop-opacity=".22"/><stop offset="1" stop-color="{cyan}" stop-opacity="0"/></radialGradient>
    <filter id="blur"><feGaussianBlur stdDeviation="18"/></filter>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity=".18"/></filter>
    <style>
      text {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .mono {{ font-family: "JetBrains Mono", "SFMono-Regular", Consolas, monospace; }}
      .dash {{ animation: dash 9s linear infinite; }}
      .dash2 {{ animation: dash 14s linear infinite reverse; }}
      .pulse {{ animation: pulse 2.8s ease-in-out infinite; transform-origin: 667px 158px; }}
      .float1 {{ animation: f1 4.8s ease-in-out infinite; }} .float2 {{ animation: f2 5.4s ease-in-out infinite; }} .float3 {{ animation: f3 6.1s ease-in-out infinite; }}
      .scan {{ animation: scan 5s ease-in-out infinite; }}
      @keyframes dash {{ to {{ stroke-dashoffset: -120; }} }}
      @keyframes pulse {{ 0%,100% {{ transform:scale(.96); opacity:.75 }} 50% {{ transform:scale(1.07); opacity:1 }} }}
      @keyframes f1 {{ 0%,100% {{ transform:translateY(0) }} 50% {{ transform:translateY(-7px) }} }}
      @keyframes f2 {{ 0%,100% {{ transform:translateY(-2px) }} 50% {{ transform:translateY(6px) }} }}
      @keyframes f3 {{ 0%,100% {{ transform:translateY(3px) }} 50% {{ transform:translateY(-5px) }} }}
      @keyframes scan {{ 0%,100% {{ opacity:0; transform:translateY(-30px) }} 45%,55% {{ opacity:.42 }} 50% {{ transform:translateY(300px) }} }}
      @media (prefers-reduced-motion: reduce) {{ .dash,.dash2,.pulse,.float1,.float2,.float3,.scan {{ animation:none !important; }} }}
    </style>
  </defs>
  <rect width="846" height="330" rx="24" fill="url(#bg)"/>
  <ellipse cx="710" cy="82" rx="260" ry="210" fill="url(#glowV)" filter="url(#blur)"/>
  <ellipse cx="620" cy="260" rx="220" ry="150" fill="url(#glowC)" filter="url(#blur)"/>
  <g opacity=".30" stroke="{grid}" stroke-width="1"><path d="M420 230H826M392 250H826M368 272H826M346 296H826"/><path d="M588 214L476 330M632 214L570 330M676 214L664 330M720 214L758 330M764 214L846 322"/></g>
  <rect class="scan" x="0" y="0" width="846" height="1.5" fill="{cyan}"/>
  <g transform="translate(42 36)">
    <rect x="0" y="0" width="225" height="28" rx="14" fill="{panel}" stroke="{violet}" stroke-opacity=".45"/>
    <circle cx="16" cy="14" r="4.3" fill="{cyan}"><animate attributeName="opacity" values=".45;1;.45" dur="2s" repeatCount="indefinite"/></circle>
    <text x="29" y="18" fill="{muted}" font-size="10.5" class="mono" letter-spacing=".8">PROFILE SYSTEM // ONLINE</text>
    <text x="0" y="91" fill="{fg}" font-size="48" font-weight="800" letter-spacing="-1.8">JÉRÉMY</text>
    <text x="2" y="126" fill="{violet}" font-size="15" font-weight="800" letter-spacing="2.2">FULL‑STACK ENGINEER</text>
    <text x="0" y="165" fill="{fg}" font-size="16" font-weight="700">SKOLEOM PLATFORM INC.</text>
    <text x="0" y="188" fill="{muted}" font-size="13">Product Engineering · Cloud · Mobile · AI</text>
    <line x1="0" y1="214" x2="316" y2="214" stroke="{line}"/>
    <text x="0" y="239" fill="{muted}" font-size="10.5" class="mono">PARIS / FRANCE</text>
    <text x="0" y="258" fill="{muted}" font-size="10.5" class="mono">BUILD {STAMP}</text>
  </g>
  <g>
    <ellipse cx="667" cy="158" rx="146" ry="66" fill="none" stroke="{violet}" stroke-opacity=".38" stroke-dasharray="4 8" class="dash"/>
    <ellipse cx="667" cy="158" rx="180" ry="88" fill="none" stroke="{cyan}" stroke-opacity=".22" stroke-dasharray="2 12" class="dash2"/>
    <ellipse cx="667" cy="158" rx="108" ry="47" fill="none" stroke="{fg}" stroke-opacity=".10"/>
    <g class="pulse"><circle cx="667" cy="158" r="42" fill="{panel}" stroke="{cyan}" stroke-opacity=".68" stroke-width="1.5"/><circle cx="667" cy="158" r="31" fill="none" stroke="{violet}" stroke-opacity=".45" stroke-dasharray="3 6"/><text x="667" y="154" text-anchor="middle" fill="{fg}" font-size="11" font-weight="800" letter-spacing="1.8">BUILD</text><text x="667" y="171" text-anchor="middle" fill="{muted}" font-size="8.5" class="mono">SHIP / SCALE</text></g>
    <g class="float1"><g transform="translate(520 103)"><rect width="90" height="28" rx="14" fill="{panel}" stroke="{violet}" stroke-opacity=".5"/><text x="45" y="18" text-anchor="middle" fill="{fg}" font-size="10" font-weight="700">NEXT.JS</text></g><g transform="translate(726 87)"><rect width="98" height="28" rx="14" fill="{panel}" stroke="{cyan}" stroke-opacity=".5"/><text x="49" y="18" text-anchor="middle" fill="{fg}" font-size="10" font-weight="700">TYPESCRIPT</text></g></g>
    <g class="float2"><g transform="translate(493 175)"><rect width="86" height="28" rx="14" fill="{panel}" stroke="{cyan}" stroke-opacity=".45"/><text x="43" y="18" text-anchor="middle" fill="{fg}" font-size="10" font-weight="700">REACT</text></g><g transform="translate(761 173)"><rect width="72" height="28" rx="14" fill="{panel}" stroke="{violet}" stroke-opacity=".48"/><text x="36" y="18" text-anchor="middle" fill="{fg}" font-size="10" font-weight="700">NODE</text></g></g>
    <g class="float3"><g transform="translate(554 234)"><rect width="82" height="28" rx="14" fill="{panel}" stroke="{violet}" stroke-opacity=".48"/><text x="41" y="18" text-anchor="middle" fill="{fg}" font-size="10" font-weight="700">FLUTTER</text></g><g transform="translate(681 246)"><rect width="68" height="28" rx="14" fill="{panel}" stroke="{cyan}" stroke-opacity=".48"/><text x="34" y="18" text-anchor="middle" fill="{fg}" font-size="10" font-weight="700">AWS</text></g></g>
  </g>
</svg>'''

def stack(theme):
    dark = theme == "dark"
    bg0 = "#090C14" if dark else "#F8F9FC"
    bg1 = "#111425" if dark else "#EEF0F8"
    panel = "#111624" if dark else "#FFFFFF"
    fg = "#F7F8FF" if dark else "#171821"
    muted = "#9AA3BA" if dark else "#656A7C"
    violet = "#8B5CF6" if dark else "#6D4DE0"
    cyan = "#22D3EE" if dark else "#0891B2"
    border = "#2B3147" if dark else "#D8DCE8"

    groups = [
        ("FRONTEND", 35, 55, ["React", "Next.js", "TypeScript", "Tailwind", "UI/UX"]),
        ("BACKEND", 438, 55, ["Node.js", "Prisma", "REST", "OAuth", "Webhooks"]),
        ("CLOUD / DEVOPS", 35, 215, ["AWS", "Docker", "Kubernetes", "K3s", "Cloudflare"]),
        ("MOBILE / AI", 438, 215, ["Flutter", "Firebase", "LLM APIs", "Automation", "Wallet APIs"]),
    ]

    cards = []
    for idx, (title, x, y, items) in enumerate(groups):
        pills = []
        for j, item in enumerate(items):
            row, col = divmod(j, 3)
            px = x + 22 + col * 103
            py = y + 76 + row * 38
            width = 92 if len(item) < 10 else 100
            dot = cyan if (idx + j) % 2 else violet
            pills.append(f'<g transform="translate({px} {py})" class="chip c{(idx+j)%3}"><rect width="{width}" height="27" rx="13.5" fill="{panel}" stroke="{border}"/><circle cx="12" cy="13.5" r="3" fill="{dot}"/><text x="21" y="17" fill="{fg}" font-size="9.2" font-weight="700">{item}</text></g>')
        cards.append(f'<g><rect x="{x}" y="{y}" width="373" height="136" rx="20" fill="{panel}" stroke="{border}"/><text x="{x+22}" y="{y+29}" fill="{muted}" font-size="9.5" class="mono" letter-spacing="1.3">0{idx+1}</text><text x="{x+48}" y="{y+30}" fill="{fg}" font-size="13" font-weight="800" letter-spacing=".7">{title}</text><line x1="{x+22}" y1="{y+46}" x2="{x+351}" y2="{y+46}" stroke="{border}"/>{"".join(pills)}</g>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="846" height="390" viewBox="0 0 846 390" role="img" aria-label="Technical capability map">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg0}"/><stop offset="1" stop-color="{bg1}"/></linearGradient>
    <radialGradient id="core"><stop offset="0" stop-color="{violet}" stop-opacity=".20"/><stop offset="1" stop-color="{violet}" stop-opacity="0"/></radialGradient>
    <style>
      text {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .mono {{ font-family: "JetBrains Mono", "SFMono-Regular", Consolas, monospace; }}
      .chip {{ animation: breathe 4s ease-in-out infinite; transform-box: fill-box; transform-origin:center; }} .c1 {{ animation-delay:.8s }} .c2 {{ animation-delay:1.6s }}
      .path {{ stroke-dasharray:4 8; animation:flow 10s linear infinite; }}
      @keyframes breathe {{ 0%,100% {{ opacity:.82 }} 50% {{ opacity:1 }} }}
      @keyframes flow {{ to {{ stroke-dashoffset:-96 }} }}
      @media (prefers-reduced-motion: reduce) {{ .chip,.path {{ animation:none !important }} }}
    </style>
  </defs>
  <rect width="846" height="390" rx="24" fill="url(#bg)"/>
  <ellipse cx="423" cy="195" rx="300" ry="180" fill="url(#core)"/>
  <g fill="none" stroke="{violet}" stroke-opacity=".20" class="path"><path d="M408 123 C423 144 423 153 423 174"/><path d="M438 123 C423 144 423 153 423 174"/><path d="M408 271 C423 249 423 238 423 216"/><path d="M438 271 C423 249 423 238 423 216"/></g>
  <g><circle cx="423" cy="195" r="46" fill="{panel}" stroke="{cyan}" stroke-opacity=".55"/><circle cx="423" cy="195" r="34" fill="none" stroke="{violet}" stroke-opacity=".42" stroke-dasharray="3 6"><animateTransform attributeName="transform" type="rotate" from="0 423 195" to="360 423 195" dur="18s" repeatCount="indefinite"/></circle><text x="423" y="191" text-anchor="middle" fill="{fg}" font-size="12" font-weight="800" letter-spacing="1.4">PRODUCT</text><text x="423" y="207" text-anchor="middle" fill="{muted}" font-size="8.6" class="mono">ENGINEERING</text></g>
  {"".join(cards)}
  <text x="423" y="372" text-anchor="middle" fill="{muted}" font-size="9.5" class="mono" letter-spacing=".8">WEB · MOBILE · CLOUD · DEVOPS · INTEGRATIONS · AI</text>
</svg>'''

for theme in ("dark", "light"):
    (OUT / f"hero.{theme}.svg").write_text(hero(theme), encoding="utf-8")
    (OUT / f"stack.{theme}.svg").write_text(stack(theme), encoding="utf-8")

print("Generated custom SVG profile assets.")
