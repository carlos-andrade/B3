# Protocolo de captura do Boletim Diário do Mercado (BDI)

| Campo | Valor |
|---|---|
| **ID** | B3-DADOS-BDI-PROTOCOLO-CAPTURA-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | PROTOCOLO_INGESTAO |
| **Fase** | Ingestão BDI |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 160dec829d2ca2a80a6fd37b5127b26ed391a8d540c970e8d9121a804b6fe35a |
| **Commit de referência (versão anterior)** | N/A — normalização inicial do cabeçalho |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação técnica e aprovação humana |
| **Origem** | B3 — Boletim Diário do Mercado (BDI) |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Captura

Para cada pregão, registrar a data e o capítulo/tabela selecionado na fonte oficial B3.

## 2. Preservação

Quando houver download:

- salvar o arquivo original em `raw/`;
- não editar o original;
- calcular SHA-256;
- registrar tamanho em bytes.

## 3. Estrutura

Registrar:

- formato;
- nome do arquivo;
- cabeçalho;
- delimitador, quando CSV;
- número de linhas/registros;
- campos encontrados.

## 4. Integridade

Verificar:

- duplicidade de chave;
- registros sem identificador;
- valores nulos em campos obrigatórios;
- inconsistência de data;
- alterações inesperadas de layout.

## 5. Normalização

A versão normalizada deve ser derivada do bruto. Nunca sobrescrever a fonte original.

## 6. Manifesto

Cada captura deve possuir manifesto contendo:

- data do pregão;
- fonte;
- capítulo;
- tabela;
- arquivo;
- SHA-256;
- quantidade de registros;
- validações executadas;
- observações.

## 7. Regra de evidência

Se o arquivo não foi efetivamente capturado, o projeto deve registrar somente a existência/documentação da fonte. Não estimar quantidade de registros nem inventar campos.

## Gate de acesso e termos

Antes de ativar captura automatizada, confirmar e registar os termos aplicáveis ao endpoint específico, autorização de acesso, limites de uso e permissões de armazenamento/reutilização. A página Pesquisa por Pregão da B3 veda coleta automatizada a partir da própria página, inclusive por ferramentas de IA; não implementar scraping dessa página. Uma API ou endpoint alternativo exige revisão de termos independente.

## 8. Microestrutura

BDI consolidado não deve ser confundido com dados intradiários. Estudos de agressão, Cumulative Delta, VWAP, TWAP e fluxo exigem dados com granularidade compatível.
