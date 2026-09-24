# FASE 08I — Reconstrução da Regra de Agregação da Colisão K4

**Arquivo:** FASE08I_COTAHIST_1986_RECONSTRUCAO_REGRA_AGREGACAO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconstrução estrutural da regra de publicação/agregação da colisão K4 de 10/10/1986  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Depois das FASES 08C–08H, a questão deixou de ser se a colisão K4 se repete. Ela não se repete no universo anual analisado.

A FASE 08I testa outra pergunta:

> **Qual dimensão estrutural normalmente separa múltiplas linhas do Mercado a Termo para o mesmo ativo no mesmo pregão, e por que essa dimensão não aparece na colisão VGO 2 de 10/10/1986?**

## 2. Universo

RAW:

`dados/cotahist/raw/anual/COTAHIST_A1986.ZIP`

SHA-256:

`350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018`

Registros tipo 01:

**177.981**

Nenhum RAW foi alterado.

## 3. Resultado estrutural

A análise encontrou:

- **5.181** combinações DATA + CODNEG com múltiplas linhas no Mercado a Termo;
- nessas situações, as linhas normalmente se separam por algum campo estrutural da K4;
- exemplos recorrentes mostram PRAZOT 030 versus 060 como dimensão separadora;
- a busca específica por múltiplas linhas no mesmo pregão, mesmo ativo e mesmo conjunto estrutural da K4, mas com estatísticas diferentes, encontrou **exatamente 1 caso**;
- esse único caso é a colisão VGO 2 de 10/10/1986.

Portanto, a evidência quantitativa reforça a singularidade estrutural já identificada nas fases anteriores.

## 4. Evidência da colisão

K4:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

### Linha 140808

- TOTNEG = 1
- QUATOT = 39.000.000
- VOLTOT = 7.410.000
- PREAB = 1,90
- PREMAX = 1,90
- PREMIN = 1,90
- PREMED = 1,90
- PREULT = 1,90
- FATCOT = 1.000

### Linha 140809

- TOTNEG = 4
- QUATOT = 190.000.000
- VOLTOT = 35.646.000
- PREAB = 1,65
- PREMAX = 1,91
- PREMIN = 1,65
- PREMED = 1,87
- PREULT = 1,75
- FATCOT = 1.000

Todos os campos da K4 permanecem iguais.

## 5. Comparação com o mesmo pregão

No próprio dia 10/10/1986, VGO 2 possui:

1. uma linha à vista — CODBDI 02 / TPMERC 010;
2. duas linhas a termo — CODBDI 62 / TPMERC 030.

A linha à vista possui:

- PREAB 1,55;
- PREMAX 1,80;
- PREMIN 1,55;
- PREMED 1,75;
- PREULT 1,70;
- TOTNEG 14;
- QUATOT 267.200.000;
- VOLTOT 46.995.000.

A existência da linha à vista não explica a duplicidade a termo, porque os mercados estão separados por CODBDI/TPMERC.

## 6. O que normalmente separa linhas a termo

A análise de 1986 encontrou **5.181** combinações de ativo/pregão com mais de uma linha no mercado a termo.

Um padrão recorrente é:

`PRAZOT = 030`

versus

`PRAZOT = 060`

Por exemplo, o arquivo contém pares como CNF 2, AZE 2, REP 2, WHM 1 e vários outros nos quais as linhas possuem o mesmo ativo, mas prazos diferentes.

Isso demonstra que o COTAHIST possui dimensões estruturais suficientes para separar diferentes agregações quando o prazo é diferente.

No caso VGO 2 de 10/10/1986, entretanto:

`PRAZOT = 060`

nas duas linhas.

Também são iguais:

- CODBDI;
- TPMERC;
- CODNEG;
- CODISI;
- DIMES;
- ESPECI;
- DATVEN;
- PREEXE;
- INDOPC;
- PTOEXE.

## 7. Nova conclusão técnica

### FATO

No universo COTAHIST 1986, múltiplas linhas do Mercado a Termo para o mesmo ativo são comuns quando existe alguma diferença estrutural entre elas.

### FATO

A colisão VGO 2 de 10/10/1986 é diferente: as duas linhas possuem a mesma K4 completa.

### FATO

A busca específica por esse padrão encontrou somente uma ocorrência em 1986.

### HIPÓTESE MAIS FORTE

A evidência passa a ser compatível com duas possibilidades principais:

**H1 — dimensão operacional ausente da K4:** existia alguma dimensão de negociação/publicação que não foi preservada nos campos utilizados para a K4.

**H2 — regra de agregação/publicação:** o processo histórico de geração do COTAHIST permitiu que dois agregados estatísticos fossem publicados sob a mesma identidade estrutural.

H1 e H2 continuam sendo hipóteses.

## 8. Hipótese de taxa de termo

Uma possibilidade específica é que a dimensão ausente esteja relacionada à **taxa/preço econômico da operação a termo**.

Essa hipótese ganhou plausibilidade estrutural porque:

- operações a termo envolvem preço contratado e prazo;
- fontes educacionais posteriores descrevem o preço a termo como preço à vista acrescido de componente relacionado à taxa; citeturn5search1
- publicações Bovespa modernas possuem tabelas específicas de taxas negociadas no Mercado a Termo por prazo. citeturn5search39

**Mas isso NÃO prova que a taxa seja a dimensão ausente em 1986.**

Não foi encontrada fonte contemporânea de 1986 que demonstre que a taxa de termo era utilizada como chave de agregação do arquivo histórico.

Portanto:

**TAXA DE TERMO = HIPÓTESE, NÃO FATO.**

## 9. Contexto regulatório

O Decreto-Lei nº 2.286, de 23/07/1986, determinou tratamento tributário para operações a termo e atribuiu ao Conselho Monetário Nacional competência para regulamentar os mercados, entidades administradoras, participantes, contratos e operações. citeturn4search0turn4search1

Isso confirma que o mercado a termo possuía estrutura normativa própria em 1986.

Contudo, o Decreto-Lei não define a regra de agregação do COTAHIST e, portanto, não resolve a colisão.

## 10. C05

A publicação contemporânea do Jornal do Brasil de 05/06/1986 mostra **Vigor PP C05** e diversas outras identificações Cxx. citeturn5search0

Isso estabelece que C05 era uma convenção efetivamente publicada no mercado naquele período.

Ainda não foi encontrada uma legenda primária contemporânea capaz de afirmar que C05 significava exatamente determinada série, direito, evento ou categoria.

Logo:

**C05 = convenção histórica comprovada; significado exato = NÃO DETERMINADO.**

## 11. Resultado da reconstrução

A FASE 08I elimina uma explicação simples:

> **a duplicidade não pode ser explicada apenas pela existência de múltiplos prazos ou por uma mudança cadastral no pregão de 10/10/1986.**

Os campos que normalmente distinguem agregações a termo estão iguais.

A investigação agora aponta para uma **dimensão não observada na K4 ou para uma regra histórica de publicação/agregação**, sem que seja possível ainda identificar qual delas.

## 12. O que ainda falta para fechar a causa

Prioridade máxima:

1. BDI Bovespa de 10/10/1986;
2. BDI de 09/10/1986 e 13/10/1986;
3. manual/regulamento operacional Bovespa do Mercado a Termo vigente em outubro de 1986;
4. tabela histórica dos códigos Cxx;
5. documentação de geração/arquivamento das séries históricas;
6. documentação histórica sobre taxa de termo e forma de publicação das operações;
7. documentação que explique DATVEN = 99991231;
8. documentação que explique DIMES = 104.

## 13. Governança

- RAW: **INTACTO**
- linhas 140808/140809: **PRESERVADAS**
- consolidação: **NÃO REALIZADA**
- correção manual: **NÃO REALIZADA**
- identidade econômica: **NÃO INFERIDA**
- causa histórica: **NÃO DECLARADA COMO RESOLVIDA**

## 14. Artefatos

Parser:

`scripts/ingestao/analisar_reconstrucao_regra_agregacao_k4_cotahist_1986_v1.py`

Commit:

`1a56180dd92bf5ea3a1fec322135f3d61703b29e`

Workflow:

`.github/workflows/cotahist-fase08i-reconstrucao-regra-agregacao-1986-v1.yml`

Commit:

`9359c44788c5cbddef071907906e9de7d8088545`

Evidência:

`dados/cotahist/quality/COTAHIST_1986_FASE08I_RECONSTRUCAO_REGRA_AGREGACAO_V1.json`

## 15. Status

**IMPLEMENTADO:** análise estrutural criada.

**EXECUTADO:** 177.981 registros tipo 01 analisados.

**VALIDADO:** 5.181 combinações DATA + CODNEG com múltiplas linhas a termo; somente 1 colisão mantém K4 completa idêntica com estatísticas diferentes.

**HIPÓTESE ATUAL:** dimensão operacional/negocial não preservada na K4 ou regra de agregação/publicação.

**NÃO RESOLVIDO:** qual é exatamente essa dimensão/regra.

## 16. Próxima frente

A investigação deve avançar para **FASE 08J — reconstrução documental primária do Mercado a Termo Bovespa em outubro de 1986**, com foco específico em:

- regras de registro;
- taxa;
- prazo;
- vencimento;
- forma de publicação diária;
- códigos Cxx;
- identificação de séries/direitos;
- e estrutura do Boletim Diário de Informações.

A hipótese de taxa deverá ser testada documentalmente, não assumida.
