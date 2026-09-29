# Matriz de Dependências COTAHIST — V1

**Data:** 2026-09-29  
**Base:** inspeção dos workflows de ingestão, normalização, materialização, FASE 10, certificação, publicação e gate histórico.

| Componente | Fase | Trigger atual | Entrada | Saída | Dependência formal | Diagnóstico |
|---|---:|---|---|---|---|---|
| importacao-diaria-v1 | 01 | schedule/push/manual | diário B3 | diário + dataset atual | nenhuma | independente |
| normalizacao-controlada-v7 | 04/05 | manual | RAW anual | manifest/checksum | nenhuma | depende de operador |
| normalizacao-1988-v1 | 04/05 | push/manual | RAW 1988 | NORMALIZED + manifest | nenhuma | legado histórico |
| materializar-normalized-AAAA | 04 | push/manual | RAW + manifest | NORMALIZED LFS | nenhuma | origem da corrida |
| fase10-integridade-AAAA | 10 | push/manual | RAW + NORMALIZED + manifest | evidência FASE10 | nenhuma | gate independente, sem predecessor formal |
| certificacao-anual-v1 | 11 | push/schedule/manual | manifests/evidências | matriz anual | nenhuma | promoção sem dependência formal |
| dataset-oficial-v1 | 12/publicação | push/schedule/manual | certificação/manifests | dataset oficial | nenhuma | promoção independente |
| dataset-oficial-v2 | 12/publicação | push/manual | NORMALIZED/certificação v2 | dataset oficial V2 | nenhuma | promoção independente |
| m3-1e-aprovacao-global | infraestrutura | push/manual | 2026 + manifestos | aprovação | nenhuma | gate específico 2026 |
| gate-historico-1986 | exceção | push/manual | RAW 1986 | NORMALIZED + manifests + auditoria + oficial | cadeia interna no próprio job | exceção controlada |

## 1. Dependência crítica

O GitHub Actions está sendo usado principalmente como mecanismo de gatilho de eventos, e não como orquestrador de precedência semântica.

Exemplo: a materialização de 1993 grava NORMALIZED e o mesmo push pode disparar a FASE10. A FASE10 não recebe um sinal formal de que a materialização terminou com sucesso; ela apenas reage à alteração dos arquivos.

## 2. Concurrency não resolve dependência

Os workflows possuem grupos concurrency, mas isso controla principalmente execuções concorrentes do mesmo workflow. Não cria dependência entre workflows diferentes.

## 3. Rebase não resolve dependência semântica

git fetch + git rebase + git push reduz conflitos no main, mas não garante que a evidência anterior foi produzida e validada. Git protege a sequência de commits; não protege a sequência lógica do pipeline.

## 4. Arquitetura alvo

RAW → NORMALIZAÇÃO → MANIFESTO → AUDITORIAS 06–08 → PRÉ-RELEASE → FASE10 → CERTIFICAÇÃO → DATASET OFICIAL → FASE12

As auditorias 06–08 podem executar em paralelo depois que a pré-condição comum estiver disponível, mas a promoção para FASE10 deve exigir todas as evidências necessárias.

## 5. Regra de promoção

A FASE10 futura não deve verificar somente se NORMALIZED existe. Deve verificar: RAW presente; RAW hash confirmado; NORMALIZED presente; NORMALIZED hash confirmado; manifesto VALIDADO; reconciliação aprovada; identidade aprovada; semântica/calendário aprovados; pré-release aprovado.

Somente então: FASE10 = LIBERADA.

## 6. Regra para 1986

1986 permanece fora do pipeline normal. O gate-historico-1986 encapsula uma cadeia interna de normalização, auditoria semântica, validação, persistência LFS, manifestos e gate final. Deve ser tratado como workflow de exceção histórica.

## 7. Regra para 1987–1988

Não migrar automaticamente os workflows históricos para o novo orquestrador. Primeiro construir matriz retrospectiva de evidências e somente depois classificar equivalências às fases 00–12.

## 8. Próxima etapa

Criar o primeiro orquestrador anual canônico em modo de validação/DRY-RUN, sem desativar workflows existentes. O teste inicial deve usar um ano já certificado, para comprovar que o DAG reproduz resultados conhecidos sem alterar dados históricos.