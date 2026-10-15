# Arquivo: PARTE01_CONTRATO_EVIDENCIA_NORMALIZED_V1.0.md

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-10043B27A796 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 959b7610729c3eda19f41420df265d471537bd0fe59f00fe7c9ad3b65a108f09 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
# Projeto: B3 - A BOLSA DO BRASIL
# Tema: Contrato de evidência auditável da camada NORMALIZED
# Caminho: docs/ingestao/PARTE01_CONTRATO_EVIDENCIA_NORMALIZED_V1.0.md
# Data de criação: 23/09/2026
# Repositório: carlos-andrade/B3

## Objetivo

Estabelecer o contrato mínimo para que a transformação RAW → NORMALIZED seja reproduzível, verificável e auditável no repositório.

## Cadeia de evidência

RAW COTAHIST validado
→ parser versionado
→ CSV NORMALIZED
→ relatório de qualidade
→ SHA-256 do NORMALIZED
→ manifesto persistido no Git.

## Evidências persistidas

Para cada ano normalizado, o repositório deve preservar:

- `dados/cotahist/normalized/manifests/COTAHIST_AAAAAAA_quality.json`;
- `dados/cotahist/normalized/manifests/COTAHIST_AAAAAAA.csv.sha256`.

O CSV NORMALIZED pode permanecer como artefato temporário do GitHub Actions quando seu volume tornar inadequado o armazenamento no Git. Seu SHA-256 permanece no repositório para permitir verificação de identidade do artefato.

## Conteúdo mínimo do manifesto

- schema_version;
- status;
- ano;
- parser_version;
- source;
- raw_file;
- raw_sha256;
- normalized_file;
- normalized_sha256;
- número de linhas;
- número de campos;
- primeira e última data;
- datas inválidas;
- datas fora do ano;
- duplicidades da chave candidata;
- definição da chave candidata;
- declaração de que RAW permanece a fonte primária.

## Regra de validação

NORMALIZED só recebe `VALIDADO` quando:

1. o RAW de origem estiver validado;
2. o parser concluir sem erro;
3. existirem registros NORMALIZED;
4. os campos obrigatórios existirem;
5. as datas forem calendariamente válidas;
6. nenhuma data estiver fora do ano selecionado;
7. o SHA-256 do CSV for calculado;
8. o manifesto e o checksum forem persistidos no repositório.

Falhas recebem estado `REVISAR` ou interrompem a execução. Nenhum número de qualidade deve ser inventado fora de execução efetiva.

## Escopo atual

O objetivo operacional é normalizar, de forma auditável, os anos de 1986 até o ano corrente que possuam RAW COTAHIST validado no repositório.

## Limitação de dados

COTAHIST é série histórica de cotações e não contém, por si só, agressão, fluxo comprador/vendedor, Cumulative Delta ou negócio-a-negócio. Esses dados exigem fontes de microestrutura próprias.

## Princípio de reprodutibilidade

O manifesto deve permitir responder:

`Qual RAW produziu este NORMALIZED?`

`Qual versão do parser foi usada?`

`Qual foi o SHA-256 do resultado?`

`Quais testes de qualidade foram executados?`

A resposta deve ser obtida exclusivamente por evidência registrada.
