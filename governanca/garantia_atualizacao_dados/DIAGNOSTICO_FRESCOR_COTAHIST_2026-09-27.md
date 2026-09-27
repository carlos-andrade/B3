# DIAGNÓSTICO DE FRESCOR — COTAHIST 2026

**Arquivo:** DIAGNOSTICO_FRESCOR_COTAHIST_2026-09-27.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Caminho:** governanca/garantia_atualizacao_dados/DIAGNOSTICO_FRESCOR_COTAHIST_2026-09-27.md  
**Data:** 27/09/2026  
**Repositório:** carlos-andrade/B3

## Resultado

Foi encontrada uma distinção crítica entre duas camadas:

- **COTAHIST diário:** possui evidência validada até 25/09/2026.
- **COTAHIST anual/oficial 2026:** permanece até 22/09/2026.

Portanto, não existe ausência total do dado de 25/09. Existe uma falha de **reconciliação/convergência da camada oficial anual**.

## Evidências

### Diário — 25/09/2026

Commit:

`1b2ef358f02c18fb1d1b061a41e97e13f957653e`

Manifest:

`dados/cotahist/normalized/manifests/diario/COTAHIST_D25092026_quality.json`

Características:

- status: VALIDADO;
- data de referência: 2026-09-25;
- linhas: 16.593;
- primeira data: 2026-09-25;
- última data: 2026-09-25;
- SHA-256 RAW: `1d62e1d49777c8b85dba3e546a5040d0f78765fb1cd439433c5303f5320ae4a8`;
- SHA-256 NORMALIZED: `f195a090d38055951972208c97f5cce49b221e462c60df9bc1c29d62ae8c93cc`.

### Anual/oficial — 2026

Manifesto:

`dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json`

Última observação:

**2026-09-22**

Linhas:

**2.904.013**

O manifesto foi regenerado em 27/09 pelo commit:

`561888200a6def1c90815e0b5f67c8b1f835fd3e`

A regeneração alterou `generated_at`, mas não acrescentou os pregões posteriores a 22/09.

## Causa técnica

O importador diário original trabalhava somente com a data corrente. Em caso de falha, indisponibilidade transitória ou ausência de persistência, o próximo ciclo não recuperava automaticamente o pregão perdido.

Isso viola a propriedade desejada de **eventual convergência** da ingestão.

## Correção aplicada

O importador foi alterado para processar automaticamente uma janela de **7 dias retroativos**, tratando HTTP 404/410 como ausência esperada de pregão/arquivo e preservando a validação de:

`RAW → ZIP → NORMALIZED → linhas → datas → SHA-256 → manifest`

Arquivo:

`scripts/ingestao/importar_cotahist_diario_v1.py`

Commit:

`3fc2afb82409af9a642541c96ded14a971ecbad7`

## Critério de sucesso

A correção será considerada operacionalmente comprovada quando uma execução do workflow produzir evidência de captura para todos os pregões disponíveis na janela e, especificamente, 23/09 e 24/09/2026, sem degradar 25/09/2026.

Depois disso, a camada anual/oficial deverá ser reconciliada ou o catálogo oficial deverá declarar explicitamente a arquitetura anual + overlay diário.

## Regra

**Workflow verde não certifica frescor.**

A certificação depende da última observação efetivamente armazenada e validada.

Até a reconciliação, a garantia global permanece **NÃO CERTIFICADA**.
