# REGRAS PERMANENTES — INGESTÃO HISTÓRICA B3

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-EC55D5AC4D6F |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 7e117e9cd69d41f70dfcaaa1685733577dff0270a088cf169f6a6b43a4c70325 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |

**Arquivo:** REGRAS_PERMANENTES_INGESTAO_HISTORICA_B3_V1.0.md
**Projeto:** B3 - A BOLSA DO BRASIL
**Tema:** Escopo temporal e preservação da série histórica
**Caminho:** docs/ingestao/REGRAS_PERMANENTES_INGESTAO_HISTORICA_B3_V1.0.md
**Data de criação:** 23/09/2026
**Repositório:** carlos-andrade/B3

## Regra 01 — Marco temporal oficial

O marco temporal oficial deste projeto é **1986**.

Toda ingestão histórica de cotações deverá tentar cobrir o intervalo **desde 1986 até o período mais recente oficialmente disponibilizado pela B3**, sem substituir 1986 por 1990.

## Regra 02 — Fonte primária

A fonte primária para cotações históricas é a B3. A página oficial informa que a série histórica de cotações contém o histórico de preços dos títulos negociados na Bolsa desde 1986.

Fonte oficial:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/

## Regra 03 — Preservação RAW

Arquivos oficiais obtidos da B3 devem ser preservados no estado bruto sempre que tecnicamente e juridicamente possível.

Não alterar o arquivo RAW para facilitar análise.

Dados NORMALIZED/Parquet/CSV são derivados e devem permanecer separados do RAW.

## Regra 04 — Integridade

Cada arquivo ingerido deverá registrar, quando disponível:

- nome original;
- período;
- fonte;
- URL de aquisição;
- data/hora de aquisição;
- tamanho;
- SHA-256;
- layout/revisão;
- quantidade de registros;
- primeira e última data efetivamente encontradas;
- erros/rejeições;
- observações sobre mudanças de metodologia ou layout.

## Regra 05 — Não fabricar continuidade

Ausência de dados, sessões sem pregão, mudanças de código, mudanças de instrumento, alterações de moeda/cotação e lacunas históricas não devem ser preenchidas por inferência.

Qualquer reconstrução deverá ser explicitamente marcada como derivada.

## Regra 06 — Moeda e ajustes

A série oficial de cotações deve ser preservada conforme fornecida pela B3. A própria B3 informa que as cotações são apresentadas na moeda e forma de cotação da época, sem ajuste automático por inflação ou proventos.

Séries ajustadas serão tratadas como camadas derivadas.

## Regra 07 — COTAHIST

O layout oficial consultado define o arquivo anual COTAHIST.AAAA.TXT, com registros de 245 bytes e registros 00 (header), 01 (cotações) e 99 (trailer).

O layout oficial também informa que o nome do arquivo identifica o ano, por exemplo COTAHIST.1990.TXT e COTAHIST.1991.TXT.

## Regra 08 — Microestrutura

COTAHIST/EOD não deve ser tratado como fluxo de ordens, agressão ou Cumulative Delta.

Métricas de microestrutura somente serão calculadas quando a fonte permitir classificação defensável dos negócios/ofertas.

## Regra 09 — Auditabilidade

Nenhum período será declarado como "ingerido" sem arquivo, metadado e validação correspondente no repositório.

## Estado

**ATIVA.** Esta regra prevalece sobre qualquer planejamento anterior que tenha adotado 1990 como início.
