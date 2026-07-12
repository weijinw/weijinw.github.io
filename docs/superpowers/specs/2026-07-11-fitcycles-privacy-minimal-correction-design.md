# FitCycles Privacy Policy Minimal Correction Design

## Goal

Correct the current FitCycles privacy policy so it accurately describes the app’s local storage, Apple Health use, Apple Watch behavior, and lack of developer-side data collection, while preserving the existing page structure and overall legal style.

## Scope

This is a minimal correction, not a full rewrite. The existing headings and page layout remain in place. Only inaccurate or incomplete wording is revised.

## Confirmed App Behavior

- FitCycles is an offline app with no internet connection and no developer-operated servers.
- The app includes no analytics, advertising, crash-reporting, or third-party SDKs.
- SwiftData stores timer routines, app settings, and completed workout history locally on the user’s device.
- FitCycles does not currently sync app data through iCloud.
- The dashboard reads selected Apple Health data on demand: workouts, active energy, exercise time, and heart rate.
- Health data read from Apple Health is not copied into the app’s SwiftData store.
- The app can write completed workouts to Apple Health after the user grants permission.
- The Apple Watch app can run the timer, start a workout, sync timer state back to the iPhone, and write completed workouts directly to Apple Health.
- Live Activities are updated locally by the app and do not use remote push notifications or a backend.

## Required Policy Changes

### Information Collection and Use

Replace the current absolute claim that the app collects no data and that all app usage remains entirely on-device with wording that distinguishes developer collection from local and Apple-platform processing.

The revised section must state that:

- FitCycles does not send personal data to the developer or to developer-controlled servers.
- Timer routines, app settings, and completed workout history are stored locally using SwiftData.
- Apple Health access requires user permission.
- The dashboard may read workouts, active energy, exercise time, and heart rate from Apple Health.
- FitCycles may write completed workouts to Apple Health.
- Health data is read on demand and is not copied into SwiftData.

### Third Party Access

Replace the current statement that no external APIs are used.

The revised section must state that:

- FitCycles uses Apple system frameworks for Apple Health, Apple Watch communication, and Live Activities.
- FitCycles does not use analytics, advertising, crash-reporting, or third-party SDKs.
- Data is not sent to the developer.

### Opt-Out Rights

Add clear user controls:

- Apple Health permissions can be changed or revoked in iOS settings.
- Users can remove local data through app-supported deletion controls where available or by uninstalling the app.

### Data Retention Policy

Replace the statement that retention is not applicable.

The revised section must state that:

- Locally stored SwiftData remains on the device until deleted through the app or the app is uninstalled.
- Data written to Apple Health remains in Apple Health until the user manages or deletes it there.
- No personal data is retained on developer-controlled servers.

### Security

Replace the statement that no user information needs safeguarding.

The revised section must state that:

- Local FitCycles data is protected by the security mechanisms provided by iOS and the user’s device.
- Apple Health data is protected and controlled through Apple Health permissions and Apple’s platform security.
- FitCycles does not transmit this data to the developer.

### Other Sections

Keep the Children, Changes, Consent, and Contact sections substantially unchanged, except for minor wording adjustments needed for consistency.

Update the effective date to July 11, 2026.

Keep the existing FitCycles support-form link.

## Files

- Modify: `fitcycles/privacy-policy/index.html`

No CSS, route, navigation, or layout changes are required.

## Validation

Run:

```bash
python3 scripts/check_site.py
```

Expected result: the static site validator passes.

Also verify that the revised policy no longer contains these inaccurate claims:

- “collects absolutely no personal data”
- “does not use any third-party services, SDKs, or APIs”
- “there is no data to retain”
- “there is no user information that needs safeguarding”

## Out of Scope

- Full plain-language rewrite of the privacy policy
- App Store privacy-label changes
- Changes to FitCycles code or permissions
- iCloud support
- Any backend or remote service
