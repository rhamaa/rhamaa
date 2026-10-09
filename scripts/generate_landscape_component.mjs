import fs from 'fs';

const svgContent = fs.readFileSync('public/art/landscape-full-pure-vector.svg', 'utf-8');

// Extract inner content of svg
const match = svgContent.match(/<svg[^>]*>([\s\S]*?)<\/svg>/i);
if (!match) throw new Error("Could not extract SVG inner contents");

const inner = match[1];

const component = `---
interface Props {
  class?: string;
}
const { class: className = '' } = Astro.props;
---
<svg class={\`reference-art reference-art--landscape \${className}\`} viewBox="0 0 1024 409" width="1024" height="409" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
${inner}
</svg>
`;

fs.writeFileSync('src/components/LandscapeArt.astro', component, 'utf-8');
console.log('Successfully wrote src/components/LandscapeArt.astro! File size:', component.length);
