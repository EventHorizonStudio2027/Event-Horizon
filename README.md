# Event Horizon Studios

Official website development repository for Event Horizon Studios.

## Current deployment status

The `main` branch contains a lightweight fallback site. The complete original Grok-built site with the studio refresh and cinematic assets is prepared separately and **has not yet been uploaded to this repository**.

The full site includes an `index.html` and an `assets/` directory containing 20 local media assets. The upload needs to preserve those paths. Do not remove the fallback until the full site has been uploaded and verified.

## Deploy

1. Upload the complete website's `index.html` and `assets/` folder to the repository root.
2. In Settings → Pages, select Deploy from a branch, `main`, `/ (root)`.
3. Verify the published page and assets at https://fatespassage.github.io/Event-Horizon/.
4. Confirm the hero and main content are visible in Safari and Chromium, both desktop and mobile.

## Quality standards

- Content must render without JavaScript. Entrance animations are optional enhancements.
- No missing relative image or video paths.
- The video is user-initiated, with a poster and controls.
- Images below the fold use lazy loading.
- Keyboard navigation and reduced-motion settings remain functional.
- GitHub Actions verifies HTML structure and referenced local assets.

## Outstanding

- Issue #1: Upload full original site and all cinematic media.
- Issue #2: Confirm black-screen issue is fixed in real browsers; add browser smoke testing.

## Local development

```bash
python3 -m http.server 8000
```

Open http://localhost:8000/ from the directory containing `index.html`.
