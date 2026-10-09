import fs from 'fs';

const svg = fs.readFileSync('public/art/landscape-full-pure-vector.svg', 'utf8');
const inkMatch = svg.match(/<g class="svg-ink-layer"[^>]*>([\s\S]*?)<\/g>/);
if (inkMatch) {
  const paths = inkMatch[1].match(/<path[^>]*\/>/g) || [];
  console.log('Total paths in svg-ink-layer:', paths.length);
  console.log('Total chars in svg-ink-layer:', inkMatch[1].length);
  for (let i = 0; i < Math.min(paths.length, 10); i++) {
    console.log(`Path ${i}:`, paths[i].slice(0, 100));
  }
} else {
  console.log('No inkMatch found');
}
