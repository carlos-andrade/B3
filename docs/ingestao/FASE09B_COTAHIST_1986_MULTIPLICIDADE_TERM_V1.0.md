# FASE 09B — Teste de multiplicidade estrutural no Mercado a Termo

**Arquivo:** FASE09B_COTAHIST_1986_MULTIPLICIDADE_TERM_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Identificação sistemática de múltiplas linhas de termo com mesma chave parcial e comparação com K4  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

A FASE 09B transforma a próxima pergunta da investigação em teste reproduzível sobre o RAW:

> Existem, em COTAHIST 1986, outras combinações de data + CODBDI + CODNEG + TPMERC + PRAZOT que aparecem em múltiplas linhas, e essas multiplicidades são explicadas por campos estruturais da K4 ou permanecem colisões estatísticas?

O teste separa duas chaves:

### Chave parcial de investigação

`DATA + CODBDI + CODNEG + TPMERC + PRAZOT`

Essa chave mantém o ativo, mercado e prazo, mas deliberadamente não inclui CODISI, DIMES e ESPECI.

### K4 completa

`DATA + CODBDI + CODNEG + TPMERC + CODISI + DIMES + ESPECI + PRAZOT`

O objetivo é verificar se multiplicidades da chave parcial normalmente são resolvidas por campos estruturais adicionais e se alguma permanece como colisão estatística real.

## 2. Implementação

Foi criado o parser:

`scripts/ingestao/analisar_multiplicidade_term_1986_v1.py`

O parser:

- lê somente registros tipo 01;
- restringe o teste ao `TPMERC=030`;
- calcula a chave parcial;
- calcula a K4;
- identifica grupos com mais de uma linha;
- compara os perfis estatísticos;
- preserva o RAW;
- não recodifica C05;
- não consolida registros.

## 3. Critério de interpretação

### Caso A — multiplicidade parcial, K4 diferente

Interpretação:

A chave parcial não é suficiente, mas a K4 contém dimensão adicional capaz de separar as linhas.

Isso é **comportamento estrutural normal**, não uma colisão K4.

### Caso B — multiplicidade parcial, K4 igual, estatísticas diferentes

Interpretação:

Existe uma colisão equivalente à anomalia Vigor e o caso merece investigação documental específica.

### Caso C — multiplicidade parcial, K4 igual, estatísticas iguais

Interpretação:

Existe duplicação estrutural com perfil estatístico idêntico. Deve ser investigada como possível duplicidade de publicação/registro, mas não deve ser automaticamente consolidada.

## 4. Aplicação ao alvo Vigor

O alvo:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060`

satisfaz simultaneamente:

- mesma chave parcial;
- mesma K4;
- dois perfis estatísticos distintos.

Portanto, ele pertence ao **Caso B**.

## 5. Hipótese que o teste pretende verificar

Se o universo de 1986 revelar muitos casos do Caso B, a colisão Vigor poderá fazer parte de uma regra geral de publicação/estruturação histórica.

Se o Caso B permanecer excepcional ou único, a investigação deverá concentrar-se em documentação específica do evento, principalmente BDI e regras operacionais da época.

Nenhuma dessas conclusões será assumida antes da execução do parser sobre o RAW integral.

## 6. Estado da execução

**IMPLEMENTADO:** parser criado e versionado.

**EXECUTADO:** não ainda no ambiente desta etapa, pois o RAW integral de 1986 não está montado como arquivo de trabalho nesta execução.

**VALIDADO:** lógica de campos e separação entre chave parcial e K4, mantendo os offsets fixos já validados nas fases anteriores.

**NÃO RESOLVIDO:** contagem final dos casos A/B/C no universo integral de 1986.

## 7. Governança

- RAW permanece intocado.
- Nenhuma linha é eliminada.
- Nenhuma linha é consolidada.
- Nenhum campo é recodificado.
- O resultado será somente leitura.
- O hash SHA-256 do RAW deverá ser publicado juntamente com o resultado da execução.

## 8. Próxima execução

Executar o parser sobre o RAW COTAHIST 1986 e publicar:

1. quantidade total de registros tipo 01;
2. grupos de termo pela chave parcial;
3. grupos parciais com múltiplas linhas;
4. quantos são resolvidos pela K4;
5. quantos permanecem colisões K4;
6. quantos possuem estatísticas diferentes;
7. exemplos auditáveis dos primeiros casos;
8. comparação direta com Vigor 140808/140809.

**FASE 09B:** IMPLEMENTADA; execução integral pendente.
