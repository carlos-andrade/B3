# PARTE03 — NEGÓCIO A NEGÓCIO: RECONCILIAÇÃO DA FONTE V1.0

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
