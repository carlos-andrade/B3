# Diagnóstico — falhas do workflow COTAHIST Normalização V4

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-CE34C5A92EAC |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 7ebe6b6b657654855902489843d585e875ff60a3b80fcdfabcd235cab93c47a4 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** DIAGNOSTICO_COTAHIST_NORMALIZACAO_V4_2026-09-24.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Falhas recorrentes do GitHub Actions na normalização COTAHIST 2011-2026  
**Caminho:** docs/ingestao/DIAGNOSTICO_COTAHIST_NORMALIZACAO_V4_2026-09-24.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Evidência observada

O workflow `.github/workflows/cotahist-normalizacao-2011-2026-v4.yml` processa 16 arquivos anuais, de 2011 a 2026.

Os manifests existentes demonstram que a normalização de 2026 já foi concluída com sucesso anteriormente, incluindo 2.904.013 registros e período de 2026-01-02 a 2026-09-22.

## 2. Causa operacional identificada

O workflow tentava publicar como um único artefato todos os CSVs normalizados de 2011-2026:

- `/tmp/normalized/*.csv`
- `/tmp/quality/*.json`
- `/tmp/quality/*.sha256`

Isso pode produzir um artefato de centenas de MB ou mais. O limite de armazenamento de artefatos do GitHub Actions é baixo nos planos Free/Pro, tornando essa estratégia inadequada para CSVs históricos grandes.

Além disso, a etapa de persistência fazia `git commit`, depois `git pull --rebase` e somente então `git push`. Isso aumenta a janela para conflitos quando outros workflows atualizam `main`.

## 3. Correção aplicada

Commit: `db025c2a58253879b21379b5bdcc00ccc23a39d2`

Alterações:

1. CSVs normalizados deixaram de ser enviados como artefato.
2. Somente relatórios JSON e hashes SHA-256 são publicados como artefato.
3. Retenção do artefato leve reduzida para 7 dias.
4. `git pull --rebase` passou para antes do commit.
5. Push passou a ter até 3 tentativas com nova sincronização.
6. A etapa de persistência agora encerra normalmente quando não há alterações.

## 4. Integridade dos dados

Os CSVs continuam sendo gerados e validados no runner. O que mudou é apenas a política de armazenamento temporário dos CSVs como artefato do Actions.

Os manifests e SHA-256 continuam sendo persistidos no repositório para auditoria.

## 5. Estado

Correção publicada em `main`. O novo commit altera o próprio workflow e dispara uma nova execução para validação.

## 6. Regra operacional

Não usar artefatos do GitHub Actions como armazenamento permanente de grandes séries históricas COTAHIST. Para dados históricos grandes, manter o bruto/normalizado em armazenamento apropriado e usar no Actions apenas artefatos leves de qualidade, metadados e hashes.
