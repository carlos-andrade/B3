# FASE 07 — RESULTADO DA IDENTIDADE HISTÓRICA COTAHIST 1986 V1.1

**Arquivo:** `FASE07_COTAHIST_1986_RESULTADO_IDENTIDADE_V1.1.md`  
**Projeto:** B3 — A Bolsa do Brasil  
**Tema:** Resultado auditável da identidade histórica de 1986  
**Caminho:** `docs/ingestao/FASE07_COTAHIST_1986_RESULTADO_IDENTIDADE_V1.1.md`  
**Data de criação:** 24/09/2026  
**Repositório:** `carlos-andrade/B3`

## 1. Evidência executada

A execução produziu **177.981 registros** de tipo 01.

Cardinalidade observada:

- CODNEG: 2.699
- CODISI: 1.350
- TPMERC: 9
- CODBDI: 15
- DIMES: 131
- ESPECI: 495

## 2. Resultado das quatro chaves

| Chave | Grupos | Unitários | Repetidos | Linhas em grupos repetidos | Máx. grupo |
|---|---:|---:|---:|---:|---:|
| K1 DATA+CODNEG+TPMERC | 172.792 | 167.610 | 5.182 | 10.371 | 3 |
| K2 DATA+CODBDI+CODNEG+TPMERC | 172.792 | 167.610 | 5.182 | 10.371 | 3 |
| K3 DATA+CODBDI+CODNEG+TPMERC+CODISI+DIMES | 172.793 | 167.612 | 5.181 | 10.369 | 3 |
| K4 chave contratual enriquecida | 177.980 | 177.979 | 1 | 2 | 2 |

## 3. Interpretação objetiva

### 3.1 K1 e K2

K1 e K2 possuem exatamente a mesma cardinalidade em 1986. Isso mostra que, nos grupos testados, adicionar CODBDI **não elimina as colisões existentes**.

Portanto:

**CODBDI não deve ser utilizado isoladamente como mecanismo para resolver identidade histórica.**

### 3.2 K3

K3 reduz marginalmente as colisões:

- 5.182 → 5.181 grupos repetidos;
- 10.371 → 10.369 linhas envolvidas.

Isso demonstra que CODISI + DIMES adicionam poder discriminante, mas **não tornam a chave única**.

### 3.3 K4

K4 reduz o universo para apenas:

- 1 grupo repetido;
- 2 registros;
- tamanho máximo 2.

Isso é uma evidência forte de que os atributos contratuais possuem informação discriminante adicional.

Entretanto, **K4 ainda não é declarada chave econômica definitiva**, porque a única colisão residual precisa ser explicada no nível de registro.

## 4. Reutilização de CODNEG

Foram observados:

- 2.699 CODNEG distintos;
- 1.797 CODNEG com mais de um valor em algum atributo analisado.

O resultado é particularmente importante porque códigos como `PET 2`, `AVI 2`, `BBD 3` e outros aparecem ao longo de múltiplos contextos de mercado/classificação.

Isso confirma empiricamente que **CODNEG não pode ser tratado como identificador econômico global e permanente**.

A própria documentação oficial da B3 define CODNEG como código de negociação do papel e TPMERC como código do mercado em que o papel está cadastrado; CODBDI é usado para classificar os papéis no Boletim Diário de Informações. citeturn0search15

## 5. Importante: TPMERC/CODBDI

A documentação oficial disponível da B3 estabelece que o COTAHIST é organizado por papel-mercado e que o registro 01 contém, entre outros, DATA DO PREGÃO, CODBDI, CODNEG e TPMERC. citeturn0search14turn0search15

Isso sustenta a utilização desses campos como **dimensões classificatórias do registro**, mas não autoriza transformar qualquer combinação em uma identidade econômica sem investigação histórica adicional.

## 6. Conclusão da FASE 07A

### Aprovado

- reutilização temporal de CODNEG demonstrada;
- K1 e K2 testadas;
- K3 testada;
- K4 testada;
- nenhum RAW/NORMALIZED alterado;
- resultado persistido no JSON de qualidade.

### Ainda pendente

A FASE 07 completa **não está encerrada**.

Precisamos concluir:

1. classificação da única colisão K4;
2. mapeamento documental de TPMERC;
3. mapeamento documental de CODBDI;
4. investigação histórica de DIMES;
5. investigação de CODISI;
6. matriz final de identidade histórica.

**Status:** FASE 07A — CONCLUÍDA.  
**Status global FASE 07 — EM EXECUÇÃO.**
