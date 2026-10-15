# COTAHIST 1986-2026 — Validação de Continuidade por Calendário

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-474C0C806C00 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 348c2d551de173d78cb77eb525c90ff16eb017c4ca748ced7bbfafa76f91e04b |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo
Separar intervalos naturais do calendário de candidatos a pregões ausentes na série COTAHIST.

## Evidência B3
A B3 informa que a série histórica de cotações cobre o histórico desde 1986 e que os dados são fornecidos na moeda e forma de cotação da época, sem ajustes por inflação ou proventos.
Fonte: https://www.b3.com.br/main.jsp?lumA=1&lumII=2C9E0371634B781701634B7C27111B5F&lumPageId=8A6A8C244DE7C289014DE80C873C130E

O layout oficial define três tipos de registro: 00 Header, 01 cotações diárias e 99 Trailer, todos em registros de 245 bytes.
Fonte: https://www.b3.com.br/data/files/C8/F3/08/B4/297BE410F816C9E492D828A8/SeriesHistoricas_Layout.pdf

A B3 mantém calendário de negociação por ano, com distinção entre segmentos e tipos de atividade. Portanto, uma diferença entre datas no COTAHIST não deve ser convertida diretamente em pregão ausente.
Fonte: https://www.b3.com.br/main.jsp?lumA=1&lumII=8A80CB81633FBF0B0163402956733E3A&lumPageId=8A6882694E91F2D4014E9248DBB001C9

## Regra de classificação
Para cada intervalo entre duas datas presentes no COTAHIST:

1. delta <= 4 dias corridos: sem alerta de intervalo longo.
2. delta > 4: registrar como candidato.
3. Consultar calendário oficial do respectivo ano.
4. Se todas as datas intermediárias forem dias sem negociação aplicável ao universo analisado: classificar como intervalo esperado.
5. Se existir sessão oficial aplicável sem registros correspondentes: classificar como candidato a ausência de dados.
6. Só classificar como falha de ingestão depois de excluir suspensão excepcional, mudança de segmento, cobertura específica do arquivo e particularidades históricas.

## Escopo histórico
A validação deverá ser executada por ano de 1986 a 2026. Para anos antigos em que o calendário eletrônico atual não seja suficiente, a fonte oficial histórica ou documento institucional equivalente deverá ser incorporado ao repositório antes da classificação definitiva.

## Regra de evidência
Nenhum gap será declarado pregão ausente somente pela diferença entre duas datas COTAHIST.

## Próxima saída esperada
Gerar:
- calendário canônico por ano;
- tabela data -> houve_negociacao;
- tabela de gaps classificados;
- contagem de sessões esperadas versus sessões observadas;
- lista de candidatos a ausência;
- trilha de fonte e SHA dos arquivos de calendário usados.
