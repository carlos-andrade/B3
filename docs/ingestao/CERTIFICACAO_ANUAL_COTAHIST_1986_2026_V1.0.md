# CERTIFICAÇÃO ANUAL COTAHIST 1986–2026

**Arquivo:** CERTIFICACAO_ANUAL_COTAHIST_1986_2026_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Tema:** Certificação operacional anual da camada de normalização COTAHIST  
**Caminho:** docs/ingestao/CERTIFICACAO_ANUAL_COTAHIST_1986_2026_V1.0.md  
**Data de criação:** 25/09/2026  
**Repositório:** carlos-andrade/B3  
**Status:** VIGENTE — ESCOPO OPERACIONAL DE NORMALIZAÇÃO

## 1. Objetivo

Registrar, de forma auditável, o estado de cada ano COTAHIST entre 1986 e 2026 com base nos artefatos efetivamente existentes no repositório.

Esta matriz certifica a camada de normalização estrutural e de qualidade definida pelos manifests COTAHIST_AYYYY_quality.json. Ela não transforma automaticamente uma validação estrutural em certificação semântica histórica completa.

## 2. Regra de certificação

Um ano recebe CERTIFICADO_NORMALIZAÇÃO quando:

1. o RAW anual está presente;
2. o manifest de qualidade está presente;
3. o manifest informa status = VALIDADO;
4. o parser registrado é 1.1.0;
5. o manifest registra 25 campos;
6. datas_invalidas = 0;
7. datas_fora_do_ano = 0.

Para 1986, a certificação é registrada como CERTIFICADO_NORMALIZAÇÃO_COM_EXCEÇÃO_SEMÂNTICA, porque a governança do projeto mantém esse ano como exceção histórica controlada. Isso não invalida sua normalização nem autoriza inferências semânticas não comprovadas.

## 3. Resultado

- 41/41 anos possuem manifest de qualidade.
- 41/41 manifests estão com status = VALIDADO.
- 41/41 registram 25 campos.
- 41/41 registram zero datas inválidas.
- 41/41 registram zero datas fora do ano.
- 1986 permanece explicitamente segregado como exceção semântica histórica.
- 2026 é um ano corrente/parcial no conjunto disponível; a última data registrada no manifest é 2026-09-22.

## 4. Limite da certificação

Esta matriz não certifica:
- interpretação econômica de códigos históricos;
- equivalência semântica universal entre períodos;
- completude econômica de cada pregão;
- ausência de problemas de microestrutura não contemplados pelo parser;
- adequação dos dados para qualquer estratégia específica;
- certificação semântica plena de 1986.

## 5. Fonte primária

A fonte operacional são os manifests versionados em dados/cotahist/normalized/manifests/.

O artefato máquina-a-máquina correspondente é:
dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv

## 6. Regra de governança

A matriz deve ser regenerada quando houver alteração em RAW, parser, normalização ou manifest. Nenhum ano deve ser promovido silenciosamente para uma categoria superior de confiança.

**Regra final:** certificação estrutural não equivale a validação semântica total.
