# BDI 2026

| Campo | Valor |
|---|---|
| **ID** | B3-DADOS-BDI-2026-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | README_DADOS |
| **Fase** | Ingestão BDI 2026 |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 8138bebe975835ba83a6f6fe567254285d9a99474543170fb010709538301d40 |
| **Commit de referência (versão anterior)** | N/A — primeira normalização do cabeçalho |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação técnica e aprovação humana |
| **Origem** | Organização dos dados BDI de 2026 |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Organização

Os arquivos de cada pregão deverão ser identificados pela data do pregão e pela tabela/capítulo de origem.

Padrão sugerido:

- `YYYY-MM-DD/`
- `raw/` — arquivo original baixado;
- `normalized/` — cópia normalizada sem alterar o conteúdo econômico;
- `manifest.json` — origem, data, hash, tamanho, registros e validações.

## Validações mínimas

1. data do pregão;
2. origem B3;
3. formato;
4. tamanho do arquivo;
5. SHA-256;
6. cabeçalho;
7. delimitador;
8. quantidade de registros;
9. duplicidades;
10. campos obrigatórios ausentes.

Nenhuma transformação deve substituir o arquivo bruto.
