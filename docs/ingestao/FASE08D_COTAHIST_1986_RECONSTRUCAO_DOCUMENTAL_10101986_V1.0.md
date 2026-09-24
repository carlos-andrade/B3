# FASE 08D — Reconstrução Documental de 10/10/1986

**Arquivo:** FASE08D_COTAHIST_1986_RECONSTRUCAO_DOCUMENTAL_10101986_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconstrução documental da colisão K4 de VGO 2 em 10/10/1986  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Investigar evidência contemporânea ou documentalmente próxima de 10/10/1986 capaz de explicar a existência de duas linhas COTAHIST com a mesma chave K4 para:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Linhas RAW: **140808** e **140809**.

A investigação deve separar estritamente:

- FATO VALIDADO;
- PADRÃO OBSERVADO;
- HIPÓTESE;
- EVIDÊNCIA AUSENTE.

Nenhuma fonte posterior será usada para inventar uma semântica histórica que não esteja documentada.

## 2. Escopo da busca

Foram pesquisadas, em 24/09/2026:

1. referências exatas a 10/10/1986 + Vigor + Bovespa;
2. referências a Vigor PP C05;
3. referências a VGO 2;
4. documentação sobre Mercado a Termo em 1986;
5. Boletim Diário de Informações/Bovespa;
6. legislação contemporânea relacionada às operações a termo.

## 3. Resultado documental

### 3.1 BDI/Bovespa de 10/10/1986

**RESULTADO: NÃO LOCALIZADO.**

A busca pública realizada nesta fase não encontrou uma cópia primária verificável do Boletim Diário de Informações da Bovespa correspondente ao pregão de 10/10/1986.

Consequentemente, não foi possível confrontar diretamente as duas linhas COTAHIST com a publicação diária original.

### 3.2 Vigor PP C05

Foi localizada uma publicação contemporânea do Jornal do Brasil, de 05/06/1986, contendo tabela de cotações da Bovespa. A publicação registra explicitamente **Vigor PP C05** e também outras ocorrências de códigos Cxx, como Weg PP C35 e Metal Duque PP C45.

Essa evidência é anterior ao registro-alvo de outubro de 1986 e demonstra que a notação **Vigor PP C05** era efetivamente utilizada em publicação de mercado naquele período.

**FATO VALIDADO:** a combinação Vigor / PP / C05 existia publicamente antes de 10/10/1986.

**NÃO DETERMINADO:** o significado específico do número C05.

Fonte:
https://pt.scribd.com/document/428840555/Jornal-do-Brasil-05-06-1986

### 3.3 Mercado a termo — contexto regulatório de 1986

Foi localizada no Senado Federal a referência oficial ao Decreto-Lei nº 2.286, de 23/07/1986, cuja ementa trata da cobrança de imposto nas operações a termo de bolsas de mercadorias e de outras providências.

A fonte é contemporânea ao período investigado e confirma que operações a termo estavam submetidas a tratamento normativo específico em 1986.

**FATO VALIDADO:** havia regulamentação federal contemporânea específica relacionada a operações a termo em julho de 1986.

**LIMITAÇÃO:** a fonte não explica a regra de gravação/agregação do COTAHIST nem a duplicidade K4 de 10/10/1986.

Fonte:
https://legis.senado.leg.br/norma/527185

## 4. Confronto com o RAW COTAHIST

O FASE 08C já estabeleceu quantitativamente:

- 177.981 registros tipo 01;
- 177.980 grupos K4;
- exatamente 1 grupo K4 duplicado;
- exatamente 2 linhas no grupo duplicado;
- 1 duplicidade no mesmo pregão;
- 0 duplicidades entre pregões;
- grupo duplicado classificado em `CODBDI=62 / TPMERC=030`;
- o grupo duplicado é VGO 2 em 10/10/1986;
- as duas linhas possuem K4 idêntica, mas não são byte-idênticas;
- os agregados de negociação são diferentes.

As duas linhas diferem, entre outros campos, em:

| Campo | Linha 140808 | Linha 140809 |
|---|---:|---:|
| TOTNEG | 1 | 4 |
| QUATOT | 39.000.000 | 190.000.000 |
| VOLTOT | 7.410.000 | 35.646.000 |
| PREAB | 190 | 165 |
| PREMAX | 190 | 191 |
| PREMIN | 190 | 165 |
| PREMED | 190 | 187 |
| PREULT | 190 | 175 |

A igualdade de K4, portanto, **não pode ser tratada como prova de igualdade econômica**.

## 5. Resultado da reconstrução documental

### FATO VALIDADO

1. A colisão K4 existe no RAW de 1986.
2. É a única colisão K4 encontrada em todo o COTAHIST 1986.
3. O evento ocorre em 10/10/1986.
4. As duas linhas pertencem ao mesmo contexto `CODBDI=62 / TPMERC=030`.
5. As duas linhas têm estatísticas de negociação diferentes.
6. A notação histórica Vigor PP C05 já era publicada em junho de 1986.
7. Operações a termo possuíam contexto regulatório específico em 1986.

### PADRÃO OBSERVADO

- O C05 não é uma ocorrência isolada de outubro: já aparece em publicação de junho.
- A convenção Cxx era usada em diversas identificações de papéis nas publicações consultadas.
- A colisão K4, contudo, não se repete em outro grupo de 1986.

### HIPÓTESES AINDA ABERTAS

A documentação disponível não permite escolher entre:

1. regra histórica de agregação/publicação;
2. duas classes de negociação não codificadas integralmente na K4;
3. duplicação/artefato de processamento do arquivo histórico;
4. outra regra operacional/cadastral específica do Mercado a Termo.

Nenhuma dessas hipóteses foi elevada a conclusão.

## 6. Evidência que continua necessária

Para encerrar a semântica da colisão, ainda são prioritários:

1. BDI Bovespa de 10/10/1986;
2. BDI dos pregões imediatamente anterior e posterior;
3. manual/layout operacional Bovespa vigente em 1986;
4. tabela histórica de códigos Cxx;
5. documentação específica do Mercado a Termo de 1986;
6. documentação cadastral que relacione VGO 2 e VGORACPP;
7. definição histórica de DIMES;
8. definição histórica de DATVEN=99991231;
9. regra de publicação que permita ou impeça duas linhas com K4 equivalente.

## 7. Governança

- RAW: **intocado**.
- Linhas 140808 e 140809: **preservadas**.
- Consolidação das linhas: **proibida nesta fase**.
- Correção manual dos valores: **proibida**.
- Inferência de identidade econômica: **não realizada**.
- Inferência do significado de C05: **não realizada**.
- Inferência do motivo da duplicidade: **não realizada**.

## 8. Conclusão da FASE 08D

A reconstrução documental ampliou a evidência histórica, mas **não resolveu a causa da colisão K4**.

A evidência mais importante desta fase é independente do COTAHIST: a publicação de junho de 1986 comprova que **Vigor PP C05** era uma identificação efetivamente utilizada no mercado antes do evento de outubro.

Entretanto, permanece ausente a fonte primária diária de 10/10/1986 e a documentação operacional necessária para explicar por que duas linhas com a mesma K4 apresentam agregados de negociação distintos.

**STATUS:**

- **IMPLEMENTADO:** busca documental direcionada executada.
- **EXECUTADO:** fontes contemporâneas e normativas localizadas e confrontadas.
- **VALIDADO:** existência histórica de Vigor PP C05; existência de contexto regulatório para operações a termo em 1986.
- **NÃO DETERMINADO:** causa da colisão K4.
- **FASE 08:** permanece aberta.

## 9. Próxima frente controlada

**FASE 08E — Reconstrução estatística da cronologia C03/C05/Cxx e DIMES/VGO 2**, usando exclusivamente o COTAHIST 1986 já preservado, para determinar:

- primeira ocorrência de cada ESPECI do VGORACPP;
- última ocorrência;
- transições por pregão;
- relação ESPECI × DIMES;
- relação ESPECI × TPMERC × PRAZOT;
- ocorrência de C05 fora de VGO 2;
- ocorrência de outros Cxx dentro do mesmo CODISI;
- eventual mudança estrutural próxima de 10/10/1986.

A FASE 08E deverá produzir evidência quantitativa antes de qualquer nova hipótese semântica.
