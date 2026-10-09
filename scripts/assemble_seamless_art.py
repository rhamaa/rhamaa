import re

with open('public/art/seamless/terrain_organic.svg', 'r', encoding='utf-8') as f:
    t_svg = f.read()

t_paths = [p for p in re.findall(r'<path[^>]+/>', t_svg) if not ('d="M0 0 C337.92 0' in p and '1024 409' in p)]

with open('public/art/seamless/circuits.svg', 'r', encoding='utf-8') as f:
    c_svg = f.read()

c_paths = [p for p in re.findall(r'<path[^>]+/>', c_svg) if not ('d="M0 0 C337.92 0' in p and '1024 409' in p)]

astro_component = f'''---
import Sun from './landscape/Sun.astro';
import TelemetryNodes from './landscape/TelemetryNodes.astro';

interface Props {{
  class?: string;
}}
const {{ class: className = '' }} = Astro.props;
---
<svg class={{`reference-art reference-art--landscape ${{className}}`}} viewBox="0 0 1024 409" width="1024" height="409" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
  <defs>
    <filter id="solar-corona-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="15" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <radialGradient id="sun-gradient" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffd56b" />
      <stop offset="70%" stop-color="#e7ac43" />
      <stop offset="100%" stop-color="#c98a24" />
    </radialGradient>
  </defs>

  <!-- Canvas Base (Transparent to blend with page theme) -->
  <rect width="1024" height="409" fill="transparent" />

  <!-- ============================================================ -->
  <!-- LAYER 1: Deep Sky & Celestial Sun Orb (Behind Mountains)     -->
  <!-- ============================================================ -->
  <Sun />

  <!-- ============================================================ -->
  <!-- LAYER 2: Seamless Unified Organic Terrain & Vegetation       -->
  <!-- Mountains, hills, meadow, trees, roots, and ground contours  -->
  <!-- flow as an unbroken, continuous hand-drawn etching           -->
  <!-- ============================================================ -->
  <g id="sub-svg-organic-terrain" class="sub-svg sub-svg--organic-terrain art-layer art-layer--organic-terrain" fill="#172724" fill-rule="evenodd" style="transform-origin: 512px 300px;">
    {''.join(t_paths)}
  </g>

  <!-- ============================================================ -->
  <!-- LAYER 3: Sky Cyber IoT Circuits & Grids                      -->
  <!-- ============================================================ -->
  <g id="sub-svg-circuits" class="sub-svg sub-svg--circuits art-layer art-layer--circuit-left" fill="#172724" fill-rule="evenodd" style="transform-origin: 512px 100px;">
    {''.join(c_paths)}
  </g>

  <!-- ============================================================ -->
  <!-- LAYER 4: Interactive Telemetry Sensor Nodes & Beacons        -->
  <!-- ============================================================ -->
  <TelemetryNodes />
</svg>
'''

with open('src/components/LandscapeArt.astro', 'w', encoding='utf-8') as f:
    f.write(astro_component)

print("LandscapeArt.astro updated with seamless unified terrain! File size:", len(astro_component))
