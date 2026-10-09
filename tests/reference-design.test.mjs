import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const readPage = () => readFile(new URL('../dist/index.html', import.meta.url), 'utf8');

test('every featured project has an accessible detail view and repository links where available', async () => {
  const html = await readPage();
  for (const id of ['captr-studio', 'inara-ai', 'rhamaa-cli', 'rhamaa-cms', 'runutin', 'kirei-solar']) {
    assert.match(html, new RegExp(`data-project-open="${id}"`));
    assert.match(html, new RegExp(`<dialog[^>]*id="detail-${id}"`));
  }
  assert.ok(html.includes('https://github.com/RhamaaCMS/RhamaaCLI'));
  assert.ok(html.includes('https://github.com/RhamaaCMS/RhamaaCMS'));
  const runutin = html.match(/<dialog[^>]*id="detail-runutin"[\s\S]*?<\/dialog>/)?.[0];
  assert.ok(runutin);
  assert.doesNotMatch(runutin, /href="https:/);
});

test('experience descriptions remain available through native keyboard-accessible disclosures', async () => {
  const html = await readPage();
  assert.equal((html.match(/<details class="experience-item"/g) || []).length, 4);
  assert.match(html, /<summary[\s\S]*?Kirei/);
  assert.match(html, /Built an IoT temperature-monitoring device/);
});
