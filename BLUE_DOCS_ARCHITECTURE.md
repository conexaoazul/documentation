# Blue Docs deployment architecture

## Goal

Keep Odoo 19 documentation reproducible, auditable, cheap to deploy and easy to roll back.

## Pipeline

1. Pull requests build and validate `Dockerfile.blue-docs` on a disposable GitHub-hosted runner.
2. Pushes to `19.0` publish:
   - `ghcr.io/conexaoazul/odoo-documentation:19.0-<sha>`
   - `ghcr.io/conexaoazul/odoo-documentation:19.0`
3. Production deployment is manual through `Deploy docs ERP to dev1`.
4. The dev1 runner only pulls the selected image and replaces the runtime container.
5. The runtime is bound to `127.0.0.1:18081` and exposed publicly by the existing Cloudflare/reverse-proxy layer.

## Why this replaces the previous split approaches

The immutable-image proposal and the direct-build-on-dev1 proposal solve different parts of the same problem. This architecture keeps the strongest part of each:

- CI owns expensive/reproducible builds;
- GHCR is the artifact boundary;
- dev1 only performs a small, reversible runtime change;
- production never changes just because a documentation commit was merged;
- rollback is an image selection, not a rebuild.

## Production gate

Before deploying a new image, confirm:

- the image workflow is green for the intended SHA;
- the image tag/digest is recorded;
- one healthy runner matches `self-hosted` + `dev1`;
- `docs-erp.conexaoazul.com` is routed to `http://127.0.0.1:18081` through Cloudflare/reverse proxy;
- the previous deployed image is known.

After deployment validate:

- `/healthz` returns `ok` locally;
- `/index.html` loads locally;
- `/BLUE_SOURCE.txt` identifies source SHA and CC-BY-SA-4.0 license;
- public HTTPS responds successfully;
- CSS, JavaScript and internal navigation work.

## ROI

This removes repeated Sphinx dependency installation from the production runner, shortens deploy time, reduces failure surface, enables deterministic rollback and keeps the upstream documentation source separate from Conexão Azul commercial content.

## `blueconnect` branch — Blue Connect rebrand (added 2026-08-21)

A second, independent branch carries the Conexão Azul commercial rebrand on top of the
upstream Odoo docs, so `19.0` stays pristine and can keep syncing from upstream without
conflicts.

**What differs from `19.0`:**

- `conf.py`: `project`/`copyright`/version display labels → "Blue Connect".
- `locale/pt_BR/LC_MESSAGES/*.po`: **msgstr-only** replace of "Odoo" → "Blue Connect"
  (2,987 occurrences) and of the illustrative example domains `mycompany.odoo.com` /
  `yourdbname.odoo.com` → `minhaempresa.blueconnect.com.br` / `seubanco.blueconnect.com.br`.
  `msgid` is never touched, so translation matching against upstream source strings stays
  intact after future syncs.
- Theme (`extensions/odoo_theme/layout_templates/{header,footer,homepage}.html`): visible
  "Odoo" strings and the logo (`odoo_logo.svg` → `https://www.conexaoazul.com/logo-light.png`)
  rebranded; external CTA links (`Try Blue Connect for FREE`, `Contact Support`, `Ask the
  Blue Connect Community`) point to `www.conexaoazul.com` (chosen over `blueconnect.com.br`,
  which was unreachable at the time).
- `legal.html` is **intentionally excluded** — it names real external Odoo legal agreements
  (Enterprise Agreement, Cloud SLA, GDPR guide, etc.) linking to odoo.com. Renaming those
  would misrepresent a real contract, not just marketing copy.
- `Dockerfile.blue-docs`: builds `CURRENT_LANG=pt_BR` instead of `en`; flattens Sphinx's
  `_build/html/pt_BR/` output (including dotfiles) into the html root before the nginx COPY
  step, otherwise the deployed site serves nginx's default welcome page instead of the docs.
- `blue-docs-image.yml`: publishes `blueconnect-<sha>` / `blueconnect` GHCR tags on push to
  this branch (mirrors the `19.0` logic, kept on a separate condition so `19.0`'s pipeline is
  untouched); publish also fires on `workflow_dispatch`, not only `push` (a push-triggered run
  can get cancelled by the concurrency group when a manual dispatch starts right after, which
  used to skip publish entirely).
- **Auto-deploy**: after a successful publish on `blueconnect`, the workflow itself calls
  `gh workflow run deploy-docs-erp-dev1.yml` with the exact `blueconnect-<sha>` tag it just
  published — no manual `workflow_dispatch` needed for this branch. This lives inside
  `blue-docs-image.yml` (which already exists on `blueconnect`) rather than as a
  `workflow_run` trigger on `deploy-docs-erp-dev1.yml`, because `workflow_run` only fires for
  workflow files present on the repo's **default branch** (`19.0` here) — adding it there
  would mean editing `19.0`, which this branch strategy exists to avoid.
- `deploy-docs-erp-dev1.yml`: accepts `blueconnect`/`blueconnect-*` image tags in addition to
  `19.0`; `DOCS_ERP_HOST` points at `documentation.conexaoazul.com`.

**Infra dedicated to this branch (none shared with existing production):**

- Self-hosted Actions runner `dev1-documentation` (label `dev1`), registered directly on
  `conexaoazul/documentation` — separate from the `azul-docs`/`BlueApps19`/`blue_whatsapp`
  runners already on this host.
- Cloudflare Tunnel `dev1-documentation` (remote-config), running as the
  `cloudflared-documentation` Docker container on dev1 — **not** the pre-existing
  `n8n-azul1-tunnel` (which serves `conector.conexaoazul.com` and lives on a different host).
- DNS: `documentation.conexaoazul.com` CNAME → `dev1-documentation` tunnel.

**Known gap, not fixed on purpose:** ~1,423 remaining `odoo.com` links across the rendered
site are legitimate technical/legal references (App Store, translate/runbot/nightly infra,
real Odoo SaaS account/subscription management, real legal agreements, training videos) —
not branding. Only the ~4 UI-chrome links (trial/help/forum/home) and the 2 illustrative
placeholder domains were in scope for text substitution. Pricing/plans and
account/subscription pages that don't exist yet on our domain are tracked separately for a
follow-up content PR rather than faked here.
