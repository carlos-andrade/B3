# Recuperação offline controlada — COTAHIST 2006

| Campo | Valor |
|---|---|
| **ID** | B3-COTAHIST-2006-OFFLINE-RECOVERY |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | PLANO_TECNICO_RECUPERACAO_OFFLINE |
| **Fase** | RECONCILIACAO_PR14 |
| **Estado** | EM_REVISAO; MERGE_BLOQUEADO_POR_VALIDACAO |
| **Versão** | 1.0.1 |
| **Data de atualização** | 2026-10-20 |
| **Autoridade superior** | [Carta Magna B3](../CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre Canónico B3](../governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../governanca/decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |

## 1. Objetivo e limites

Registar como recuperar e validar o normalizado COTAHIST de 2006 sem descarregar nova cópia externa, sem substituir o RAW, sem alterar manifesto/checksum para satisfazer um teste e sem certificar dados com base apenas na existência de ficheiros.

Este plano não é evidência de validação e não autoriza publicação/redistribuição adicional.

## 2. Estado do repositório na verificação

- O PR #14, `feat/cotahist-2006-offline-recovery → main`, foi consultado em 2026-10-20.
- A branch do PR tinha 51 commits exclusivos e estava 2.329 commits atrás de `main` no snapshot consultado; GitHub reportou `mergeable=false` / `mergeable_state=dirty`.
- Os 13 workflows FASE01–FASE11/Gate 06–08 existem já em `main`; não devem ser adicionados outra vez como ficheiros paralelos.
- A versão da branch do PR difere materialmente da versão atual em múltiplos workflows. As diferenças incluem triggers de branch e destino de persistência. A versão atual de `main` usa triggers em `main` e persistência em `main`; não se pode reintroduzir automaticamente a versão da feature branch.
- O RAW, o manifesto de origem e os sidecars/checksums relevantes comparados têm os mesmos objetos Git nos dois snapshots consultados.
- O CSV canónico de 2006 está presente em `main` como objeto Git LFS. Um ponteiro LFS, o hash declarado no manifesto ou a presença do ficheiro não substituem uma verificação física do conteúdo materializado.
- A evidência FASE01 foi encontrada tanto em `main` como na branch do PR, mas com timestamp diferente. A diferença não prova, por si, regressão de dados; é evidência que precisa de reconciliação documental quando aplicável.

## 3. Diagnóstico do conflito

Não é seguro resolver o conflito por escolha global de `ours`/ `theirs`, reset de branch ou merge apressado. A branch está muito atrás de `main`; o conflito reflete divergência temporal e alterações posteriores nos mesmos workflows, não apenas algumas linhas sobrepostas.

### Classes de divergência

1. **Workflows já existentes em main:** harmonização individual, sem duplicação de ficheiros.
2. **Triggers e persistência:** manter o contrato operacional da versão atual de `main`, exceto se houver decisão normativa aprovada que justifique alteração.
3. **Evidências FASE01/FASE00:** preservar evidências atuais e históricas, sem substituir timestamp ou estado para parecer mais recente/aprovado.
4. **CSV normalizado/LFS:** preservar o objeto físico existente em `main`; validar hash/contagem/campos/datas independentemente antes de qualquer substituição.
5. **Fases posteriores:** resultado de uma fase não certifica a seguinte; cada gate deve ter a sua evidência independente.

## 4. Plano de resolução controlada

1. **Base:** a branch de revisão nasce do HEAD atual de `main`.
2. **Inventário:** comparar individualmente os 13 workflows de 2006/Gate 06–08, mais FASE00 quando relevante, entre a branch original e `main`.
3. **Sem duplicação:** manter como fonte canónica os workflows já presentes em `main`. Incorporar apenas alterações de lógica que sejam demonstradas como necessárias, compatíveis com a governança e testáveis.
4. **Validação estática:** verificar sintaxe YAML, referências de ficheiros, triggers, escopos sparse-checkout, permissões mínimas, isolamento direcional das fases, idempotência e destino de persistência.
5. **Validação de dados:** materializar o objeto Git LFS em ambiente de CI, calcular SHA-256 físico, conferir contagem esperada, os 25 campos, datas, tipos de registo e reconciliação integral RAW × NORMALIZED.
6. **Execução por fases:** executar em ordem FASE00 → FASE01 → FASE02 → FASE03 → FASE04A/04B → FASE05 → FASE06 → FASE07 → FASE08 → Gate 06–08 → FASE09 → FASE10 → Gate → FASE11. Inspecionar logs e artefactos reais.
7. **Promoção:** não fazer merge até todos os critérios obrigatórios estarem satisfeitos e a validação do PR ter sido atualizada.

## 5. Critérios de aceitação

- [ ] Nenhuma regressão em relação ao conteúdo atual de `main`.
- [ ] Nenhum workflow duplicado com a mesma responsabilidade e nome.
- [ ] Triggers e destinos de persistência coerentes com governança e documentados.
- [ ] O RAW continua imutável e com hash conferido.
- [ ] O objeto LFS físico é validado; não apenas o pointer.
- [ ] O normalizado corresponde ao RAW nos 25 campos, contagem e datas.
- [ ] Cada fase e gate tem evidência da execução real.
- [ ] Os manifestos e sidecars não são reescritos para ocultar divergências.
- [ ] O PR continua sem merge enquanto existir qualquer critério bloqueante pendente.

## 6. Histórico da resolução

- 2026-10-20: detetada divergência substancial da branch do PR face a `main`; criação de branch de revisão baseada no HEAD atual de `main`.
- 2026-10-20: criado este plano para registar as diferenças e os critérios de aceitação. A existência do plano não significa que a resolução funcional ou os testes estejam concluídos.

## 7. Decisão

**PR #14 permanece bloqueado para merge até a reconciliação individual dos workflows e a validação operacional completa.** A branch de revisão é um registo de trabalho separado; não altera `main` nem declara o dataset certificado.
