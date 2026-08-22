"""Blue Connect documentation i18n defaults and template context."""
from __future__ import annotations

from pathlib import PurePosixPath


DEFAULT_LANGUAGE = "pt_BR"
LANGUAGE_LABELS = {
    "pt_BR": "PT-BR",
    "en": "EN",
    "es": "ES",
}


def _localized_url(language: str, pagename: str) -> str:
    page = "index.html" if pagename == "index" else f"{pagename}.html"
    if language == DEFAULT_LANGUAGE:
        return f"/{page}"
    return f"/{language}/{page}"


def enrich_language_context(app, pagename, templatename, context, doctree):
    current = app.config.language or DEFAULT_LANGUAGE
    available = getattr(app.config, "blueconnect_languages", ["pt_BR", "en", "es"])
    context["language"] = LANGUAGE_LABELS.get(current, current.upper())
    context["alternate_languages"] = [
        (LANGUAGE_LABELS.get(code, code.upper()), code, _localized_url(code, pagename))
        for code in available
        if code != current
    ]


def setup(app):
    app.add_config_value("blueconnect_languages", ["pt_BR", "en", "es"], "html")
    app.connect("html-page-context", enrich_language_context)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
