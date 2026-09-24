# FASE 07C — CODBDI do COTAHIST 1986

**Arquivo:** FASE07C_COTAHIST_1986_CODBDI_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconciliação semântica histórica do campo CODBDI  
**Caminho:** docs/ingestao/FASE07C_COTAHIST_1986_CODBDI_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo
Identificar todos os CODBDI observados no COTAHIST 1986, medir frequência, cobertura temporal e relação com CODNEG/TPMERC, e confrontar os códigos com a tabela oficial B3.

## Evidência oficial
No registro tipo 01, CODBDI ocupa as posições 11–12 e é utilizado para classificar os papéis na emissão do Boletim Diário de Informações. A tabela B3 documenta códigos como 02 (lote padrão), 10 (direitos e recibos), 12 (fundos imobiliários), 38/42 (exercício de opções), 62 (mercado a termo), 70/71 (futuros), 78/82 (opções), entre outros.

Fonte: B3, *LAYOUT DO ARQUIVO – COTAÇÕES HISTÓRICAS*, tabela CODBDI.

## Regra histórica
A tabela oficial disponível é evidência documental de sua versão publicada, não prova automática da semântica exata em 1986. O resultado marcará códigos como documentados ou não mapeados. Nenhum significado será inventado para código desconhecido.

## Análise adicional
Além da frequência, o resultado registra:
- número de pregões por CODBDI;
- número de CODNEG distintos;
- distribuição de TPMERC dentro de cada CODBDI;
- códigos não mapeados.

CODBDI é atributo classificatório. Não será usado isoladamente como identidade econômica permanente.

## Governança
RAW e NORMALIZED permanecem imutáveis. A análise não corrige registros históricos.

## Artefatos
Script: `scripts/ingestao/analisar_codbdi_cotahist_1986_v1.py`  
Resultado esperado: `dados/cotahist/quality/COTAHIST_1986_CODBDI_V1.json`

## Próxima frente
Após execução e auditoria do JSON: **07D — CODISI**.
