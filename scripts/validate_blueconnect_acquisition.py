#!/usr/bin/env python3
"""Validate the Blue Connect documentation acquisition contract without external services."""

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"{label}: missing {needle!r}")


def main() -> None:
    theme = read("extensions/odoo_theme/__init__.py")
    layout = read("extensions/odoo_theme/layout.html")
    template = read("extensions/odoo_theme/layout_templates/commercial_cta.html")
    tracking = read("extensions/odoo_theme/static/js/docs_growth.js")
    styles = read("extensions/odoo_theme/static/css/docs_growth.css")

    ast.parse(theme)

    expected_pages = (
        "blue_connect/overview",
        "blue_connect/crm_omnichannel",
        "blue_connect/financeiro_asaas",
        "blue_connect/data_intelligence",
        "blue_connect/growth_sales",
        "blue_connect/ai_automation",
        "blue_connect/saas_revenue",
        "blue_connect/releases_marketplace",
        "blue_connect/module_index",
    )
    for page in expected_pages:
        require(theme, f"'{page}':", "commercial page mapping")

    for key in (
        "utm_source",
        "utm_medium",
        "utm_campaign",
        "source",
        "surface",
        "solution",
        "intent",
        "page",
        "version",
    ):
        require(theme, f"'{key}'", "diagnostic attribution")

    require(
        theme,
        "https://www.conexaoazul.com/diagnostico/blueconnect?",
        "diagnostic destination",
    )
    require(theme, "docs_growth.css", "commercial page stylesheet")
    require(theme, "js/docs_growth.js", "growth tracking asset")

    require(layout, 'layout_templates/commercial_cta.html', "layout conversion surface")
    for attribute in (
        "data-blueconnect-cta",
        "data-docs-source",
        "data-docs-solution",
        "data-docs-intent",
        "data-docs-page",
    ):
        require(template, attribute, "CTA context envelope")

    for event in ("docs_commercial_intent", "docs_solution_view", "docs_search"):
        require(tracking, event, "analytics event")
    require(tracking, "[redacted]", "search privacy guard")
    require(tracking, "has_results", "search demand signal")
    require(styles, ".ca_docs_growth", "conversion surface styles")

    print("Blue Connect acquisition contract: OK")


if __name__ == "__main__":
    main()
