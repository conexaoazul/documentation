"""Expose the federated BlueApps manifest catalog to Sphinx/Jinja context."""
from __future__ import annotations

import json
from pathlib import Path


def _load_catalog(app):
    configured = getattr(app.config, "blueapps_catalog_path", "static/data/blueapps-catalog.json")
    path = Path(app.confdir) / configured
    if not path.exists():
        return {"schema": "blueconnect.blueapps.catalog.v1", "versions": []}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"schema": "blueconnect.blueapps.catalog.v1", "versions": []}


def inject_catalog(app, pagename, templatename, context, doctree):
    context["blueapps_catalog"] = _load_catalog(app)


def setup(app):
    app.add_config_value("blueapps_catalog_path", "static/data/blueapps-catalog.json", "html")
    app.connect("html-page-context", inject_catalog)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
