# FASE 08F — Estrutura Estatística da Colisão K4 — COTAHIST 1986

**Arquivo:** FASE08F_COTAHIST_1986_ESTRUTURA_ESTATISTICA_K4_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** análise matemática e estrutural das linhas 140808/140809  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo
Investigar se as duas linhas da colisão K4 de 10/10/1986 possuem propriedades estatísticas distintas que ajudem a caracterizar sua coexistência estruturalmente, sem atribuir significado econômico prévio.

## 2. Método
Para cada registro são preservados os campos RAW e calculados:
- preço implícito = VOLTOT / QUATOT;
- PREULT / FATCOT;
- PREMED / FATCOT;
- amplitude PREMAX−PREMIN;
- diferença entre VOLTOT e PREULT/FATCOT × QUATOT;
- teste de preço implícito dentro de PREMIN–PREMAX.

Comparações:
1. linhas 140808/140809;
2. VGO 2 com CODBDI=62 e TPMERC=030;
3. todo o universo CODBDI=62 e TPMERC=030;
4. grupos com a mesma chave K4.

## 3. Regra de classificação
**FATO:** campo preservado no RAW.  
**DERIVADO:** cálculo reproduzível.  
**PADRÃO:** comportamento do conjunto.  
**HIPÓTESE:** interpretação não confirmada.

## 4. Observação estrutural preliminar
A linha 140808 possui TOTNEG=1 e VOLTOT/QUATOT=0,19, exatamente igual a PREULT/FATCOT (190/1000).
A linha 140809 possui TOTNEG=4 e VOLTOT/QUATOT≈0,1876105263, dentro de PREMIN/FATCOT–PREMAX/FATCOT e próxima de PREMED/FATCOT (187/1000).

Essas relações são matematicamente observáveis. Elas não provam a razão histórica da duplicidade.

## 5. Governança
- RAW intocado;
- nenhuma linha removida;
- nenhuma linha consolidada;
- nenhum valor estatístico corrigido;
- SHA-256 do RAW registrado no JSON;
- nenhuma causa econômica inferida automaticamente.

## 6. Status inicial
**IMPLEMENTADO:** aguardando execução do workflow  
**EXECUTADO:** aguardando publicação do JSON  
**VALIDADO:** aguardando conferência do JSON

## 7. Próxima decisão técnica
Se o JSON confirmar que a diferença estatística é estruturalmente recorrente, a FASE 08G deverá testar a recorrência de perfis estatísticos sob K4 idêntica. Se for isolada, a investigação documental deverá permanecer aberta.
