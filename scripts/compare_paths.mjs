import fs from 'fs';

const fullSvg = fs.readFileSync('public/art/landscape-full-pure-vector.svg', 'utf8');
const oak = fs.readFileSync('src/components/landscape/TreeOak.astro', 'utf8');
const meadow = fs.readFileSync('src/components/landscape/Meadow.astro', 'utf8');

console.log('Full SVG length:', fullSvg.length);
console.log('Oak length:', oak.length);
console.log('Meadow length:', meadow.length);

// Check if paths in oak are also in fullSvg
const oakPaths = (oak.match(/<path[^>]*\/>/g) || []);
console.log('Oak paths count:', oakPaths.length);

let inFull = 0;
for (const p of oakPaths) {
  if (fullSvg.includes(p)) inFull++;
}
console.log('Oak paths found in fullSvg:', inFull, 'out of', oakPaths.length);
