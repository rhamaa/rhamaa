import fs from 'fs';

const trace = fs.readFileSync('public/art/test_color_trace.svg', 'utf8');
console.log('test_color_trace size:', trace.length);
console.log('head:', trace.slice(0, 500));
