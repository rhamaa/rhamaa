import { gsap } from 'gsap';

export function initAntigravityMotion() {
  if (typeof window === 'undefined') return;

  // Respect user preference for reduced motion (Web Accessibility / WCAG Guidelines)
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) return;

  // 1. Hero Art Antigravity Levitation
  const heroArt = document.querySelector('.hero__art');
  if (heroArt) {
    gsap.to(heroArt, {
      y: -14,
      rotation: 0.5,
      duration: 3.8,
      ease: 'sine.inOut',
      repeat: -1,
      yoyo: true,
    });
  }

  // 2. Journey Lines subtle breathing oscillation
  const journeyLines = document.querySelector('.journey-lines');
  if (journeyLines) {
    gsap.to(journeyLines, {
      y: -8,
      rotation: -0.4,
      duration: 5,
      ease: 'sine.inOut',
      repeat: -1,
      yoyo: true,
    });
  }

  // 3. Contact Section Art Weightless Drift
  const contactArt = document.querySelector('.contact-section__art');
  if (contactArt) {
    gsap.to(contactArt, {
      y: -12,
      duration: 4.2,
      ease: 'sine.inOut',
      repeat: -1,
      yoyo: true,
    });
  }

  // 4. SVG Elements Levitation & Micro-interactions
  // Ambient glows pulsing gently like living circuits
  const glowElements = document.querySelectorAll('.art-ambient-glow');
  glowElements.forEach((glow, idx) => {
    gsap.to(glow, {
      scale: 1.15,
      opacity: 0.85,
      duration: 2.4 + (idx % 3) * 0.5,
      ease: 'sine.inOut',
      repeat: -1,
      yoyo: true,
    });
  });

  // Floating subcards and inner cards drifting independently
  const floatingCards = document.querySelectorAll('.art-floating-card');
  floatingCards.forEach((card, idx) => {
    gsap.to(card, {
      y: -6,
      duration: 3 + (idx % 2) * 0.8,
      ease: 'sine.inOut',
      repeat: -1,
      yoyo: true,
    });
  });

  // Orbit nodes floating in small circles/arcs
  const orbitNodes = document.querySelectorAll('.art-orbit-node');
  orbitNodes.forEach((node, idx) => {
    gsap.to(node, {
      y: (idx % 2 === 0 ? -8 : 8),
      x: (idx % 2 === 0 ? 5 : -5),
      duration: 2.8 + (idx % 3) * 0.4,
      ease: 'sine.inOut',
      repeat: -1,
      yoyo: true,
    });
  });

  // Tech pulse components (sensors & telemetry activity)
  const pulses = document.querySelectorAll('.art-pulse');
  pulses.forEach((pulse, idx) => {
    gsap.to(pulse, {
      opacity: 0.35,
      duration: 1.5 + (idx % 2) * 0.5,
      ease: 'power2.inOut',
      repeat: -1,
      yoyo: true,
    });
  });

  // 5. Multi-Layer Topological Landscape Antigravity Motion Engine
  const landscapeContainer = document.querySelector('.contact-section') as HTMLElement | null;
  const landscapeSvg = document.querySelector('.reference-art--landscape') as SVGSVGElement | null;
  
  // Distinct Semantic Layer References
  const layerSun = document.querySelector('.art-layer--sun');
  const sunCorona = document.querySelector('.sun-corona');
  const organicTerrain = document.querySelector('.art-layer--organic-terrain');
  const circuits = document.querySelector('.art-layer--circuit-left, .sub-svg--circuits');
  const interactiveNodes = document.querySelectorAll('.interactive-node');
  const beaconPulses = document.querySelectorAll('.beacon-pulse');

  // Ambient 1: Celestial Sun floating gracefully behind mountain horizon
  if (layerSun) {
    gsap.to(layerSun, {
      y: -14,
      x: 5,
      duration: 5.5,
      ease: 'sine.inOut',
      repeat: -1,
      yoyo: true,
    });
  }

  // Ambient 2: Solar Corona Pulsing
  if (sunCorona) {
    gsap.to(sunCorona, {
      scale: 1.14,
      opacity: 0.38,
      duration: 3.4,
      ease: 'sine.inOut',
      repeat: -1,
      yoyo: true,
    });
  }

  // Ambient 3: Unified Organic Terrain subtle grounded breathing
  if (organicTerrain) {
    gsap.to(organicTerrain, {
      y: -3,
      duration: 6,
      ease: 'sine.inOut',
      repeat: -1,
      yoyo: true,
    });
  }

  // Ambient 4: Sky IoT Circuits data stream vibration
  if (circuits) {
    gsap.to(circuits, {
      y: -5,
      duration: 3.4,
      ease: 'sine.inOut',
      repeat: -1,
      yoyo: true,
    });
  }

  // Ambient 5: Radiating Beacon Pulses
  beaconPulses.forEach((pulse, idx) => {
    gsap.to(pulse, {
      scale: 1.5,
      opacity: 0,
      transformOrigin: 'center center',
      duration: 2.3 + (idx % 3) * 0.4,
      ease: 'power2.out',
      repeat: -1,
    });
  });

  // Interactive Hover & Deep Multi-Plane Spatial Parallax
  if (landscapeContainer && landscapeSvg) {
    landscapeContainer.addEventListener('mousemove', (e: MouseEvent) => {
      const rect = landscapeContainer.getBoundingClientRect();
      const nx = (e.clientX - rect.left) / rect.width - 0.5;
      const ny = (e.clientY - rect.top) / rect.height - 0.5;

      // Master 3D Spatial Canvas Tilt
      gsap.to(landscapeSvg, {
        rotateY: nx * 9,
        rotateX: -ny * 7,
        duration: 0.8,
        ease: 'power2.out',
      });

      // Layer 1 (Sun): Deepest celestial plane, shifts in counter-parallax
      if (layerSun) gsap.to(layerSun, { x: -nx * 32, y: -ny * 22, duration: 1.2, ease: 'power2.out' });

      // Layer 2 (Organic Terrain): Grounded foreground & mountain mesh moves seamlessly without seam tearing
      if (organicTerrain) gsap.to(organicTerrain, { x: nx * 14, y: ny * 9, duration: 0.85, ease: 'power2.out' });

      // Layer 3 (Circuits): Floating vector telemetry in the sky
      if (circuits) gsap.to(circuits, { x: nx * 20, y: ny * 13, duration: 0.65, ease: 'power2.out' });

      // Layer 4: Interactive Telemetry Nodes
      interactiveNodes.forEach((node, idx) => {
        gsap.to(node, {
          x: nx * (24 + (idx % 3) * 4),
          y: ny * (18 + (idx % 2) * 4),
          duration: 0.5,
          ease: 'power2.out',
        });
      });
    });

    landscapeContainer.addEventListener('mouseleave', () => {
      // Smoothly return all layers to baseline equilibrium
      gsap.to(landscapeSvg, { rotateY: 0, rotateX: 0, duration: 1.4, ease: 'power2.out' });
      if (layerSun) gsap.to(layerSun, { x: 0, y: 0, duration: 1.4, ease: 'power2.out' });
      if (organicTerrain) gsap.to(organicTerrain, { x: 0, y: 0, duration: 1.4, ease: 'power2.out' });
      if (circuits) gsap.to(circuits, { x: 0, y: 0, duration: 1.4, ease: 'power2.out' });
      interactiveNodes.forEach((node) => {
        gsap.to(node, { x: 0, y: 0, duration: 1.2, ease: 'power2.out' });
      });
    });

    // Individual Node Hover Excitement
    interactiveNodes.forEach((node) => {
      node.addEventListener('mouseenter', () => {
        gsap.to(node, { scale: 1.5, duration: 0.3, ease: 'back.out(2)' });
      });
      node.addEventListener('mouseleave', () => {
        gsap.to(node, { scale: 1, duration: 0.4, ease: 'power2.out' });
      });
    });
  }

  // 5. Interactive Mouse Parallax for Spatial Depth
  const heroInner = document.querySelector('.hero__inner') as HTMLElement | null;
  if (heroInner && heroArt) {
    heroInner.addEventListener('mousemove', (e: MouseEvent) => {
      const rect = heroInner.getBoundingClientRect();
      const relX = (e.clientX - rect.left) / rect.width - 0.5;
      const relY = (e.clientY - rect.top) / rect.height - 0.5;

      gsap.to(heroArt, {
        x: relX * 22,
        y: relY * 18,
        rotateY: relX * 4,
        rotateX: -relY * 4,
        duration: 0.8,
        ease: 'power2.out',
      });
    });

    heroInner.addEventListener('mouseleave', () => {
      gsap.to(heroArt, {
        x: 0,
        rotateY: 0,
        rotateX: 0,
        duration: 1.2,
        ease: 'power2.out',
      });
    });
  }
}
