# PARTE 01 — DESCOBERTA DO ENDPOINT OFICIAL COTAHIST V1.0

Arquivo: PARTE01_DESCOBERTA_ENDPOINT_COTAHIST_V1.0.md
Projeto: B3 - A BOLSA DO BRASIL
Tema: Descoberta operacional da interface oficial de aquisição das séries históricas
Caminho: docs/ingestao/PARTE01_DESCOBERTA_ENDPOINT_COTAHIST_V1.0.md
Data de criação: 23/09/2026
Repositório: carlos-andrade/B3

## 1. Objetivo

Registrar a descoberta do mecanismo atualmente exposto pela B3 para acesso às séries históricas de cotações e atualizar a estratégia de aquisição do projeto.

## 2. Evidência oficial

A página oficial Cotações históricas | B3 informa que a série histórica contém o histórico de preços dos títulos negociados na Bolsa desde 1986. A mesma página informa que os arquivos são disponibilizados em ZIP e que, após a descompactação, os dados são interpretados em TXT mediante o layout oficial.

Fonte oficial:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/

A página oficial também apresenta a ação “Acesse agora a série histórica de cotações”, que atualmente direciona para a interface hospedada em:

https://bvmf.bmfbovespa.com.br/en-us/historical-quotes/FormSeriesHistoricasArqI.asp

## 3. Interface descoberta

A interface oficial atualmente acessível pelo portal B3 apresenta:

- Séries anuais — todos os dias de negociação;
- Série mensal — últimos 12 meses;
- Série diária — ano corrente;
- aviso de que o arquivo do ano corrente contém dados até o último dia de negociação;
- seleção de período para aquisição.

Isso confirma que o projeto deve tratar a interface atual como fonte operacional de descoberta, em vez de depender exclusivamente da URL histórica fixa utilizada por scripts legados.

## 4. URL histórica legada

O pipeline existente utiliza a convenção:

https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A{AAAA}.ZIP

Essa convenção permanece registrada como endpoint legado/conhecido, mas a aquisição física ainda precisa ser validada no ambiente de execução.

## 5. Estado da aquisição em 23/09/2026

**NÃO INGESTADO.**

A infraestrutura de execução não conseguiu resolver o DNS de bvmf.bmfbovespa.com.br. Portanto:

- nenhum ZIP foi considerado baixado;
- nenhum SHA-256 foi fabricado;
- nenhum ano foi marcado como validado;
- 1986 continua sendo o marco temporal oficial do projeto;
- a ausência dos arquivos no repositório não deve ser confundida com ausência de disponibilidade na B3.

## 6. Próxima etapa técnica

1. Obter o arquivo anual de 1986 por meio da interface oficial ou mecanismo de download por ela acionado.
2. Preservar o ZIP original em dados/cotahist/raw/anual/.
3. Descompactar somente para validação/processamento.
4. Validar:
   - ZIP íntegro;
   - exatamente um TXT;
   - registro inicial 00;
   - registros 01;
   - registro final 99;
   - 245 bytes por registro;
   - contagem total de registros;
   - SHA-256 do ZIP.
5. Registrar metadados e manifesto.
6. Repetir para 1987, 1988, ... até o ano corrente.
7. Só depois iniciar a normalização anual.

## 7. Regra de integridade

Este documento não autoriza o uso de datasets de terceiros como substitutos silenciosos da fonte primária B3. Dados secundários podem ser usados para auditoria ou comparação, mas devem ser identificados como secundários.

## 8. Referência de layout

O layout oficial B3 define o arquivo COTAHIST.AAAA.TXT com registros 00 (header), 01 (cotações) e 99 (trailer), com 245 bytes por registro.
