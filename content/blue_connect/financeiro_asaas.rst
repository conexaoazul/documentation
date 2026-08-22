=========================
Financeiro, Asaas e NFSe
=========================

A família financeira conecta cobrança e recebimento ao fluxo nativo de vendas e faturamento. A
ideia é manter pedidos, faturas, clientes e lançamentos no ERP enquanto o Asaas atua como meio de
pagamento, cobrança, recorrência e emissão fiscal quando aplicável.

Quando usar
===========

Use esta solução para:

* gerar cobranças via PIX, boleto ou cartão;
* acompanhar pagamentos e baixar faturas;
* emitir, consultar ou cancelar NFSe por fluxo integrado;
* operar assinaturas e receita recorrente;
* acompanhar recebimentos, pendências e indicadores financeiros;
* reconciliar eventos externos sem criar um financeiro paralelo.

Módulos principais
==================

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Módulo
     - Responsabilidade
   * - ``blue_payment_asaas``
     - Integração principal de cobrança Asaas com o fluxo comercial/financeiro.
   * - ``blue_payment_asaas_nfse``
     - Emissão, consulta e cancelamento de NFSe vinculados aos documentos do ERP.
   * - ``blue_payment_asaas_subscriptions``
     - Assinaturas recorrentes e métricas como MRR, ARR, LTV e churn.
   * - ``blue_payment_asaas_bi``
     - Indicadores de recebimentos, saldo, pendências e acompanhamento gerencial.
   * - ``blue_asaas_financial_sync``
     - Sincronização de movimentos financeiros para a contabilidade quando o cenário exigir.
   * - ``blue_asaas_payment_sync``
     - Automação específica de baixa e sincronização de pagamentos.

Fluxo recomendado
=================

#. Configure empresa, diário, contas e impostos no Financeiro antes da integração.
#. Cadastre e valide a conta Asaas no ambiente correto.
#. Defina quais meios de pagamento estarão disponíveis por fluxo comercial.
#. Valide cobrança em sandbox/homologação antes de produção.
#. Habilite NFSe somente após confirmar cadastro fiscal, serviço, município e regras aplicáveis.
#. Para recorrência, defina produto/plano e política de renovação antes de ativar automações.
#. Monitore falhas de webhook e reconciliação como exceção operacional, não como rotina manual.

Autoridade dos dados
====================

O documento comercial e financeiro do ERP continua sendo a referência operacional. O retorno do
provedor atualiza esse contexto por identificadores e eventos controlados. A integração não deve
criar uma segunda verdade de cliente, cobrança ou receita.

Guias relacionados
==================

* :doc:`../applications/finance/accounting`
* :doc:`../applications/finance/payment_providers`
* :doc:`../applications/finance/fiscal_localizations`
* :doc:`../applications/sales/sales`
* :doc:`../applications/sales/subscriptions`

.. warning::

   Credenciais, webhooks e ambientes de homologação/produção devem ser tratados separadamente.
   Não reutilize segredo de produção em testes e não considere um pagamento confirmado somente
   porque um payload externo afirma que ele ocorreu quando o fluxo exigir reconfirmação.
