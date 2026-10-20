# Recuperação offline controlada — COTAHIST 2006

**Estado:** proposta de recuperação; não constitui certificação nem autorização para publicar dados adicionais.  
**Branch de trabalho:** `fix/pr14-conflicts-main-sync`  
**Fonte de dados:** RAW ZIP de 2006 já existente no repositório.  
**Proibido:** nova captura externa nesta cadeia, substituir RAW, alterar manifesto/checksum sem evidência ou promover o CSV sem validação física e semântica.

## Contexto

O repositório contém o RAW anual de 2006, manifesto e checksums, e o CSV normalizado está versionado via Git LFS. A recuperação proposta tem de validar o objeto físico de LFS e comparar o CSV com o RAW; um ponteiro LFS ou manifesto, isoladamente, não prova o conteúdo materializado.

## Divergência identificada no PR #14

A branch original foi criada antes de mudanças substanciais em `main`. A integração direta foi marcada como conflitante pelo GitHub. Os workflows de recuperação já existem em `main`; vários conteúdos divergem entre as branches e as persistências nas duas versões têm alvos incompatíveis (`main` versus branch de feature). Não deve ser feito um merge automático que escolha um lado globalmente.

## Resolução segura

1. Manter `main` como base atualizada.
2. Preservar os ficheiros e dados atuais de `main`, incluindo CSV LFS e evidências mais recentes.
3. Tratar a branch do PR como fonte para revisão, não como autoridade para retroceder workflows ou evidências da `main`.
4. Inspecionar os workflows de 2006 que já existem em `main`; harmonizar eventuais diferenças em alteração específica e testável, sem duplicar os ficheiros.
5. Executar as fases em ordem, com evidência independente por fase e sem extrapolar o resultado de uma fase para as seguintes.
6. Antes de certificar, validar objeto LFS materializado, SHA-256, contagem, 25 campos, datas, tipos de registo e reconciliação integral RAW × NORMALIZED.
7. Não fundir o PR enquanto as validações exigidas não forem executadas e inspecionadas.

## Estado da verificação

- A branch original do PR #14 está 51 commits à frente e 2.329 atrás da `main` no snapshot consultado.
- Os 13 workflows-alvo já existem na `main`; o conteúdo difere de forma material em pelo menos os controlos de trigger e persistência.
- Os checksums e manifestos centrais de 2006 coincidem entre os snapshots comparados.
- O CSV canónico normalizado existe em `main` como objeto Git LFS; o PR não deve apagar nem substituir esse artefacto.
- A FASE01 tem evidência versionada, mas a cadeia tem de ser executada e verificada na revisão atual. Evidência histórica não prova que as fases seguintes estejam aprovadas.

## Critérios de aceitação

- Nenhuma regressão de conteúdo atual de `main`.
- Nenhuma alteração ao RAW, manifesto ou sidecar apenas para fazer passar um teste.
- Workflows consistentes com a governança e com uma única branch de destino explicitamente documentada.
- Cada fase reporta o seu próprio resultado e falha fechada quando uma precondição falha.
- Certificação apenas após validação independente física e semântica.
- A análise de COTAHIST não implica cobertura de futuros ou prova de abertura de contratos BRICKMASTER.

## Decisão

**PR #14 permanece bloqueado para merge até resolução dos conflitos, reconciliação dos workflows e validação operacional.** Este documento registra a decisão e não substitui os logs dos workflows nem os artefactos de auditoria.
