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

Cada release deve resumir o benefício percebido pelo usuário e apontar para documentação,
evidência ou roadmap. O detalhe técnico permanece nos repositórios e nos artefatos de QA.

Estados de maturidade
---------------------

* **Entregue**: incorporado à linha canônica ou disponível para uso conforme o plano aplicável.
* **QA / evolução**: implementado ou em integração, sujeito a testes, homologação e guardrails.
* **Próximo**: direção planejada, sem compromisso de disponibilidade ou data fixa.

Marketplace Blue Connect
========================

O marketplace organiza capabilities por resultado de negócio:

* **ERP & CRM**: módulos para operação transacional e comercial.
* **Omnichannel**: WhatsApp, Chatwoot, Kanban e contexto compartilhado de atendimento.
* **Financeiro**: cobrança, pagamentos, NFSe, assinaturas e indicadores.
* **Data & Consultas**: CPF, CNPJ, crédito, enriquecimento e APIs de dados.
* **Growth & Sales**: geração, scoring, distribuição, cadências e próxima ação.
* **AI Agents & Skills**: agentes e capacidades reutilizáveis com fronteiras de autoridade.
* **Automação n8n**: workflows para integrações, eventos, alertas e rotinas recorrentes.
* **Revenue Ops & SaaS**: lifecycle de receita, assinaturas, instâncias e Control Plane.

Documentação por solução
------------------------

* :doc:`crm_omnichannel`
* :doc:`financeiro_asaas`
* :doc:`data_intelligence`
* :doc:`growth_sales`
* :doc:`ai_automation`
* :doc:`saas_revenue`
* :doc:`module_index`

BlueApps
-------

O catálogo BlueApps reúne módulos especializados para Odoo 19. Preço, installability, edition e
maturidade são contratos independentes. Um módulo estar no catálogo ou no repositório não significa
que esteja automaticamente ativado em todos os tenants ou publicado em marketplaces externos.

Agents, Skills e n8n
--------------------

Agents e Skills devem ser descritos pelo resultado que entregam e pelas fronteiras de autoridade.
Uma skill pode preparar ou executar uma ação, mas operações financeiras, destrutivas ou com impacto
comercial podem exigir policy e aprovação humana.

Workflows n8n entram como templates reutilizáveis para conectar sistemas sem transformar o n8n em
fonte de verdade. ERP, CRM, billing, mensageria e APIs continuam responsáveis pelos respectivos
estados canônicos.

Catálogos estruturados
======================

Para consumo por agentes e integrações, a arquitetura também prevê índices estruturados de
capabilities e releases. Esses contratos são mecanismos de descoberta e rastreabilidade; não
substituem repositórios, sistemas transacionais ou evidências de QA.

A linha de rastreabilidade recomendada é:

``Repo -> Capability -> Release -> Documentation -> Marketplace -> Roadmap -> Evidence``

Essa separação ajuda clientes, parceiros, agentes e equipe interna a distinguir produto disponível
de trabalho em evolução.
