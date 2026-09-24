# FASE 08H — Recorrência de Colisões K4 em Múltiplos Anos

**Arquivo:** FASE08H_COTAHIST_RECORRENCIA_K4_MULTIANOS_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Verificação multianual de K4 idêntica com estatísticas diferentes  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Testar, em todos os arquivos anuais COTAHIST disponíveis no repositório no momento da execução, se o fenômeno observado em 1986 — duas linhas tipo 01 com K4 idêntica e campos estatísticos diferentes — reaparece em outros anos.

A análise foi desenhada para separar quatro situações:

1. K4 duplicada;
2. K4 duplicada com estatísticas comparadas idênticas;
3. K4 duplicada com estatísticas diferentes;
4. igualdade estatística sem identidade econômica inferida.

## 2. Universo auditado

Foram encontrados **41 arquivos anuais**, de **1986 a 2026**, todos com o padrão `COTAHIST_AYYYY.ZIP`.

Foram processados **24.314.082 registros tipo 01**.

A análise preservou e registrou o SHA-256 de cada arquivo RAW utilizado.

## 3. Definição operacional da K4

A mesma chave utilizada na investigação de 1986 foi aplicada uniformemente a todos os anos:

- DATAPREGAO;
- CODBDI;
- CODNEG;
- TPMERC;
- CODISI;
- DIMES;
- ESPECI;
- PRAZOT;
- DATVEN;
- PREEXE;
- INDOPC;
- PTOEXE.

A comparação estatística foi feita sobre:

- PREAB;
- PREMAX;
- PREMIN;
- PREMED;
- PREULT;
- TOTNEG;
- QUATOT;
- VOLTOT;
- FATCOT.

A igualdade de K4 **não foi interpretada como identidade econômica**.

## 4. Resultado global

| Métrica | Resultado |
|---|---:|
| Anos analisados | 41 |
| Período | 1986–2026 |
| Registros tipo 01 | 24.314.082 |
| Grupos K4 | 24.314.081 |
| Grupos K4 duplicados | 1 |
| Linhas pertencentes a grupos duplicados | 2 |
| Grupos K4 duplicados com estatísticas diferentes | 1 |
| Grupos K4 duplicados estatisticamente idênticos | 0 |
| Anos com qualquer duplicidade K4 | 1986 |
| Anos com K4 + estatísticas diferentes | 1986 |

## 5. Resultado decisivo

A colisão identificada em 1986 **não reapareceu em nenhum dos outros 40 anos analisados**.

O resultado multianual encontrado foi:

> **24.314.082 registros tipo 01 → 24.314.081 grupos K4 → somente 1 grupo K4 duplicado → somente 1 grupo com estatísticas diferentes → somente 1986.**

Portanto, dentro do universo anual disponível no repositório e sob a definição K4 adotada, a ocorrência é **historicamente única no período 1986–2026**.

Isso é um fato estatístico do acervo analisado. Não determina, por si só, a causa histórica da duplicidade.

## 6. Colisão de 1986

O único grupo encontrado é:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Linhas RAW:

- 140808;
- 140809.

Campos estatísticos diferentes:

- PREAB;
- PREMAX;
- PREMIN;
- PREMED;
- PREULT;
- TOTNEG;
- QUATOT;
- VOLTOT.

O FATCOT permaneceu igual.

A ocorrência pertence ao contexto:

- CODBDI = 62;
- TPMERC = 030;
- PRAZOT = 060;
- ESPECI = PP *C05;
- DIMES = 104;
- CODISI = VGORACPP.

## 7. Comparação com a FASE 08G

A FASE 08G demonstrou, dentro de 1986, que o perfil estatístico normalizado da linha 140808 ocorre em outros registros, enquanto o perfil da linha 140809 não apresentou recorrência exata sob o critério adotado.

A FASE 08H acrescenta uma dimensão diferente:

- a **K4 duplicada** não reaparece nos outros anos;
- portanto, a anomalia estrutural não pode ser classificada como um padrão recorrente anual do arquivo COTAHIST sob a chave K4 estudada.

Esses dois resultados não devem ser confundidos:

- perfil estatístico recorrente ≠ K4 recorrente;
- K4 única ≠ identidade econômica determinada.

## 8. Interpretação controlada

### FATO

A colisão K4 de 10/10/1986 é a única colisão K4 encontrada em 41 arquivos anuais, de 1986 a 2026.

### FATO

As duas linhas da colisão de 1986 possuem estatísticas diferentes.

### FATO

Não foi encontrada outra ocorrência multianual com a mesma estrutura de K4 duplicada e estatísticas diferentes.

### HIPÓTESE

A singularidade histórica pode estar relacionada a uma regra operacional, cadastral ou de publicação específica daquele período/contexto.

Essa hipótese **não está demonstrada** pela FASE 08H.

### NÃO DETERMINADO

A análise não determina:

- por que a K4 foi repetida;
- por que os agregados estatísticos foram separados;
- qual regra histórica de publicação produziu as duas linhas;
- o significado histórico completo de C05;
- o significado histórico completo de DIMES 104;
- a razão de DATVEN = 99991231;
- se a duplicidade representa duas classes econômicas, duas agregações, um processamento histórico ou outra regra operacional.

## 9. Integridade dos dados

Para todos os anos, o parser calculou e registrou SHA-256 do ZIP RAW.

O SHA-256 de 1986 permaneceu:

`350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018`

Não houve alteração dos arquivos RAW.

## 10. Governança

Durante a FASE 08H:

- RAW não foi alterado;
- nenhum registro foi apagado;
- nenhum registro foi consolidado;
- nenhuma identidade econômica foi inferida;
- nenhuma causa histórica foi declarada como resolvida.

O artefato JSON é evidência reprodutível da execução.

## 11. Artefatos

### Parser

`scripts/ingestao/analisar_recurrencia_colisoes_k4_cotahist_multianos_v1.py`

Commit inicial:

`46a2387bf144ce75f77ee69e523cae36248bd7f0`

Correção de execução:

`a25880fd927c388d5f4aab99ad4a7dbbf29d057f`

### Workflow

`.github/workflows/cotahist-fase08h-recurrencia-k4-multianos-v1.yml`

Commit:

`57b723b0187726012b9ec9a76cd0e408f8a442fb`

### Evidência

`dados/cotahist/quality/COTAHIST_FASE08H_RECORRENCIA_K4_MULTIANOS_V1.json`

Commit de publicação:

`c19566cf1481c245b6908f4a3e2238138656c229`

### Execução

Workflow run:

`36070061381`

Conclusão:

**SUCCESS**

## 12. Status

**IMPLEMENTADO:** parser multianual e workflow criados no repositório.

**EXECUTADO:** 41 arquivos anuais, 1986–2026, processados.

**VALIDADO:** somente 1 grupo K4 duplicado em todo o universo; somente 1 grupo com estatísticas diferentes; ocorrência exclusivamente em 1986.

## 13. Próxima frente controlada

A FASE 08H encerra a pergunta de recorrência multianual sob a K4 atual.

A próxima investigação deve deixar de procurar outra ocorrência da mesma colisão e concentrar-se na **reconstrução da regra histórica de publicação/agregação de 1986**, priorizando documentação contemporânea e, se necessário, uma análise de vizinhança estrutural dos registros do mercado a termo.

Nenhuma alteração do RAW deve ser feita até que a regra histórica seja demonstrada por evidência suficiente.
