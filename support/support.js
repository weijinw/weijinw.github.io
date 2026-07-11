'use strict';

const SUPPORT_APPS = Object.freeze({
  general: Object.freeze({
    label: 'General support',
    prefix: '[App Support]',
    returnPath: '/',
  }),
  fitcycles: Object.freeze({
    label: 'FitCycles',
    prefix: '[FitCycles Support]',
    returnPath: '/fitcycles/',
  }),
  speedlens: Object.freeze({
    label: 'SpeedLens',
    prefix: '[SpeedLens Support]',
    returnPath: '/speedlens/',
  }),
  alwayson: Object.freeze({
    label: 'AlwaysOn Desk Clock',
    prefix: '[AlwaysOn Support]',
    returnPath: '/alwayson/',
  }),
});

const FORM_SELECTORS = Object.freeze({
  form: '#support-form',
  app: '#support-app',
  title: '#support-title-input',
  message: '#support-message',
  prefix: '#subject-prefix',
  cancel: '#cancel-support',
});

const RECIPIENT_CODES = Object.freeze([
  119, 101, 108, 107, 105, 110, 46, 119, 111, 110, 103,
  64, 103, 109, 97, 105, 108, 46, 99, 111, 109,
]);

function normalizeAppKey(value) {
  const key = String(value || '').trim().toLowerCase();
  return Object.prototype.hasOwnProperty.call(SUPPORT_APPS, key) ? key : 'general';
}

function getSupportConfig(appKey) {
  return SUPPORT_APPS[normalizeAppKey(appKey)];
}

function buildSubject(appKey, title) {
  const cleanTitle = String(title || '').trim();
  return `${getSupportConfig(appKey).prefix} ${cleanTitle}`.trim();
}

function getRecipient() {
  return RECIPIENT_CODES.map((code) => String.fromCharCode(code)).join('');
}

function buildMailtoUrl({ appKey, title, message }) {
  const subject = buildSubject(appKey, title);
  const body = String(message || '').trim();
  return `mailto:${getRecipient()}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}

function getReturnPath(appKey) {
  return getSupportConfig(appKey).returnPath;
}

function updatePrefixPreview(appSelect, preview) {
  if (!preview) return;
  preview.textContent = `Email subject starts with ${getSupportConfig(appSelect.value).prefix}`;
}

function initSupportForm(doc = document, win = window) {
  const form = doc.querySelector(FORM_SELECTORS.form);
  if (!form) return;

  const appSelect = doc.querySelector(FORM_SELECTORS.app);
  const titleInput = doc.querySelector(FORM_SELECTORS.title);
  const messageInput = doc.querySelector(FORM_SELECTORS.message);
  const prefixPreview = doc.querySelector(FORM_SELECTORS.prefix);
  const cancelButton = doc.querySelector(FORM_SELECTORS.cancel);

  const params = new URLSearchParams(win.location.search);
  appSelect.value = normalizeAppKey(params.get('app'));
  updatePrefixPreview(appSelect, prefixPreview);

  appSelect.addEventListener('change', () => {
    updatePrefixPreview(appSelect, prefixPreview);
  });

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    win.location.href = buildMailtoUrl({
      appKey: appSelect.value,
      title: titleInput.value,
      message: messageInput.value,
    });
  });

  cancelButton.addEventListener('click', () => {
    if (doc.referrer) {
      try {
        const referrer = new URL(doc.referrer);
        if (referrer.origin === win.location.origin) {
          win.history.back();
          return;
        }
      } catch {
        // Fall through to the app-specific return path.
      }
    }

    win.location.href = getReturnPath(appSelect.value);
  });
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    SUPPORT_APPS,
    FORM_SELECTORS,
    normalizeAppKey,
    buildSubject,
    buildMailtoUrl,
    getReturnPath,
    initSupportForm,
  };
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => initSupportForm());
  } else {
    initSupportForm();
  }
}
