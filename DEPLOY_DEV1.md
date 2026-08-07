# docs-erp.conexaoazul.com — dev1 handoff

## Objetivo

Publicar a documentação ERP/Odoo 19 deste repositório em `https://docs-erp.conexaoazul.com`, executando o build e o runtime no runner self-hosted `dev1`.

O portal institucional/técnico existente em `https://docs.conexaoazul.com` continua pertencendo ao repositório `conexaoazul/azul-docs`. Os dois portais devem ser integrados por navegação explícita, não por duplicação de conteúdo.

## Arquitetura

- Fonte ERP: `conexaoazul/documentation`, branch `19.0`.
- Build: Sphinx `make html` em Python 3.12 isolado via Docker.
- Runtime: container `conexaoazul-docs-erp` com `nginx:1.27-alpine`.
- Origin local no dev1: `127.0.0.1:18081`.
- URL pública esperada: `https://docs-erp.conexaoazul.com`.
- TLS e exposição pública: Cloudflare/reverse proxy existente no dev1.

## O que o workflow já faz

1. checkout do ref solicitado;
2. build do Sphinx em container descartável;
3. valida `_build/html/index.html`;
4. publica release imutável em `/opt/conexaoazul/docs-erp/releases/<sha>`;
5. troca o symlink `/opt/conexaoazul/docs-erp/current`;
6. sobe/recria `conexaoazul-docs-erp` em `127.0.0.1:18081`;
7. executa healthcheck local;
8. se o DNS já existir, valida também `https://docs-erp.conexaoazul.com`.

## Gates que exigem o agente no dev1 / Cloudflare

### 1. Runner

Confirmar que o runner possui os labels:

- `self-hosted`
- `dev1`

E acesso local a Docker, `/opt/conexaoazul`, `curl` e DNS.

### 2. Reverse proxy ou Cloudflare Tunnel

Reusar o padrão operacional já adotado no dev1. O upstream deve ser:

`http://127.0.0.1:18081`

Host público:

`docs-erp.conexaoazul.com`

Não exponha a porta 18081 diretamente à Internet.

### 3. DNS Cloudflare

Criar/validar `docs-erp.conexaoazul.com` na zona `conexaoazul.com`.

Preferência:

- se o dev1 usa Cloudflare Tunnel, adicionar hostname público `docs-erp.conexaoazul.com -> http://127.0.0.1:18081` e criar o DNS gerenciado pelo Tunnel;
- se o dev1 usa reverse proxy público, criar o registro DNS proxied apontando para o origin já usado pelos demais serviços.

Não commitar tokens, Zone IDs sensíveis ou credenciais Cloudflare no repositório.

### 4. Primeira execução

Executar manualmente `Deploy docs ERP to dev1`, usando `19.0` como ref.

Validar:

- container `conexaoazul-docs-erp` healthy/running;
- `curl -fsS http://127.0.0.1:18081/` retorna HTML;
- `curl -fsSI https://docs-erp.conexaoazul.com/` retorna 2xx/3xx esperado;
- assets CSS/JS carregam sem erro;
- navegação interna do Sphinx funciona.

### 5. Integração com docs.conexaoazul.com

No repositório `conexaoazul/azul-docs`, adicionar navegação explícita para o portal ERP:

- sidebar/menu: `Documentação ERP/Odoo 19`;
- destino: `https://docs-erp.conexaoazul.com`;
- abrir no mesmo contexto ou nova aba conforme UX do portal.

Preferir link direto em vez de iframe como padrão. Iframe fica opcional apenas se houver uma página-hub específica, pois headers de segurança, navegação, SEO, cookies e responsividade tornam iframe menos robusto.

### 6. Segurança e governança

- documentação ERP pública somente se o conteúdo do fork for intencionalmente público;
- conteúdo interno deve permanecer fora desta publicação ou protegido por Cloudflare Access;
- manter o fork próximo do upstream Odoo e colocar customizações comerciais próprias em `azul-docs` ou módulos Odoo dedicados;
- releases são imutáveis por SHA para facilitar rollback;
- para rollback, apontar `/opt/conexaoazul/docs-erp/current` para release anterior e recriar/reload do container.

## Critério de encerramento

O handoff está concluído quando:

1. workflow passa no runner dev1;
2. URL `https://docs-erp.conexaoazul.com` abre com HTTPS válido;
3. assets e links essenciais passam smoke test;
4. `docs.conexaoazul.com` possui link visível para o novo portal;
5. evidências do deploy e do DNS são registradas na PR.
