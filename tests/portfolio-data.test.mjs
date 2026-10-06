import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import test from 'node:test';

const root = dirname(fileURLToPath(import.meta.url));
const dataPath = join(root, '../src/data/portfolio.json');

async function loadPortfolio() {
  return JSON.parse(await readFile(dataPath, 'utf8'));
}

test('contact_contains_only_linkedin', async () => {
  const portfolio = await loadPortfolio();

  assert.deepEqual(Object.keys(portfolio.contact), ['linkedin']);
  assert.equal(portfolio.contact.linkedin, 'https://id.linkedin.com/in/nuurrhama/en');
});

test('project_links_are_verified_https_urls', async () => {
  const portfolio = await loadPortfolio();
  const linkedProjects = portfolio.projects.filter((project) => project.repositoryUrl !== null);

  assert.ok(linkedProjects.length > 0);
  for (const project of linkedProjects) {
    const repository = new URL(project.repositoryUrl);
    assert.equal(repository.protocol, 'https:', `${project.title} must use HTTPS`);
    assert.equal(repository.hostname, 'github.com', `${project.title} must link to GitHub`);
    assert.equal(repository.pathname.split('/')[1], 'rhamaa', `${project.title} must use the verified owner`);
  }
});

test('prototype_labels_remain_visible', async () => {
  const portfolio = await loadPortfolio();
  const captr = portfolio.projects.find((project) => project.id === 'captr-studio');
  const kirei = portfolio.projects.find((project) => project.id === 'kirei-solar');

  assert.equal(captr?.status, 'Dalam pengembangan');
  assert.equal(kirei?.status, 'Prototipe R&D');
});

test('unconfirmed_role_and_education_dates_are_omitted', async () => {
  const portfolio = await loadPortfolio();
  const kirei = portfolio.experience.find((item) => item.company === 'Kirei');
  const ukri = portfolio.education.find((item) => item.institution === 'Universitas Kebangsaan Republik Indonesia');

  assert.equal(kirei?.period, undefined);
  assert.equal(ukri?.period, undefined);
});

test('timeline_is_chronological', async () => {
  const portfolio = await loadPortfolio();
  const firstYears = portfolio.timeline.map((item) => Number(item.period.match(/\d{4}/)?.[0]));
  const projectIds = new Set(portfolio.projects.map((project) => project.id));

  assert.ok(firstYears.every(Number.isFinite));
  assert.deepEqual(firstYears, [...firstYears].sort((a, b) => a - b));
  for (const phase of portfolio.timeline) {
    for (const id of phase.projectIds) assert.ok(projectIds.has(id), `${id} must exist in projects`);
  }
});
