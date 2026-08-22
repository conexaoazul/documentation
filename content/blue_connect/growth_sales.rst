========================================
Prospecção, CRM e máquina de vendas
========================================

Esta família cobre a jornada anterior e posterior à entrada do lead no CRM: geração, organização,
enriquecimento, segmentação, distribuição, cadência e abordagem comercial.

Quando usar
===========

Use esta solução quando sua equipe precisa:

* gerar ou importar listas de prospects;
* classificar ICP, vertente, segmento ou potencial;
* enriquecer dados antes da abordagem;
* distribuir leads entre equipes e vendedores com regras de capacidade;
* executar cadências de follow-up;
* preparar mensagens e propostas com contexto do CRM;
* conectar prospecção ao atendimento omnichannel.

Módulos principais
==================

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Módulo
     - Responsabilidade
   * - ``blue_lead_generator``
     - Geração/importação de leads para alimentar a operação comercial.
   * - ``blue_partner_taxonomy``
     - Taxonomia de parceiros, vertentes, soluções, tiers e status comerciais.
   * - ``blue_sales_machine``
     - Enriquecimento, scoring ICP e classificação para priorização de oportunidades.
   * - ``blue_outbound_engine``
     - Preparação de abordagem outbound e campanhas por vertente/segmento.
   * - ``blue_crm_lead_distribution_custom``
     - Regras de distribuição, capacidade por vendedor/equipe e rastreabilidade da atribuição.
   * - ``blue_crm_lead_followup``
     - Cadências e próximos passos automáticos conforme estágio e interação.
   * - ``blue_proposta_whatsapp``
     - Apoio à criação de proposta/mensagem comercial usando contexto da oportunidade.

Jornada recomendada
===================

#. **Capturar** o lead com origem e identificadores mínimos.
#. **Normalizar** telefone, e-mail, CPF/CNPJ e razão/nome quando disponíveis.
#. **Enriquecer** somente com provedores e regras aprovadas.
#. **Classificar** ICP, vertente, prioridade e potencial.
#. **Distribuir** respeitando empresa, equipe, capacidade e elegibilidade do vendedor.
#. **Executar a próxima ação** por atividade, cadência, WhatsApp, e-mail ou ligação.
#. **Medir resultado** em oportunidade, receita, perda, tempo de resposta e aprendizado.

Distribuição de leads
=====================

A distribuição deve ser entendida como uma política operacional, não apenas como round-robin. Em
cenários com capacidade por vendedor/equipe, o mesmo usuário pode ter limites diferentes em cada
equipe. Regras multiempresa devem usar a empresa da oportunidade e da equipe como fronteira de
seleção e segurança.

Omnichannel como continuação da jornada
=======================================

Quando o lead entra em conversa ativa, use :doc:`crm_omnichannel` para conectar o atendimento ao
CRM sem perder origem, responsável, estágio e histórico comercial.

Guias relacionados
==================

* :doc:`../applications/sales/crm`
* :doc:`../applications/marketing/marketing_automation`
* :doc:`../applications/productivity/whatsapp`
* :doc:`data_intelligence`

.. tip::

   Para o usuário comercial, a interface ideal responde sempre a três perguntas: **quem priorizar,
   por quê e qual a próxima ação**. As automações devem reduzir trabalho mecânico sem esconder o
   motivo de uma atribuição ou recomendação.
