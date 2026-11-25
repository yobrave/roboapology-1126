import os
import sys
from pathlib import Path


class ApologyPublisher:
    def __init__(self) -> None:
        self.root = Path(__file__).resolve().parent
        self.env_out = os.environ.get("MAKEFUN_OUTPUT_DIR")

    def load(self) -> str:
        raw = (self.root / "entry.txt").read_text(encoding="utf-8")
        stripped = raw.strip()
        if not stripped:
            raise ValueError("entry.txt holds no text")
        return stripped

    def emit(self, text: str) -> str:
        base = Path(self.env_out) if self.env_out else Path.cwd() / "out"
        base.mkdir(parents=True, exist_ok=True)
        dest = base / "entry.txt"
        with dest.open("w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
            fh.write("\n")
        return str(dest)


def run() -> int:
    bot = ApologyPublisher()
    msg = bot.load()
    if len(msg) > 400:
        print("entry too long:", len(msg), file=sys.stderr)
        return 2
    print("published ->", bot.emit(msg))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
