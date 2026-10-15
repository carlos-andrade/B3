# PARTE03 — NEGÓCIO A NEGÓCIO: RECONCILIAÇÃO DA FONTE V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-1FA363EAF02E |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 8ccbaeb6c4a83a73c9d39f5b3e9894109f1d8f19fd617a4cbb3eadb2e55917cb |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** PARTE03_NEGOCIO_A_NEGOCIO_RECONCILIACAO_FONTE_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconciliacao da rota oficial e separacao entre BDM e UP2DATA  
**Caminho:** docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_RECONCILIACAO_FONTE_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Evidência oficial

A B3 confirma que, desde 15/12/2025, os dados anteriormente disponíveis na página de Cotações passaram ao Boletim Diário do Mercado.

Para derivativos, a rota oficial é:

Derivativos > Derivativos de bolsa > Negócio a negócio.

Fonte:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/cotacoes/

O Comunicado Externo 01/2026-VTEC também mapeia “Negócio a Negócio – Listados” para:

Derivativos > Derivativos de bolsa > Negócio a negócio.

## 2. Distinção importante

A página “Dados disponíveis” do UP2DATA descreve “Informações de negócios” de derivativos como dados consolidados, incluindo mínimo, máximo e volume do dia.

Isso não deve ser confundido com o dataset trade-by-trade requerido neste projeto.

Assim:

- Informações de negócios consolidadas = validação diária;
- Negócio a negócio = candidata a fonte trade-by-trade;
- SPRD/BVBG.187 = fonte consolidada/EOD;
- Cumulative Delta = somente após validação do dataset de negócios individuais.

## 3. Consequência operacional

A próxima aquisição deve priorizar o Boletim Diário do Mercado e não substituir a tabela Negócio a negócio por dados consolidados do UP2DATA.

Se o BDM oferecer download CSV/PDF para a tabela histórica, o arquivo deve ser capturado integralmente antes do parsing.

## 4. Datas

- 16/09/2026;
- 17/09/2026.

## 5. Instrumentos

- WIN;
- WDO;
- DI1.

## 6. Estado de evidência

Rota BDM oficial: CONFIRMADA.  
Mapeamento oficial da tabela: CONFIRMADO.  
Arquivo trade-by-trade histórico: NÃO CAPTURADO.  
Layout trade-by-trade: NÃO VALIDADO.  
Agressor explícito: NÃO CONFIRMADO.  
Cumulative Delta: NÃO CALCULADO.

## 7. Regra

Não utilizar o fato de existir uma tabela “Negócio a negócio” como prova de que existe um campo de agressor.

O layout efetivamente baixado deverá ser inspecionado e documentado antes da classificação.

## 8. Próxima frente

Localizar os mecanismos de histórico/download do BDM para as duas datas, capturar o arquivo bruto e registrar:

- URL/recurso;
- data de referência;
- formato;
- tamanho;
- SHA-256;
- colunas;
- número de registros;
- intervalo temporal;
- contratos presentes.

Somente depois disso iniciar a reconstrução de agressão e Cumulative Delta.
