# PARTE03 — NEGÓCIO A NEGÓCIO: FONTE OFICIAL E ROTA DE AQUISIÇÃO V1.0

**Arquivo:** PARTE03_NEGOCIO_A_NEGOCIO_FONTE_OFICIAL_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Fonte oficial para dados trade-by-trade de derivativos listados  
**Caminho:** docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_FONTE_OFICIAL_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Evidência oficial

A B3 informa que, desde 15/12/2025, as informações anteriormente disponíveis na página de Cotações passaram a ser consultadas no Boletim Diário do Mercado.

Para derivativos, a rota indicada é:

**Derivativos > Derivativos de bolsa > Negócio a negócio.**

Fonte oficial:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/cotacoes/

## 2. Confirmação da tabela

O Glossário de Dados Públicos da B3 lista explicitamente:

**Negócio a negócio - Listados (.PDF)**

e associa a informação de derivativos ao capítulo:

**Derivativos de bolsa > Negócio a negócio.**

Fonte:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/boletim-diario/dados-publicos-de-produtos-listados-e-de-balcao/

## 3. Implicação para o projeto

A fonte correta para a reconstrução de microestrutura não deve ser confundida com:

- SPRD/EOD;
- PriceReport consolidado;
- OHLCV;
- indicadores derivados.

A camada de Negócio a Negócio é a candidata primária para reconstruir trades individuais.

## 4. Escopo

Datas:

- 16/09/2026;
- 17/09/2026.

Instrumentos:

- WIN;
- WDO;
- DI1.

## 5. Aquisição

O próximo passo operacional é localizar, na infraestrutura atual do Boletim Diário do Mercado, o recurso correspondente à tabela **Negócio a negócio - Listados** para cada pregão.

A URL final do arquivo não será inventada. O identificador, extensão, tamanho e hash só serão registrados após captura efetiva.

## 6. Dados esperados

Após captura e inspeção do layout, deverão ser mapeados:

- data;
- horário;
- instrumento;
- contrato;
- preço;
- quantidade;
- identificador do negócio, se disponível;
- campos de compra/venda/agressor, se disponíveis;
- demais campos originais.

## 7. Agressão

A existência da tabela Negócio a Negócio não implica, por si só, que todo campo necessário à classificação de agressor esteja presente.

Agressor somente será considerado REAL após validação do layout e da semântica do campo.

## 8. Estado

Fonte oficial identificada: SIM.  
Tabela oficial identificada: SIM.  
Rota de derivativos identificada: SIM.  
Arquivo histórico 16/09/2026 capturado: PENDENTE.  
Arquivo histórico 17/09/2026 capturado: PENDENTE.  
Layout validado: PENDENTE.  
Agressor-side real: PENDENTE.

## 9. Conclusão

A arquitetura de ingestão deve migrar da investigação genérica de endpoints para a camada oficial **Boletim Diário do Mercado > Derivativos de bolsa > Negócio a negócio**.

Nenhum dado numérico de microestrutura será produzido antes da captura e validação do arquivo.
