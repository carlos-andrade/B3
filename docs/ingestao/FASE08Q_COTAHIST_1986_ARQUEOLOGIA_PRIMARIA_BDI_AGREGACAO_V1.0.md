# FASE 08Q — COTAHIST 1986: Arqueologia Primária do BDI e Regra de Agregação

**Arquivo:** FASE08Q_COTAHIST_1986_ARQUEOLOGIA_PRIMARIA_BDI_AGREGACAO_V1.0.md  
**Projeto:** B3 — Bolsa do Brasil  
**Fase:** 08Q  
**Data de criação:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo

Recuperar uma fonte primária ou quase primária capaz de explicar como a Bovespa publicava/agregava operações a termo em outubro de 1986, com foco no BDI de 09/10, 10/10 e 13/10/1986 e na colisão:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060`.

## Busca documental

Foi realizada busca dirigida por BDI/Boletim Diário de Informações, Bovespa, Mercado a Termo, Vigor, VGO 2, PP C05, datas 09/10/1986, 10/10/1986, 11/10/1986 e 13/10/1986, Tipo, prazo, taxa, comitente, corretora e regras de agregação.

**Resultado:** não foi localizada, em acesso público verificável, uma cópia do BDI de 10/10/1986 que permita ler diretamente a linha VGO/Vigor e sua classificação operacional.

Isto é **EVIDÊNCIA AUSENTE**, não prova de inexistência.

## Evidências recuperadas

A pesquisa anterior localizou reprodução contemporânea no Jornal do Brasil de 05/06/1986 com a estrutura do Mercado a Termo:

`Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°`

A mesma publicação apresenta Vigor PP C05. Isso demonstra que, em 1986, Tipo e Prazo eram dimensões publicadas separadamente. A legenda oficial de C05, porém, continua não recuperada.

Fontes acadêmicas consultadas também identificam o BDI como publicação da Bolsa de Valores de São Paulo e como fonte histórica de dados financeiros. Isso confirma a relevância institucional do BDI, mas não substitui o exemplar primário de outubro de 1986.

A Instrução CVM nº 36/1984 confirma a existência de controles formais para mercados futuros, a termo e opções antes de 1986. O Decreto-Lei nº 2.286/1986 integra o contexto regulatório do mercado a termo. Nenhum dos dois documentos decodifica C05, DIMES 104, Tipo ou a colisão do COTAHIST.

Documentação posterior da Bovespa confirma a função do BDI na divulgação das operações, mas não deve ser retroprojetada automaticamente para 1986.

## Confronto com o RAW

A FASE 08P estabeleceu:

- 09/10/1986: 1 linha VGO 2 a termo PRAZOT 060;
- 10/10/1986: 2 linhas VGO 2 a termo PRAZOT 060;
- 13/10/1986: 1 linha VGO 2 a termo PRAZOT 060.

Nas três datas, a linha a termo mantém ESPECI `PP *C05` e DIMES `104`.

Portanto, a FASE 08Q não encontrou uma explicação baseada em mudança explícita desses campos.

## Fatos

1. O BDI era publicação institucional da Bovespa.
2. O Mercado a Termo tinha estrutura formal de controle e divulgação antes de outubro de 1986.
3. Tipo e Prazo aparecem como dimensões separadas em evidência contemporânea de 1986.
4. Vigor PP C05 já aparecia antes da colisão.
5. O BDI primário de 10/10/1986 não foi localizado publicamente nesta etapa.

## Não demonstrado

Não foi demonstrado que C05 seja taxa, Tipo, comprador/vendedor, corretora, comitente ou prazo.

Também não foi demonstrado que Tipo, taxa, comprador/vendedor, corretora ou comitente seja a dimensão responsável pela duplicidade.

## Matriz de hipóteses

| Hipótese | Status |
|---|---|
| Diferença de PRAZOT | REFUTADA |
| C05 primeira ocorrência em 10/10 | REFUTADA |
| DIMES 104 primeira ocorrência em 10/10 | REFUTADA |
| Spot vs. termo | REFUTADA |
| Perfil estatístico raro | REFUTADA |
| Recorrência 1986–2026 | REFUTADA |
| C05 = Tipo | NÃO DEMONSTRADO |
| Tipo = Prazo | REFUTADA |
| Tipo = comprador/vendedor | NÃO DEMONSTRADO |
| Tipo = corretora/comitente | NÃO DEMONSTRADO |
| Tipo = taxa | NÃO DEMONSTRADO |
| Dimensão operacional oculta | POSSÍVEL, NÃO PROVADA |
| Regra histórica de agregação/publicação | HIPÓTESE PRINCIPAL |
| Erro de processamento | NÃO CONFIRMADO |

## Conclusão

A FASE 08Q não resolveu a causa da colisão, mas reduziu o espaço de hipóteses.

A regra de governança permanece: preservar C05 literalmente, não inferir Tipo, não consolidar as linhas 140808/140809 e não atribuir causa econômica sem fonte histórica.

## Próxima frente

Migrar da busca web genérica para acervos institucionais e coleções digitalizadas, priorizando:

1. arquivo histórico Bovespa/B3;
2. CVM;
3. Hemeroteca Digital/Biblioteca Nacional;
4. bibliotecas universitárias;
5. exemplares físicos/digitalizados do BDI de 09, 10 e 13/10/1986;
6. manuais Bovespa de 1985–1987;
7. circulares e normas internas de pregão.

**Status:** IMPLEMENTADO / EXECUTADO / VALIDADO quanto à busca e classificação das evidências.

**Causa da colisão:** NÃO RESOLVIDA.

### Fontes web consultadas

- BDI como publicação histórica da BOVESPA: https://repositorio.ufmg.br/bitstreams/512aa5c3-b92a-4902-bd4a-632812b514bd/download
- Literatura sobre uso histórico do BDI: https://www.scielo.br/j/rcf/a/TdygWbTx9wsGZfBbxmWFQh/
- Material histórico sobre mercado a termo e BDI: https://fernandonogueiracosta.wordpress.com/wp-content/uploads/2010/03/como-investir-no-mercado-a-termo.pdf
