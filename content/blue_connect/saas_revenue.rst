=====================================
SaaS, assinaturas e receita recorrente
=====================================

A família Blue SaaS conecta a jornada comercial de um software recorrente ao ciclo de vida da
instância, assinatura, cobrança, portal e provisionamento. O ERP mantém o contexto comercial;
a execução de infraestrutura continua desacoplada e entra por bridges controlados.

Quando usar
===========

Use esta solução quando sua operação precisa:

* criar trial a partir de lead ou oportunidade;
* relacionar venda/assinatura a uma instância SaaS;
* promover a mesma instância de trial para produção;
* acompanhar lifecycle comercial e operacional sem acoplar CRM ao runtime;
* ligar cobrança recorrente e confirmação de receita ao provisionamento;
* expor contexto de assinatura e instância no portal;
* integrar um Control Plane sem torná-lo o sistema de registro comercial.

Módulos principais
==================

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Módulo
     - Responsabilidade
   * - ``blue_saas``
     - Núcleo do lifecycle de instâncias entre CRM, vendas, trial e produção.
   * - ``blue_saas_control_plane_bridge``
     - Bridge entre o contexto comercial da instância e o Control Plane operacional.
   * - ``blue_saas_subscription_bridge``
     - Conecta instâncias às assinaturas recorrentes Enterprise e ao Control Plane.
   * - ``blue_saas_revenue_lifecycle``
     - Integra marketplace, CRM, trial, venda, Asaas, assinatura, portal e provisionamento.
   * - ``blue_payment_asaas_subscriptions``
     - Camada financeira de cobrança/assinaturas recorrentes quando Asaas é o provedor escolhido.
   * - ``blue_automation_marketplace``
     - Catálogo/ativação de automações que podem compor uma oferta SaaS quando habilitado.

Jornada recomendada
===================

#. **Lead / oportunidade** registra necessidade, produto, origem e responsável.
#. **Oferta / pedido** define o que será contratado e em quais condições.
#. **Trial** cria ou associa a instância sem confundir avaliação com produção.
#. **Conversão** promove a mesma identidade de instância quando a venda/receita é confirmada.
#. **Assinatura** passa a governar recorrência comercial quando o produto utiliza assinatura.
#. **Control Plane** executa ou acompanha mudanças de infraestrutura por contrato explícito.
#. **Portal e operação** mostram ao cliente e ao time somente o estado que cada papel precisa ver.

Fronteiras importantes
======================

CRM / Vendas
   Autoridade sobre oportunidade, responsável, proposta e venda.

Assinaturas / Financeiro
   Autoridade sobre recorrência comercial, cobrança e documentos financeiros.

Blue SaaS
   Mantém a identidade e o lifecycle da instância no contexto de negócio.

Control Plane
   Executa ou observa operações de infraestrutura. Não deve reescrever silenciosamente a verdade
   comercial do ERP.

Bridge
   Traduz eventos e estados entre os lados com idempotência e rastreabilidade.

Enterprise e dependências
=========================

Algumas capacidades, como o bridge de assinatura, dependem de módulos Enterprise. Instale apenas
os satélites compatíveis com a edição e com a arquitetura do tenant. O núcleo não deve ganhar uma
dependência Enterprise apenas para atender um cenário opcional.

Guias relacionados
==================

* :doc:`../applications/sales/subscriptions`
* :doc:`../applications/sales/crm`
* :doc:`../applications/sales/sales`
* :doc:`financeiro_asaas`
* :doc:`ai_automation`

.. tip::

   Na UX, o usuário comercial deve enxergar **cliente, oferta, assinatura e estado da instância**.
   Detalhes de cluster, container, runner ou deploy pertencem ao cockpit operacional, não ao fluxo
   cotidiano do vendedor.
