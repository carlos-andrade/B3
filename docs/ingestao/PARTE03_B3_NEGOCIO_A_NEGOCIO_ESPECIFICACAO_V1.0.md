# PARTE03 — B3 NEGÓCIO A NEGÓCIO: ESPECIFICAÇÃO V1.0

**Arquivo:** PARTE03_B3_NEGOCIO_A_NEGOCIO_ESPECIFICACAO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Especificação da camada de negócios para WIN/WDO/DI  
**Caminho:** docs/ingestao/PARTE03_B3_NEGOCIO_A_NEGOCIO_ESPECIFICACAO_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Evidência

A B3 informa que, desde 15/12/2025, os dados anteriormente disponíveis na página de cotações passaram a ser consultados no Boletim Diário do Mercado. Para derivativos, o caminho indicado é:

**Derivativos > Derivativos de bolsa > Negócio a negócio.**

Fonte oficial B3.

## 2. Importância para o projeto

A B3 também identifica explicitamente “Negócio a Negócio – Listados” tanto para renda variável quanto para derivativos no Boletim Diário do Mercado.

Isso confirma a existência da categoria de dados necessária para a camada de microestrutura.

## 3. Separação das fontes

### Camada A — Negócio a negócio

Objetivo:

- reconstrução temporal dos negócios;
- preço;
- quantidade;
- sequência dos negócios;
- cálculo de volume financeiro;
- cálculo de VWAP;
- investigação de agressor;
- Cumulative Delta somente se houver campo ou regra documental que permita classificá-lo.

### Camada B — Negócios consolidados

Objetivo:

- validação EOD;
- conferência de volume;
- conferência de preço mínimo/máximo;
- reconciliação contra totais oficiais.

### Camada C — Cadastro de instrumentos

Objetivo:

- identificar o contrato exato;
- vencimento;
- código;
- instrumento;
- atributos necessários à normalização.

## 4. Regra para agressão

Não assumir:

- comprador = negócio no ask;
- vendedor = negócio no bid;

sem que os campos bid/ask ou uma regra oficial/documentada permitam essa classificação.

Quando o dataset fornecer explicitamente o lado agressor, preservar o campo original.

Quando não fornecer, marcar:

AGGRESSOR_SIDE = UNAVAILABLE

Nesse caso, qualquer delta calculado por heurística deverá ser classificado como PROXY, nunca como Cumulative Delta oficial.

## 5. Regra para Cumulative Delta

### DELTA_REAL

Somente quando existir informação suficiente para classificar cada negócio como agressão compradora ou vendedora.

Delta do negócio:

delta_i = quantity_i × side_i

onde:

side_i = +1 para agressão compradora  
side_i = -1 para agressão vendedora

Cumulative Delta:

CD_t = soma(delta_i), para todos os negócios até t.

### DELTA_PROXY

Permitido apenas em análise exploratória e sempre rotulado como proxy.

Não pode substituir DELTA_REAL nos testes principais.

## 6. Campos normalizados

O schema-alvo deverá suportar:

- trading_date
- timestamp
- timezone
- instrument
- contract
- ticker
- price
- quantity
- financial_volume
- trade_id
- aggressor_side
- bid
- ask
- source
- source_file
- source_hash
- retrieved_at

Campos inexistentes na fonte permanecem nulos.

## 7. Eventos Copom 281

Primeira coleta:

- 16/09/2026 — dia da decisão;
- 17/09/2026 — primeiro pregão seguinte.

Instrumentos:

- WIN;
- WDO;
- DI.

A janela EVENTO não deve receber um horário artificial enquanto o timestamp exato da publicação do comunicado não estiver comprovado.

## 8. Validação cruzada

Para cada contrato:

1. somar quantidade dos negócios;
2. calcular volume financeiro;
3. determinar mínimo/máximo;
4. comparar com o consolidado oficial;
5. verificar número de negócios quando disponível;
6. registrar diferenças;
7. investigar ajustes ou diferenças de escopo antes de aceitar o dataset.

## 9. Estado atual

Fonte Negócio a Negócio: CONFIRMADA  
Localização oficial: Boletim Diário do Mercado  
Dataset binário 16/09/2026: PENDENTE  
Dataset binário 17/09/2026: PENDENTE  
Cadastro de instrumentos: PENDENTE  
Agressor: PENDENTE  
Cumulative Delta real: PENDENTE

## 10. Conclusão operacional

A arquitetura não usará BVBG.187.01 como substituto do negócio a negócio.

O próximo artefato deve ser a captura dos dados efetivamente disponibilizados pelo Boletim Diário do Mercado para 16/09/2026 e 17/09/2026.

Sem o arquivo binário, nenhum número de microestrutura será inventado ou apresentado como observado.
