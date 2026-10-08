#!/usr/bin/env python3
"""Rebuild the 2026-10-08 illustrated review ZIP from versioned files."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse

ROOT = Path(__file__).resolve().parent
NAME = "辞书综述_完整材料包_20261008.zip"
FILES = [
    "README.md",
    "辞书知识与语言模型融合研究综述_润色版.md",
    "辞书知识与语言模型融合研究综述_插图版.md",
    "辞书知识与语言模型融合研究综述_插图版.html",
    "辞书知识与语言模型融合研究综述_插图版.pdf",
    *[f"images/figure-{i:02d}.png" for i in range(1, 6)],
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=str(ROOT.parent / "dist"))
    args = ap.parse_args()
    dest = Path(args.out_dir).resolve()
    dest.mkdir(parents=True, exist_ok=True)
    output = dest / NAME
    missing = [rel for rel in FILES if not (ROOT / rel).is_file()]
    if missing:
        raise SystemExit("Missing required files: " + ", ".join(missing))
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=6) as z:
        for rel in FILES:
            z.write(ROOT / rel, arcname=f"辞书知识与语言模型融合研究综述_20261008/{rel}")
    with ZipFile(output) as z:
        assert z.testzip() is None
        assert len(z.namelist()) == len(FILES)
    print(f"Created {output} ({output.stat().st_size:,} bytes; {len(FILES)} files)")

if __name__ == "__main__":
    main()
