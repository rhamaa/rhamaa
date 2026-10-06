import assert from 'node:assert/strict';
import { readFile, readdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import test from 'node:test';

const root = dirname(fileURLToPath(import.meta.url));
const htmlPath = join(root, '../dist/index.html');

async function readPage() {
  return readFile(htmlPath, 'utf8');
}

async function readStyles() {
  const html = await readPage();
  const assetDirectory = join(root, '../dist/_astro');
  const availableFiles = await readdir(assetDirectory);
  const linkedFiles = [...html.matchAll(/href="\/_astro\/([^\"]+\.css)"/g)].map(([, file]) => file);

  assert.ok(linkedFiles.length > 0, 'the static page should link its built stylesheets');
  assert.ok(linkedFiles.every((file) => availableFiles.includes(file)), 'all linked stylesheets should exist');
  return (await Promise.all(linkedFiles.map((file) => readFile(join(assetDirectory, file), 'utf8')))).join('\n');
}

test('static_page_has_primary_navigation_targets', async () => {
  const html = await readPage();

  for (const section of ['projects', 'timeline', 'about', 'contact']) {
    assert.match(html, new RegExp(`id="${section}"`));
    assert.match(html, new RegExp(`href="#${section}"`));
  }
});

test('static_page_declares_English_as_the_default_language', async () => {
  const html = await readPage();

  assert.match(html, /<html lang="en">/);
  assert.match(html, /property="og:locale" content="en_US"/);
});

test('static_page_keeps_project_statuses_visible', async () => {
  const html = await readPage();

  assert.match(html, /In development/);
  assert.match(html, /R&amp;D prototype|R&D prototype/);
});

test('static_page_omits_unconfirmed_role_and_education_dates', async () => {
  const html = await readPage();

  assert.doesNotMatch(html, /Juni 2025|2021–2025/);
});

test('static_page_uses_the_verified_linkedin_contact', async () => {
  const html = await readPage();

  assert.match(html, /https:\/\/id\.linkedin\.com\/in\/nuurrhama\/en/);
  assert.match(html, /aria-label="[^\"]*LinkedIn[^\"]*"/);
});

test('hero_displays_professional_position_and_message', async () => {
  const html = await readPage();

  assert.ok(html.includes('Full-stack engineer'), 'the professional position should be visible');
  assert.ok(html.includes('Building technology from devices to applications'));
});

test('static_page_respects_keyboard_entry_and_reduced_motion', async () => {
  const html = await readPage();
  const styles = await readStyles();

  assert.ok(html.includes('class="skip-link"'));
  assert.ok(html.includes('href="#main-content"'));
  assert.ok(styles.includes('prefers-reduced-motion:reduce'));
  assert.ok(styles.includes('scroll-behavior:auto'));
});

test('external_links_open_safely', async () => {
  const html = await readPage();
  const externalLinks = [...html.matchAll(/<a\b[^>]*target="_blank"[^>]*>/g)].map(([link]) => link);

  assert.ok(externalLinks.length > 0);
  for (const link of externalLinks) assert.match(link, /rel="noreferrer"/);
});
