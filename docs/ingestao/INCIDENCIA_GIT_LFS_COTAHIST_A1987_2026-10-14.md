# Incidência — armazenamento Git LFS do COTAHIST A1987

| Campo | Valor |
|---|---|
| **ID** | B3-INC-LFS-1987-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | INCIDENTE |
| **Fase** | Resolução e auditoria pós-migração |
| **Estado** | CONCLUIDO |
| **Versão** | 1.2.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — calcular segundo norma GOVERNANCA v1.0.3 |
| **Commit de referência (versão anterior)** | [547085a823c33701163cce3519c0fde88429b176](https://github.com/carlos-andrade/B3/commit/547085a823c33701163cce3519c0fde88429b176) |
| **Data de criação** | 2026-10-14 |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Responsável técnico B3 |
| **Aprovador** | Pendente de aprovação formal; conclusão técnica apoiada em evidência |
| **Origem** | Aviso de checkout Git LFS e validação posterior |
| **Autoridade superior** | [Layout Mestre B3](https://github.com/carlos-andrade/B3/blob/main/docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Norma GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | [Workflow 38591026646](https://github.com/carlos-andrade/B3/actions/runs/38591026646); [commit e8c6bf21](https://github.com/carlos-andrade/B3/commit/e8c6bf21eeba789b763a9c88d6433dabe8b31b9a); auditoria física e Dataset Oficial V2 |
| **Escopo** | Correção da representação do CSV NORMALIZED A1987 no Git LFS; não altera o conteúdo RAW/NORMALIZED |
| **Objetivo** | Registar a discrepância inicial, a migração controlada e a verificação de integridade |
| **Dependências** | Workflow de migração, runbook, auditoria física global, manifestos e Dataset Oficial V2 |

## Resumo

A execução do workflow [COTAHIST — Dataset Oficial V2, run 38577163285](https://github.com/carlos-andrade/B3/actions/runs/38577163285) terminou com sucesso. O workflow materializou seletivamente os CSV anuais, validou 41 anos contra a auditoria física global e publicou o dataset V2. Durante o checkout Git LFS foi emitido o aviso:

`Encountered 1 file that should have been a pointer, but wasn't: dados/cotahist/normalized/anual/COTAHIST_A1987.csv`

## Evidência verificável

A regra em `.gitattributes` é:

```gitattributes
dados/cotahist/normalized/anual/*.csv filter=lfs diff=lfs merge=lfs -text
```

A árvore Git de `main` mostrou:

| Ficheiro | Tamanho do blob Git | Observação |
|---|---:|---|
| `COTAHIST_A1986.csv` | 133 bytes | ponteiro LFS |
| `COTAHIST_A1987.csv` | 15.518.211 bytes | conteúdo CSV guardado diretamente como blob Git |
| `COTAHIST_A2026.csv` | 134 bytes | ponteiro LFS |

O conteúdo do CSV A1987 está acessível no repositório; a inconsistência é entre a regra declarada e a forma de armazenamento do blob. Não há evidência nesta incidência de divergência do SHA-256 de conteúdo: a auditoria física global está aprovada para 41/41 anos e o Dataset Oficial V2 contém A1987 como `VALIDADO`.

## Impacto

- **Dados:** nenhuma alteração feita nesta investigação.
- **Integridade:** sem bloqueio observado; a auditoria física e o gerador V2 passaram.
- **Armazenamento:** exceção ao padrão Git LFS para CSV anuais.
- **Operação:** aviso não bloqueante no checkout, deve ser eliminado por uma correção controlada.

## Plano de resolução histórico — concluído

Os passos abaixo registam o plano original; a execução e o encerramento constam da secção final deste documento.

1. Não reescrever nem deduplicar o CSV.
2. Antes de qualquer migração, registar o SHA-256 atual do conteúdo, tamanho, contagem de linhas, 25 campos e intervalo de datas.
3. Converter apenas a representação de armazenamento do A1987 para LFS numa alteração isolada, sem alterar os bytes do conteúdo.
4. Confirmar que o ponteiro LFS foi criado e que o objeto LFS está disponível após push e novo checkout.
5. Recalcular o SHA-256 do conteúdo materializado e comparar com a auditoria física e manifesto; validar contagem, campos e datas.
6. Executar novamente a auditoria física global e o Dataset Oficial V2.
7. Fechar a incidência apenas quando o aviso desaparecer e todos os hashes/contagens continuarem coerentes.

## Restrições

- Não alterar RAW nem conteúdo NORMALIZED.
- Não regenerar manifestos para fazer coincidir hashes incorretos.
- Não marcar como corrigido apenas porque o workflow passa.
- Manter a geração fail-closed e preservar a evidência histórica.


## Adenda — workflow de migração controlada preparado (2026-10-14)

Foi preparado e publicado diretamente em `main` (o repositório está configurado para não aceitar Pull Requests) o workflow manual [cotahist-lfs-migracao-controlada-a1987-v1.yml](https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-lfs-migracao-controlada-a1987-v1.yml) e o respetivo [runbook](https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/RUNBOOK_MIGRACAO_GIT_LFS_COTAHIST_A1987_V1.md).

O workflow tem apenas `workflow_dispatch`, sem cron nem gatilho push. O modo padrão é `preflight`; a opção `migrate` exige seleção manual. Antes de converter, verifica SHA-256 `5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`, 15.518.211 bytes, 130.665 linhas, 25 campos e datas 1987-01-02–1987-12-30. Depois do push, exige checkout limpo, materialização LFS, igualdade do hash/estrutura, auditoria física global e regeneração do Dataset Oficial V2.

**Estado atualizado (2026-10-14):** workflow e runbook publicados diretamente em `main`, sem reescrever histórico, porque Pull Requests estão desativadas no repositório. O estado posterior e autoritativo está documentado na secção Fecho pós-migração controlada, abaixo.


## Fecho pós-migração controlada — 2026-10-14

| Campo | Valor |
|---|---|
| **ID** | B3-INC-LFS-1987-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | INCIDENTE |
| **Fase** | Resolução e validação pós-migração |
| **Estado** | CONCLUIDO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — recalcular após normalização documental |
| **Commit de referência (versão anterior)** | [e8c6bf21eeba789b763a9c88d6433dabe8b31b9a](https://github.com/carlos-andrade/B3/commit/e8c6bf21eeba789b763a9c88d6433dabe8b31b9a) |
| **Data de criação** | 2026-10-14 |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Responsável técnico B3 |
| **Aprovador** | Pendente — encerramento técnico baseado na evidência do workflow, sem alegar aprovação separada |
| **Origem** | Aviso de checkout Git LFS e auditorias pós-migração |
| **Autoridade superior** | [Layout Mestre B3](https://github.com/carlos-andrade/B3/blob/main/docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Norma GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Workflow [38591026646](https://github.com/carlos-andrade/B3/actions/runs/38591026646); commit [e8c6bf21](https://github.com/carlos-andrade/B3/commit/e8c6bf21eeba789b763a9c88d6433dabe8b31b9a); auditoria física global e Dataset Oficial V2 |



**Estado: RESOLVIDO COM EVIDÊNCIA.** A execução [38591026646](https://github.com/carlos-andrade/B3/actions/runs/38591026646) concluiu com sucesso em modo `migrate`. Commit de migração: [e8c6bf21eeba789b763a9c88d6433dabe8b31b9a](https://github.com/carlos-andrade/B3/commit/e8c6bf21eeba789b763a9c88d6433dabe8b31b9a).

Gates pós-migração aprovados:
- O ficheiro `dados/cotahist/normalized/anual/COTAHIST_A1987.csv` está agora representado no Git por ponteiro LFS (133 bytes), com OID SHA-256 `5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc` e tamanho declarado de 15.518.211 bytes.
- Checkout limpo materializou o objeto LFS e confirmou o conteúdo: SHA-256 `5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`, 15.518.211 bytes, 130.665 linhas de dados, 25 campos, intervalo 1987-01-02–1987-12-30.
- Auditoria física global executada após a migração: `APROVADO`, 41/41 anos validados, zero falhas. Evidência: [AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json).
- Dataset Oficial V2 foi regenerado no checkout pós-migração, com 41 anos incluídos. [Dataset Oficial V2](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json).
- O workflow concluiu todas as etapas pós-migração; nenhuma etapa de validação pós-migração foi ignorada. A persistência não precisou de novo commit porque as evidências geradas já coincidiam com as evidências canónicas existentes.

**Decisão:** fechar a incidência de representação Git LFS A1987. A migração alterou apenas a representação de armazenamento Git/LFS; o conteúdo NORMALIZED, o RAW e os manifestos foram preservados. Não houve reescrita de histórico. A atualização diária de 2026 continua independente deste incidente.
