# FASE 08E — Reconstrução Estatística da Cronologia C03/C05/Cxx e DIMES/VGO 2

**Arquivo:** FASE08E_COTAHIST_1986_CRONOLOGIA_CXX_DIMES_VGO2_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconstrução estatística das transições históricas de VGO 2 / VGORACPP em 1986  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Testar, diretamente no COTAHIST 1986 preservado, se a colisão K4 de 10/10/1986 coincide com alguma transição estrutural de:

- ESPECI: C03 / C05 / outros Cxx;
- DIMES: 102 / 104;
- CODBDI × TPMERC × PRAZOT;
- CODNEG VGO 2;
- CODISI VGORACPP.

A análise não altera o RAW e não tenta inferir significado econômico sem documentação histórica.

## 2. Implementação

Parser:

`scripts/ingestao/analisar_cronologia_cxx_dimes_vgo2_1986_v1.py`

Commit:

`44147e22aec59b838a23237fdfaeb4a43c5d717b`

Workflow:

`.github/workflows/cotahist-fase08e-cronologia-1986-v1.yml`

Commit:

`1ae0f0fb051708466f7d85a4b978dd6b2f74b567`

O workflow publica:

`dados/cotahist/quality/COTAHIST_1986_FASE08E_CRONOLOGIA_V1.json`

## 3. Perguntas controladas

1. C05 surge exatamente em 10/10/1986?
2. DIMES 104 surge exatamente em 10/10/1986?
3. O VGO 2 muda de C03 para C05 no pregão da colisão?
4. C05 aparece em outros CODNEG?
5. VGO 2 possui outros Cxx depois da mudança?
6. Há mudança de mercado/prazo coincidente com a colisão?
7. O evento é uma transição cadastral ou uma anomalia isolada?

## 4. Regra de classificação

**FATO:** somente o que estiver presente no RAW ou no JSON publicado.

**PADRÃO:** comportamento cronológico repetível no conjunto.

**HIPÓTESE:** explicação possível, sem confirmação documental.

**NÃO DETERMINADO:** questão sem evidência suficiente.

## 5. Gate de validação

Até que o JSON de evidência seja publicado e conferido:

**STATUS: IMPLEMENTADO / EXECUÇÃO NÃO COMPROVADA NO ARTEFATO DE SAÍDA.**

Não serão apresentados números derivados do parser como se fossem resultados validados.

## 6. Resultado esperado para a investigação

A principal hipótese a testar é se a duplicidade de 10/10/1986 está ligada a uma transição C03→C05 ou DIMES 102→104.

Mesmo que exista coincidência temporal, isso não será considerado causalidade sem evidência documental independente.

## 7. Governança

- RAW intocado;
- nenhuma linha removida;
- nenhuma linha consolidada;
- nenhuma correção manual;
- nenhuma identidade econômica inferida;
- resultados reproduzíveis por workflow;
- SHA-256 do RAW preservado no JSON.

## 8. Próximo passo

Após a publicação do JSON, confrontar:

`vgo2_especi_intervals`

`vgo2_dimes_intervals`

`vgo2_especi_transitions`

`vgo2_dimes_transitions`

`vgo2_market_transitions`

e a janela de 01/10/1986 a 17/10/1986.

Só então será definida a conclusão estatística da FASE 08E.


## 9. Resultado executado e validado

O workflow foi executado automaticamente após a gravação do código.

**Run:** 36068299927  
**Conclusão:** success  
**Artefato publicado:** `dados/cotahist/quality/COTAHIST_1986_FASE08E_CRONOLOGIA_V1.json`  
**Commit de publicação:** `282be08d18360521018487ca4f11681bfaaa8ba2`

### 9.1 Resultados quantitativos

- Registros tipo 01: **177.981**
- VGO 2: **443**
- CODISI VGORACPP: **473**
- VGO 2 / ESPECI:
  - `PP  C03`: **53**
  - `PP *C03`: **123**
  - `PP *C05`: **261**
  - `PP *S/D`: **6**
- VGO 2 / DIMES:
  - `102`: **182**
  - `104`: **261**
- VGORACPP / ESPECI:
  - `PP  C03`: **70**
  - `PP *C03`: **128**
  - `PP *C05`: **269**
  - `PP *S/D`: **6**
- VGORACPP / DIMES:
  - `102`: **204**
  - `104`: **269**

### 9.2 Cronologia crítica

A sequência observada para VGO 2 é:

**02/01/1986 → PP C03 + DIMES 102**

**04/03/1986 → PP *C03**

**03/06/1986 → PP *S/D**

**06/06/1986 → PP *C05 + DIMES 104**

Os dois últimos estados mudam simultaneamente: `PP *S/D → PP *C05` e `DIMES 102 → DIMES 104`.

Portanto, **10/10/1986 não é a data de introdução de C05 nem de DIMES 104**.

### 9.3 Janela da anomalia

Em **09/10/1986**, VGO 2 já aparece com:

`CODBDI=62 | TPMERC=030 | PRAZOT=060 | ESPECI=PP *C05 | DIMES=104`

Em **10/10/1986**, as duas linhas da colisão mantêm exatamente esse contexto cadastral/mercadológico.

Em **13/10/1986**, o contexto continua:

`CODBDI=62 | TPMERC=030 | PRAZOT=060 | ESPECI=PP *C05 | DIMES=104`

Isso elimina, como explicação suficiente, uma simples transição cadastral ocorrida no dia da colisão.

### 9.4 C05 em outros papéis

Foram encontrados **449 registros** contendo C05 em ESPECI e pertencentes a outros CODNEG que não VGO 2.

Portanto, **C05 não é exclusivo de VGO 2**.

### 9.5 Outros Cxx em VGO 2

VGO 2 possui **176 registros** com ESPECI contendo Cxx diferente de C05.

Isso confirma que VGO 2 percorreu historicamente múltiplos estados Cxx; contudo, a transição relevante para a anomalia já havia ocorrido meses antes.

## 10. Conclusão estatística

**FATO VALIDADO:** a transição estrutural relevante de VGO 2 ocorreu em 06/06/1986, quando o estado observado passou de `PP *S/D`/DIMES 102 para `PP *C05`/DIMES 104.

**FATO VALIDADO:** em 09/10, 10/10 e 13/10/1986, VGO 2 permanece em `PP *C05` + DIMES 104.

**FATO VALIDADO:** a colisão K4 de 10/10/1986 não coincide com a primeira aparição de C05, nem com a mudança 102→104.

**FATO VALIDADO:** C05 ocorre em centenas de registros de outros CODNEG; portanto, sua simples presença não identifica a colisão.

**HIPÓTESE REBAIXADA:** explicar a duplicidade K4 por uma transição C03→C05 ou 102→104 em 10/10/1986 não é compatível com a cronologia observada.

**NÃO DETERMINADO:** a razão pela qual duas linhas com K4 idêntica foram publicadas para o mesmo VGO 2 / termo / 60 dias em 10/10/1986.

## 11. Status da FASE 08E

**IMPLEMENTADO:** ✅  
**EXECUTADO:** ✅  
**VALIDADO:** ✅

A FASE 08E está encerrada quanto ao objetivo estatístico definido.

O RAW continua intacto.

## 12. Próxima frente

**FASE 08F — Análise estrutural dos campos estatísticos da colisão K4.**

Objetivo: verificar se as duas linhas 140808/140809 podem ser separadas por alguma propriedade estatística não pertencente à K4, incluindo:

- relação preço × quantidade × volume;
- consistência matemática `preço × quantidade` versus `VOLTOT`;
- número de negócios;
- fatores de cotação;
- diferenças de escala;
- comparação com todas as linhas de VGO 2 em mercado a termo;
- identificação de padrões de duplicidade estatística sem depender da semântica econômica.

Nenhuma hipótese econômica será introduzida antes dessa análise.
