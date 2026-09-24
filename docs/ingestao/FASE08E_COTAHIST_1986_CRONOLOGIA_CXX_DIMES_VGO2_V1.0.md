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
