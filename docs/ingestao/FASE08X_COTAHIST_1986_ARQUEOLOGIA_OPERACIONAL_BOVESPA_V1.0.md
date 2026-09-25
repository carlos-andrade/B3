# FASE 08X — Arqueologia Operacional Bovespa

**Arquivo:** FASE08X_COTAHIST_1986_ARQUEOLOGIA_OPERACIONAL_BOVESPA_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Investigar documentação operacional sobre CODBDI, ESPECI, PRAZOT, C05, BDI e Mercado a Termo para testar se existe uma dimensão operacional não preservada na chave K4 da colisão de 10/10/1986.

## 2. Registro-alvo

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Linhas RAW: 140808 e 140809.

RAW SHA-256: `350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018`

## 3. Achado operacional

Foi localizada documentação pública reproduzindo o layout do arquivo histórico. Ela descreve:

- CODBDI como código usado para classificar papéis na emissão do Boletim Diário de Informações;
- TPMERC como código do mercado em que o papel está cadastrado;
- ESPECI como especificação do papel;
- PRAZOT como prazo em dias do Mercado a Termo.

Isso confirma que CODBDI, TPMERC, ESPECI e PRAZOT são dimensões estruturais distintas. citeturn0search2

## 4. C05 antes da colisão

O Jornal do Brasil de 05/06/1986 registra Vigor PP C05 e outras ocorrências Cxx. A mesma publicação mostra a estrutura histórica do Mercado a Termo separando Tipo e Prazo.

Portanto, C05 não surgiu especificamente em 10/10/1986 e não deve ser convertido automaticamente em Tipo. citeturn0search0

## 5. Documentação posterior

Manual operacional posterior da Bovespa mostra que informações do Mercado a Termo eram divulgadas no BDI e que taxas mínima, máxima e média podiam ser divulgadas para diferentes tipos de termo. Essa fonte é apenas controle estrutural e não foi retroprojetada como regra de 1986. citeturn0search56

## 6. Teste da hipótese C05

**FATOS:**
- C05 aparece em ESPECI;
- Vigor PP C05 existia antes de outubro de 1986;
- Tipo e Prazo aparecem separadamente em fonte histórica;
- ESPECI e PRAZOT são campos distintos no COTAHIST.

**NÃO DEMONSTRADO:**
- C05 = Tipo;
- C05 = comprador;
- C05 = vendedor;
- C05 = corretora;
- C05 = comitente;
- C05 = taxa;
- C05 = tipo de contrato;
- C05 = prazo.

## 7. Relação com a colisão

As linhas 140808 e 140809 têm a mesma chave:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060`

Consequentemente, a duplicidade não é explicada por diferença explícita nesses campos.

A hipótese de trabalho passa a ser uma dimensão operacional usada no processo de negociação/publicação, mas não preservada na chave histórica.

**Estado: POSSÍVEL, NÃO PROVADO.**

## 8. Perfis estatísticos

**140808:** TOTNEG 1; QUATOT 39.000.000; VOLTOT 74.100,00; preços 1,90.

**140809:** TOTNEG 4; QUATOT 190.000.000; VOLTOT 356.460,00; PREAB 1,65; PREMIN 1,65; PREMED 1,87; PREMAX 1,91; PREULT 1,75.

Nenhuma fonte recuperada permite atribuir esses perfis a classes operacionais específicas.

## 9. Matriz

| Hipótese | Estado |
|---|---|
| C05 surgiu em 10/10/1986 | REFUTADA |
| C05 = PRAZOT | REFUTADA |
| C05 = Tipo | NÃO DEMONSTRADO |
| CODBDI classifica papéis para o BDI | DOCUMENTADO |
| ESPECI e PRAZOT são distintos | DOCUMENTADO |
| Dimensão operacional não preservada na K4 | POSSÍVEL, NÃO PROVADA |
| Regra histórica de agregação/publicação | HIPÓTESE PRINCIPAL |
| Erro de processamento | NÃO CONFIRMADO |
| Causa da colisão | NÃO RESOLVIDA |

## 10. Governança

RAW intocado; linhas 140808/140809 preservadas; C05, VGO 2, DIMES 104 e DATVEN 99991231 mantidos literalmente; nenhuma consolidação, exclusão ou inferência econômica.

## 11. Próxima frente

**FASE 08Y — reconstrução documental do mecanismo de publicação do BDI.**

Prioridades: exemplos históricos de um mesmo título aparecendo em múltiplas linhas; relação Tipo × Prazo × Cxx; Vigor em pregões próximos; e recuperação dos BDI de 09, 10 e 13/10/1986.

## 12. Estado

**IMPLEMENTADO:** documentado.  
**EXECUTADO:** busca operacional dirigida.  
**VALIDADO:** distinção CODBDI/TPMERC/ESPECI/PRAZOT e existência anterior de Vigor PP C05.  
**EVIDÊNCIA AUSENTE:** legenda primária de C05 e regra contemporânea da duplicidade.  
**NÃO RESOLVIDO:** causa da colisão K4.  
**FASE 08:** ABERTA.
