========================================
Visão geral da plataforma
========================================

O Blue Connect organiza capacidades adicionais ao ERP/CRM em camadas que compartilham o mesmo
contexto de clientes, oportunidades, pedidos, faturas, atividades e operações.

Escolha pelo que você quer resolver
===================================

**Atendimento, WhatsApp e CRM omnichannel**
   Centralize conversas, oportunidades, agentes, Kanban, agenda e contexto comercial.
   Veja :doc:`crm_omnichannel`.

**Cobrança, pagamentos, NFSe e recorrência**
   Integre Asaas ao fluxo financeiro e comercial, com PIX, boleto, cartão, NFSe e indicadores.
   Veja :doc:`financeiro_asaas`.

**Consultas e enriquecimento de dados**
   Use provedores de dados para CPF, CNPJ e outros sinais em fluxos de consulta e qualificação.
   Veja :doc:`data_intelligence`.

**Prospecção e máquina de vendas**
   Organize geração, enriquecimento, segmentação, distribuição, cadência e abordagem comercial.
   Veja :doc:`growth_sales`.

**IA, agentes e automações**
   Adicione inteligência e automação sem criar um segundo sistema de registro para CRM,
   financeiro ou atendimento. Veja :doc:`ai_automation`.

**SaaS, assinaturas e receita recorrente**
   Conecte instâncias, contratos, assinatura, provisionamento e lifecycle de receita.
   Veja :doc:`saas_revenue`.

Como a arquitetura é organizada
===============================

O desenho segue quatro princípios:

#. **O aplicativo nativo continua sendo a autoridade dos dados.** CRM continua no CRM,
   Helpdesk continua no Helpdesk e agenda continua no Calendar/Appointments.
#. **Integrações reutilizam contratos centrais.** Credenciais e transporte não devem ser
   duplicados em cada módulo.
#. **Módulos especializados são opt-in.** Uma capacidade adicional só entra quando faz sentido
   para o processo e para a edição instalada.
#. **Automação não substitui governança.** Ações financeiras, destrutivas ou com impacto
   comercial podem exigir regras, aprovação ou decisão humana.

Documentação nativa relacionada
================================

Os módulos Blue Connect complementam os guias nativos, não os substituem. Para fundamentos,
consulte também:

* :doc:`../applications/sales/crm`
* :doc:`../applications/finance/accounting`
* :doc:`../applications/productivity/whatsapp`
* :doc:`../applications/productivity/calendar`
* :doc:`../applications/productivity/appointments`
* :doc:`../applications/services/helpdesk`
* :doc:`../applications/productivity/ai`

.. note::

   A disponibilidade de cada módulo depende da edição, do ambiente, das integrações contratadas
   e da homologação aplicável. A presença nesta documentação descreve a arquitetura e o fluxo
   suportado, não uma promessa automática de ativação em qualquer tenant.
