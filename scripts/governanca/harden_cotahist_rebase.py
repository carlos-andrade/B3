from pathlib import Path
import re
import sys

WORKFLOWS = Path('.github/workflows')
YEAR_RE = re.compile(r'(?:2014|2015|2016|2017)')

def main() -> int:
    changed = []
    skipped_custom = []
    candidates = sorted(WORKFLOWS.glob('cotahist-*.yml'))
    candidates += [p for p in [WORKFLOWS / 'rec001-cotahist-bloomberg-mail.yml'] if p.exists()]
    for path in candidates:
        if not YEAR_RE.search(path.name) and path.name != 'rec001-cotahist-bloomberg-mail.yml':
            continue
        content = path.read_text(encoding='utf-8')
        if 'git rebase origin/main' not in content:
            continue
        if 'git add ' not in content or 'git push origin HEAD:main' not in content:
            continue
        if 'diff-filter=U' in content or 'Conflito apenas na evidência' in content:
            skipped_custom.append(str(path))
            continue
        updated = content.replace('git rebase origin/main', 'git rebase -X theirs origin/main')
        if updated != content:
            path.write_text(updated, encoding='utf-8', newline='')
            changed.append(str(path))
    print(f'WORKFLOWS_SCANNED={len(candidates)}')
    print(f'WORKFLOWS_PATCHED={len(changed)}')
    print(f'WORKFLOWS_WITH_CUSTOM_RESOLUTION_SKIPPED={len(skipped_custom)}')
    for path in changed:
        print(f'PATCHED={path}')
    if not changed:
        print('No changes required.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
