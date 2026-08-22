=========================
Blue Connect: visão geral
=========================

O **Blue Connect** é a camada operacional da Conexão Azul para integrar ERP, CRM, atendimento,
automação, dados e inteligência artificial em uma mesma arquitetura de negócio.

Esta documentação continua cobrindo o núcleo ERP/CRM baseado em Odoo 19, enquanto o ecossistema
Blue Connect adiciona capabilities especializadas por meio de módulos, integrações e serviços.

.. toctree::
   :maxdepth: 2

   releases_marketplace

Visão da plataforma
===================

ERP + CRM
---------

O núcleo transacional reúne vendas, CRM, financeiro, estoque, projetos, serviços, marketing e
operações em uma base comum. Os capítulos de :doc:`../applications` detalham os aplicativos e
fluxos disponíveis.

Omnichannel
-----------

A camada de atendimento conecta canais como WhatsApp aos registros operacionais e comerciais,
permitindo que conversas, oportunidades, clientes e atividades compartilhem contexto.

AI Agents
---------

Agentes de IA podem apoiar qualificação, atendimento, cobrança, vendas e rotinas operacionais.
Capacidades com impacto comercial, financeiro ou destrutivo permanecem sujeitas a governança e,
quando aplicável, decisão humana.

Skills e automações
-------------------

Skills reutilizáveis, integrações e workflows permitem transformar tarefas recorrentes em
capabilities componíveis. A Conexão Azul utiliza n8n e integrações nativas para conectar sistemas,
APIs e eventos sem duplicar a autoridade dos sistemas de origem.

Dados e consultas
-----------------

O ecossistema inclui APIs de consulta e enriquecimento para CPF, CNPJ, crédito, veículos,
protestos e outros sinais utilizados por fluxos comerciais e operacionais.

Marketplace BlueApps
--------------------

O catálogo BlueApps reúne módulos especializados para Odoo 19. Em agosto de 2026, o catálogo
interno consolidado contém mais de 100 módulos vendáveis, com preço e maturidade tratados por
regras de governança. A presença no catálogo não implica publicação automática em marketplaces
externos. Consulte :doc:`releases_marketplace` para a organização por capability e maturidade.

Maturidade e roadmap
====================

Usamos três estados públicos para evitar confundir roadmap com disponibilidade geral:

* **Entregue**: capability já incorporada à linha canônica ou disponível no produto.
* **QA / evolução**: capability implementada ou em integração, ainda sujeita a homologação.
* **Próximo**: direção de produto planejada, sem promessa de disponibilidade ou data fixa.

Entre as frentes atuais estão Revenue & Growth Intelligence, experimentos governados,
Vendor Control Plane, contratos universais de plataforma, observabilidade, metering e uma futura
camada de marketplace para agentes, skills e automações.

Links do ecossistema
====================

* `Site Blue Connect <https://www.conexaoazul.com/blue-connect-platform>`__
* `Releases e Marketplace <https://www.conexaoazul.com/blue-connect-releases>`__
* `Roadmap 2026 <https://www.conexaoazul.com/roadmap-2026>`__
* `Documentação de APIs de dados <https://docs.conexaoazul.com/blue-credit-api/intro>`__
* `Repositório público da documentação <https://github.com/conexaoazul/documentation>`__

.. note::

   O Blue Connect combina software próprio, módulos, integrações e componentes open source.
   Marcas, serviços e tecnologias de terceiros continuam pertencendo aos respectivos titulares.
