# FASE 07C — CODBDI do COTAHIST 1986

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-B661D2788A1E |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | a91d4b1bdf778b6f0f3f38c9c8f92600370246d318ca02552f36c38bf77f5221 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
