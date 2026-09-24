# FASE 07 — COTAHIST 1986 — STATUS DE EXECUÇÃO E EVIDÊNCIA

**Projeto:** B3 — A Bolsa do Brasil  
**Escopo:** Identidade histórica COTAHIST 1986  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Registrar de forma auditável quais frentes da FASE 07 possuem evidência JSON efetivamente presente no repositório e quais permanecem pendentes de execução.

Regra: **implementado não significa executado**. Uma frente só pode ser considerada executada quando a evidência resultante estiver presente no caminho esperado e puder ser lida/reconciliada.

## 2. Situação verificada

| Frente | Tema | Implementação | Evidência JSON | Situação |
|---|---|---:|---:|---|
| 07A | Identidade histórica / chaves K1–K4 | Sim | Sim | EXECUTADA |
| 07B | TPMERC | Sim | Sim | EXECUTADA |
| 07C | CODBDI | Sim | Sim | EXECUTADA |
| 07D | CODISI | Sim | Sim | EXECUTADA |
| 07E | DIMES | Sim | Sim | VALIDADA |
| 07F | Colisão K4 | Sim | Sim | EM VALIDAÇÃO |
| 07G | Matriz final de identidade | Sim | Sim | EXECUTADA |

## 3. Evidências verificadas

### 07B — TPMERC

Arquivo:

`dados/cotahist/quality/COTAHIST_1986_TPMERC_V1.json`

Evidência lida no repositório:

- 177.981 registros;
- 9 códigos TPMERC observados;
- 9 códigos documentados pela tabela de referência utilizada;
- 0 códigos desconhecidos.

Distribuição observada:

- 010: 96.479
- 012: 835
- 013: 152
- 017: 99
- 020: 36.021
- 030: 36.596
- 060: 11
- 070: 7.027
- 080: 761

A documentação registra explicitamente que a semântica posterior do layout não é presumida como prova automática da semântica original de 1986.

### 07C — CODBDI

Arquivo:

`dados/cotahist/quality/COTAHIST_1986_CODBDI_V1.json`

Evidência lida no repositório:

- 177.981 registros;
- 15 códigos CODBDI observados;
- 14 mapeados pela tabela documental utilizada;
- 1 não mapeado: **96**.

Distribuição dos principais códigos está preservada integralmente no JSON. O código 96 permanece deliberadamente sem descrição inferida.

### 07D — CODISI

Arquivo:

`dados/cotahist/quality/COTAHIST_1986_CODISI_V1.json`

Evidência lida no repositório:

- 177.981 registros;
- 1.350 CODISI distintos;
- 0 registros em branco;
- 1.350 códigos não brancos.

A regra histórica registrada é crítica:

**Em 1986, CODISI é tratado como código interno do papel, e não como ISIN.**

A documentação B3 consultada registra o início da interpretação ISIN a partir de 15/05/1995. Portanto, não é permitido retroprojetar a semântica moderna para 1986.

## 4. Evidências adicionais — 07E e 07F

### 07E — DIMES

Arquivo: `dados/cotahist/quality/COTAHIST_1986_DIMES_V1.json`

Commit de evidência: `3d68f2ee63cf918bb2e44f746c9281251098034a`

Verificação:
- 177.981 registros;
- 131 DIMES distintos;
- 0 registros DIMES em branco;
- 100% dos campos DIMES com comprimento bruto de 3 bytes;
- RAW e NORMALIZED declarados inalterados.

O workflow 07E teve uma segunda tentativa com falha de publicação por conflito add/add durante rebase; a etapa **Executar análise DIMES** terminou com sucesso. O artefato já havia sido publicado corretamente na primeira tentativa. O workflow foi corrigido para atualizar as ações para Node 24 e fazer `git pull --rebase` antes da preparação do commit.

### 07F — Colisão K4

Arquivo: `dados/cotahist/quality/COTAHIST_1986_COLISAO_K4_V1.json`

A evidência existente foi considerada **não válida para fechamento**, porque o parser anterior mantinha `PREEXE`, `PTOEXE` e `DATVEN` em tipos incompatíveis com a chave K4 consolidada em 07A. O resultado `NO_MATCH` não deve ser usado como conclusão histórica.

Foi corrigido o parser em:
- `scripts/ingestao/investigar_colisao_k4_cotahist_1986_v1.py`
- commit: `0251ef6cad0e1decfff634209e21d87127f87573`

O novo workflow 07F está em execução pendente, run `36036976520`, para gerar a evidência semanticamente reconciliada.

### 07G — Matriz final

A evidência `dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_FINAL_V1.json` permanece válida como consolidação, mas não substitui 07F.

A FASE 07 global permanece **ABERTA** até a validação independente do novo artefato 07F.

## 5. Integridade dos dados

Nenhuma das análises autoriza alteração de:

- `dados/cotahist/raw/`
- dados normalizados já reconciliados;
- registros históricos originais.

Os resultados são evidências analíticas separadas.

## 6. Verificação adicional — 07G

A evidência `dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_FINAL_V1.json` está presente e informa:

- 177.981 registros;
- K4: 177.980 grupos, 177.979 unitários, 1 grupo repetido, 2 linhas no grupo repetido;
- 2.699 CODNEG distintos;
- 1.818 CODNEG com múltiplos contextos de atributos;
- `residual_k4_count = 0` na matriz final;
- RAW e normalizado declarados inalterados;
- encerramento do próprio artefato: `FASE_07G_ANALISE_EXECUTADA`.

**Importante:** esta evidência não substitui o artefato específico 07F. A ausência de `COTAHIST_1986_COLISAO_K4_V1.json` impede declarar a investigação da colisão 07F como validada de forma independente.

## 7. Próxima ação controlada

A próxima ação deve ser exclusivamente operacional:

1. executar/confirmar 07E;
2. confirmar a criação do JSON DIMES;
3. executar/confirmar 07F;
4. inspecionar as duas linhas da colisão K4;
5. somente então emitir o fechamento formal da FASE 07.

**Não declarar a FASE 07 concluída antes dessas evidências.**
