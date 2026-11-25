# Event Horizon Studios — production recovery

**Source of truth:** GitHub `main`. **Official site:** https://eventhorizonstudio2027.github.io/Event-Horizon/

## Approved design
Restore the recovered nine-section Event Horizon website, including the original artwork and animations, cinematic nebula background, official centered metallic wordmark, square bouncing animated video logo in the left rail, and the interactive map. Do **not** redesign or substitute the existing simplified landing page.

## Critical production discrepancy
The current `main/index.html` is a simplified replacement, not the approved recovered design. The recovered multi-file build has `index.html` plus an `assets/` directory with images, MP4 video, and `interactive_map.gz`. The approved package must be committed as a unit; publishing HTML without the assets breaks media.

## Recovery acceptance gates
1. Commit recovered `index.html` and **all** its media assets together to `main`.
2. Pass `scripts/verify-site.py` and the Site integrity GitHub Actions workflow.
3. Load the GitHub Pages URL in desktop and mobile browsers without a blank screen or crash.
4. Verify nine sections, all navigation, background and wordmark, animated video playback and bouncing position, and map load.
5. Check browser console/network errors and accessibility/reduced-motion behavior.

**Status:** Not deployed/verified. Do not mark the production restoration complete until all gates pass. Keep completed issues separate from open issues and renumber open work starting at 1.
