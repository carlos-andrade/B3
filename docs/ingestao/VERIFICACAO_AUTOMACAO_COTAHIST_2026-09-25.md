# VERIFICAÇÃO DA AUTOMAÇÃO DE IMPORTAÇÃO COTAHIST — 2026-09-25

## Objetivo

Registrar a verificação do processo de importação automática diária do COTAHIST B3 após a implantação da V1.

## Estado verificado

### Workflow

Arquivo:

`.github/workflows/cotahist-importacao-diaria-v1.yml`

Configuração confirmada:

- execução agendada: `30 23 * * *` UTC;
- execução manual disponível via `workflow_dispatch`;
- permissão `contents: write`;
- concorrência controlada;
- timeout de 30 minutos;
- execução do importador diário;
- persistência em `dados/cotahist/raw/diario`;
- persistência da normalização em `dados/cotahist/normalized/diario`;
- persistência dos manifests em `dados/cotahist/normalized/manifests/diario`;
- publicação de evidências como artifact.

## Importador

Arquivo:

`scripts/ingestao/importar_cotahist_diario_v1.py`

Configuração confirmada:

- timezone operacional: `America/Sao_Paulo`;
- construção automática do arquivo diário;
- fonte operacional: B3;
- validação do ZIP;
- exigência de exatamente um arquivo dentro do ZIP;
- SHA-256 do RAW;
- normalização pelo parser COTAHIST 1.1.0;
- validação estrutural da saída normalizada;
- SHA-256 do normalizado;
- manifest JSON;
- preservação do RAW;
- comportamento sem alteração quando o mesmo arquivo já existe.

## Evidência de execução

**Não foi localizada evidência de uma execução concluída da V1 durante esta verificação.**

Também não foi localizado, neste momento, o diretório:

`dados/cotahist/normalized/manifests/diario`

no branch `main`.

Portanto, a automação está **implantada**, mas a execução operacional ainda deve ser considerada **NÃO COMPROVADA** até existir uma primeira execução observável e seu respectivo manifest/evidência.

## Classificação

| Item | Estado |
|---|---|
| Código do importador | IMPLANTADO |
| Workflow agendado | IMPLANTADO |
| Fonte operacional configurada | IMPLANTADA |
| Normalização automática | IMPLANTADA |
| Manifest diário | IMPLEMENTADO NO CÓDIGO |
| Primeira execução observável | **NÃO COMPROVADA** |
| Primeiro arquivo diário importado | **NÃO COMPROVADO** |
| Primeira validação real do endpoint | **NÃO COMPROVADA** |

## Regra de confiança

A existência do workflow não será tratada como prova de que a ingestão funcionou.

A cadeia somente será promovida para **VALIDADA EM PRODUÇÃO** depois de observar:

`workflow executado → aquisição real → RAW → SHA-256 → normalização → manifest → persistência no repositório`

## Próximo marco

A primeira execução efetiva deverá ser verificada antes de considerar a automação operacionalmente certificada.

Após a primeira execução, registrar:

- ID da execução;
- data/hora;
- resultado;
- data do COTAHIST adquirido;
- quantidade de linhas;
- SHA-256 RAW;
- SHA-256 normalizado;
- primeira/última data;
- commit gerado;
- eventuais falhas.

## Relação com 1986

A automação diária não depende da resolução semântica do COTAHIST 1986.

O problema histórico de 1986 permanece isolado como exceção controlada e não bloqueia a ingestão dos dados atuais.

## Conclusão

Em 2026-09-25, o repositório possui o **mecanismo de importação diária automática do COTAHIST implementado**, porém ainda não há evidência suficiente para declarar a primeira execução real como bem-sucedida.

Essa distinção permanece obrigatória na Carta de Confiança dos Dados e no Modelo de Governança.
