========================================
Dados, consultas e enriquecimento
========================================

A família de dados reúne consultas, saldo, recarga, provedores e enriquecimento para apoiar
qualificação comercial, análise cadastral e fluxos operacionais.

Quando usar
===========

Use esta solução quando sua operação precisa:

* consultar CPF ou CNPJ por provedores integrados;
* enriquecer contatos e oportunidades com dados externos;
* vender créditos, planos ou pacotes de consulta;
* expor uma experiência de portal/marketplace para consumo de dados;
* rastrear saldo e utilização por cliente ou empresa;
* combinar consulta com CRM, cobrança e automações.

Módulos principais
==================

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Módulo
     - Responsabilidade
   * - ``blue_credit_query``
     - Núcleo de consultas, saldo, recarga e experiência de uso da plataforma de dados.
   * - ``blue_credit_query_marketplace``
     - Catálogo público de planos, créditos e acesso comercial às consultas/APIs.
   * - ``blue_credit_query_asaas``
     - Integração financeira para compra de créditos, planos e eventos de pagamento.
   * - ``blue_assertiva``
     - Provedor de consulta/enriquecimento por API Assertiva.
   * - ``blue_lemiti``
     - Provedor de consulta/enriquecimento por API Lemiti.
   * - ``blue_disparador_lemiti_assertiva``
     - Uso de dados enriquecidos em fluxos autorizados de comunicação e prospecção.

Como pensar o fluxo
===================

#. O cliente ou usuário inicia uma consulta pelo portal, CRM ou fluxo autorizado.
#. O núcleo identifica o provedor e valida saldo/entitlement quando aplicável.
#. A chamada externa é executada com as credenciais configuradas para a empresa.
#. O retorno útil é normalizado e associado ao registro de negócio correspondente.
#. O consumo é registrado para saldo, auditoria e eventual cobrança.
#. Dados enriquecidos só entram em automações posteriores quando o processo e a base legal
   permitirem.

Boas práticas
=============

* Normalize CPF, CNPJ, telefone e demais identificadores antes da consulta.
* Evite guardar payload bruto quando apenas campos específicos são necessários.
* Mantenha token e segredo fora de logs e mensagens de erro.
* Trate timeout, indisponibilidade e limite do provedor como estados esperados de integração.
* Diferencie claramente **consulta**, **enriquecimento**, **validação** e **decisão**. Um dado
  retornado por um provedor não deve, sozinho, executar uma decisão crítica sem regra explícita.

Integrações relacionadas
========================

A camada de dados pode alimentar CRM e prospecção, enquanto a camada financeira pode cuidar da
compra de créditos e recorrência. Veja também:

* :doc:`growth_sales`
* :doc:`financeiro_asaas`
* :doc:`../applications/sales/crm`

Documentação de API
===================

Para integrações externas e exemplos de consumo, consulte também a documentação dedicada das
APIs de dados: `Data Azul / Blue Credit API <https://docs.conexaoazul.com/blue-credit-api/intro>`__.
