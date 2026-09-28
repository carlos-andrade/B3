# FASE 10A — M2 — Certificação física NORMALIZED anual 1987 V2.0

**Arquivo:** FASE10A_M2_CERTIFICACAO_FISICA_1987_V2.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_M2_CERTIFICACAO_FISICA_1987_V2.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** EM EXECUÇÃO

## 1. Objetivo

Validar a decisão V2.0 de que a certificação anual deve exigir a existência física do CSV NORMALIZED canônico, além do RAW e do quality manifest.

A prova será executada para **1987**, sem alterar RAW, sem deduplicar registros e sem reinterpretar dados.

## 2. Regra V2.0

Cadeia obrigatória:

`RAW → NORMALIZED → SHA-256 → VALIDAÇÃO → PERSISTÊNCIA → MANIFEST → CERTIFICAÇÃO FÍSICA`

A certificação física deve bloquear quando houver:

- NORMALIZED ausente;
- SHA-256 divergente;
- contagem divergente;
- schema divergente;
- datas divergentes;
- quality manifest inválido.

## 3. Escopo 1987

RAW:

`dados/cotahist/raw/anual/COTAHIST_A1987.ZIP`

NORMALIZED canônico:

`dados/cotahist/normalized/anual/COTAHIST_A1987.csv`

Manifest:

`dados/cotahist/normalized/manifests/COTAHIST_A1987_quality.json`

Valores esperados:

- Parser: **1.1.0**
- Registros: **130665**
- Campos: **25**
- Primeira data: **1987-01-02**
- Última data: **1987-12-30**
- SHA-256 NORMALIZED: **5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc**
- Tamanho persistido: **15.518.211 bytes**

## 4. Implementação

Script:

`scripts/ingestao/certificar_cotahist_anual_v2.py`

Workflow:

`.github/workflows/cotahist-m2-certificacao-fisica-1987-v2.yml`

O script calcula o SHA físico do CSV, percorre o CSV para confirmar 25 campos e datas válidas, e reconcilia os valores contra o manifesto.

## 5. Resultado

Preenchido automaticamente após execução:

- Run ID: **PENDENTE**
- Job ID: **PENDENTE**
- Conclusão: **PENDENTE**
- SHA físico: **PENDENTE**
- Linhas físicas: **PENDENTE**
- Evidência V2: **PENDENTE**
- Commit da evidência: **PENDENTE**

## 6. Critério de aprovação

**M2 = APROVADO** somente se:

1. o workflow terminar com SUCCESS;
2. a evidência V2 for persistida no repositório;
3. SHA físico = SHA do manifesto;
4. linhas físicas = manifesto;
5. datas inicial/final = manifesto;
6. schema = 25 campos;
7. status da certificação = CERTIFICADO;
8. nenhuma falha for registrada.

## 7. Próxima etapa

Depois da aprovação:

**M3 — persistência NORMALIZED anual em lotes controlados.**

Não iniciar 1986–2026 em massa antes da aprovação formal deste M2.
