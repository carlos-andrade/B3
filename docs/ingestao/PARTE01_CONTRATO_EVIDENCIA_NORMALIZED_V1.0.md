# Arquivo: PARTE01_CONTRATO_EVIDENCIA_NORMALIZED_V1.0.md
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
