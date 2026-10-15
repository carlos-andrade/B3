# PARTE03 — B3 INTRADAY: EVIDÊNCIA DE ACESSO POR PREGÃO V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-FF27B9BC27D2 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | b09d580026f95275fe7d0d311dbe5997fcaaac425984f8db4276f01e634f5279 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** PARTE03_B3_INTRADAY_EVIDENCIA_ACESSO_2026-09-24.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Evidência da disponibilidade retroativa dos arquivos B3  
**Caminho:** docs/ingestao/PARTE03_B3_INTRADAY_EVIDENCIA_ACESSO_2026-09-24.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Evidência oficial

A página oficial Pesquisa por Pregão informa que os boletins e arquivos da B3 podem ser obtidos por seleção de data e download, inclusive para arquivos retroativos.

Fonte:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/

## 2. Arquivos relevantes confirmados

A página oficial apresenta atualmente:

- BVBG.086.01 — PriceReport;
- BVBG.187.01 — Simplified Price Report - Derivatives;
- BVBG.028.02 — Instruments File;
- BVBG.029.02 — Instruments File - Indicators.

## 3. Mudança estrutural da B3

A página oficial de Cotações informa que, desde 15/12/2025, os dados passaram a ser consultados no Boletim Diário do Mercado.

Para derivativos, o caminho oficial é:

Derivativos > Derivativos de bolsa > Negócio a negócio.

Fonte:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/cotacoes/

## 4. Resultado da pesquisa de 24/09/2026

A busca web confirmou a página oficial e a infraestrutura de arquivos da B3, porém o conteúdo indexado não expôs o identificador/URL final do download para os arquivos de 16/09/2026 e 17/09/2026.

Logo:

RAW_16_09 = PENDENTE
RAW_17_09 = PENDENTE
DOWNLOAD_URL_EXATO = PENDENTE
SHA256 = PENDENTE

## 5. Consequência metodológica

Não será considerado que os dados foram capturados apenas porque a B3 confirma que eles existem e podem ser pesquisados retroativamente.

A captura será marcada como concluída somente quando o arquivo binário/CSV efetivo estiver disponível e for preservado no repositório.

## 6. Próximo procedimento

O próximo passo operacional é resolver o mecanismo de download da página dinâmica do BDI/Pesquisa por Pregão.

Depois:

1. baixar 16/09/2026;
2. baixar 17/09/2026;
3. preservar RAW;
4. SHA-256;
5. identificar WIN/WDO/DI;
6. validar contratos;
7. normalizar;
8. comparar com os dados EOD;
9. construir a janela Copom 281.

## 7. Regra de integridade

Nenhum retorno, volume, agressão, delta ou métrica de microestrutura será preenchido por estimativa enquanto o dataset primário permanecer pendente.
