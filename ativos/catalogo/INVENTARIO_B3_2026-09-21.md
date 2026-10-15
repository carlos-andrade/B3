# Inventário B3 — 2026-09-21

| Campo | Valor |
|---|---|
| **ID** | B3-CAT-INV-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | INVENTARIO_TECNICO |
| **Fase** | GOVERNANCA_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | a38505ced5f3250acef4180b39c0880a7d4fafd284aa4df0a22d3b7682bcc09c |
| **Commit de referência (versão anterior)** | [cdd654d7f7f9c7357a5b9dcb68895d525fd67284](https://github.com/carlos-andrade/B3/commit/cdd654d7f7f9c7357a5b9dcb68895d525fd67284) |
| **Data de criação** | 2026-09-21 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório |
| **Origem** | Evidência e protocolo de captura BVBG.028.02 descritos neste documento; confirmar a captura oficial em execução própria |
| **Autoridade superior** | [Norma de cabeçalho documental da GOVERNANÇA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Evidência da fonte

A página oficial de pesquisa por pregão da B3 registra o **BVBG.028.02 Instruments File — Cadastro de instrumentos** para a data de referência disponível, e a documentação da B3 define o BVBG.028.02 como o arquivo de identificação dos instrumentos.

## Regra de processamento

1. Baixar o arquivo oficial da B3.
2. Preservar o arquivo bruto sem alteração.
3. Validar encoding, delimitador, cabeçalho e quantidade de registros.
4. Normalizar somente em uma cópia derivada.
5. Classificar os instrumentos por categoria.
6. Criar diretório individual apenas para registros efetivamente presentes no cadastro.
7. Registrar contagens e inconsistências.
8. Não preencher campos ausentes por inferência.

## Situação

A fonte oficial está identificada, mas a interface pública consultada é dinâmica. A extração automatizada deve ser executada pelo coletor versionado em `ferramentas/importar_bvbg028.py`, preservando o arquivo original e seu hash.

**Importante:** este arquivo não declara uma quantidade de instrumentos sem que o CSV oficial tenha sido efetivamente capturado e validado.
