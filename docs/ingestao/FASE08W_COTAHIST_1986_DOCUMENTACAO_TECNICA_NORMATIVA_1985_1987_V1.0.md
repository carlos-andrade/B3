# FASE 08W — Documentação Técnica e Normativa Bovespa 1985–1987

**Arquivo:** FASE08W_COTAHIST_1986_DOCUMENTACAO_TECNICA_NORMATIVA_1985_1987_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Busca de documentação contemporânea sobre Mercado a Termo, códigos, boletins e regras de publicação/agregação  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

A FASE 08W foi definida para procurar documentação técnica/normativa Bovespa do período 1985–1987 capaz de:

1. decodificar os códigos históricos de Tipo;
2. esclarecer a notação C05;
3. identificar dimensões operacionais do Mercado a Termo;
4. estabelecer como as operações eram agregadas para divulgação;
5. relacionar essas regras ao BDI e à estrutura posteriormente preservada no COTAHIST;
6. testar a hipótese de que uma dimensão operacional não foi preservada na chave K4.

## 2. Registro-alvo

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Linhas RAW: **140808 e 140809**.

RAW SHA-256:

`350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018`

RAW permanece intocado.

## 3. Fontes normativas contemporâneas localizadas

### 3.1 Instrução CVM nº 36/1984

A CVM mantém a redação original da Instrução CVM nº 36, publicada em agosto de 1984, que tratava dos mercados a futuro, a termo e de opções.

A norma determina que as Bolsas que operassem nesses mercados mantivessem sistemas de controle para verificar diariamente o grau de concentração dos investidores e que os levantamentos e controles ficassem à disposição da CVM.

Isso demonstra que, antes do evento de 1986, existiam controles operacionais diários específicos sobre esses mercados.

**Limitação:** a Instrução CVM 36 não apresenta, nas partes recuperadas, a legenda dos códigos C05/Tipo nem a regra de agregação do COTAHIST.

Fonte: CVM — Instrução CVM 36, redação original.

## 4. Normas de 1986 relacionadas a financiamento e operações

### 4.1 Instrução CVM nº 51/1986

A Instrução CVM nº 51 foi publicada em 09/06/1986 e trata de operações de Conta Margem e outras matérias relacionadas a financiamento/empréstimo de ações.

A redação disponível contém obrigação de publicação, nos boletins das Bolsas, de informações agregadas sobre compras em margem, especificando quantidade, volume e número de negócios por ação.

Essa evidência é relevante porque confirma que, em 1986, o boletim da Bolsa era utilizado como veículo formal de divulgação de estatísticas operacionais.

**Limitação crítica:** o dispositivo localizado trata de conta margem, não estabelece a regra de agregação das operações a termo do registro VGO 2 e não decodifica C05/Tipo.

Fonte: CVM — Instrução CVM 51, redação original/consolidada.

## 5. Decreto-Lei nº 2.286/1986

O Decreto-Lei nº 2.286, de 23/07/1986, atribuiu ao CMN competência para regulamentar mercados a termo e atividades das entidades que os administravam e de seus participantes, inclusive contratos e operações.

Isso confirma que outubro de 1986 estava dentro de um ambiente regulatório específico para mercados de liquidação futura.

**Limitação:** a norma não fornece a estrutura de campos do COTAHIST nem a regra de publicação que explique a colisão K4.

## 6. Pesquisa específica por documentação Bovespa 1985–1987

Foram pesquisadas combinações envolvendo:

- Bovespa;
- Mercado a Termo;
- Operações a Termo;
- 1985, 1986 e 1987;
- Tipo;
- Prazo;
- C05;
- Vigor;
- PP-G;
- PB-G;
- PP-H;
- Boletim Diário de Informações;
- COTAHIST;
- manual de procedimentos;
- codificação.

### Resultado

Não foi localizado, em fonte pública indexada e verificável, um **manual Bovespa contemporâneo de 1985–1987** que forneça simultaneamente:

- legenda dos códigos históricos Tipo;
- legenda de C05;
- regra de agregação da tabela Mercado a Termo;
- correspondência direta com os campos do COTAHIST de 1986.

Portanto, a FASE 08W não pode declarar que encontrou a documentação técnica decisiva.

Classificação: **EVIDÊNCIA AUSENTE**.

## 7. Documentação posterior usada somente como controle

Foi localizada documentação Bovespa posterior contendo capítulo específico sobre Mercado a Termo. Ela mostra que, em período posterior, existiam dimensões distintas envolvendo tipo de termo, prazo, comitente, participante, comprador/vendedor e taxa, e que informações de taxas mínima, máxima e média podiam ser divulgadas no BDI.

Essa documentação é útil para demonstrar que o processo operacional de mercado a termo possui múltiplas dimensões, mas **não pode ser retroprojetada como regra de 1986 sem fonte contemporânea**.

Fonte posterior: Manual de Procedimentos Operacionais do Segmento Bovespa.

## 8. Resultado para a hipótese da dimensão oculta

A documentação normativa permite estabelecer um ponto importante:

**o processo institucional do mercado a termo possuía controles e dimensões operacionais além de preço e prazo.**

Entretanto, isso ainda não demonstra que uma dessas dimensões tenha sido removida da chave K4 de 1986.

Não foi localizada evidência que permita afirmar:

- C05 = Tipo;
- C05 = taxa;
- C05 = comprador;
- C05 = vendedor;
- C05 = corretora;
- C05 = comitente;
- Tipo = qualquer uma dessas dimensões;
- a duplicidade de 10/10/1986 decorre de uma dessas dimensões.

## 9. Confronto com os dados observados

A FASE 08P já estabeleceu:

| Data | Linhas VGO 2 termo 060 |
|---|---:|
| 09/10/1986 | 1 |
| 10/10/1986 | 2 |
| 13/10/1986 | 1 |

Todas as linhas do período utilizam:

- ESPECI = `PP *C05`;
- DIMES = `104`;
- PRAZOT = `060`.

A colisão de 10/10/1986 continua sendo a única duplicidade K4 identificada no universo COTAHIST 1986–2026 analisado.

A documentação normativa pesquisada não fornece, até aqui, o campo ausente que diferencie as duas linhas.

## 10. Matriz de hipóteses após 08W

| Hipótese | Estado |
|---|---|
| Existe contexto regulatório específico para operações a termo em 1984–1986 | **CONFIRMADO** |
| Bolsas mantinham controles operacionais diários | **CONFIRMADO** |
| BDI/boletins eram veículo formal de divulgação de informações operacionais | **CONFIRMADO** |
| C05 = Tipo | **NÃO DEMONSTRADO** |
| Tipo = comprador/vendedor | **NÃO DEMONSTRADO** |
| Tipo = corretora/comitente | **NÃO DEMONSTRADO** |
| C05 = taxa | **NÃO DEMONSTRADO** |
| Dimensão operacional adicional existia no mercado | **COMPATÍVEL COM AS FONTES**, mas sem ligação com a colisão |
| Dimensão operacional adicional explica 140808/140809 | **NÃO PROVADO** |
| Regra histórica de agregação explica a colisão | **HIPÓTESE PRINCIPAL** |
| Erro de processamento | **NÃO CONFIRMADO** |

## 11. Conclusão

A FASE 08W avançou a investigação normativa, mas **não encontrou a peça documental decisiva**.

O que foi fortalecido:

1. o Mercado a Termo estava sujeito a controles operacionais formais antes e durante 1986;
2. havia obrigação/regime de divulgação de determinadas informações em boletins das Bolsas;
3. o mercado possuía dimensões operacionais além de preço e prazo;
4. isso mantém plausível a hipótese de que o processo de publicação/agregação utilizasse informação que não aparece na K4.

O que permanece sem prova:

1. qual era a legenda histórica de Tipo;
2. o significado de C05;
3. qual dimensão diferenciava as duas linhas 140808/140809;
4. qual regra de agregação produziu duas linhas com K4 idêntica;
5. se a duplicidade representa duas classes operacionais, dois agregados, ou outra regra histórica.

## 12. Governança

- RAW intocado.
- Linhas 140808/140809 preservadas.
- C05 literal.
- VGO 2 literal.
- DIMES 104 literal.
- Nenhuma consolidação.
- Nenhuma exclusão.
- Nenhuma identidade econômica inferida.
- Nenhuma regra posterior foi retroprojetada como regra de 1986.

## 13. Próxima frente

A FASE 08W indica que a busca em legislação geral também atingiu o limite de valor probatório.

A próxima prioridade deve ser **documentação operacional primária da própria Bovespa**, especialmente:

1. manuais internos ou circulares de 1985–1987;
2. tabelas de códigos de negociação;
3. documentação do cadastro de papéis;
4. documentação do BDI;
5. especificação de arquivos históricos;
6. exemplares físicos/digitalizados do BDI de 09, 10 e 13/10/1986;
7. registros do Centro de Memória/MUB3 que permitam identificar esses objetos.

## 14. Estado

**IMPLEMENTADO:** FASE 08W documentada.

**EXECUTADO:** busca normativa e técnica dirigida ao período 1985–1987.

**VALIDADO:** existência de controles formais do mercado a termo e de mecanismos de divulgação em boletins no período; ausência, nas fontes públicas recuperadas, de manual contemporâneo suficiente para explicar a colisão.

**EVIDÊNCIA AUSENTE:** legenda primária de Tipo/C05 e regra de agregação Bovespa de 1986.

**NÃO RESOLVIDO:** causa da colisão K4.

**FASE 08:** ABERTA.
