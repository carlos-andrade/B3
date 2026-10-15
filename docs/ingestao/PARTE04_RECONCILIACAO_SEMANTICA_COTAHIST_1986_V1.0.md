# PARTE04 — Reconciliação Semântica COTAHIST 1986

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-843AB62FC543 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 3c3838914a75a66cad3757f230086c4759ae0358a97cb4d7f66ce1327c3de8ed |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** PARTE04_RECONCILIACAO_SEMANTICA_COTAHIST_1986_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconciliação semântica do primeiro ano da série COTAHIST  
**Caminho:** docs/ingestao/PARTE04_RECONCILIACAO_SEMANTICA_COTAHIST_1986_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Regra
1986 é o ano-piloto. Nenhum processamento interpretativo de 1987 será liberado antes da aprovação desta reconciliação.

## Ordem
1. mapear TPMERC;
2. mapear CODBDI;
3. determinar chave lógica;
4. investigar os casos OHLC;
5. validar volume/quantidade;
6. validar calendário;
7. comparar amostras RAW → NORMALIZED;
8. liberar 1987 somente com evidência.

O layout oficial da B3 define CODBDI como classificação para o Boletim Diário de Informações e TPMERC como código do mercado do papel. A B3 informa que a série cobre títulos negociados desde 1986 e preserva a moeda/forma de cotação da época.

Esta etapa é analítica: RAW não será alterado e códigos não serão classificados definitivamente apenas por frequência.

**Status: 1986 BLOQUEADO PARA LIBERAÇÃO.**
