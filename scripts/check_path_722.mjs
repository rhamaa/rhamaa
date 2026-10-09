import fs from 'fs';

const fullSvg = fs.readFileSync('public/art/landscape-full-pure-vector.svg', 'utf8');
const pMatch = fullSvg.match(/<path[^>]*transform="translate\(722,\s*213\)"[^>]*>/);
if (pMatch) {
  console.log('Path at 722,213 in fullSvg:');
  console.log(pMatch[0].slice(0, 500));
} else {
  console.log('No exact match at translate(722, 213)');
}
