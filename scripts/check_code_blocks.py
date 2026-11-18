"""Run every ```python block in the guides and fail if any of them raises.

Each block runs on its own in a fresh namespace, so every example must be
self-contained and prove itself with assert statements.

Usage: python3 scripts/check_code_blocks.py [files...]
"""

import pathlib
import re
import sys
import traceback

BLOCK = re.compile(r"^```python\n(.*?)^```", re.MULTILINE | re.DOTALL)


def blocks(path):
    text = path.read_text(encoding="utf-8")
    for match in BLOCK.finditer(text):
        line = text.count("\n", 0, match.start()) + 2
        yield line, match.group(1)


def main(argv):
    root = pathlib.Path(__file__).resolve().parent.parent
    paths = [pathlib.Path(arg) for arg in argv] or sorted((root / "guides").glob("*.md"))
    ran = failed = 0
    for path in paths:
        for line, source in blocks(path):
            ran += 1
            try:
                code = compile(source, f"{path.name}:{line}", "exec")
                exec(code, {"__name__": "__guide__"})
            except Exception:
                failed += 1
                print(f"FAIL {path}:{line}")
                traceback.print_exc(limit=3)
    print(f"{ran - failed}/{ran} code blocks passed")
    return 1 if failed or not ran else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
