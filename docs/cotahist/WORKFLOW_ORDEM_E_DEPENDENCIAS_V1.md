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
