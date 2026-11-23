# Event Horizon Studios — Recovery status (2026-11-23)

## Source of truth and deployment safety
The existing `main/index.html` is an older simplified page; it does **not** represent the full original nine-section website. Do not overwrite the production entrypoint until the full media assets have been committed and a browser smoke test passes.

## Recovered build (local, not yet deployed)
- Nine sections retained; ~59 KB HTML with 23 separate assets (~3.9 MB ZIP).
- Animated black-hole logo remains in top-left rail; official Event Horizon Studios wordmark centered at top.
- Interactive map is fetched and decompressed only on explicit user click.
- Improvements made in the local package: check map HTTP response and browser decompression support; release previous iframe before reload; clearer error/loading feedback; minimum 44px rail hit targets; subtle rail logo outline and reduced-motion support.
- Static asset reference audit: all locally referenced media exist.

## Still open — reset numbering
1. Deploy **all** recovered assets alongside HTML; current GitHub Pages version is not the recovered build. GitHub issue #4.
2. Browser smoke test on desktop and mobile; headless Chromium timed out in the current environment.
3. Verify looping/bouncing video playback and 3D map launch over HTTPS.
4. Verify responsive rail alignment and all section links after deployment.

## Release gate
Do not claim crash resolved or site live until the deployed URL loads and functional checks pass. Latest ZIP must be extracted with `index.html` adjacent to `assets/`.
