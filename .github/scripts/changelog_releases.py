"""Publish every CHANGELOG.md entry that has no GitHub Release yet.

Each entry starts with a level-2 heading such as "## 2026-11-03 · capstone follow-alongs".
The heading becomes the release title, and its slug ("2026-11-03-capstone-follow-alongs")
becomes the tag. Entries are published oldest first, so the newest one ends up as "Latest".

Run in GitHub Actions with GH_TOKEN set; pass --dry-run to only print what would happen.
"""
import os
import re
import subprocess
import sys
import tempfile

REPO_URL = "https://github.com/" + os.environ.get("GITHUB_REPOSITORY", "TomYang1993/AI-career-path-minimal-steps")


def entries(text):
    parts = re.split(r"^## +(.+?)\s*$", text, flags=re.M)
    # parts = [intro, heading1, body1, heading2, body2, ...], newest first
    return [(parts[i], parts[i + 1].strip()) for i in range(1, len(parts), 2)]


def slug(heading):
    return re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-")


def release_exists(tag):
    return subprocess.run(["gh", "release", "view", tag], capture_output=True).returncode == 0


def main():
    dry = "--dry-run" in sys.argv
    found = entries(open("CHANGELOG.md", encoding="utf-8").read())
    if not found:
        sys.exit("No '## ' entries found in CHANGELOG.md")
    newest = slug(found[0][0])
    for heading, body in reversed(found):
        tag = slug(heading)
        if not dry and release_exists(tag):
            print(f"skip   {tag} (already released)")
            continue
        notes = f"{body}\n\nFull steps: {REPO_URL}#readme\n"
        print(f"create {tag}: {heading}")
        if dry:
            print(notes)
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(notes)
        cmd = ["gh", "release", "create", tag, "--title", heading, "--notes-file", f.name,
               "--target", os.environ.get("GITHUB_SHA", "main"), f"--latest={'true' if tag == newest else 'false'}"]
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
