========================
IA, agentes e automações
========================

A camada de IA e automação adiciona interpretação, recomendação e execução assistida sobre os
processos existentes. O objetivo é ampliar o ERP/CRM, não criar uma segunda base de clientes,
financeiro, agenda ou atendimento.

Quando usar
===========

Use esta família para:

* resumir e interpretar contexto de CRM e atendimento;
* sugerir próxima ação comercial;
* apoiar qualificação, cobrança, suporte e operação;
* conectar workflows via n8n e integrações externas;
* criar automações reutilizáveis e governadas;
* controlar quais ações podem ser executadas automaticamente e quais exigem aprovação.

Módulos e componentes principais
================================

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Componente
     - Responsabilidade
   * - ``blue_magica_ai_core``
     - Fundação comum para recursos de IA e contratos compartilhados.
   * - ``blue_magica_ai_crm``
     - Contexto e capacidades de IA voltadas ao CRM.
   * - ``blue_magica_ai_chatwoot``
     - Insights de IA sobre conversas usando a conexão canônica do Chatwoot.
   * - ``blue_magica_ai_provider_openai``
     - Adapter de provedor para os recursos compatíveis da camada Magica AI.
   * - ``blue_automation_marketplace``
     - Catálogo e ativação de automações reutilizáveis quando o produto/tenant estiver habilitado.
   * - n8n / workflows
     - Orquestração de integrações e tarefas entre sistemas sem substituir o sistema de registro.

Princípio de autoridade
=======================

Antes de automatizar, defina quem é o dono de cada informação:

* CRM e oportunidade → aplicativo CRM;
* cliente → Contatos;
* ticket → Helpdesk;
* evento → Calendar/Appointments;
* cobrança e fatura → Financeiro;
* conversa → canal/Chatwoot, com vínculo ao CRM;
* automação → orquestra o fluxo, mas não vira a fonte paralela dos dados.

Governança de execução
======================

Uma automação pode ter diferentes níveis de autonomia. Como referência operacional:

``AI_CAN_EXECUTE``
   Ação de baixo risco que pode ser executada automaticamente dentro de limites definidos.

``AI_CAN_PREPARE``
   A IA prepara conteúdo, análise ou ação, mas a execução final depende de outro ator/regra.

``HUMAN_REQUIRED``
   Exige decisão humana antes de produzir efeito no negócio.

``DENY``
   A ação não deve ser executada naquele contexto.

A classificação depende do impacto, da reversibilidade e da política da operação. Pagamentos,
alterações destrutivas, comunicação sensível e mudanças de acesso merecem controles mais fortes.

Boas práticas de UX
===================

* Mostre a evidência que levou à recomendação.
* Diferencie claramente **sugestão** de **ação já executada**.
* Exiba o sistema onde o efeito será aplicado.
* Permita revisão humana quando a consequência for relevante.
* Registre resultado e feedback para melhorar regras futuras.

Guias relacionados
==================

* :doc:`../applications/productivity/ai`
* :doc:`../applications/productivity/whatsapp`
* :doc:`../applications/marketing/marketing_automation`
* :doc:`crm_omnichannel`
* :doc:`growth_sales`
