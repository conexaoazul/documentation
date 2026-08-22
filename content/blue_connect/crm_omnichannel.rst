==========================
CRM e atendimento omnichannel
==========================

Esta família conecta atendimento e operação comercial sem transformar o Chatwoot em um segundo
CRM nem o Odoo em um segundo inbox. Cada camada tem uma responsabilidade clara.

Quando usar
===========

Use esta solução quando sua equipe precisa:

* relacionar conversas do WhatsApp e outros canais a contatos e oportunidades;
* sincronizar contexto comercial entre atendimento e CRM;
* acompanhar alterações em tempo real no Odoo;
* mover oportunidades entre CRM e Kanban operacional com segurança;
* disparar mensagens a partir de eventos de negócio;
* transformar conversas em sinais de receita e insights de IA;
* abrir Helpdesk ou agenda nativa a partir de eventos do fluxo operacional.

Módulos principais
==================

.. list-table::
   :header-rows: 1
   :widths: 27 31 42

   * - Módulo
     - Papel
     - Experiência para o usuário
   * - ``blue_chatwoot``
     - Fundação de conexão
     - Centraliza conta, inboxes, identidade e transporte seguro do Chatwoot.
   * - ``blue_chat_v3``
     - Operação comercial
     - Sincronização CRM, roteamento, distribuição, labels, agentes e fluxos de vendas.
   * - ``blue_chat_plus``
     - UX em tempo real
     - Viewer de conversa, notificações, badges e atualização reativa no backend.
   * - ``blue_chat_kanban``
     - Bridge governado
     - Sincroniza CRM e Kanban com HMAC, idempotência e proteção contra loops.
   * - ``blue_chatwoot_message_trigger``
     - Mensageria por evento
     - Permite mensagens e templates a partir de ações e processos do Odoo.
   * - ``blue_chatwoot_revenue_ops``
     - Revenue intelligence
     - Converte sinais de conversa em casos e oportunidades de atuação comercial.
   * - ``blue_magica_ai_chatwoot``
     - IA sobre conversas
     - Usa contexto do atendimento para gerar insights no CRM sem duplicar credenciais.

Extensões nativas do bridge
===========================

O bridge também pode projetar eventos para aplicativos nativos do Odoo:

``blue_chat_kanban_helpdesk``
   Cria ou atualiza um único ticket por empresa e conversa quando o card alcança o estágio
   configurado para suporte. Reutiliza o cliente já vinculado ao lead.

``blue_chat_kanban_calendar``
   Usa ``scheduled_at`` do item operacional para criar ou atualizar um evento de calendário.
   Por padrão, não adiciona o cliente como participante, evitando convites inesperados.

``blue_chat_kanban_appointment``
   Complementa o Calendar com um tipo nativo de agendamento e sua duração/política de equipe.
   Requer o aplicativo Enterprise ``appointment`` e atualmente é voltado a tipos baseados em
   usuários.

Fluxo recomendado
=================

#. Configure a fundação ``blue_chatwoot`` por empresa.
#. Mapeie inboxes e equipes antes de habilitar automações.
#. Ative ``blue_chat_v3`` para operação comercial e sincronização.
#. Use ``blue_chat_plus`` quando a experiência em tempo real for necessária.
#. Configure ``blue_chat_kanban`` somente com segredo HMAC e ``account_id`` coerente.
#. Habilite Helpdesk, Calendar ou Appointments apenas para os processos que realmente precisam
   dessas projeções.
#. Adicione mensageria, revenue intelligence e IA como camadas complementares.

Segurança e idempotência
========================

O webhook do bridge valida assinatura HMAC, janela contra replay, vínculo de conta e identidade do
evento. Eventos repetidos com o mesmo conteúdo não devem criar registros duplicados. Um mesmo
``event_id`` com payload diferente é tratado como conflito.

O bridge não cria oportunidades CRM automaticamente a partir do webhook. A projeção parte de uma
oportunidade já existente e vinculada à conversa, reduzindo o risco de duplicação silenciosa.

Guias relacionados
==================

* :doc:`../applications/sales/crm`
* :doc:`../applications/productivity/whatsapp`
* :doc:`../applications/productivity/discuss`
* :doc:`../applications/services/helpdesk`
* :doc:`../applications/productivity/calendar`
* :doc:`../applications/productivity/appointments`

.. tip::

   Para operação diária, pense em **conversa → oportunidade → próxima ação**. O usuário não
   precisa conhecer a divisão entre módulos para trabalhar; a modularidade existe para manter a
   implantação, a segurança e a evolução do produto previsíveis.
