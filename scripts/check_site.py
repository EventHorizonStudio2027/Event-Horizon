#!/usr/bin/env python3
"""Event Horizon website pre-deploy smoke checks."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
html_path = root / "index.html"
errors = []
if not html_path.is_file():
    errors.append("Missing root index.html")
else:
    html = html_path.read_text(encoding="utf-8", errors="replace")
    if "<main" not in html.lower() and "<section" not in html.lower():
        errors.append("No main content or sections found")
    if "<video" not in html.lower() and "video/mp4" not in html.lower():
        errors.append("Cinematic video not embedded or linked")
    if not re.search(r"<img\b|data:image/", html, re.I):
        errors.append("No images found")
    for ref in re.findall(r"""(?:src|poster)=["']([^"']+)["']""", html, re.I):
        if ref.startswith(("data:", "http:", "https:", "//", "#")):
            continue
        if not (root / ref.split("?")[0].split("#")[0]).is_file():
            errors.append(f"Missing media reference: {ref[:140]}")
    if re.search(r"<body[^>]*style=[^>]*display\s*:\s*none", html, re.I):
        errors.append("Body hidden by inline display:none")
    print(f"HTML size: {len(html):,} characters")
if errors:
    print("FAILED:\n" + "\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("Event Horizon static media smoke checks passed.")
