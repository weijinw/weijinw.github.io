# FitCycles Privacy Minimal Correction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Correct the FitCycles privacy policy so it accurately describes local SwiftData storage, Apple Health access, Apple Watch behavior, local Live Activities, and the absence of developer-side data collection.

**Architecture:** Keep the existing privacy-policy page structure, navigation, CSS, and support link. Replace only the inaccurate policy copy inside `fitcycles/privacy-policy/index.html`, then verify the required facts and removed claims with a deterministic inline Python content check plus the repository’s existing static-site validator.

**Tech Stack:** Static HTML, Python 3 standard library, existing `scripts/check_site.py` validator.

## Global Constraints

- This is a minimal correction, not a full rewrite.
- Preserve the existing headings and page layout.
- Do not modify CSS, routes, navigation structure, FitCycles code, permissions, App Store privacy labels, or iCloud behavior.
- Keep the existing FitCycles support-form link.
- Use July 11, 2026 as the policy effective date.
- FitCycles has no internet connection, no developer-operated servers, and no analytics, advertising, crash-reporting, or third-party SDKs.
- SwiftData stores timer routines, app settings, and completed workout history locally; app data is not synced through iCloud.
- Apple Health data is read on demand for workouts, active energy, exercise time, and heart rate, and is not copied into SwiftData.
- Completed workouts may be written to Apple Health after permission is granted.
- The Apple Watch app can run the timer, start a workout, sync timer state to iPhone, and write completed workouts directly to Apple Health.
- Live Activities are updated locally and do not use remote push notifications or a backend.

---

### Task 1: Correct and verify the FitCycles privacy policy

**Files:**
- Modify: `fitcycles/privacy-policy/index.html:32-60`

**Interfaces:**
- Consumes: The approved design in `docs/superpowers/specs/2026-07-11-fitcycles-privacy-minimal-correction-design.md`.
- Produces: A privacy policy whose copy matches the confirmed FitCycles data flow while preserving the existing page shell, navigation, footer, and support route.

- [ ] **Step 1: Run a failing content test against the current policy**

Run from the repository root:

```bash
python3 - <<'PY'
from pathlib import Path

policy = Path("fitcycles/privacy-policy/index.html").read_text(encoding="utf-8")

required = (
    "stored locally on your device using SwiftData",
    "workouts, active energy, exercise time, and heart rate",
    "not copied into the app's SwiftData store",
    "Apple Watch app can run the timer",
    "Live Activities are updated locally",
    "does not include analytics, advertising, crash-reporting, or third-party SDKs",
    "This Privacy Policy is effective as of July 11, 2026.",
)

removed = (
    "collects absolutely no personal data",
    "does not use any third-party services, SDKs, or APIs",
    "there is no data to retain",
    "there is no user information that needs safeguarding",
)

missing = [phrase for phrase in required if phrase not in policy]
still_present = [phrase for phrase in removed if phrase in policy]

assert not missing, f"Missing required policy text: {missing}"
assert not still_present, f"Outdated claims still present: {still_present}"
PY
```

Expected: the command exits nonzero because the current policy is missing the required wording and still contains outdated absolute claims.

- [ ] **Step 2: Replace the policy article with the approved minimal correction**

In `fitcycles/privacy-policy/index.html`, replace the existing `<article class="policy-content">...</article>` block with this exact block:

```html
    <article class="policy-content">
      <h2>Information Collection and Use</h2>
      <p>FitCycles does not send personal data to the developer or to developer-controlled servers. Timer routines, app settings, and completed workout history are stored locally on your device using SwiftData and are not synced through iCloud.</p>
      <p>With your permission, FitCycles can access Apple Health. The dashboard reads workouts, active energy, exercise time, and heart rate on demand. This Health data is not copied into the app's SwiftData store. FitCycles can also write completed workouts to Apple Health.</p>
      <p>The Apple Watch app can run the timer, start a workout, sync timer state back to the iPhone, and write completed workouts directly to Apple Health. Live Activities are updated locally by the app and do not use remote push notifications or a developer-operated backend.</p>

      <h2>Third Party Access</h2>
      <p>FitCycles uses Apple system frameworks, including HealthKit, Watch Connectivity, and ActivityKit, to provide Apple Health, Apple Watch, and Live Activity features. The app does not include analytics, advertising, crash-reporting, or third-party SDKs. Data used through these Apple frameworks is not sent to the developer.</p>

      <h2>Opt-Out Rights</h2>
      <p>You can change or revoke FitCycles' Apple Health permissions at any time through iOS settings or the Health app. You can remove locally stored routines and workout history through app-supported deletion controls where available, or remove all locally stored FitCycles data by uninstalling the app.</p>

      <h2>Data Retention Policy</h2>
      <p>Timer routines, app settings, and completed workout history stored by FitCycles remain on your device until you delete them through the app where supported or uninstall the app. Workouts written to Apple Health remain there until you manage or delete them through Apple Health. FitCycles does not retain personal data on developer-controlled servers.</p>

      <h2>Children</h2>
      <p>The Service Provider does not use the Application to knowingly solicit personal information from or market to children under the age of 13. FitCycles does not send personal data to the developer or to developer-controlled servers.</p>
      <p>If you are a parent or guardian and have concerns about a child's use of FitCycles, please contact the Service Provider through the support form below.</p>

      <h2>Security</h2>
      <p>Locally stored FitCycles data is protected by the security mechanisms provided by iOS and your device. Apple Health data is protected through Apple Health permissions and Apple's platform security. FitCycles does not transmit this local or Health data to the developer.</p>

      <h2>Changes</h2>
      <p>This Privacy Policy may be updated from time to time for any reason. The Service Provider will notify you of changes by updating this page. You are advised to review this Privacy Policy periodically.</p>
      <p>This Privacy Policy is effective as of July 11, 2026.</p>

      <h2>Your Consent</h2>
      <p>By using the Application and granting any optional Apple Health permissions, you consent to this Privacy Policy.</p>

      <h2>Contact Us</h2>
      <p>If you have questions about this Privacy Policy or the Application's privacy practices, use the <a href="../../support/?app=fitcycles">FitCycles support form</a>.</p>
    </article>
```

Do not change the surrounding header, `<main class="policy-shell">`, footer, stylesheet reference, or support URL.

- [ ] **Step 3: Re-run the content test and confirm it passes**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

policy = Path("fitcycles/privacy-policy/index.html").read_text(encoding="utf-8")

required = (
    "stored locally on your device using SwiftData",
    "workouts, active energy, exercise time, and heart rate",
    "not copied into the app's SwiftData store",
    "Apple Watch app can run the timer",
    "Live Activities are updated locally",
    "does not include analytics, advertising, crash-reporting, or third-party SDKs",
    "This Privacy Policy is effective as of July 11, 2026.",
)

removed = (
    "collects absolutely no personal data",
    "does not use any third-party services, SDKs, or APIs",
    "there is no data to retain",
    "there is no user information that needs safeguarding",
)

missing = [phrase for phrase in required if phrase not in policy]
still_present = [phrase for phrase in removed if phrase in policy]

assert not missing, f"Missing required policy text: {missing}"
assert not still_present, f"Outdated claims still present: {still_present}"
print("FitCycles privacy content check passed.")
PY
```

Expected output:

```text
FitCycles privacy content check passed.
```

- [ ] **Step 4: Run the full static-site validator**

Run:

```bash
python3 scripts/check_site.py
```

Expected output:

```text
Site validation passed: 9 HTML pages checked.
```

- [ ] **Step 5: Review the final diff for scope and wording**

Run:

```bash
git diff --check
git diff -- fitcycles/privacy-policy/index.html
```

Expected:

- `git diff --check` produces no output and exits successfully.
- The diff changes only policy copy inside `fitcycles/privacy-policy/index.html`.
- The page shell, navigation, stylesheet link, footer, and support-form URL remain unchanged.

- [ ] **Step 6: Commit the correction**

Run:

```bash
git add fitcycles/privacy-policy/index.html
git commit -m "Correct FitCycles privacy disclosures"
```

Expected: one commit containing only `fitcycles/privacy-policy/index.html`.

## Self-Review Results

- Spec coverage: all confirmed data flows, required wording changes, effective date, support link, and out-of-scope constraints are represented in Task 1.
- Placeholder scan: no placeholders or deferred implementation instructions remain.
- Interface consistency: the plan modifies only the approved policy file and uses the existing validator without introducing new production interfaces.
