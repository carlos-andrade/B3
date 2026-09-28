# M3-1 — Decisão de armazenamento do NORMALIZED anual COTAHIST V1.0

**Arquivo:** M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** M3-1B CONCLUÍDO — LFS APROVADO — MANIFEST 2026 RECONCILIADO — M3-1C LIBERADO

## 1. Contexto

O Gate M3-0 de capacidade foi executado para o COTAHIST 2026.

Resultado físico:

- NORMALIZED: **392.044.266 bytes**
- limite operacional do gate: **100.000.000 bytes**
- SHA-256 NORMALIZED: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- registros tipo 01: **2.919.760**
- campos: **25**
- primeira data: **2026-01-02**
- última data: **2026-09-23**
- decisão M3-0: **GIT_STANDARD_LIMIT**

A interrupção foi deliberada para impedir persistência inadequada em Git convencional.

## 2. Decisão arquitetural

O mecanismo físico aprovado para NORMALIZED anual acima do limite operacional de Git convencional é **Git LFS**, mantendo:

- caminho lógico canônico;
- versionamento associado ao repositório;
- objeto físico recuperável;
- verificação SHA-256;
- integração com CI;
- fail-closed.

A aprovação global de M3-1 continua condicionada às etapas M3-1C, M3-1D e M3-1E.

## 3. M3-1A — Preparação — CONCLUÍDA

Foi criado o tracking LFS:

`dados/cotahist/normalized/anual/*.csv filter=lfs diff=lfs merge=lfs -text`

Arquivo:

`.gitattributes`

## 4. M3-1B — Prova física 2026 — CONCLUÍDA

Workflow:

`.github/workflows/cotahist-m3-1b-prova-lfs-2026.yml`

Evidência:

- Run: `36419262539`
- Job: `108917764369`
- Commit de persistência: `dcb7dd16649245d0ac3e9f58a1bca521941e7fb1`
- NORMALIZED: **392.044.266 bytes**
- SHA físico: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- LFS materializado fisicamente com sucesso.

Registro:

`docs/ingestao/M3-1B_RESULTADO_PROVA_LFS_2026_2026-09-28.md`

## 5. Reconciliação do manifest — CONCLUÍDA

A investigação identificou a causa da divergência.

O manifest NORMALIZED original foi criado no commit `ccea173449b70c1f2b95a787a04c2020b06fe1f7`, usando RAW SHA:

`e40dc0cdb5ad6315296d88cdb5654240f15412be6fc13e3d47bc8606f9132fee`

Posteriormente, o RAW COTAHIST 2026 foi atualizado no commit:

`e4598cdcdca6a955b4208109fe2fea5f8699fb4b`

com novo SHA:

`4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`

A nova versão do RAW contém dados até **2026-09-23**. O manifest não foi regenerado após essa atualização.

Portanto, a divergência foi classificada como:

**MANIFESTO DEFASADO EM RELAÇÃO AO RAW ATUAL.**

Não há evidência, neste gate, de defeito do parser `1.1.0`.

### Manifest corrigido

- RAW SHA: `4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`
- NORMALIZED SHA: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- linhas: **2.919.760**
- campos: **25**
- primeira data: **2026-01-02**
- última data: **2026-09-23**

Commits da correção:

- Manifest: `2ee46d6028e1bed8be9d350bfca84ae2e46fcd46`
- Checksum: `29a953d789da23fda2741601fa6b0349dc1b8cd5`
- Evidência: `9935e514037a6fb7e9f575dc08307ccfbfcef24b`

Evidência:

`dados/cotahist/quality/COTAHIST_A2026_RECONCILIACAO_MANIFEST_V1.json`

## 6. Automação permanente da reconciliação

Foi criado:

`.github/workflows/cotahist-m3-1b-reconciliar-manifest-2026.yml`

A rotina foi configurada para reagir a alterações do:

- RAW COTAHIST 2026;
- NORMALIZED LFS 2026;
- parser `normalize_cotahist.py`;
- próprio workflow.

A rotina:

1. calcula SHA do RAW atual;
2. reconstrói NORMALIZED;
3. compara SHA do NORMALIZED físico persistido;
4. verifica registros, datas e campos;
5. reconcilia o manifest quando necessário;
6. protege o push contra concorrência;
7. mantém o processo fail-closed.

**Observação:** a instalação da automação foi registrada; sua execução automática posterior deverá ser considerada evidência operacional independente.

## 7. M3-1C — CI — LIBERADO

A reconciliação removeu o bloqueio documental que impedia o próximo gate.

M3-1C deve validar:

- reconstrução determinística;
- SHA;
- existência física;
- materialização LFS;
- conteúdo físico versus ponteiro;
- certificação V2;
- integridade do manifest;
- falha fechada em qualquer divergência.

## 8. M3-1D — Dataset Oficial

Somente após M3-1C:

- validar o Dataset Oficial;
- confirmar acesso ao CSV materializado;
- confirmar bloqueio quando o objeto estiver ausente.

## 9. M3-1E — Aprovação global

Somente após M3-1C e M3-1D:

**M3-1 = APROVADO**

Antes disso, a migração histórica 1986–2025 permanece bloqueada.

## 10. Governança

É proibido:

- persistir NORMALIZED anual em Git convencional acima do limite operacional;
- dividir CSV arbitrariamente;
- reduzir campos para caber;
- deduplicar para reduzir volume;
- alterar RAW para obter um NORMALIZED menor;
- aprovar um manifest apenas por coincidência de SHA sem verificar o RAW atual.

A cadeia oficial permanece:

`RAW → NORMALIZE → SHA → VALIDATE → PERSIST → CERTIFY → RECONCILE`

## 11. Estado atual

- **M3-0:** CONCLUÍDO — GIT_STANDARD_LIMIT
- **M3-1A:** CONCLUÍDO
- **M3-1B:** CONCLUÍDO — PROVA FÍSICA LFS 2026
- **Reconciliação manifest 2026:** CONCLUÍDA
- **M3-1C:** LIBERADO / PRÓXIMO GATE
- **M3-1D:** BLOQUEADO ATÉ M3-1C
- **M3-1E:** BLOQUEADO ATÉ M3-1D
- **M3 histórico 1986–2025:** BLOQUEADO
- **RAW:** PRESERVADO
- **Parser:** 1.1.0
- **NORMALIZED 2026:** PERSISTIDO VIA GIT LFS

## 12. Critério de aprovação M3-1

M3-1 somente poderá ser aprovado quando:

- LFS disponível;
- quota suficiente ou política definida;
- 2026 persistido;
- SHA reproduzível;
- M3-1C aprovado;
- Dataset Oficial validado;
- documentação atualizada;
- RAW preservado;
- nenhuma divergência de integridade permanecer aberta.
