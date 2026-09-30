# Orquestrador Anual Canônico COTAHIST — V2 (DRY-RUN FASE 00–12)

**Data:** 2026-09-30  
**Workflow:** `.github/workflows/cotahist-orquestrador-anual-dryrun-v2.yml`  
**Modo:** somente leitura.

## Objetivo

O DRY-RUN V2 verifica, em uma única execução, a cadeia completa de precedência do COTAHIST anual, da FASE 00 à FASE 12.

Ele não substitui os workflows de produção e não executa qualquer promoção.

## Sequência canônica

```
00 GOVERNANÇA / PRÉ-CONDIÇÕES
        ↓
01 AQUISIÇÃO / RAW
        ↓
02 INTEGRIDADE DA FONTE
        ↓
03 PARSING
        ↓
04 NORMALIZAÇÃO
        ↓
05 MANIFESTO / CHECKSUM
        ↓
06 RECONCILIAÇÃO
        ↓
07 IDENTIDADE / CHAVES / CAMPOS
        ↓
08 SEMÂNTICA / CALENDÁRIO / CONSISTÊNCIA
        ↓
09 PRÉ-RELEASE
        ↓
10 VALIDAÇÃO INDEPENDENTE
        ↓
11 CERTIFICAÇÃO / PROMOÇÃO
        ↓
12 FECHAMENTO DO ANO / ABERTURA DO PRÓXIMO
```

## Matriz de verificação

| Fase | Gate do DRY-RUN | Evidência principal |
|---|---|---|
| 00 | Governança existente | `docs/cotahist/WORKFLOW_ORDEM_E_DEPENDENCIAS_V1.md` |
| 01 | RAW anual existente | `dados/cotahist/raw/anual/COTAHIST_AAAAAA.ZIP` |
| 02 | Integridade da fonte comprovada | `...FASE02_INTEGRIDADE_FONTE_V1.json` |
| 03 | Parser versionado e compatível | `scripts/ingestao/normalize_cotahist.py` + versão do manifesto |
| 04 | Normalizado existente | `dados/cotahist/normalized/anual/COTAHIST_AAAAAA.csv` |
| 05 | Manifesto válido | `..._quality.json` |
| 06 | Reconciliação comprovada | `...FASE06_RECONCILIACAO_V1.json` |
| 07 | Identidade/chaves comprovadas | `...FASE07_IDENTIDADE_CHAVES_V1.json` |
| 08 | Semântica/calendário comprovados | `...FASE08_SEMANTICA_CALENDARIO_V1.json` |
| 09 | Pré-release comprovado | `...FASE09_PRE_RELEASE_V1.json` |
| 10 | Validação independente autorizada | `...FASE10_INTEGRIDADE_V1.json` |
| 11 | Certificação anual presente | matriz `COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv` |
| 12 | Fechamento/abertura comprovados | `...FASE12_FECHAMENTO_AAAA_ABERTURA_AAAA+1_V1.json` |

## Estados

- **OK** — evidência encontrada e compatível.
- **AUSENTE** — evidência obrigatória não encontrada.
- **BLOQUEADO** — evidência existe, mas seu conteúdo não satisfaz o contrato.
- **NAO_APLICAVEL** — regra formal determina que a fase não se aplica ao ano.
- **EXCECAO_CONTROLADA** — exceção formal registrada e auditável.

## Regra fail-closed

Qualquer FASE obrigatória em **AUSENTE** ou **BLOQUEADO** impede:

- promoção;
- publicação;
- certificação nova;
- alteração do dataset oficial;
- desativação de workflows.

A existência de uma evidência posterior não retrocertifica uma fase anterior.

## FASE 11 no DRY-RUN

O DRY-RUN apenas verifica a certificação existente na matriz anual.

Ele **não certifica** e **não promove** o ano.

## FASE 12 no DRY-RUN

Para anos anteriores a 2026, o DRY-RUN procura o artefato de transição:

`FASE12_FECHAMENTO_<ano>_ABERTURA_<ano+1>`.

Para 2026, a fase é marcada como **NAO_APLICAVEL**, pois a matriz anual atual termina em 2026 e não há ciclo oficial 2027 no escopo atual.

## Resultado

O resultado contém:

- todas as fases 00–12;
- status individual;
- caminho da evidência;
- detalhes de bloqueio;
- lista de códigos bloqueadores;
- estado de promoção;
- confirmação de ausência de mutações.

O workflow termina com código diferente de zero quando houver bloqueadores. Isso é deliberado: **DRY-RUN concluído com bloqueio não significa falha do mecanismo de auditoria**; significa que o mecanismo detectou uma pré-condição não satisfeita.

## Caso inicial

O primeiro caso de execução permanece **1993**, porque esse ano possui FASE10 e certificação já conhecidas e permite testar o encadeamento completo sem introduzir imediatamente um ano ainda não certificado.

## Segurança operacional

O workflow possui:

- `permissions: contents: read`;
- nenhum `git commit`;
- nenhum `git push`;
- nenhuma publicação;
- nenhuma alteração de workflow;
- verificação final de working tree limpo.

Os workflows legados permanecem ativos.
