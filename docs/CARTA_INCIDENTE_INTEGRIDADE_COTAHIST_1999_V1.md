# CARTA DE INCIDENTE E INTEGRIDADE — COTAHIST 1999

**Projeto:** B3 — A BOLSA DO BRASIL  
**Repositório:** `carlos-andrade/B3`  
**Versão:** 1.0.0  
**Data:** 2026-10-12  
**Estado:** INCIDENTE ABERTO — recuperação parcial persistida  
**Artefatos afetados:** COTAHIST anual de 1999, normalizador e evidência FASE04  
**Autoridade normativa operacional:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`

## 1. Fato observado

O CSV canónico `dados/cotahist/normalized/anual/COTAHIST_A1999.csv` não existia no repositório, embora o manifesto e o sidecar declarassem um SHA-256 esperado.

Foi executada uma recuperação determinística a partir do RAW imutável. A recuperação inicial produziu 129.841 registos, 25 campos e datas entre 1999-01-04 e 1999-12-30, mas o hash calculado (`d4c009984c23bde54532a9388da9841eca690286e10dc9c3502248f233840c7b`) divergiu do hash registado (`0bf3643a8a06f6e513f97d8cf4d5fd0a7ac718af6d8a55a9ac8bdd230d4e2b1d`).

A auditoria persistida em `dados/cotahist/quality/COTAHIST_1999_FASE04_RECUPERACAO_V1.json` classificou o resultado como bloqueado para promoção, sem alterar o RAW nem deduplicar registos.

## 2. Causa técnica identificada

A comparação do histórico do normalizador identificou alteração nos offsets dos três campos finais:

| Campo | Implementação anterior | Implementação corrigida |
|---|---:|---:|
| `ptoexe` | bytes 218–230, precisão de 6 casas | bytes 218–230, precisão de 6 casas |
| `codisi` | bytes 231–242 | bytes 231–242 |
| `dismes` | bytes 243–245 | bytes 243–245 |

A implementação publicada como versão 1.1.1 havia alterado incorretamente estes intervalos para 218–224, 225–236 e 237–245. A versão 1.1.2 restaura os offsets do layout de 245 bytes e eleva a versão do parser. A execução subsequente deverá provar se a saída reproduz o hash histórico; até lá, a correção está implementada, mas não validada.

## 3. Alterações persistidas

- Workflow de recuperação: `.github/workflows/cotahist-recuperar-normalized-1999-v1.yml`
- Normalizador corrigido: `scripts/ingestao/normalize_cotahist.py`, versão 1.1.2
- CSV regenerado e auditoria de divergência persistidos pelo commit `34a66a213f81874f995cd4c2153cb4239a6d3c45`
- Correção do normalizador persistida pelo commit `70acbb8559fcecafd894629315513b5dbe9fdd42`
- Reexecução configurada pelo commit `afe1c4c018bd27ec6f6ab8dd092b2d654c975ac3`

## 4. Regras de contenção

1. Não alterar o RAW nem o seu checksum.
2. Não atualizar manifesto ou sidecar apenas para fazê-los coincidir com uma saída divergente.
3. Não deduplicar registos na FASE04; identidade e cardinalidade pertencem à FASE07.
4. Exigir existência física, tamanho não nulo, hash calculado e reconciliação com manifesto/sidecar antes de promover qualquer artefato.
5. Exigir evidência canónica da FASE03 e validação independente antes de desbloquear as fases seguintes.
6. Distinguir código publicado, execução iniciada, execução concluída, evidência persistida e gate aprovado.

## 5. Próximos passos

1. Confirmar o resultado do workflow `COTAHIST 1999 - Recuperar CSV normalizado`.
2. Verificar o SHA-256 do CSV após a correção do parser.
3. Se o hash coincidir, validar separadamente o sidecar e a evidência canónica da FASE03.
4. Se o hash não coincidir, comparar os campos por registo contra a implementação histórica antes de alterar manifesto.
5. Só depois reexecutar FASE05 e FASE06; manter FASE07–08 e o ano 2000 bloqueados até aos respetivos gates.

## 6. Estado no momento do registo

**Incidente aberto.** A correção dos offsets foi publicada, mas a execução de recuperação subsequente ainda estava em fila no GitHub Actions. Não declarar FASE04, FASE05 ou FASE06 como validadas com base apenas neste documento.
