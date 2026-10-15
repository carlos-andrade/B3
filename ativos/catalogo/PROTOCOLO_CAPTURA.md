# Protocolo de captura do Cadastro de Instrumentos B3

| Campo | Valor |
|---|---|
| **ID** | B3-ATIVOS-CATALOGO-PROTOCOLO-CAPTURA-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | PROTOCOLO_INGESTAO |
| **Fase** | Catálogo B3 — captura de instrumentos |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 0e9fa5bc9e71121b2665bcc7a36cb3625dd514039517b78e49102d9527cc15b9 |
| **Commit de referência (versão anterior)** | N/A — normalização inicial do cabeçalho |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação técnica e aprovação humana |
| **Origem** | B3 — Cadastro de Instrumentos (Listado), BVBG.028.02 |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Transformar o cadastro oficial diário em uma base versionada e auditável.

## Ordem obrigatória

1. Capturar o arquivo oficial.
2. Preservar o bruto.
3. Registrar SHA-256.
4. Validar cabeçalho e delimitador.
5. Contar registros.
6. Detectar códigos duplicados.
7. Detectar registros sem ticker/código.
8. Classificar por instrumento/mercado.
9. Gerar inventário derivado.
10. Registrar manifesto e log.
11. Publicar no GitHub.

## Regra de evidência

Nenhuma quantidade de ativos será apresentada como fato antes da captura e validação do arquivo correspondente à data. Estruturas de pastas criadas previamente são taxonomia do projeto, não inventário de mercado.

## Saída mínima

- CSV bruto
- CSV normalizado
- manifesto JSON
- log de validação
- SHA-256
- data de referência
- commit Git

## Próxima execução

Executar:

`python ferramentas/importar_bvbg028.py --date YYYY-MM-DD`

Depois validar os resultados antes de gerar estudos de mercado.
