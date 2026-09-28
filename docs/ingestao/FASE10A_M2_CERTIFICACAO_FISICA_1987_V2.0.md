# FASE 10A — M2 — Certificação física NORMALIZED anual 1987 V2.0

**Arquivo:** FASE10A_M2_CERTIFICACAO_FISICA_1987_V2.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_M2_CERTIFICACAO_FISICA_1987_V2.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** **APROVADO**

## 1. Objetivo

Validar a decisão V2.0 de que a certificação anual deve exigir a existência física do CSV NORMALIZED canônico, além do RAW e do quality manifest.

A prova foi executada para **1987**, sem alterar RAW, sem deduplicar registros e sem reinterpretar dados.

## 2. Regra V2.0

Cadeia obrigatória:

`RAW → NORMALIZED → SHA-256 → VALIDAÇÃO → PERSISTÊNCIA → MANIFEST → CERTIFICAÇÃO FÍSICA`

A certificação física bloqueia quando houver:

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

Valores reconciliados:

- Parser: **1.1.0**
- Registros: **130665**
- Campos: **25**
- Primeira data: **1987-01-02**
- Última data: **1987-12-30**
- SHA-256 NORMALIZED: **5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc**
- Tamanho físico: **15.518.211 bytes**

## 4. Execução

Script:

`scripts/ingestao/certificar_cotahist_anual_v2.py`

Workflow:

`.github/workflows/cotahist-m2-certificacao-fisica-1987-v2.yml`

Run ID:

**36403697669**

Job ID:

**108867281490**

Conclusão:

**SUCCESS**

O workflow executou com sucesso:

1. checkout;
2. certificação NORMALIZED físico;
3. persistência da evidência;
4. publicação do artefato.

## 5. Evidência física

Arquivo:

`dados/cotahist/certificacao/v2/COTAHIST_A1987_CERTIFICACAO_FISICA_V2.0.json`

Status:

**CERTIFICADO**

Certificação:

**CERTIFICADO_NORMALIZACAO_FISICO**

SHA físico:

`5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`

SHA do manifesto:

`5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`

Linhas físicas:

**130665**

Linhas do manifesto:

**130665**

Data inicial física = manifesto:

**1987-01-02**

Data final física = manifesto:

**1987-12-30**

Falhas:

**[]**

Commit da evidência:

`925a4d566bd7e8fd4babedada2865df9068f2fc8`

Mensagem:

`data(certificacao): certificar NORMALIZED fisico A1987 V2`

## 6. Critérios de aprovação

Todos atendidos:

1. workflow SUCCESS — **OK**;
2. evidência V2 persistida — **OK**;
3. SHA físico = manifesto — **OK**;
4. linhas físicas = manifesto — **OK**;
5. datas inicial/final = manifesto — **OK**;
6. schema = 25 campos — **OK**;
7. status = CERTIFICADO — **OK**;
8. nenhuma falha — **OK**.

## 7. Integração com Dataset Oficial

A integração V2 também foi implementada em:

`scripts/ingestao/gerar_dataset_oficial_cotahist_v2.py`

e:

`.github/workflows/cotahist-dataset-oficial-v2.yml`

A primeira execução controlada do Dataset Oficial V2 retornou **FAILURE por bloqueio esperado**, porque os demais anos ainda não possuem NORMALIZED anual físico e certificação física V2.

Isso é comportamento **fail-closed correto**, não erro de processamento.

Run de integração:

**36403827859**

Job:

**108867698262**

Resultado:

**FAILURE esperado — publicação bloqueada**

A execução identificou explicitamente a ausência de NORMALIZED/certificação física nos anos ainda não migrados. O ano 1987 não foi reportado como ausente.

## 8. Decisão

**M2 = APROVADO.**

A arquitetura V2 está comprovada para o primeiro ano migrado e o Dataset Oficial V2 está protegido contra publicação incompleta.

## 9. Próxima etapa

**M3 — persistência NORMALIZED anual em lotes controlados.**

O próximo objetivo é migrar os demais anos sem alterar RAW, mantendo SHA, manifesto, certificação física e rastreabilidade.

A publicação do Dataset Oficial V2 somente será liberada quando a cadeia completa de 1986–2026 estiver coerente.
