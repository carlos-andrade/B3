# ORDEM E GOVERNANCA DOS WORKFLOWS COTAHIST

**Versão:** 1.0  
**Status:** VIGENTE PARA ORGANIZAÇÃO  
**Data:** 2026-09-29  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Estabelecer uma ordem lógica única para os workflows do COTAHIST, sem apagar o histórico dos workflows já utilizados.

A ordem operacional não deve depender da ordem alfabética apresentada pelo GitHub.

## 2. Pipeline canônico

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
06 SEMÂNTICA / INVARIANTES
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

## 3. Regra de dependência

Um workflow posterior não deve ser considerado autorização implícita para executar uma etapa anterior.

Cada etapa deve possuir:
- pré-condições;
- entrada;
- saída;
- evidência;
- status;
- dependências;
- critério de promoção.

## 4. FASE 10

A FASE 10 é um **gate independente de release**. Ela não substitui as fases 0–9.

Para os anos 1987–1993, a existência de RAW + NORMALIZED + manifesto + FASE 10 não deve ser interpretada retroativamente como prova de que cada fase 0–9 foi executada individualmente. A auditoria deve classificar cada fase como EXECUTADA COM EVIDÊNCIA, EXECUTADA IMPLICITAMENTE, NÃO DOCUMENTADA, NÃO EXECUTADA ou NÃO APLICÁVEL.

## 5. Ordenação dos workflows

Os workflows existentes permanecem preservados. Primeiro será criada uma camada de catálogo/dependências. Depois, em migração controlada, os workflows ativos poderão receber nomenclatura padronizada.

Convenção para novos workflows:

```
cotahist-<fase>-<funcao>-<escopo>-vN.yml
```

Exemplos:

```
cotahist-01-aquisicao-diaria-v1.yml
cotahist-04-normalizacao-anual-v1.yml
cotahist-10-validacao-independente-v1.yml
cotahist-11-certificacao-anual-v1.yml
cotahist-12-fechamento-transicao-v1.yml
```

## 6. Não-renomeação imediata

Não renomear em massa os workflows históricos sem análise de dependências. Renomeações podem alterar referências, gatilhos, documentação e rastreabilidade.

A migração deve ocorrer por etapas:
1. inventário;
2. classificação;
3. definição das dependências;
4. criação dos novos nomes;
5. validação;
6. desativação controlada dos antigos;
7. preservação do histórico.

## 7. Regra contra corrida

A existência simultânea de workflows independentes acionados por `push` pode produzir corrida entre materialização e validação.

Portanto:

**NORMALIZED materializado → confirmação → FASE 10**

deve ser uma dependência explícita, e não apenas uma coincidência temporal.

O mesmo princípio vale para:

**FASE 10 → certificação → FASE 12**.

## 8. Regra de promoção

Nenhum workflow deve promover um ano para estado superior apenas porque um workflow anterior terminou com `success`. O artefato de evidência e seus critérios de validação também precisam ser verificados.

## 9. Estado atual

1994 permanece **ABERTO SOB CONTROLE** enquanto esta reorganização é incorporada. Nenhum novo release anual será considerado automaticamente certificado por mera existência de manifesto.

## 10. Histórico

| Versão | Data | Alteração |
|---|---|---|
| 1.0 | 2026-09-29 | Criação da ordem canônica e política de migração controlada. |


## 10. Atualização após a cadeia 1994 — 2026-10-01

A regra de dependência foi operacionalizada no ciclo 1994.

A sequência passou a ser explicitamente linear:

**FASE06 → FASE07 → FASE08 → GATE → FASE09 → GATE → FASE10 → GATE → FASE11 → GATE → FASE12.**

O workflow de cadeia 1994 foi ajustado para fail-closed e a própria rotina de FASE09–12 interrompe as fases dependentes quando uma fase anterior falha.

A experiência dos Runs #8 e #10 demonstrou que o gate também precisa distinguir campos informativos de condições reais de aprovação. O contrato de correção agora utiliza `correction_contract_valid` como condição do contrato.

### 10.1 Regra de localização

A existência do RAW deve ser verificada pelo caminho canônico:

`dados/cotahist/raw/anual/COTAHIST_A<AAAA>.ZIP`

Não declarar ausência com base em busca incompleta.

### 10.2 Estado atual

- 1994: cadeia FASE06–12 concluída no Run #13.
- 1995: RAW, manifesto e checksum confirmados.
- próximo ciclo: 1995.
- 1996+: aguardando fechamento de 1995.



## Aditivo normativo — FASE06/FASE07 — 2026-10-01

A experiência da FASE06/1995 estabelece que **semântica não pode assumir unicidade de chave**.

A FASE06 verifica presença e consistência semântica dos campos e invariantes OHLC/quantidade/volume. Duplicidades de uma chave candidata são registradas como observação diagnóstica.

A decisão sobre a chave lógica, sua cardinalidade e sua unicidade pertence à FASE07 — IDENTIDADE / CHAVES / CAMPOS — e deve ser fundamentada no layout aplicável e em evidência histórica.

Assim, a sequência passa a ter o seguinte contrato explícito:

**FASE06 = semântica/invariantes; FASE07 = identidade/chaves/cardinalidade.**

Nenhum workflow pode duplicar essa responsabilidade ou introduzir uma regra de unicidade fora da FASE07.

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



## Aditivo normativo — GATE 06–08 — 2026-10-01

O GATE 06–08 passa a ser uma barreira formal de promoção técnica, com contrato específico em 'docs/cotahist/CONTRATO_GATE_06_08_PROMOCAO_TECNICA_V1.md'.

Sequência obrigatória:

**FASE06 → FASE07 → FASE08 → GATE 06–08 → FASE09.**

O Gate deve verificar as três evidências separadamente, seus estados permitidos, o ano/ciclo, exceções, bloqueadores e o isolamento de responsabilidades. A decisão é fail-closed:

**LIBERADO_PARA_FASE09** somente quando todas as condições estiverem satisfeitas; caso contrário, **BLOQUEADO_PARA_FASE09**.

O Gate não executa análise técnica, não corrige fases e não substitui evidências. Problemas são corrigidos na fase de origem.

README e documentação genérica não constituem gatilhos operacionais para reexecutar fases concluídas.
