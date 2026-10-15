# FASE 07E — DIMES do COTAHIST 1986

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-B8F66536C73F |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | cc19eac93a6414fb1ef6b752dfc6aa233e26981d2ea294423a80897d1c19d3fc |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** FASE07E_COTAHIST_1986_DIMES_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconciliação histórica do campo DIMES  
**Caminho:** docs/ingestao/FASE07E_COTAHIST_1986_DIMES_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo

Determinar a natureza observável do campo DIMES em 1986, medir sua cardinalidade e frequência e verificar sua relação temporal com CODNEG, CODISI, ESPECI e TPMERC.

## Evidência documental

No layout oficial B3 do COTAHIST, DIMES ocupa as posições 243–245, com formato 9(03). A descrição documental é:

- “NÚMERO DE DISTRIBUIÇÃO DO PAPEL”;
- “NÚMERO DE SEQÜÊNCIA DO PAPEL CORRESPONDENTE AO ESTADO DE DIREITO VIGENTE”.

Fonte documental: B3, **LAYOUT DO ARQUIVO – COTAÇÕES HISTÓRICAS**, revisão 02, 05/10/2020.

Fonte oficial:
https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf

## Regra histórica

O layout é uma fonte documental posterior ao ano analisado. Portanto, a descrição oficial é usada para interpretar o campo, mas não se presume que toda a semântica operacional posterior seja retroativamente idêntica em 1986.

Para 1986:

- DIMES é preservado exatamente como atributo do registro;
- valores são analisados como códigos de três posições;
- não se transforma DIMES em identificador econômico;
- não se presume DIMES = CODNEG;
- não se presume DIMES = CODISI;
- alterações de DIMES no mesmo CODNEG devem ser tratadas como evidência de mudança de estado/atributo até investigação adicional;
- nenhuma alteração é feita no RAW ou no NORMALIZED.

## Métricas

O analisador calcula:

1. quantidade total de registros tipo 01;
2. quantidade de DIMES vazios e não vazios;
3. cardinalidade de DIMES;
4. frequência de cada valor;
5. quantidade de pregões por DIMES;
6. quantidade de CODNEG distintos por DIMES;
7. quantidade de CODISI distintos por DIMES;
8. quantidade de ESPECI distintos por DIMES;
9. distribuição TPMERC por DIMES;
10. CODNEG que apresentam mais de um DIMES ao longo de 1986;
11. CODISI não vazio que apresenta mais de um DIMES.

## Artefatos

**Script:** `scripts/ingestao/analisar_dimes_cotahist_1986_v1.py`

**Resultado esperado:** `dados/cotahist/quality/COTAHIST_1986_DIMES_V1.json`

## Governança

RAW e NORMALIZED permanecem inalterados.

O resultado desta frente é uma análise de atributo histórico. Não constitui declaração de identidade econômica definitiva.

## Próxima frente

**07F — investigação da colisão residual K4.**
