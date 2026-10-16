#!/usr/bin/env python3
"""Verificador SOLO LECTURA de manifiestos sha256sum del laboratorio ORIGINAL."""
from pathlib import Path
import argparse
import hashlib
import re

PATTERN = re.compile(r"^([0-9a-fA-F]{64})\s+\*?(.+?)\s*$")

def digest_file(path):
    h = hashlib.sha256()
    with path.open("rb") as file:
        for data in iter(lambda: file.read(1024 * 1024), b""):
            h.update(data)
    return h.hexdigest()

def verify(root, manifest):
    root = root.resolve(strict=True)
    manifest = manifest.resolve(strict=True)
    if not root.is_dir() or not manifest.is_file():
        raise ValueError("root debe ser directorio y manifest fichero")
    report = {"ok": 0, "fail": 0, "unresolved": 0, "invalid": 0, "unsafe": 0}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        match = PATTERN.match(line)
        if match is None:
            report["invalid"] += 1
            continue
        expected, relative_name = match.groups()
        relative = Path(relative_name)
        if relative.is_absolute():
            report["unsafe"] += 1
            continue
        candidate = (root / relative).resolve(strict=False)
        if not candidate.is_relative_to(root):
            report["unsafe"] += 1
            continue
        if not candidate.is_file() or candidate.is_symlink():
            report["unresolved"] += 1
            continue
        if digest_file(candidate).lower() == expected.lower():
            report["ok"] += 1
        else:
            report["fail"] += 1
    return report

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,required=True)
    parser.add_argument('--manifest',type=Path,required=True)
    args=parser.parse_args()
    try:
        result=verify(args.root,args.manifest)
    except (OSError,ValueError) as exc:
        parser.exit(2, f"ERROR: {type(exc).__name__}: {exc}\n")
    for key,value in result.items():
        print(f"{key.upper()}={value}")
    return 0 if result['ok'] and not any(result[k] for k in ('fail','unresolved','invalid','unsafe')) else 1

if __name__=='__main__':
    raise SystemExit(main())
