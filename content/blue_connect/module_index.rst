========================================
Índice de módulos principais
========================================

Este índice é voltado a administradores, implementadores e suporte. Para usuários finais, prefira
navegar pelo objetivo de negócio em :doc:`overview`.

CRM e omnichannel
=================

* ``blue_chatwoot`` — fundação de conexão e transporte Chatwoot.
* ``blue_chat_v3`` — operação comercial, sincronização, roteamento e distribuição.
* ``blue_chat_plus`` — experiência realtime no backend.
* ``blue_chat_kanban`` — bridge governado Odoo ↔ Kanban/Control Plane.
* ``blue_chatwoot_message_trigger`` — mensagens disparadas por eventos de negócio.
* ``blue_chatwoot_revenue_ops`` — inteligência de receita baseada em conversas.
* ``blue_magica_ai_chatwoot`` — IA aplicada ao contexto das conversas.
* ``blue_chat_kanban_helpdesk`` — projeção opcional para Helpdesk nativo.
* ``blue_chat_kanban_calendar`` — projeção opcional para Calendar nativo.
* ``blue_chat_kanban_appointment`` — extensão Enterprise para Appointments.

Veja :doc:`crm_omnichannel`.

Financeiro e Asaas
==================

* ``blue_payment_asaas`` — cobrança e pagamentos Asaas.
* ``blue_payment_asaas_nfse`` — NFSe integrada ao fluxo financeiro/comercial.
* ``blue_payment_asaas_subscriptions`` — assinaturas recorrentes via Asaas.
* ``blue_payment_asaas_bi`` — indicadores e acompanhamento financeiro.
* ``blue_asaas_financial_sync`` — sincronização de movimentos financeiros.
* ``blue_asaas_payment_sync`` — sincronização/baixa de pagamentos.

Veja :doc:`financeiro_asaas`.

Dados e consultas
=================

* ``blue_credit_query`` — núcleo de consultas, saldo e recarga.
* ``blue_credit_query_marketplace`` — catálogo/marketplace de planos e créditos.
* ``blue_credit_query_asaas`` — integração financeira da plataforma de consultas.
* ``blue_assertiva`` — provedor Assertiva.
* ``blue_lemiti`` — provedor Lemiti.
* ``blue_disparador_lemiti_assertiva`` — uso de dados enriquecidos em fluxos autorizados.

Veja :doc:`data_intelligence`.

Prospecção e vendas
===================

* ``blue_lead_generator`` — geração/importação de leads.
* ``blue_partner_taxonomy`` — taxonomia comercial e segmentação.
* ``blue_sales_machine`` — enriquecimento e scoring ICP.
* ``blue_outbound_engine`` — preparação de campanhas e abordagem outbound.
* ``blue_crm_lead_distribution_custom`` — distribuição e capacidade por equipe/vendedor.
* ``blue_crm_lead_followup`` — cadências de follow-up.
* ``blue_proposta_whatsapp`` — apoio à proposta/mensagem pelo WhatsApp.

Veja :doc:`growth_sales`.

IA e automações
===============

* ``blue_magica_ai_core`` — fundação Magica AI.
* ``blue_magica_ai_crm`` — IA aplicada ao CRM.
* ``blue_magica_ai_chatwoot`` — IA aplicada a conversas.
* ``blue_magica_ai_provider_openai`` — adapter de provedor da camada Magica AI.
* ``blue_automation_marketplace`` — catálogo/ativação de automações.

Veja :doc:`ai_automation`.

SaaS e receita recorrente
=========================

* ``blue_saas`` — lifecycle de instâncias SaaS.
* ``blue_saas_control_plane_bridge`` — integração governada com o Control Plane.
* ``blue_saas_subscription_bridge`` — vínculo com assinaturas recorrentes Enterprise.
* ``blue_saas_revenue_lifecycle`` — jornada marketplace → CRM → trial → receita → produção.
* ``blue_payment_asaas_subscriptions`` — cobrança recorrente quando Asaas é utilizado.

Veja :doc:`saas_revenue`.

.. note::

   Este é um índice dos módulos **principais** do ecossistema, não um inventário de todos os addons
   existentes no repositório BlueApps. Addons internos, wrappers específicos de cliente,
   compatibilidade, migrações e componentes técnicos devem permanecer fora da navegação principal
   enquanto não representarem uma capability que faça sentido para o usuário.
