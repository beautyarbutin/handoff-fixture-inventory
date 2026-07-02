from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "docs" / "t2_prompt_template.md"
ARMS_DIR = ROOT / "docs" / "arms"


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a T2 prompt for one handoff arm.")
    parser.add_argument("arm", help="Arm file stem, for example A_full or E_summary_only")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional output path. Prints to stdout when omitted.",
    )
    args = parser.parse_args()

    arm_path = _find_arm_path(args.arm)
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    handoff = arm_path.read_text(encoding="utf-8").strip()
    prompt = template.replace("{{HANDOFF_BLOCK}}", handoff)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(prompt, encoding="utf-8")
    else:
        print(prompt)


def _find_arm_path(arm: str) -> Path:
    candidates = [
        ARMS_DIR / f"{arm}.json",
        ARMS_DIR / f"{arm}.md",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    known = sorted(path.stem for path in ARMS_DIR.iterdir() if path.is_file())
    raise SystemExit(f"Unknown arm {arm!r}. Known arms: {', '.join(known)}")


if __name__ == "__main__":
    main()

