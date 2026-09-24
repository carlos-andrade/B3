# FASE 07E — DIMES do COTAHIST 1986

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
