#!/usr/bin/env python3
"""Verify that the recovered Event Horizon website is complete before publishing."""
from pathlib import Path
from html.parser import HTMLParser
import sys

ROOT = Path(__file__).resolve().parents[1]
class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = 0
        self.refs = []
        self.ids = set()
        self.links = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section": self.sections += 1
        if "id" in d: self.ids.add(d["id"])
        for key in ("src", "poster"):
            if d.get(key, "").startswith("assets/"): self.refs.append(d[key])
        if tag == "link" and d.get("href", "").startswith("assets/"): self.refs.append(d["href"])
        if tag == "a" and d.get("href", "").startswith("#"): self.links.append(d["href"][1:])

def main():
    index = ROOT / "index.html"
    if not index.exists(): sys.exit("FAIL: index.html missing")
    html = index.read_text(encoding="utf-8")
    audit = Audit(); audit.feed(html)
    failures = []
    if audit.sections < 9: failures.append(f"Only {audit.sections} sections; recovered original has 9")
    if not (ROOT / "assets").is_dir(): failures.append("assets/ folder missing")
    for ref in set(audit.refs):
        if not (ROOT / ref.split("?",1)[0]).is_file(): failures.append(f"Missing asset: {ref}")
    for target in audit.links:
        if target and target not in audit.ids: failures.append(f"Broken anchor: #{target}")
    if "interactive_map.gz" in html and not (ROOT / "assets/interactive_map.gz").exists():
        failures.append("Interactive map asset missing")
    if not any((ROOT/"assets").glob("*.mp4")) if (ROOT/"assets").exists() else True:
        failures.append("Animated video asset missing")
    print(f"Sections: {audit.sections}; asset references: {len(audit.refs)}; anchors: {len(audit.links)}")
    for issue in failures: print("FAIL:",issue)
    if failures: sys.exit(1)
    print("PASS: static recovery integrity checks (not browser playback verification)")
if __name__ == "__main__": main()
