# Blue immutable documentation artifact

This repository remains the canonical CC-BY-SA-4.0 documentation source. The Blue integration builds it as a separate static container instead of embedding the source tree in the Odoo add-on image.

## Local validation

```bash
docker build \
  --file Dockerfile.blue-docs \
  --build-arg SOURCE_SHA="$(git rev-parse HEAD)" \
  --tag blue-docs:local \
  .

docker run --rm -p 18080:8080 blue-docs:local
```

Health endpoint:

```text
http://127.0.0.1:18080/healthz
```

## Publishing contract

- Pull requests build and validate the image without publishing it.
- Pushes to `19.0` publish an immutable SHA tag and update the `19.0` channel tag.
- No deployment is performed by this workflow.
- `BLUE_SOURCE.txt` records source, branch, commit and license inside the artifact.
- BlueApps consumes a validated artifact URL through `blue_docs_portal.url`.
