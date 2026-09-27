# FASE 10A — M1 — Persistência NORMALIZED anual 1987 V1.0

**Arquivo:** FASE10A_M1_PERSISTENCIA_NORMALIZED_1987_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_M1_PERSISTENCIA_NORMALIZED_1987_V1.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** **APROVADO**

## 1. Objetivo

Executar a primeira prova de migração definida no contrato NORMALIZED anual V2.0, usando exclusivamente o ano de 1987.

O teste provou a cadeia:

`RAW → NORMALIZED → SHA-256 → VALIDAÇÃO → PERSISTÊNCIA → MANIFEST`

## 2. Escopo

Ano: **1987**

RAW:
`dados/cotahist/raw/anual/COTAHIST_A1987.ZIP`

RAW SHA-256:
`16db2bbda8cf770ad177af762c6e651422dee7b1dc7a62ea75fa10e5760f517d`

NORMALIZED canônico:
`dados/cotahist/normalized/anual/COTAHIST_A1987.csv`

NORMALIZED SHA-256:
`5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`

Parser:
`1.1.0`

Registros:
`130665`

Linhas físicas do CSV, incluindo cabeçalho:
`130666`

Campos:
`25`

Primeira data:
`1987-01-02`

Última data:
`1987-12-30`

Tamanho persistido:
**15.518.211 bytes**

## 3. Critérios de aceitação

Todos os critérios foram atendidos:

1. RAW de 1987 existente — **OK**;
2. manifesto `VALIDADO` — **OK**;
3. normalização regenerada a partir do RAW — **OK**;
4. validação estrutural — **OK**;
5. contagem/campos/datas coincidentes — **OK**;
6. SHA-256 coincidente — **OK**;
7. tamanho inferior a 100 MB — **OK**;
8. persistência no caminho canônico — **OK**;
9. SHA-256 após persistência idêntico — **OK**;
10. persistência executada por GitHub Actions — **OK**;
11. RAW não alterado — **OK**;
12. nenhum dado deduplicado/corrigido/reinterpretado — **OK**.

## 4. Evidência de execução

Workflow:

`.github/workflows/cotahist-normalized-m1-1987.yml`

Commit de criação do workflow:

`ca42f4f12d0a3faa6200e70cdd07ad2f250a0000`

Run ID:

`36358206263`

Job ID:

`108730032767`

Conclusão:

**success**

O workflow registrou:

- `COTACOES_01=130665`;
- `PARSER_VERSION=1.1.0`;
- `PRIMEIRA_DATA=1987-01-02`;
- `ULTIMA_DATA=1987-12-30`;
- `MANIFESTO_VS_REGENERACAO=OK`;
- `NORMALIZED_1987_BYTES=15518211`;
- SHA persistido exatamente igual ao manifesto.

## 5. Commit de persistência

Commit:

`aa80859b1c227652dca1e6853fe054df59db5fd4`

Mensagem:

`data(normalized): persistir COTAHIST A1987 canonico`

Arquivo criado:

`dados/cotahist/normalized/anual/COTAHIST_A1987.csv`

## 6. Artefato de execução

Artifact ID:

`10943649552`

Nome:

`cotahist-normalized-m1-1987`

Tamanho do ZIP do artefato:

`4.124.424 bytes`

Retenção:

30 dias.

O artefato é evidência temporária. A fonte permanente é o CSV versionado no repositório.

## 7. Fail-closed

Nenhuma divergência foi tolerada.

A prova foi interrompível em qualquer etapa por:

- SHA divergente;
- contagem divergente;
- schema divergente;
- datas divergentes;
- arquivo ausente;
- tamanho igual ou superior a 100 MB.

O valor do manifesto não foi alterado para acomodar a execução.

## 8. Decisão

**M1 = APROVADO.**

A persistência anual NORMALIZED está tecnicamente comprovada para um ano histórico real, com regeneração determinística a partir do RAW e reconciliação exata do SHA-256.

Isso autoriza a entrada na etapa **M2**.

## 9. Próxima etapa

**M2 — reconciliação física e integração com certificação anual + Dataset Oficial.**

M2 deverá:

1. alterar a referência canônica do Dataset Oficial para `dados/cotahist/normalized/anual/`;
2. exigir existência física do NORMALIZED;
3. comparar SHA-256 físico × manifesto;
4. atualizar a certificação anual para verificar o CSV físico;
5. executar a cadeia completa para 1987;
6. somente depois preparar M3 para os demais anos.

**Não iniciar lote 1986–2026 antes de M2 estar certificado.**
