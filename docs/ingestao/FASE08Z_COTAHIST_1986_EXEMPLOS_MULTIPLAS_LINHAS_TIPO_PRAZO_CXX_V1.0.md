# FASE 08Z — COTAHIST 1986 — EXEMPLOS HISTÓRICOS DE MÚLTIPLAS LINHAS: TIPO × PRAZO × CXX

**Arquivo:** FASE08Z_COTAHIST_1986_EXEMPLOS_MULTIPLAS_LINHAS_TIPO_PRAZO_CXX_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Teste documental de múltiplas linhas do mesmo emissor/título e dimensões publicadas  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

A FASE 08Z procura encontrar exemplos históricos em que um mesmo emissor ou família de título aparece em mais de uma linha do Mercado a Termo, verificando se **Tipo** pode separar linhas com o mesmo **Prazo**.

O objetivo é testar a hipótese de que uma dimensão publicacional não preservada na K4 poderia ser Tipo. A fase não pode, porém, atribuir Tipo às linhas RAW 140808/140809 sem o BDI de 10/10/1986.

## 2. Registro-alvo

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060`

Linhas RAW: 140808 e 140809. RAW SHA-256 preservado:

`350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018`

## 3. Evidência contemporânea — Jornal do Brasil, 05/06/1986

A reprodução histórica da Bovespa apresenta a seção **Mercado a Termo** com as colunas:

**Tipo | Prazo | Quant | Fech | Máx | Min | Méd | N°**

A tabela contém exemplos particularmente úteis para esta fase.

### 3.1 Mendes Júnior: múltiplas séries com o mesmo prazo

Na mesma publicação aparecem, no Mercado a Termo:

- `Mendes Júnior PA 030`
- `Mendes Júnior PB 030`
- `Mendes Júnior PP 030`

Os três registros apresentam **PRAZO 030**, mas possuem **Tipo distinto: PA, PB e PP**. A publicação mostra estatísticas separadas para cada linha. citeturn5view0

Isso é evidência direta de que, historicamente, **Tipo podia funcionar como dimensão de separação de linhas mesmo quando o Prazo era igual**.

Importante: isso não significa que PA/PB/PP sejam decodificados aqui como comprador, vendedor, corretora ou outra entidade. O fato utilizado é exclusivamente estrutural: a publicação separa os registros por Tipo.

### 3.2 Eluma: múltiplas codificações com prazo 030

A mesma publicação apresenta linhas como:

- `Eluma PP C-030`
- `Eluma PP E--030`

ambas no bloco do Mercado a Termo e com prazo 030. citeturn5view0

Isso reforça que a representação histórica podia carregar mais de uma dimensão textual/classificatória além do prazo.

### 3.3 Outros exemplos de Tipo × Prazo

A publicação também mostra numerosos registros com `PP 030`, `PB 030`, `PA 030`, além de códigos compostos como `C-030` e `E--030`. citeturn5view0

## 4. Evidência posterior de controle — 27/12/1988

Uma publicação de 27/12/1988 apresenta a tabela **Operações a Termo** com as colunas:

**Títulos | Tipo | Prazo | Quant. | Fech. | Máx. | Min. | Méd. | Volume | Nº neg.**

Exemplos recuperados:

- `B.brasil | PP-Q | 030`
- `Mendes Júnior | PB-Q | 030`
- `Sharp | PB-Q | 030`

A estrutura confirma a persistência documental da separação entre **Título**, **Tipo** e **Prazo** em publicação posterior. citeturn2search30

Essa fonte é usada apenas como controle estrutural posterior; não é retroprojetada como regra específica de 1986.

## 5. O que 08Z demonstra

A FASE 08Z muda o estado de uma hipótese importante.

Antes, a possibilidade de Tipo como dimensão operacional adicional era apenas plausível.

Agora existe evidência contemporânea de 1986 de que:

**mesmo emissor/família de título + mesmo prazo + Tipo diferente → linhas estatísticas separadas.**

O exemplo mais claro é:

`Mendes Júnior PA 030`
`Mendes Júnior PB 030`
`Mendes Júnior PP 030`

Portanto, **Tipo é uma dimensão historicamente capaz de produzir multiplicidade de linhas sem mudança do prazo**.

## 6. O que 08Z NÃO demonstra

Ainda não podemos afirmar:

- que C05 seja o Tipo das linhas Vigor;
- que as linhas 140808 e 140809 tenham Tipos diferentes;
- que Tipo seja a causa da colisão K4;
- que a regra de publicação de 10/10/1986 seja idêntica à observada em 05/06/1986;
- que os códigos PA/PB/PP tenham significado econômico específico sem legenda primária.

A evidência decisiva continua sendo o BDI de 10/10/1986 ou documentação técnica contemporânea que permita mapear as linhas RAW para a publicação.

## 7. Relação com a colisão K4

A colisão possui:

`CODBDI 62 | VGO 2 | TPMERC 030 | VGORACPP | DIMES 104 | PP *C05 | PRAZOT 060`

As duas linhas têm K4 idêntica.

A FASE 08Z demonstra que **Tipo é uma dimensão histórica real e pode separar linhas com o mesmo prazo**. Como Tipo não está representado na K4 investigada, a hipótese de uma dimensão publicacional omitida na chave ganha suporte documental adicional.

Mas permanece uma lacuna fundamental:

> não sabemos se as duas linhas Vigor de 10/10/1986 possuíam Tipos diferentes.

Assim, Tipo passa de **“possível”** para **“dimensão historicamente demonstrada como capaz de separar linhas”**, mas sua relação causal com a colisão continua **NÃO PROVADA**.

## 8. Estado das hipóteses após 08Z

| Questão | Estado |
|---|---|
| Diferença de Prazo explica a colisão | **REFUTADA** |
| C05 = Prazo | **REFUTADA** |
| C05 = Tipo | **NÃO DEMONSTRADO** |
| Tipo existe como dimensão publicada | **DOCUMENTADO** |
| Tipo pode separar linhas com mesmo Prazo | **DOCUMENTADO EM 1986** |
| Mendes Júnior PA/PB/PP com Prazo 030 | **DOCUMENTADO** |
| Eluma com variantes C-030/E--030 | **DOCUMENTADO** |
| Tipo diferente nas linhas Vigor 140808/140809 | **EVIDÊNCIA AUSENTE** |
| Dimensão não preservada na K4 | **GANHA SUPORTE DOCUMENTAL** |
| Tipo é a dimensão ausente da colisão | **NÃO PROVADO** |
| Regra histórica de agregação/publicação | **HIPÓTESE PRINCIPAL** |
| Erro de processamento | **NÃO CONFIRMADO** |
| Causa da colisão | **NÃO RESOLVIDA** |

## 9. Conclusão

A FASE 08Z encontrou a primeira evidência contemporânea particularmente relevante para a hipótese de uma dimensão oculta na K4.

Em 05/06/1986, a própria publicação da Bovespa mostra **Mendes Júnior PA 030, PB 030 e PP 030** como linhas distintas, todas com o mesmo prazo 030. Isso prova que a dimensão **Tipo** podia separar estatísticas de um mesmo emissor/família de título sem alterar o prazo. citeturn5view0

Consequentemente, é tecnicamente plausível que uma dimensão de Tipo ou outra dimensão publicacional tenha existido além dos campos atualmente preservados na K4.

Entretanto, não é permitido converter essa plausibilidade em causa da colisão Vigor. O BDI de 10/10/1986 ainda é necessário para verificar os Tipos das duas linhas.

**Status:** IMPLEMENTADO / EXECUTADO / VALIDADO quanto à existência histórica de multiplicidade por Tipo com mesmo Prazo.

**NÃO RESOLVIDO:** se as linhas 140808/140809 tinham Tipos distintos e se isso explica a colisão.

## 10. Governança

- RAW intocado.
- Linhas 140808/140809 preservadas.
- C05 não decodificado.
- PA/PB/PP não semanticamente decodificados.
- Nenhuma identidade econômica inferida.
- Nenhuma consolidação realizada.
- Fontes posteriores não retroprojetadas para 1986.

## 11. Próxima frente

A próxima investigação deve tentar localizar:

1. BDI de 10/10/1986;
2. BDI de 09/10 e 13/10/1986;
3. documentos Bovespa que expliquem PA/PB/PP e outros códigos de Tipo;
4. exemplos em outubro de 1986 de Vigor ou outros títulos com mais de uma linha a termo no mesmo pregão;
5. eventual regra de exportação/transformação do BDI para COTAHIST.
