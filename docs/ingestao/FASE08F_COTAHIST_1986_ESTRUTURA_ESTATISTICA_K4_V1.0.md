# FASE 08F — Estrutura Estatística da Colisão K4 — COTAHIST 1986

**Arquivo:** FASE08F_COTAHIST_1986_ESTRUTURA_ESTATISTICA_K4_V1.0.md
**Projeto:** B3 - A BOLSA DO BRASIL
**Tema:** análise matemática e estrutural das linhas 140808/140809
**Data:** 24/09/2026
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Investigar se as duas linhas da colisão K4 de 10/10/1986 possuem propriedades estatísticas distintas que ajudem a caracterizar sua coexistência estruturalmente, sem atribuir significado econômico prévio.

## 2. Escala e método

O layout oficial B3 define os campos de preço como valores com duas casas decimais e FATCOT como fator de cotação. FATCOT=1000 significa cotação por lote de mil ações. VOLTOT também possui duas casas decimais. Assim, a comparação deve respeitar a unidade de cotação e o fator de cotação.

Cálculos:
- preço implícito = VOLTOT / QUATOT;
- PREULT / FATCOT;
- PREMED / FATCOT;
- amplitude PREMAX−PREMIN;
- diferença entre VOLTOT e PREULT/FATCOT × QUATOT;
- teste de preço implícito dentro de PREMIN/FATCOT–PREMAX/FATCOT.

Comparações:
1. linhas 140808/140809;
2. VGO 2 com CODBDI=62 e TPMERC=030;
3. todo o universo CODBDI=62 e TPMERC=030;
4. grupos com a mesma chave K4.

## 3. Resultado executado

Workflow FASE 08F: run 36068809896 — success.

Commit de publicação da evidência: 823e2aea837c8f993ab981916f7082df58abcb2d.

Evidência publicada:
dados/cotahist/quality/COTAHIST_1986_FASE08F_ESTRUTURA_ESTATISTICA_K4_V1.json

RAW SHA-256:
350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018

Registros tipo 01: 177.981.

## 4. Linha 140808

- TOTNEG = 1
- QUATOT = 39.000.000
- VOLTOT = 74.100,00
- PREAB = PREMAX = PREMIN = PREMED = PREULT = 1,90
- FATCOT = 1.000

VOLTOT / QUATOT = 0,0019.

PREULT / FATCOT = 0,0019.

A diferença VOLTOT − (PREULT/FATCOT × QUATOT) é 0.

Classificação: FATO + DERIVADO.

## 5. Linha 140809

- TOTNEG = 4
- QUATOT = 190.000.000
- VOLTOT = 356.460,00
- PREAB = 1,65
- PREMIN = 1,65
- PREMED = 1,87
- PREMAX = 1,91
- PREULT = 1,75
- FATCOT = 1.000

VOLTOT / QUATOT = 0,001876105263...

PREMED / FATCOT = 0,00187.

A diferença relativa entre preço implícito e PREMED/FATCOT é aproximadamente +0,3265%.

O preço implícito permanece entre PREMIN/FATCOT e PREMAX/FATCOT.

A diferença VOLTOT − (PREULT/FATCOT × QUATOT) é 23.960,00.

Classificação: FATO + DERIVADO.

## 6. Comparação estrutural

Universo VGO 2 / CODBDI=62 / TPMERC=030: 188 registros.

- TOTNEG=1: 52
- TOTNEG>1: 136
- preço implícito dentro de PREMIN–PREMAX: 175/188
- preço implícito a até 1% de PREMED/FATCOT: 188/188

Universo CODBDI=62 / TPMERC=030: 36.596 registros.

- TOTNEG=1: 16.262
- TOTNEG>1: 20.334
- preço implícito dentro de PREMIN–PREMAX: 32.802
- preço implícito a até 1% de PREMED/FATCOT: 36.574

A colisão K4 permanece única no arquivo: 1 grupo duplicado com 2 linhas.

A relação numérica 0,0019 também não é exclusiva: foram encontrados 8 registros no universo CODBDI=62 / TPMERC=030 com VOLTOT/QUATOT exatamente igual a 0,0019, incluindo a linha 140808. Portanto, a coerência matemática da linha 140808 é um padrão recorrente de preço/quantidade/volume, mas não explica por si só a duplicidade K4.

## 7. Conclusão

FATO VALIDADO: as duas linhas compartilham a mesma K4, mas apresentam perfis estatísticos diferentes.

FATO VALIDADO: a linha 140808 possui TOTNEG=1 e coerência aritmética exata entre VOLTOT, QUATOT, PREULT e FATCOT.

FATO VALIDADO: a linha 140809 possui TOTNEG=4, faixa de preços 1,65–1,91 e preço implícito 0,001876105263..., próximo de PREMED/FATCOT.

PADRÃO VALIDADO: TOTNEG=1 não é exclusivo do caso; 52 de 188 registros VGO 2 em termo possuem TOTNEG=1.

FATO VALIDADO: a colisão K4 continua sendo única no COTAHIST 1986.

FATO VALIDADO: o perfil numérico 0,0019 ocorre em 8 registros de termo 62/030; a linha 140808 é um deles.

NÃO DETERMINADO: a razão histórica/operacional que levou duas linhas com K4 idêntica a coexistirem em 10/10/1986.

HIPÓTESE CONTROLADA: os dois registros podem representar agregações estatísticas distintas, mas o arquivo não contém campo explícito que identifique a regra de separação.

## 8. Governança

- RAW intocado;
- nenhuma linha removida;
- nenhuma linha consolidada;
- nenhum valor estatístico corrigido;
- SHA-256 do RAW preservado no JSON;
- nenhuma causa econômica inferida.

## 9. Status

IMPLEMENTADO: OK
EXECUTADO: OK
VALIDADO: OK

## 10. Próxima frente

FASE 08G — Recorrência histórica de perfis estatísticos sob K4 idêntica.
