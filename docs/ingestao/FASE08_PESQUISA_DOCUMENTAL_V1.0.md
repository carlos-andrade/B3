# FASE 08 — Pesquisa Documental Histórica — COTAHIST 1986

**Arquivo:** FASE08_PESQUISA_DOCUMENTAL_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Pesquisa documental da colisão K4 de 10/10/1986  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Investigar fontes contemporâneas capazes de explicar:

1. a convenção histórica VGO 2;
2. o código C05 em ESPECI = PP *C05;
3. DATVEN = 99991231;
4. a coexistência de duas linhas com K4 idêntica e agregados de negociação diferentes;
5. a semântica histórica do mercado a termo no registro-alvo.

## 2. Registro-alvo

19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0

Linhas RAW: 140808 e 140809.

## 3. Evidência documental localizada

### 3.1 Jornal do Brasil — 05/06/1986

Foi localizada uma publicação contemporânea de 05/06/1986 contendo tabela de cotações da Bovespa. A tabela registra Vigor PP C05 e apresenta outras ocorrências do padrão Cxx, como Weg PP C35, Metal Duque PP C45 e Brahma OP C15.

A evidência demonstra que a identificação Vigor PP C05 existia publicamente antes do registro-alvo de outubro de 1986 e que a notação Cxx era usada para múltiplos papéis.

A fonte não apresenta legenda suficiente para decodificar o número 05.

## 4. O que a pesquisa não resolveu

Continuam sem documentação primária suficiente:

- legenda oficial contemporânea para C05;
- significado completo de VGO 2;
- significado histórico de DIMES 104;
- significado de DATVEN = 99991231;
- regra documental explicando duas linhas com K4 idêntica e agregados diferentes;
- legenda dos códigos históricos de Tipo;
- relação entre Tipo e a colisão K4.

## 5. Semântica atualmente sustentada

| Elemento | Estado |
|---|---|
| CODBDI 62 | Mercado a termo — documentado pelo layout B3 |
| TPMERC 030 | Termo — documentado pelo layout B3 |
| PRAZOT 060 | Campo de prazo do termo; valor 60 — documentado |
| VGO 2 | Código histórico observado; sem decodificação completa |
| VGORACPP | Código interno histórico observado |
| DIMES 104 | Campo de distribuição/estado de direito; sem reconstrução histórica completa |
| PP C05 | Convenção histórica comprovada; significado do C05 não resolvido |
| DATVEN 99991231 | Placeholder aparente; sem definição histórica comprovada |
| duplicidade K4 | fato RAW comprovado; causa não determinada |
| Tipo histórico | dimensão publicada separadamente de Prazo; legenda de 1986 não recuperada |

## 6. Regra de evidência

Não será feita nenhuma transformação de C05, VGO 2, Tipo ou DATVEN com base apenas em analogia moderna.

A colisão permanecerá preservada no RAW e será tratada como evento histórico observável até existir documentação primária suficiente.

## 7. Fases estatísticas e documentais já concluídas

### 7.1 FASE 08H — Recorrência multianual

Foram analisados 41 anos, de 1986 a 2026, totalizando 24.314.082 registros tipo 01.

Resultado:

- 24.314.081 grupos K4;
- 1 único grupo K4 duplicado;
- 2 linhas no grupo duplicado;
- 1 único grupo com estatísticas diferentes;
- somente 1986 apresentou colisão K4.

A colisão é, portanto, única no universo analisado, mas isso não determina sua causa histórica.

### 7.2 FASE 08K — Arqueologia do BDI/COTAHIST

A publicação contemporânea de 05/06/1986 preserva a estrutura pública:

**Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°**

Ela registra Vigor PP C05.

Conclusão: Tipo e Prazo são dimensões distintas; C05 não deve ser convertido automaticamente em Tipo.

### 7.3 FASE 08L–08N — Dimensões históricas

As fases 08L, 08M e 08N confirmaram a existência documental de uma dimensão Tipo e de códigos históricos como PP-G/PB-G/PP-H em publicações posteriores, mas não localizaram legenda primária suficiente para atribuir esses códigos a comprador, vendedor, corretora, comitente ou taxa.

## 8. FASE 08O — Busca da legenda primária dos códigos de Tipo

A FASE 08O foi executada em 25/09/2026 com busca dirigida a:

1. manuais/regulamentos Bovespa de 1985–1987;
2. tabelas de códigos;
3. especificações do Mercado a Termo;
4. circulares e documentação normativa;
5. BDI de 09/10, 10/10 e 13/10/1986;
6. ocorrências de Vigor nos pregões próximos.

### 8.1 Resultado

Não foi localizada uma legenda primária contemporânea suficiente para decodificar os códigos históricos de Tipo.

Também não foi localizada cópia pública verificável dos BDI de 09/10, 10/10 ou 13/10/1986.

A evidência contemporânea do Jornal do Brasil continua demonstrando a estrutura **Tipo × Prazo** e a ocorrência de **Vigor PP C05**, mas não fornece a legenda do Tipo nem do C05.

### 8.2 O que foi descartado

Não foi aceita como fato nenhuma das seguintes equivalências:

- Tipo = comprador;
- Tipo = vendedor;
- Tipo = corretora/participante;
- Tipo = comitente;
- Tipo = taxa;
- C05 = Tipo;
- Tipo = Prazo.

As quatro primeiras permanecem hipóteses documentais possíveis; as duas últimas equivalências não são sustentadas pela evidência localizada.

### 8.3 Impacto na colisão

A FASE 08O mantém aberta a possibilidade de uma dimensão operacional adicional não preservada na K4, mas não demonstra que a coluna Tipo seja essa dimensão nem que ela explique as linhas RAW 140808/140809.

A hipótese principal continua sendo:

**regra histórica de agregação/publicação ou dimensão operacional não representada na K4.**

O processamento como erro permanece não confirmado.

Documento detalhado:

`docs/ingestao/FASE08O_COTAHIST_1986_LEGENDA_PRIMARIA_TIPO_V1.0.md`

Commit: `c1e9b1c1ee7d2104e22765bb6c3ce7e1b72ca224`.

## 9. Governança

- RAW permanece intocado.
- Linhas 140808 e 140809 permanecem preservadas.
- C05 permanece literal.
- VGO 2 permanece literal.
- DIMES 104 permanece literal.
- DATVEN 99991231 permanece literal.
- Nenhuma consolidação estatística é realizada.
- Nenhuma identidade econômica é inferida.
- Nenhuma causalidade é atribuída à coluna Tipo.

## 10. Próxima frente controlada

A investigação deve avançar em duas linhas:

### A — Arquivos institucionais

Buscar acervos físicos/digitalizados de Bovespa/B3, CVM, Biblioteca Nacional, Senado/Diário Oficial, FGV, universidades e jornais que reproduzam o BDI integral.

### B — Reconstrução interna no COTAHIST

Testar, com dados já preservados:

1. Vigor em 09/10, 10/10 e 13/10/1986;
2. múltiplas linhas do mesmo título com diferentes classes publicadas;
3. relação PRAZOT × ESPECI × DIMES × estatísticas;
4. padrões que permitam falsificar a hipótese de agregação.

## 11. Estado

**IMPLEMENTADO:** FASE 08O executada e documentada.

**EXECUTADO:** busca dirigida por legenda primária e BDI próximo ao evento.

**VALIDADO:** ausência de legenda primária suficiente nas fontes públicas recuperadas; existência histórica de Tipo separado de Prazo; existência de Vigor PP C05 antes de outubro de 1986.

**NÃO RESOLVIDO:** legenda dos códigos históricos e relação causal com a colisão K4.

**FASE 08:** ABERTA — investigação histórica continua.
