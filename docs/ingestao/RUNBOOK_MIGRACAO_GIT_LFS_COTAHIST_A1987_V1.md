# Runbook — migração controlada Git LFS COTAHIST A1987

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-B0CB4E5740AD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 5fbce1f89236b72d2c1510d826fc89dc58701fb0f0953f0e26cf3af946d07ec8 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |

**Data de preparação:** 2026-10-14  
**Repositório:** https://github.com/carlos-andrade/B3  
**Estado:** workflow integrado em `main` por commit direto; migração ainda não executada.

## Objetivo

Corrigir exclusivamente a representação Git do ficheiro NORMALIZED A1987 para Git LFS, sem modificar o conteúdo, sem reescrever histórico e sem alterar RAW, manifestos ou sidecars.

## Pré-condições imutáveis

O conteúdo antes da migração tem de corresponder exatamente a:

- Caminho: `dados/cotahist/normalized/anual/COTAHIST_A1987.csv`
- SHA-256: `5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`
- Tamanho: 15.518.211 bytes
- Linhas de dados: 130.665
- Campos: 25
- Primeira data: 1987-01-02
- Última data: 1987-12-30

Qualquer divergência interrompe o workflow antes de criar um commit.

## Execução controlada

Workflow: [cotahist-lfs-migracao-controlada-a1987-v1.yml](../../.github/workflows/cotahist-lfs-migracao-controlada-a1987-v1.yml)

1. Fazer merge da proposta após revisão.
2. Abrir **Actions → COTAHIST - migração controlada Git LFS A1987 → Run workflow**.
3. Executar primeiro com `mode=preflight`. Este modo valida o conteúdo e o ponteiro LFS preparado no índice, mas não cria commit nem faz push.
4. Só depois de rever o log de preflight e confirmar todos os valores esperados, executar manualmente com `mode=migrate`.
5. O modo `migrate` cria um commit normal de avanço, faz push sem reescrever histórico, realiza checkout novo do branch `main`, materializa o objeto LFS e verifica novamente SHA-256, tamanho, linhas, campos e intervalo de datas.
6. O workflow volta a executar a auditoria física global 1986–2026 e o gerador do Dataset Oficial V2. Ambos devem terminar sem divergências; as evidências resultantes são persistidas.
7. Confirmar que o aviso `should have been a pointer, but wasn't` desapareceu num checkout limpo e que a auditoria global continua `APROVADO`, 41/41 anos.

## Segurança e prevenção de loops

- O workflow só tem `workflow_dispatch`; não tem `schedule` nem gatilho `push`.
- Não executa migração automaticamente quando o ficheiro do workflow é integrado.
- O modo padrão é `preflight`; migração exige escolha manual explícita de `migrate`.
- As tentativas de push são limitadas a três; não há loop de polling.
- Só o CSV NORMALIZED A1987 é regravado como ponteiro LFS; os bytes do conteúdo devem permanecer idênticos.
- Não usar `git lfs migrate import` nem reescrever commits antigos.
- Se o push, a materialização LFS, a auditoria física ou o dataset falharem, não declarar a incidência resolvida. Registar a falha e interromper qualquer nova tentativa até análise.

## Estado de conclusão

**Ainda pendente.** O workflow e este runbook são uma preparação, não prova de migração. Fechar a incidência apenas após execução `migrate` bem-sucedida, checkout limpo, SHA-256 idêntico e auditorias pós-migração aprovadas.
