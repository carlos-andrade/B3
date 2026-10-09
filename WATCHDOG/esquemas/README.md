<!--
Projeto: B3 — A BOLSA DO BRASIL
Arquivo: README.md
Caminho: WATCHDOG/esquemas/README.md
Data de criação: 2026-10-09
Versão: 1.0.0
-->

# Esquemas de evidência do Watchdog

A V1 produz dois artefatos por execução:

- `watchdog-report.json`: formato legível por máquina, contendo `schema_version`, `generated_at_utc`, `commit`, `branch`, `status`, `summary` e `checks`.
- `watchdog-report.md`: resumo legível por pessoas com verificações, severidades, caminhos afetados e resultado final.

O JSON usa UTF-8 e timestamps ISO 8601 em UTC. Cada verificação deve incluir identificador estável, estado, severidade, descrição e, quando aplicável, caminho do arquivo. Não incluir segredos nem despejar conteúdo de arquivos inteiros.
