# Project: Landscape Artwork Reconstruction & Seam Elimination

## Architecture
- Root SVG container: `src/components/LandscapeArt.astro` with `viewBox="0 0 1024 409"`, `width="1024"`, `height="409"`.
- Clean 4-Layer Semantic Hierarchy:
  1. **Layer 1: Deep Sky & Celestial Sun**
     - `Sun.astro` (`.art-layer--sun`) with radial gradient `#sun-gradient` and glow filter `#solar-corona-glow`.
     - Elements: `.sun-core`, `.sun-halo`, `.sun-corona`.
  2. **Layer 2: Distant Mountains & Ridges**
     - `MountainLeft.astro`, `MountainRight.astro`, `MountainFarRight.astro`.
     - Crags and hatching preserved, artificial vertical partition cuts ($x=251, 314$) and horizontal ridge slit ($y=117-120$) healed.
  3. **Layer 3: Seamless Organic Terrain & Vegetation**
     - Continuous, organic vector etching where rolling hills, meadow, tree trunks, root flares, and foliage form an unbroken contour.
     - Eliminates horizontal cuts ($y=330$), vertical split ($x=725$), floating pine gap ($y=299$), and flat ridge cuts.
     - Subcomponents: `HillsLeft.astro`, `ButteLeft.astro`, `Meadow.astro`, `TreeOak.astro`, `TreeTwin.astro`, `TreePine.astro` (or unified organic terrain with synchronized motion).
  4. **Layer 4: Sky Cyber IoT Circuits & Telemetry Overlays**
     - `CircuitLeft.astro` (`.art-layer--circuit-left`), `CircuitRight.astro` (`.art-layer--circuit-right`), `TelemetryNodes.astro` (`.art-layer--telemetry-nodes`).
     - Distinct vector overlays floating above the landscape with pulsing beacons (`.beacon-pulse`) and interactive nodes (`.interactive-node`).
- **Motion Engine**: `src/scripts/motion.ts`
  - Celestial sun ambient float (`sine.inOut`, `y: -14, x: 5`, 5.5s) and corona pulse.
  - Telemetry beacon pulse loop (`scale: 1.5, opacity: 0`) and interactive hover zoom.
  - Spatial 3D parallax on `.contact-section` with synchronized foreground displacements to eliminate seam tearing.
  - Full support for `prefers-reduced-motion: reduce`.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Seamless Organic Terrain & Vegetation | Unify trees, roots, and ground terrain into seamless vector etching; eliminate flat cuts at y=330, x=725, y=299, and ridge cuts. | M1 | ORIGINAL_REQUEST R1 |
| 2 | Semantic Celestial & Cyber Layering | Preserve Sun Orb in deep sky behind mountains and Cyber IoT Circuit / Telemetry overlays in sky. | M1 | ORIGINAL_REQUEST R2 |
| 3 | GSAP Antigravity Motion Compatibility | Sun float loop, telemetry beacon pulses, synchronized parallax without seam tearing, prefers-reduced-motion. | M1 | ORIGINAL_REQUEST R3 |
| 4 | Clean SVG Hierarchy & ViewBox | Keep viewBox="0 0 1024 409", width="1024", height="409", valid Astro SVG markup. | M1 | ORIGINAL_REQUEST AC |
| 5 | Test Suite & Zero Regressions | Pass all 16 tests cleanly via `npm test`. | M1 | ORIGINAL_REQUEST AC |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Landscape Artwork Reconstruction & Motion Harmonization | Reconstruct LandscapeArt.astro and landscape subcomponents for seamless organic contour, harmonize motion.ts parallax, pass npm test | none | IN_PROGRESS |

## Interface Contracts
### LandscapeArt.astro ↔ ContactBlock.astro
- Rendered in `ContactBlock.astro` as `<LandscapeArt class="contact-section__art" />`.
- Outer SVG element attributes: `class="reference-art reference-art--landscape ..."`, `viewBox="0 0 1024 409"`, `width="1024"`, `height="409"`.

### LandscapeArt.astro ↔ src/scripts/motion.ts
- Preserved CSS selector hooks:
  - `.reference-art--landscape`
  - `.art-layer--sun`, `.sun-corona`
  - `.art-layer--mountain-left`, `.art-layer--mountain-right`, `.art-layer--mountain-far-right`
  - `.art-layer--hills-left`, `.art-layer--butte-left`
  - `.art-layer--foreground-meadow`, `.art-layer--tree-oak`, `.art-layer--tree-twin`, `.art-layer--tree-pine` (and shadow layers)
  - `.art-layer--circuit-left`, `.art-layer--circuit-right`
  - `.interactive-node`, `.beacon-pulse`

## Code Layout
- `src/components/LandscapeArt.astro` — Main SVG container
- `src/components/landscape/*` — Modular SVG layers
- `src/scripts/motion.ts` — GSAP animation & parallax logic
- `tests/*` — Read-only verification test suite
