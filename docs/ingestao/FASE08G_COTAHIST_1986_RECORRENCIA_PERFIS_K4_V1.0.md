# FASE 08G — Recorrência Histórica de Perfis Estatísticos sob K4 Idêntica

**Arquivo:** FASE08G_COTAHIST_1986_RECORRENCIA_PERFIS_K4_V1.0.md
**Projeto:** B3 - A BOLSA DO BRASIL
**Tema:** teste de recorrência da colisão K4 e de perfis estatísticos
**Data:** 24/09/2026
**Repositório:** carlos-andrade/B3

## 1. Objetivo
Testar se a coexistência de duas linhas com K4 idêntica em 10/10/1986 é recorrente no arquivo ou se constitui ocorrência isolada, separando recorrência de K4 de recorrência de perfil estatístico.

## 2. Método
Foram executados três testes:
1. repetição exata da K4;
2. repetição de perfil estatístico normalizado por FATCOT, incluindo TOTNEG, preços ajustados e VOLTOT/QUATOT;
3. comparação de registros do mesmo dia, mercado, CODNEG e TPMERC.

Nenhuma recorrência de perfil é tratada como prova de mesma origem econômica.

## 3. Escopo
Arquivo RAW: COTAHIST_A1986.ZIP.
Registros tipo 01: 177.981.

## 4. Critério
**FATO:** repetição literal dos campos da K4.
**DERIVADO:** perfil estatístico calculado.
**PADRÃO:** recorrência observada no conjunto.
**HIPÓTESE:** interpretação ainda não documentalmente comprovada.

## 5. Resultado
O JSON publicado pelo workflow contém:
- contagem de grupos K4 duplicados;
- linhas e perfis de cada grupo;
- recorrência exata dos perfis estatísticos;
- correspondências relaxadas das linhas 140808 e 140809;
- registros do mesmo contexto diário;
- SHA-256 do RAW.

## 6. Regra de interpretação
Se K4 duplicada ocorrer somente uma vez, isso caracteriza a colisão de 10/10/1986 como **isolada dentro do COTAHIST 1986**. Se perfis estatísticos semelhantes ocorrerem muitas vezes, isso demonstra apenas que os números estatísticos não são identificadores únicos.

Uma recorrência de perfil semelhante não autoriza consolidar, excluir ou reclassificar registros.

## 7. Governança
- RAW intocado;
- nenhum registro removido;
- nenhuma consolidação;
- nenhuma correção dos valores originais;
- nenhuma identidade econômica inferida.

## 8. Resultado validado

Workflow: **36069511740 — success**.

Evidência: `dados/cotahist/quality/COTAHIST_1986_FASE08G_RECORRENCIA_PERFIS_K4_V1.json`

Commit da evidência: **72214498bdb24f122b54ed1dc47b1dbb967b365c**.

RAW SHA-256: **350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018**.

Resultados:

- 177.981 registros tipo 01;
- 1 grupo K4 duplicado;
- 2 linhas no grupo duplicado: 140808 e 140809;
- a colisão continua sendo única no arquivo;
- a linha 140808 possui **58 correspondências** de perfil estatístico normalizado exato em outros registros;
- a linha 140809 possui **0 correspondências** de perfil estatístico normalizado exato;
- existem **7.392 famílias** de perfis estatísticos normalizados recorrentes, abrangendo 62.784 registros;
- a maior família contém 685 registros.

A comparação do mesmo dia, CODNEG, CODBDI e TPMERC encontrou somente as duas linhas da própria colisão.

## 9. Interpretação

**FATO VALIDADO:** a K4 duplicada é única no COTAHIST 1986.

**FATO VALIDADO:** o perfil estatístico da linha 140808 não é único; há 58 ocorrências de perfil normalizado exato em outros registros.

**FATO VALIDADO:** o perfil da linha 140809 não reaparece exatamente sob o critério adotado.

**PADRÃO VALIDADO:** perfis estatísticos recorrentes são comuns no arquivo; portanto, estatística isolada não funciona como identificador de identidade econômica.

**NÃO DETERMINADO:** por que as duas linhas foram publicadas simultaneamente sob a mesma K4 em 10/10/1986.

A evidência enfraquece a hipótese de que a colisão possa ser explicada simplesmente por um perfil estatístico raro. Também não demonstra a causa da separação.

## 10. Governança

- RAW intocado;
- nenhuma linha removida;
- nenhuma linha consolidada;
- nenhum valor corrigido;
- nenhum significado econômico inferido a partir de recorrência estatística.

## 11. Status

IMPLEMENTADO: OK
EXECUTADO: OK
VALIDADO: OK

## 12. Próxima frente
Após a validação, decidir se a investigação precisa ampliar o escopo para múltiplos anos COTAHIST ou se a evidência disponível em 1986 já é suficiente para manter a anomalia como caso histórico isolado.
