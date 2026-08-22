#!/usr/bin/env python3
"""Generate a version-aware BlueApps catalog from checked-out addon trees."""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path


def load_manifest(path: Path) -> dict:
    try:
        return ast.literal_eval(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_parse_error": str(exc)}


def scan_branch(root: Path, version: str) -> dict:
    modules = []
    for manifest in sorted(root.rglob("__manifest__.py")):
        data = load_manifest(manifest)
        module_dir = manifest.parent
        rel = module_dir.relative_to(root).as_posix()
        modules.append(
            {
                "technical_name": module_dir.name,
                "path": rel,
                "version_line": version,
                "name": data.get("name"),
                "summary": data.get("summary"),
                "version": data.get("version"),
                "category": data.get("category"),
                "license": data.get("license"),
                "price": data.get("price"),
                "currency": data.get("currency"),
                "installable": data.get("installable", True),
                "application": data.get("application", False),
                "depends": data.get("depends", []),
                "parse_error": data.get("_parse_error"),
            }
        )
    return {"version": version, "module_count": len(modules), "modules": modules}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--versions", nargs="+", default=["19.0", "18.0", "17.0"])
    args = parser.parse_args()

    source_root = Path(args.source_root)
    payload = {
        "schema": "blueconnect.blueapps.catalog.v1",
        "source_repo": "conexaoazul/blueapps",
        "versions": [],
    }
    for version in args.versions:
        branch_root = source_root / version
        if not branch_root.exists():
            payload["versions"].append({"version": version, "module_count": 0, "modules": [], "missing": True})
            continue
        payload["versions"].append(scan_branch(branch_root, version))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
