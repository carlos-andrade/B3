# FASE 08Y — COTAHIST 1986 — RECONSTRUÇÃO DO MECANISMO DE PUBLICAÇÃO DO BDI

**Arquivo:** FASE08Y_COTAHIST_1986_RECONSTRUCAO_PUBLICACAO_BDI_TIPO_PRAZO_CXX_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Relação histórica entre Tipo, Prazo e códigos Cxx  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Reconstruir, por evidência histórica publicada, como o mercado a termo apresentava Tipo, Prazo, quantidade, preços e número de negócios, e testar se essa estrutura ajuda a explicar a colisão K4 de 10/10/1986.

## 2. Registro-alvo

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Linhas RAW: 140808 e 140809. RAW SHA-256: `350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018`.

## 3. Evidência contemporânea

A publicação do Jornal do Brasil de 05/06/1986 reproduz dados da Bovespa. Ela apresenta uma seção **Mercados a Vista** e, separadamente, uma seção **Mercado a Termo**.

Na seção Mercado a Termo, o cabeçalho recuperado é:

**Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°**

A mesma publicação contém, na identificação dos papéis em outra tabela, ocorrências como `Vigor PP C05`, `Weg PP C35`, `Met Duque PP C45` e `Brahma OP C15`. citeturn3view0turn4view0turn5view0

## 4. Resultado estrutural

### 4.1 Tipo e Prazo são dimensões distintas

A própria tabela histórica do Mercado a Termo publica explicitamente as colunas **Tipo** e **Prazo**. Portanto, Tipo não deve ser convertido em Prazo.

### 4.2 Cxx não pode ser tratado automaticamente como Tipo

Na mesma publicação, `C05`, `C35`, `C45` e `C15` aparecem associados à identificação de papéis em outra área de cotações, enquanto a tabela do Mercado a Termo possui uma coluna explicitamente chamada **Tipo**.

Isso sustenta estruturalmente:

**C05 ≠ Tipo**, como equivalência automática.

A evidência não decodifica o significado histórico de C05.

### 4.3 Cxx também não é Prazo

O prazo aparece como dimensão própria na tabela do Mercado a Termo. Logo:

**C05 ≠ Prazo**.

## 5. Relação com a colisão K4

As duas linhas-alvo possuem a mesma combinação estrutural:

`CODBDI 62 | CODNEG VGO 2 | TPMERC 030 | ESPECI PP *C05 | PRAZOT 060`

A publicação histórica demonstra que existia uma dimensão chamada Tipo, mas essa dimensão não está presente na K4 usada para detectar a colisão.

Isso mantém abertas duas possibilidades:

1. dimensão operacional/publicacional adicional não preservada na K4;
2. regra histórica de agregação/publicação que permitia mais de uma linha para a mesma combinação estrutural do COTAHIST.

Não há evidência suficiente para escolher entre elas.

## 6. Teste da hipótese “dois Tipos diferentes”

Não foi recuperado o BDI de 10/10/1986. Portanto, não é possível atribuir as linhas RAW 140808 e 140809 a dois Tipos diferentes.

Para provar essa hipótese seriam necessários: exemplar do BDI de 10/10/1986, leitura das duas linhas Vigor, identificação do Tipo de cada linha e correspondência inequívoca com cada registro RAW.

Esses elementos permanecem como **EVIDÊNCIA AUSENTE**.

## 7. Controle da janela 09/10–13/10/1986

A FASE 08P já estabeleceu no RAW:

| Data | Linhas a termo VGO 2 | Prazo | ESPECI | DIMES |
|---|---:|---:|---|---:|
| 09/10/1986 | 1 | 060 | PP *C05 | 104 |
| 10/10/1986 | 2 | 060 | PP *C05 | 104 |
| 13/10/1986 | 1 | 060 | PP *C05 | 104 |

A sequência `1 → 2 → 1` é fato estatístico do arquivo. Ela não prova diferença de Tipo nem erro de processamento.

## 8. Estado das hipóteses

| Questão | Estado |
|---|---|
| Diferença de Prazo explica a colisão | **REFUTADA** |
| C05 surgiu no dia da colisão | **REFUTADA** |
| C05 = Prazo | **REFUTADA** |
| C05 = Tipo | **NÃO DEMONSTRADO / NÃO INFERIR** |
| Tipo e Prazo são dimensões distintas | **DOCUMENTADO** |
| Cxx aparece na identificação histórica dos papéis | **DOCUMENTADO** |
| Tipo separado de Cxx na publicação contemporânea | **DOCUMENTADO ESTRUTURALMENTE** |
| Tipo diferente nas linhas 140808/140809 | **EVIDÊNCIA AUSENTE** |
| Dimensão operacional não preservada na K4 | **POSSÍVEL, NÃO PROVADO** |
| Regra histórica de agregação/publicação | **HIPÓTESE PRINCIPAL** |
| Erro de processamento | **NÃO CONFIRMADO** |
| Causa da colisão | **NÃO RESOLVIDA** |

## 9. Conclusão

A FASE 08Y produz um avanço documental delimitado: a publicação contemporânea de 1986 mostra **Tipo** e **Prazo** como dimensões distintas e mostra **Cxx** na identificação histórica dos papéis em outra tabela/seção.

Isso elimina uma interpretação estrutural indevida: **C05 não pode ser usado como sinônimo automático de Tipo ou de Prazo**.

Entretanto, a evidência não recupera o BDI de 10/10/1986 e não permite atribuir as duas linhas RAW a dois Tipos diferentes.

A hipótese principal permanece: **regra histórica de agregação/publicação ou dimensão operacional não representada na chave K4**.

## 10. Governança

- RAW intocado.
- Linhas 140808 e 140809 preservadas.
- C05, VGO 2, DIMES 104 e DATVEN 99991231 preservados literalmente.
- Nenhuma linha eliminada ou consolidada.
- Nenhuma identidade econômica inferida.
- Nenhuma causalidade atribuída a Tipo.
- Nenhuma equivalência moderna retroprojetada para 1986.

## 11. Próxima frente

Prioridade: BDI de 10/10/1986; BDI de 09/10 e 13/10; documentação Bovespa contemporânea sobre Tipo; legenda dos códigos Cxx; regra técnica de transformação do boletim para o arquivo histórico; exemplos em que o mesmo título aparece mais de uma vez no Mercado a Termo no mesmo pregão.

**Status:** IMPLEMENTADO / EXECUTADO / VALIDADO quanto à separação documental Tipo × Prazo e à presença histórica de Cxx.

**EVIDÊNCIA AUSENTE:** BDI primário de 10/10/1986 e identificação dos Tipos das duas linhas Vigor.

**NÃO RESOLVIDO:** causa histórica da colisão K4.
