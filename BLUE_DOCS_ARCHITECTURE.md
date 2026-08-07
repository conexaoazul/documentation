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
