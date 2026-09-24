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
| 07E | DIMES | Sim | Não localizada | PENDENTE |
| 07F | Colisão K4 | Sim | Não localizada | PENDENTE |
| 07G | Matriz final de identidade | Sim | Não localizada | PENDENTE |

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

## 4. Frentes ainda não comprovadas por evidência

Os seguintes arquivos não foram localizados no branch padrão durante a verificação:

- `dados/cotahist/quality/COTAHIST_1986_DIMES_V1.json`
- `dados/cotahist/quality/COTAHIST_1986_COLISAO_K4_V1.json`
- `dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_FINAL_V1.json`

Consequentemente:

- 07E não é marcada como executada;
- 07F não é marcada como resolvida;
- 07G não é marcada como concluída;
- a FASE 07 global permanece **ABERTA**.

## 5. Integridade dos dados

Nenhuma das análises autoriza alteração de:

- `dados/cotahist/raw/`
- dados normalizados já reconciliados;
- registros históricos originais.

Os resultados são evidências analíticas separadas.

## 6. Próxima ação controlada

A próxima ação deve ser exclusivamente operacional:

1. executar 07E;
2. confirmar a criação do JSON DIMES;
3. executar/confirmar 07F;
4. inspecionar as duas linhas da colisão K4;
5. executar/confirmar 07G;
6. somente então emitir o fechamento formal da FASE 07.

**Não declarar a FASE 07 concluída antes dessas evidências.**
