#!/usr/bin/env python3
"""Validate the Blue Connect information architecture exposed by the Sphinx menu."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def require_once(text: str, needle: str, label: str) -> None:
    count = text.count(needle)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one {needle!r}, found {count}")


def main() -> None:
    root_index = read("content/index.rst")
    blue_index = read("content/blue_connect.rst")
    header = read("extensions/odoo_theme/layout_templates/header.html")

    root_blue = root_index.find("    blue_connect\n")
    root_apps = root_index.find("    applications\n")
    if root_blue < 0 or root_apps < 0 or root_blue > root_apps:
        raise SystemExit("content/index.rst must expose Blue Connect before User Docs/applications")

    groups = {
        "blue_connect/customer_revenue": [
            ("CRM e Omnichannel", "crm_omnichannel"),
            ("Prospecção e Vendas", "growth_sales"),
        ],
        "blue_connect/operations_monetization": [
            ("Financeiro e Asaas", "financeiro_asaas"),
            ("SaaS e Recorrência", "saas_revenue"),
        ],
        "blue_connect/intelligence_automation": [
            ("Dados e Consultas", "data_intelligence"),
            ("IA e Automações", "ai_automation"),
        ],
        "blue_connect/ecosystem_admin": [
            ("Releases e Marketplace", "releases_marketplace"),
            ("Índice de módulos", "module_index"),
        ],
    }

    require_once(blue_index, "   blue_connect/overview\n", "Blue Connect root menu")
    for group in groups:
        require_once(blue_index, f"   {group}\n", "Blue Connect root menu")

    leaf_names = [leaf for leaves in groups.values() for _, leaf in leaves]
    for leaf in leaf_names:
        if f"   blue_connect/{leaf}\n" in blue_index:
            raise SystemExit(
                f"Blue Connect root menu must not flatten leaf solution {leaf!r}; keep it in a submenu"
            )

    seen = []
    for group, entries in groups.items():
        group_text = read(f"content/{group}.rst")
        for label, leaf in entries:
            require_once(group_text, f"   {label} <{leaf}>\n", f"submenu {group}")
            seen.append(leaf)

    if sorted(seen) != sorted(leaf_names) or len(seen) != len(set(seen)):
        raise SystemExit("Each Blue Connect solution must appear in exactly one navigation group")

    for pathto in (
        "pathto('blue_connect')",
        "pathto('applications')",
        "pathto('blue_connect/releases_marketplace')",
    ):
        require_once(header, pathto, "desktop quick navigation")

    print("Blue Connect navigation contract: OK")


if __name__ == "__main__":
    main()
