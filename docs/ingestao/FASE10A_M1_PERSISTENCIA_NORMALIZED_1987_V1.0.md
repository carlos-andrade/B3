# FASE 10A — M1 — Persistência NORMALIZED anual 1987 V1.0

**Arquivo:** FASE10A_M1_PERSISTENCIA_NORMALIZED_1987_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_M1_PERSISTENCIA_NORMALIZED_1987_V1.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** EXECUÇÃO CONTROLADA

## 1. Objetivo

Executar a primeira prova de migração definida no contrato NORMALIZED anual V2.0, usando exclusivamente o ano de 1987.

O teste deve provar, antes de qualquer lote:

`RAW → NORMALIZED → SHA-256 → VALIDAÇÃO → PERSISTÊNCIA → MANIFEST`

## 2. Escopo

Ano: **1987**

RAW:
`dados/cotahist/raw/anual/COTAHIST_A1987.ZIP`

RAW SHA-256:
`16db2bbda8cf770ad177af762c6e651422dee7b1dc7a62ea75fa10e5760f517d`

NORMALIZED canônico esperado:
`dados/cotahist/normalized/anual/COTAHIST_A1987.csv`

NORMALIZED SHA-256 esperado:
`5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`

Parser:
`1.1.0`

Registros esperados:
`130665`

Campos esperados:
`25`

Primeira data:
`1987-01-02`

Última data:
`1987-12-30`

## 3. Critérios de aceitação

O M1 somente pode ser considerado concluído se:

1. o RAW de 1987 existir;
2. o manifesto de qualidade estiver `VALIDADO`;
3. a normalização for regenerada a partir do RAW;
4. a validação estrutural passar;
5. contagem, campos e datas coincidirem com o manifesto;
6. o SHA-256 regenerado coincidir exatamente com o manifesto;
7. o arquivo tiver menos de 100 MB;
8. o arquivo for persistido no caminho canônico;
9. o SHA-256 do arquivo persistido permanecer idêntico;
10. a persistência ocorrer por GitHub Actions;
11. nenhuma alteração for feita no RAW;
12. nenhum dado for deduplicado, corrigido ou reinterpretado.

## 4. Fail-closed

Qualquer divergência deve interromper a persistência.

Em particular:

- SHA divergente → BLOQUEAR;
- contagem divergente → BLOQUEAR;
- schema divergente → BLOQUEAR;
- datas divergentes → BLOQUEAR;
- arquivo ausente → BLOQUEAR;
- tamanho ≥ 100 MB → BLOQUEAR.

Não é permitido substituir o valor esperado do manifesto para fazer o teste passar.

## 5. Workflow

Workflow dedicado:

`.github/workflows/cotahist-normalized-m1-1987.yml`

Commit de criação do workflow:
`ca42f4f12d0a3faa6200e70cdd07ad2f250a0000`

O workflow é acionado por alteração deste documento ou manualmente e executa a prova de 1987 isoladamente.

## 6. Resultado

Preenchido automaticamente após a execução do workflow.

- Run ID:
- Status:
- Job:
- Tamanho NORMALIZED:
- SHA-256 persistido:
- Commit de persistência:
- M1:

## 7. Próxima etapa

Somente após M1 = **APROVADO**:

**M2 — reconciliação física e integração com certificação anual + Dataset Oficial.**

Não iniciar lote 1986–2026 antes de M1 e M2 estarem certificados.
