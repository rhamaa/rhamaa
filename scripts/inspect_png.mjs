import fs from 'fs';

const buf = fs.readFileSync('public/art/landscape-art.png');
const width = buf.readUInt32BE(16);
const height = buf.readUInt32BE(20);
console.log(`landscape-art.png dimensions: ${width}x${height}`);
