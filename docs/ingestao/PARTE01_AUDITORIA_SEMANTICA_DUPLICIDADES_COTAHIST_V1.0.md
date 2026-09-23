# PARTE01 — Auditoria Semântica das Duplicidades COTAHIST

## Arquivo
PARTE01_AUDITORIA_SEMANTICA_DUPLICIDADES_COTAHIST_V1.0.md

## Projeto
B3 — A BOLSA DO BRASIL

## Caminho
docs/ingestao/PARTE01_AUDITORIA_SEMANTICA_DUPLICIDADES_COTAHIST_V1.0.md

## Data de criação
2026-09-23

## Repositório
carlos-andrade/B3

## Objetivo

Documentar a interpretação das duplicidades encontradas ao agrupar registros COTAHIST pela chave candidata:

`data_pregao + codbdi + codneg + tpmerc + dismes`

A auditoria não elimina registros. O RAW permanece a evidência primária.

## Resultado da auditoria

A execução do GitHub Actions concluiu os 41 anos de 1986 a 2026 com sucesso.

O primeiro caso auditado, 1986, apresentou 5.182 grupos duplicados e 5.189 linhas excedentes. Nenhum grupo era idêntico em todos os 25 campos; os 5.182 grupos apresentaram diferenças semânticas.

Os campos com diferenças mais frequentes em 1986 foram:

- PRAZOT: 5.180 grupos
- PREABE: 5.153
- PREMAX: 5.151
- PREMIN: 5.147
- PREMED: 5.153
- PREULT: 5.139
- QUATOT: 5.019
- VLTOT/VOLTOT: 5.181
- TOTNEG: 3.878

Isso demonstra que a chave candidata anterior é insuficiente para representar exclusivamente uma série de negociação.

## Interpretação técnica

Os exemplos mostram que um mesmo:

- pregão;
- CODBDI;
- código de negociação;
- tipo de mercado;
- número de distribuição;

pode possuir múltiplos registros legítimos, especialmente quando `TPMERC=030` e `PRAZOT` varia.

Exemplo observado em 1986:

- `CNF 2`, TPMERC 030, DISMES 008;
- PRAZOT 030 e PRAZOT 060;
- preços, quantidade, número de negócios e volume distintos.

Portanto, esses registros não devem ser tratados como duplicatas a serem removidas.

## Nova hipótese de chave

A próxima chave de investigação deverá incorporar, no mínimo:

`data_pregao + codbdi + codneg + tpmerc + prazot + dismes`

A inclusão de `DATVEN` também deverá ser testada, principalmente em instrumentos cujo vencimento seja material para a identificação da série.

Esta é uma hipótese de modelagem, não uma chave definitiva.

## Próxima validação obrigatória

1. Reexecutar a auditoria com `PRAZOT` incorporado.
2. Medir duplicidades residuais.
3. Testar `DATVEN` como componente adicional.
4. Separar por `TPMERC`.
5. Avaliar `CODOISI/CODISI` como identificador econômico, sem assumir validade universal antes da documentação histórica.
6. Investigar mudanças de codificação ao longo de 1986–2026.
7. Somente depois definir a chave natural do NORMALIZED.
8. Não excluir nenhuma linha do RAW ou NORMALIZED antes da conclusão.

## Regra de integridade

Duplicidade de chave candidata != erro de dados.

Um registro somente poderá ser descartado se existir evidência documental e técnica suficiente de que representa duplicação física do mesmo registro econômico.

## Relação com microestrutura

COTAHIST é uma série histórica de cotações de fim de pregão. Esta auditoria não cria dados de agressão, fluxo, Cumulative Delta, VWAP intradiário ou negócio-a-negócio.

Essas camadas deverão ser tratadas posteriormente com fontes de microestrutura apropriadas.

## Estado

- RAW 1986–2026: VALIDADO e persistido.
- NORMALIZED: evidências de qualidade e checksums presentes no repositório.
- Auditoria semântica da chave candidata: CONCLUÍDA.
- Chave natural definitiva: PENDENTE.
- Exclusão de registros: PROIBIDA nesta etapa.
