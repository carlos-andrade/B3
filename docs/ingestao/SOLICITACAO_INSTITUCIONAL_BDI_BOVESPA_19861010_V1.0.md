# SOLICITAÇÃO INSTITUCIONAL — BDI BOVESPA 10/10/1986 — FASE 09C

**Arquivo:** SOLICITACAO_INSTITUCIONAL_BDI_BOVESPA_19861010_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Recuperação de fonte primária para resolver colisão K4 do COTAHIST 1986  
**Data de criação:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Solicitar à B3, ao Centro de Memória ou ao canal institucional competente a localização e disponibilização, ou ao menos a identificação arquivística inequívoca, do **BDI — Segmento BOVESPA / Cotações do Histórico Regular** correspondente ao pregão de **10/10/1986**.

O documento é necessário para investigar uma colisão única encontrada no COTAHIST 1986.

## 2. Alvo exato

- Data do pregão: **10/10/1986**
- Segmento: **BOVESPA**
- Publicação: **BDI — Cotações do Histórico Regular**
- Seção prioritária: **Mercado a Termo**
- Ativo: **Vigor / VGO 2**
- Especificação observada no COTAHIST: **PP *C05**
- Prazo: **060**
- CODBDI: **62**
- TPMERC: **030**
- CODISI: **VGORACPP**
- DIMES: **104**
- DATVEN: **99991231**
- PREEXE: **0**
- INDOPC: **0**
- PTOEXE: **0**
- Linhas RAW: **140808 e 140809**

## 3. O que se solicita

Solicita-se, preferencialmente:

1. cópia digital do BDI de 10/10/1986;
2. identificação da página/seção onde aparece Vigor/VGO2;
3. identificação do título, edição e código/catalogação do documento;
4. identificação do formato original, se preservado;
5. informação sobre eventual microfilme, papel, imagem, PDF ou outro suporte;
6. informação sobre o sistema/catálogo no qual o item está registrado;
7. se o exemplar de 10/10/1986 não estiver disponível, indicação do BDI de 09/10/1986 e/ou 13/10/1986;
8. eventual manual, legenda ou regulamento de 1986 que defina os campos **Tipo**, **Prazo**, **Cxx** e a regra de agregação das operações a termo.

## 4. Justificativa técnica

A análise do COTAHIST 1986 encontrou exatamente uma colisão K4:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

As duas linhas possuem a mesma K4, mas estatísticas diferentes:

- linha 140808: TOTNEG=1, QUATOT=39.000.000, VOLTOT=74.100,00, preços=1,90;
- linha 140809: TOTNEG=4, QUATOT=190.000.000, VOLTOT=356.460,00, PREAB=1,65, PREMAX=1,91, PREMIN=1,65, PREMED=1,87, PREULT=1,75.

A colisão é única no COTAHIST 1986 e também única no universo anual analisado de 1986–2026.

A investigação documental encontrou evidência contemporânea de que o Mercado a Termo era publicado com **Tipo** e **Prazo** como dimensões distintas, além de Quant, Fech, Máx, Mín, Méd e N°. Contudo, ainda não foi possível provar qual dimensão histórica explica as duas linhas Vigor.

## 5. Critério de encerramento

A investigação será considerada resolvida somente se a documentação primária ou normativa contemporânea permitir:

- identificar as duas linhas no BDI;
- observar diferenças de Tipo, condição ou outra dimensão não preservada na K4; ou
- demonstrar documentalmente uma regra de agregação/publicação capaz de produzir os dois agregados.

Não será feita fusão, descarte, seleção ou recodificação das linhas COTAHIST sem essa evidência.

## 6. Evidência institucional já localizada

Comunicado BM&FBOVESPA nº 031/2016-DO identifica expressamente os arquivos de **Cotações do Histórico Regular (BDI — Segmento BOVESPA)** e informa sua posterior descontinuação no contexto da integração da pós-negociação.

Fonte:
https://www.b3.com.br/data/files/EA/21/EB/0F/8E92451090C77145790D8AA8/CE%20031.2016-DO-PT-%20Novo%20Boletim%20de%20Neg%C3%B3cios%20%E2%80%93%20Consolida%C3%A7%C3%A3o%20dos%20Boletins%20Di%C3%A1rios%20de%20Informa%C3%A7%C3%B5es%20dos%20Mercados%20de%20Derivativos%20e%20de%20Rend.pdf

## 7. Estado

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM — protocolo de solicitação preparado  
**VALIDADO:** SIM — alvo documental e critérios definidos  
**BDI 10/10/1986 RECUPERADO:** NÃO  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**RAW ALTERADO:** NÃO

## 8. Próxima ação

Enviar esta especificação ao canal institucional adequado da B3/Centro de Memória, mantendo o Issue #4 como rastreador público da investigação.

