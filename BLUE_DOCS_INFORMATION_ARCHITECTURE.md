# Blue Connect documentation information architecture

## Purpose

Keep the `blueconnect` documentation useful for end users while preserving the upstream Sphinx/Odoo structure and making BlueApps capabilities discoverable without turning the manual into a raw addon catalog.

## Native pattern to preserve

The documentation uses a predictable Sphinx hierarchy:

- `content/index.rst` is the root navigation;
- a domain has a short index file, for example `content/applications/sales.rst`;
- detailed pages live under the matching directory, for example `content/applications/sales/`;
- `.. toctree::` defines structural navigation;
- contextual `.. seealso::` links connect related domains without duplicating pages.

Blue Connect follows the same pattern:

- `content/blue_connect.rst` is the product/capability index;
- `content/blue_connect/` contains solution pages;
- the homepage exposes the same high-level journeys visually;
- native application indexes link back to the relevant Blue Connect solution pages.

## UX rule: solution first, module second

The primary navigation is organized by the user's problem, not by technical addon name:

1. CRM and omnichannel;
2. Finance and Asaas;
3. Data and consultations;
4. Prospecting and sales;
5. AI and automation;
6. SaaS and recurring revenue.

Technical module names are shown inside solution pages and in `module_index.rst` for administrators, implementation teams and support.

This prevents users from having to understand repository boundaries before they can find documentation.

## Source-of-truth rule

Blue Connect pages complement native application documentation rather than copying it.

Examples:

- CRM fundamentals stay in `applications/sales/crm`;
- accounting stays in `applications/finance/accounting`;
- WhatsApp stays in `applications/productivity/whatsapp`;
- Helpdesk stays in `applications/services/helpdesk`;
- Calendar and Appointments stay under Productivity;
- Blue Connect pages explain how our modules extend or connect those applications.

## Module documentation tiers

Use three documentation tiers:

### Tier 1: solution journey

Public, user-oriented pages that explain outcomes, recommended flow, boundaries and related native apps.

### Tier 2: module index

A compact mapping of technical addon names to capabilities for administrators and support.

### Tier 3: implementation detail

Repository README files, architecture docs, migrations, API contracts and runbooks. Link them when useful, but do not make them the primary end-user navigation.

## Maturity and availability

Documentation must distinguish capability discovery from universal availability.

A module may depend on:

- Odoo edition;
- installed dependencies;
- tenant configuration;
- external provider credentials;
- commercial entitlement;
- QA or homologation state.

Use `Entregue`, `QA / evolução` and `Próximo` where maturity must be shown publicly. Never present repository presence alone as evidence of general availability.

## Homepage rule

The homepage should expose Blue Connect solution journeys before the generic upstream application catalog while preserving the original User Docs, Administration, Developer and Contributing areas below it.

This makes the site read as a Blue Connect product manual rather than only a visual rebrand of upstream documentation.

## Cross-linking rule

Add contextual `seealso` links from native application indexes when Blue Connect adds a meaningful extension:

- Sales → omnichannel and growth;
- Finance → Asaas/financial suite;
- Productivity → omnichannel and AI;
- Marketing → growth and automation;
- Services → Helpdesk/Calendar/Appointments bridge.

Do not add every BlueApps module to every native toctree. Structural duplication makes navigation noisy and increases maintenance cost.

## Traceability

For commercial/product capabilities, prefer the chain:

`Repo -> Capability -> Release -> Documentation -> Marketplace -> Roadmap -> Evidence`

Documentation is the human-readable bridge in that chain, not the authority for runtime state, billing, entitlement or deployment.
