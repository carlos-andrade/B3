# PARTE03 — BDM: ROTA HISTÓRICA E TESTE DE ARQUIVO V1.0

**Arquivo:** PARTE03_BDM_NEGOCIO_A_NEGOCIO_ROTA_HISTORICA_2026-09-24.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Investigação do Boletim Diário do Mercado para o Copom 281  
**Caminho:** docs/ingestao/PARTE03_BDM_NEGOCIO_A_NEGOCIO_ROTA_HISTORICA_2026-09-24.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Nova evidência

A pesquisa encontrou o domínio oficial de arquivos do Boletim Diário do Mercado:

https://arquivos.b3.com.br/bdi/download/bdi/

Há PDFs históricos indexados nesse domínio. Exemplos encontrados pelo mecanismo de pesquisa incluem arquivos no padrão:

BDI_03-3_YYYYMMDD.pdf

Portanto, o BDM possui uma infraestrutura histórica de arquivos por data.

## 2. Evidência oficial relacionada

A página oficial de Cotações da B3 informa que, desde 15/12/2025, os dados passaram para o Boletim Diário do Mercado e que derivativos estão no capítulo:

Derivativos > Derivativos de bolsa > Negócio a negócio.

Fonte:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/cotacoes/

## 3. Teste Copom 281

Foram testados como candidatos os recursos:

- 16/09/2026: BDI_03-3_20260916.pdf
- 17/09/2026: BDI_03-3_20260917.pdf

O mecanismo de acesso disponível não conseguiu recuperar esses dois PDFs diretamente. As URLs permanecem CANDIDATAS e não são tratadas como arquivos capturados.

## 4. Consequência

Não foram produzidos:

- SHA-256;
- tamanho confirmado;
- número de páginas;
- conteúdo integral;
- tabela de negócios;
- número de negócios;
- dados de WIN/WDO/DI1.

## 5. Descoberta relevante

Os PDFs BDM são uma fonte de divulgação/consulta e podem servir para validação do mercado, mas não há evidência nesta etapa de que o PDF contenha o nível tick-by-tick necessário para reconstruir Cumulative Delta.

Portanto, mesmo que o PDF seja capturado, ele deverá ser classificado como fonte de consulta/validação até que seu conteúdo efetivo seja inspecionado.

## 6. Próxima ação

A próxima etapa deve usar um ambiente HTTP externo, preferencialmente GitHub Actions, para:

1. baixar os candidatos BDI;
2. validar HTTP;
3. validar PDF;
4. calcular SHA-256;
5. guardar artefato;
6. extrair texto/tabelas;
7. localizar o capítulo Derivativos > Derivativos de bolsa > Negócio a negócio;
8. verificar se existe granularidade de negócio individual.

A aquisição do Negócio a Negócio trade-by-trade continua PENDENTE até essa validação.
