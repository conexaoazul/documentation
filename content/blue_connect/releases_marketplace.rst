======================
Releases e Marketplace
======================

O Blue Connect evolui como um ecossistema de capabilities, não como uma coleção de páginas
isoladas. Por isso, releases, documentação e marketplace compartilham a mesma linguagem de
maturidade.

Release stream
==============

A visão pública de releases está disponível em
`Blue Connect Releases <https://www.conexaoazul.com/blue-connect-releases>`__.

Cada release resume benefícios percebidos pelo usuário e aponta para documentação ou roadmap.
O detalhe técnico permanece nos repositórios e nos artefatos de QA.

Estados de maturidade
---------------------

* **Entregue**: incorporado à linha canônica ou disponível para uso conforme o plano aplicável.
* **QA / evolução**: implementado ou em integração, sujeito a testes, homologação e guardrails.
* **Próximo**: direção planejada, sem compromisso de disponibilidade ou data fixa.

Marketplace Blue Connect
========================

O marketplace organiza capabilities em categorias combináveis:

* **ERP & CRM**: módulos Odoo/BlueApps para operação transacional e comercial.
* **Omnichannel**: WhatsApp, inbox, Kanban e contexto compartilhado de atendimento.
* **AI Agents**: agentes especializados para vendas, suporte, cobrança e triagem.
* **Skills**: capacidades reutilizáveis que agentes e automações podem invocar com governança.
* **Automação n8n**: workflows para integrações, eventos, alertas e rotinas recorrentes.
* **Data & Consultas**: CPF, CNPJ, crédito, veículos, protestos e enriquecimento de dados.
* **Revenue Ops**: attribution, evidência, experimentação e learning loops.
* **Control Plane**: release, entitlement, usage, runtime health, billing shadow e suporte.

BlueApps
-------

O catálogo interno consolidado do BlueApps contém mais de 100 módulos vendáveis para Odoo 19.
Preço, installability e maturidade são tratados como contratos independentes. Um módulo estar no
catálogo não significa que ele esteja publicado automaticamente em marketplaces externos.

Agents e Skills
---------------

Agents e Skills devem ser descritos pelo resultado que entregam e pelas fronteiras de autoridade.
Uma skill pode preparar ou executar uma ação, mas operações financeiras, destrutivas ou com impacto
comercial podem exigir policy e aprovação humana conforme o fluxo.

n8n Marketplace
---------------

Workflows n8n entram como templates reutilizáveis para conectar sistemas sem transformar o n8n em
fonte de verdade. ERP, CRM, billing, mensageria e APIs continuam responsáveis pelos respectivos
estados canônicos.

Catálogos estruturados
======================

Além das páginas para leitura humana, o Blue Connect publica índices JSON para integrações,
agentes, automações e validações internas consumirem a mesma fonte sem scraping de HTML:

* `Capability Graph <https://www.conexaoazul.com/data/blueconnect-capabilities.json>`__ — lista
  capabilities, categoria, maturidade, ``source_repo``, ``source_ref`` e rota pública.
* `Release Index <https://www.conexaoazul.com/data/blueconnect-releases.json>`__ — lista releases,
  status, benefício resumido, links e fontes de evidência.

Esses índices são contratos públicos de descoberta. Eles não substituem a autoridade dos
repositórios, sistemas transacionais ou evidências de QA. Seu objetivo é conectar descoberta,
documentação e automação com uma representação comum.

Rastreabilidade
===============

Uma capability pública deve apontar, sempre que possível, para uma ou mais destas evidências:

* documentação funcional;
* release pública;
* módulo ou contrato técnico;
* status de QA/homologação;
* roadmap quando ainda não estiver disponível.

A linha de rastreabilidade recomendada é:

``Repo -> Capability -> Release -> Documentation -> Marketplace -> Roadmap -> Evidence``.

Essa separação reduz promessas ambíguas e ajuda clientes, parceiros, agentes e equipe interna a
distinguir produto disponível de trabalho em evolução.
