# COTAHIST — Resultado Consolidado da Auditoria de Continuidade V2

**Arquivo:** COTAHIST_1986_2026_RESULTADO_AUDITORIA_V2.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Auditoria de integridade, continuidade, duplicidade e coerência OHLC do COTAHIST  
**Caminho:** docs/ingestao/COTAHIST_1986_2026_RESULTADO_AUDITORIA_V2.md  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Escopo

Auditoria dos arquivos anuais COTAHIST de **1986 a 2026**, totalizando **41 anos**. O ano de 2026 está parcial, com dados até **23/09/2026**.

A B3 informa que a série histórica de cotações cobre os títulos negociados desde 1986 e que os preços são fornecidos na moeda e forma de cotação da época, sem ajustes por inflação ou proventos.

## 2. Resultado estrutural

| Teste | Resultado |
|---|---:|
| Anos processados | 41 |
| Primeira data global | 1986-01-02 |
| Última data global | 2026-09-23 |
| Anos com erro de comprimento | 0 |
| Grupos de registros exatamente duplicados | 0 em todos os anos |
| Anos com repetição de identidade de instrumento | 36 |
| Anos com alguma inconsistência OHLC | 15 |

**Não foi encontrado erro estrutural de tamanho de registro em nenhum dos 41 arquivos.**

Os registros de header/trailer aparecem como registros diferentes de tipo 01, mas isso é comportamento esperado do formato COTAHIST e não foi classificado como erro estrutural.

A especificação oficial da B3 confirma três tipos de registro — 00 Header, 01 cotações e 99 Trailer — e tamanho de 245 bytes.

## 3. Duplicidade

### 3.1 Registro exatamente duplicado

Resultado: **zero grupos em todos os 41 anos**.

O critério é rigoroso: todos os 25 campos do registro precisam ser idênticos.

Isso é um resultado de integridade importante: a auditoria não encontrou cópias byte-a-byte equivalentes entre registros tipo 01.

### 3.2 Repetição da identidade do instrumento

A repetição da chave composta por data, BDI, código de negociação, mercado, ISIN e dimensão ocorre em 36 anos.

Isso **não deve ser interpretado automaticamente como duplicidade inválida**. O mesmo instrumento-identidade pode aparecer em múltiplos registros com atributos diferentes no arquivo histórico. Portanto, esses grupos foram classificados como **candidatos para investigação semântica**, e não como erro.

## 4. Continuidade temporal

Foram detectados candidatos a intervalo superior a quatro dias corridos em todos os anos.

Esse teste deliberadamente não classifica os intervalos como pregões ausentes. Um intervalo de calendário pode resultar de fins de semana, feriados, sessões especiais, suspensões, mudanças de calendário histórico, eventos extraordinários ou ausência efetiva de dados.

Portanto, **não há evidência suficiente nesta V2 para afirmar que exista pregão faltante**.

A próxima validação deverá cruzar os candidatos contra um calendário oficial de negociação aplicável a cada período histórico.

## 5. OHLC

Foram identificadas inconsistências OHLC nos seguintes anos:

| Ano | Inconsistências |
|---:|---:|
| 1986 | 29 |
| 1988 | 1 |
| 1990 | 6 |
| 1991 | 1 |
| 1994 | 2 |
| 1998 | 18 |
| 1999 | 32 |
| 2000 | 68 |
| 2001 | 108 |
| 2002 | 44 |
| 2003 | 25 |
| 2005 | 620 |
| 2006 | 1 |
| 2011 | 2 |
| 2020 | 280 |

Total: **1.237 ocorrências**.

Essas ocorrências não foram classificadas automaticamente como corrupção. A B3 declara que a série histórica é fornecida na **forma de cotação da época**, sem ajustes por inflação ou proventos. Portanto, registros históricos devem ser interpretados considerando convenções de preço, eventos corporativos, mudanças de mercado e características dos ativos de cada período.

### Prioridade de investigação

1. **2005 — 620**
2. **2020 — 280**
3. **2001 — 108**
4. **2000 — 68**
5. **2002 — 44**
6. **1999 — 32**
7. **1986 — 29**

Esses anos devem ser investigados por amostragem de registros antes de qualquer correção.

## 6. 2026

O arquivo de 2026 contém dados até **2026-09-23**, com 2.919.760 registros tipo 01, 182 datas distintas, zero registros com comprimento diferente de 245 bytes, zero grupos de registro exatamente duplicado, 5.149 grupos de repetição da identidade de instrumento e 9.011 linhas excedentes nesses grupos. Foram detectadas zero inconsistências OHLC pela regra atual.

O resultado é, portanto, **parcial**, não uma auditoria do ano civil completo.

## 7. Interpretação quantitativa

### Confirmado
- Estrutura física dos registros: íntegra nos 41 arquivos.
- Nenhum registro tipo 01 exatamente duplicado.
- Cobertura temporal global: 1986-01-02 a 2026-09-23.
- Nenhuma ocorrência de linha tipo 01 com tamanho diferente de 245 bytes.

### Candidato
- Intervalos de calendário superiores a quatro dias.
- Repetições de identidade de instrumento.
- Inconsistências OHLC.

### Ainda não demonstrado
- Pregões efetivamente ausentes.
- Corrupção de preços.
- Duplicidades econômicas.
- Erros de identificação de instrumentos.
- Necessidade de correção de qualquer registro.

## 8. Próxima fase

1. **Calendário:** comparar cada intervalo longo com calendário oficial de negociação.
2. **OHLC:** extrair os registros problemáticos completos e classificar a regra violada.
3. **Identidade:** analisar grupos repetidos por código de negociação, ISIN, mercado, dimensão e atributos de preço.
4. **Integridade temporal:** produzir uma matriz anual de datas presentes, datas esperadas e justificativa do intervalo.

Nenhuma alteração nos dados normalizados deve ser feita antes desses cruzamentos.

## 9. Evidência primária

- `dados/cotahist/quality/COTAHIST_1986_2026_resumo_v2.json`
- `dados/cotahist/quality/COTAHIST_1986_2026_continuidade_v2.json`
- `docs/ingestao/COTAHIST_AUDITORIA_CONTINUIDADE_V2.md`

## 10. Referência oficial

A B3 disponibiliza a série histórica de cotações desde 1986 e documenta o formato COTAHIST de 245 bytes, com registros 00, 01 e 99.