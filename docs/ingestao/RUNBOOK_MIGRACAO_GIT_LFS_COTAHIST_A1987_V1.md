# Runbook — migração controlada Git LFS COTAHIST A1987

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-B0CB4E5740AD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | CONCLUIDO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | b3839c1e1debde12b7573a7573e8fe33ae68eaaa86d937c5071694e196a4d7a1 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Proprietário do repositório — autorização de execução confirmada em 2026-10-16 |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |

**Data de preparação:** 2026-10-14  
**Repositório:** https://github.com/carlos-andrade/B3  
**Estado histórico da preparação:** workflow integrado em `main` por commit direto. A migração foi executada posteriormente com preflight aprovado; ver a secção de fecho abaixo.

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

**Estado histórico substituído pelo fecho de 2026-10-16:** a migração foi concluída e validada. A prova está documentada abaixo; este texto de estado inicial é preservado apenas como contexto histórico.


## Fecho operacional e reconciliação — 2026-10-16

### Preflight obrigatório — aprovado
- Run de preflight: [38590349969](https://github.com/carlos-andrade/B3/actions/runs/38590349969) — `success`, modo `preflight`; sem commit e sem push.
- Conteúdo original: SHA-256 `5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`; 15.518.211 bytes; 130.665 registos; 25 campos; datas observadas 1987-01-02–1987-12-30.
- Ponteiro staged validado: OID SHA-256 igual ao hash do conteúdo e tamanho `15518211`.

### Migração controlada — concluída
- Run de migração: [38591026646](https://github.com/carlos-andrade/B3/actions/runs/38591026646) — `success`, modo `migrate`.
- Commit de migração: [e8c6bf21eeba789b763a9c88d6433dabe8b31b9a](https://github.com/carlos-andrade/B3/commit/e8c6bf21eeba789b763a9c88d6433dabe8b31b9a).
- Caminho: `dados/cotahist/normalized/anual/COTAHIST_A1987.csv`.
- Representação no Git atual: ponteiro Git LFS de 133 bytes; OID `5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`; tamanho do objeto `15518211` bytes.
- Checkout limpo e materialização do objeto LFS: aprovados. Hash, tamanho, 130.665 registos, 25 campos e intervalo de datas preservados.
- Auditoria física global: `APROVADO`, 41/41 anos validados, zero falhas.
- Dataset Oficial V2 regenerado e persistido com sucesso.

### Verificação independente do estado atual do repositório
Na árvore `main` verificada em 2026-10-16, o blob do CSV A1987 tem 133 bytes e contém um ponteiro LFS válido para o objeto de 15.518.211 bytes. O sidecar, o manifesto de qualidade e a certificação física mantêm o SHA-256 `5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`.

**Decisão final:** migração A1987 para Git LFS concluída. Não executar nova migração. Não reescrever histórico, não alterar bytes RAW/NORMALIZED e não regenerar manifestos fora dos workflows controlados.