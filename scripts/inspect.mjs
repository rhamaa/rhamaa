import fs from 'fs';

const svg = fs.readFileSync('public/art/landscape-full-pure-vector.svg', 'utf8');
const lines = svg.split('\n');
console.log('Total lines:', lines.length);
for (let i = 0; i < Math.min(lines.length, 120); i++) {
  if (lines[i].includes('<g') || lines[i].includes('<!--') || lines[i].includes('id=')) {
    console.log(`${i}: ${lines[i].trim()}`);
  }
}
