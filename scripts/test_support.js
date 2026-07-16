'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const support = require('../support/support.js');

assert.equal(support.normalizeAppKey('fitcycles'), 'fitcycles');
assert.equal(support.normalizeAppKey('SPEEDLENS'), 'speedlens');
assert.equal(support.normalizeAppKey('HEART-BASELINE'), 'heart-baseline');
assert.equal(support.normalizeAppKey('unknown'), 'general');
assert.equal(support.normalizeAppKey(''), 'general');

assert.equal(
  support.buildSubject('fitcycles', 'Timer stops early'),
  '[FitCycles Support] Timer stops early'
);
assert.equal(
  support.buildSubject('speedlens', 'Export issue'),
  '[SpeedLens Support] Export issue'
);
assert.equal(
  support.buildSubject('alwayson', 'Calendar is blank'),
  '[AlwaysOn Support] Calendar is blank'
);
assert.equal(
  support.buildSubject('heart-baseline', 'Watch check did not start'),
  '[Heart Baseline Support] Watch check did not start'
);
assert.equal(
  support.buildSubject('general', 'Website question'),
  '[App Support] Website question'
);

const mailto = support.buildMailtoUrl({
  appKey: 'fitcycles',
  title: 'Timer & Watch',
  message: 'Steps:\n1. Start workout\n2. Open Watch',
});
assert.match(mailto, /^mailto:/);
assert.match(mailto, /subject=%5BFitCycles%20Support%5D%20Timer%20%26%20Watch/);
assert.match(mailto, /body=Steps%3A%0A1.%20Start%20workout%0A2.%20Open%20Watch/);

assert.equal(support.getReturnPath('fitcycles'), '/fitcycles/');
assert.equal(support.getReturnPath('speedlens'), '/speedlens/');
assert.equal(support.getReturnPath('alwayson'), '/alwayson/');
assert.equal(support.getReturnPath('heart-baseline'), '/heart-baseline/');
assert.equal(support.getReturnPath('general'), '/');

const html = fs.readFileSync(path.join(__dirname, '..', 'support', 'index.html'), 'utf8');
for (const selector of Object.values(support.FORM_SELECTORS)) {
  assert.match(html, new RegExp(`id=["']${selector.slice(1)}["']`));
}
assert.match(html, /<option value="heart-baseline">Heart Baseline<\/option>/);

const source = fs.readFileSync(path.join(__dirname, '..', 'support', 'support.js'), 'utf8');
const literalRecipient = [119, 101, 108, 107, 105, 110, 46, 119, 111, 110, 103, 64, 103, 109, 97, 105, 108, 46, 99, 111, 109]
  .map((code) => String.fromCharCode(code))
  .join('');
assert.equal(source.includes(literalRecipient), false);

console.log('Support form tests passed.');
