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


## 12. Atualização de operação — 2026-10-01

O DRY-RUN continua sendo somente leitura e não substitui os workflows de produção.

A experiência da cadeia 1994 adiciona um requisito: quando o orquestrador for usado para promoção, a dependência deve ser verificada em sequência e não apenas por coexistência de artefatos.

Para o ciclo produtivo, a ordem obrigatória é:

**00 → 01 → 02 → 03–05 → 06 → 07 → 08 → GATE → 09 → GATE → 10 → GATE → 11 → GATE → 12.**

O caminho canônico do RAW anual deve ser resolvido antes de qualquer operação de aquisição:

`dados/cotahist/raw/anual/COTAHIST_A<AAAA>.ZIP`

A matriz de certificação e os manifestos devem ser consultados para evitar reaquisição, duplicação ou falsa conclusão de ausência.



## Aditivo — separação de responsabilidades FASE06/FASE07 — 2026-10-01

O DRY-RUN deve interpretar FASE06 como **reconciliação semântica e invariantes**, não como prova automática de unicidade de chave.

A análise de chaves e cardinalidade pertence à FASE07. Uma evidência FASE06 pode conter `logical_key_uniqueness_assessment=DEFERRED_TO_FASE07` e continuar válida quando todas as demais condições semânticas forem satisfeitas.

O DRY-RUN deve tratar essa condição como estado esperado de dependência, e não como bloqueio, enquanto a FASE07 ainda não tiver sido executada.

## REGRA ESTRUTURAL — ISOLAMENTO, MONOTONICIDADE E IMUTABILIDADE DAS FASES — 2026-10-01

As fases do COTAHIST são **monotônicas e isoladas**.

### Regra 1 — uma fase não retorna para fase anterior
Uma fase N não pode reabrir, recalcular, substituir, corrigir ou alterar a evidência normativa da fase N-1 ou de qualquer fase anterior. Se uma inconsistência anterior for descoberta, ela deve ser tratada como **incidente de governança/correção versionada da própria fase afetada**, sem transformar a fase posterior em responsável por ela.

### Regra 2 — uma fase não executa responsabilidade de fase posterior
Uma fase N não pode antecipar critérios pertencentes à fase N+1. Em especial:
- FASE06 não decide unicidade/cardinalidade de chave;
- FASE07 não reescreve a semântica certificada da FASE06;
- FASE08 não redefine identidade da FASE07;
- FASE09–12 não substituem os gates técnicos anteriores.

### Regra 3 — correção permanece na fase de origem
Se uma regra da FASE06 estiver errada, corrige-se a FASE06. Não se cria uma correção da FASE07 para mascarar a FASE06. Se uma regra da FASE07 estiver errada, corrige-se a FASE07.

### Regra 4 — dependência é somente leitura
Uma fase posterior pode **consumir** a evidência autorizada da fase anterior e os dados-fonte necessários à sua própria análise, mas não pode alterá-los nem reinterpretar silenciosamente o estado certificado da fase anterior.

### Regra 5 — promoção é unidirecional
O fluxo é exclusivamente:

**N-1 → N → N+1**

Não existe fluxo operacional **N+1 → N-1** nem **N → N+1 com responsabilidade de N+1 executada dentro de N**.

### Regra 6 — novo teste não retrocertifica
Uma fase posterior pode detectar um incidente com impacto potencial em fase anterior. Isso gera um **registro de impacto e revisão controlada**, não uma reexecução silenciosa nem uma alteração retroativa da evidência histórica.

### Regra 7 — gatilhos não podem quebrar a monotonicidade
Workflows de uma fase concluída não devem ser disparados por alterações genéricas de documentação, README ou artefatos de fases posteriores. O gatilho deve refletir somente a própria fase e suas entradas autorizadas.

### Matriz de responsabilidade

| Fase | Responsabilidade própria | Não pode assumir |
|---|---|---|
| 00 | governança/pré-condições | validação técnica posterior |
| 01 | aquisição/RAW | integridade semântica |
| 02 | integridade da fonte | parsing/normalização |
| 03 | parsing | normalização/identidade |
| 04 | normalização | identidade/semântica posterior |
| 05 | manifesto/checksum | semântica/chaves |
| 06 | semântica/invariantes | identidade/cardinalidade FASE07 |
| 07 | identidade/chaves/cardinalidade | reescrever FASE06 |
| 08 | semântica/calendário/consistência | reabrir identidade |
| 09 | pré-release | corrigir fases anteriores |
| 10 | validação independente | substituir evidências anteriores |
| 11 | certificação/promoção | refazer fases técnicas silenciosamente |
| 12 | fechamento/transição | certificar o próximo ano |

**Regra de governança:** descobrir algo numa fase posterior não autoriza essa fase a executar o trabalho de uma fase anterior.

