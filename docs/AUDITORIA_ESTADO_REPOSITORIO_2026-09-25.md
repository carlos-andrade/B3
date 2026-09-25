# AUDITORIA DE ESTADO DO REPOSITÓRIO — PONTO ZERO DA FASE DE CONSOLIDAÇÃO

**Arquivo:** AUDITORIA_ESTADO_REPOSITORIO_2026-09-25.md  
**Projeto:** B3 — A BOLSA DO BRASIL  
**Caminho:** docs/AUDITORIA_ESTADO_REPOSITORIO_2026-09-25.md  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3  
**Status:** VIGENTE COMO DIAGNÓSTICO DE BASE  
**Versão:** 1.0

## 1. Resultado executivo

A auditoria confirma que a base COTAHIST anual possui arquivos RAW de **1986 a 2026**, sem lacunas aparentes na estrutura anual observada.

A camada de manifests NORMALIZED possui evidências `quality.json` para os anos de **1986 a 2026**, totalizando 41 anos na estrutura do repositório.

Os manifests amostrados diretamente — 1986, 1990, 2000, 2005, 2010, 2011, 2012, 2015, 2020, 2024, 2025 e 2026 — apresentam status **VALIDADO**, parser 1.1.0, 25 campos e datas dentro do ano.

Isso demonstra que a infraestrutura histórica está substancialmente mais avançada do que a situação dos workflows antigos poderia sugerir.

## 2. RAW COTAHIST

Diretório:

`dados/cotahist/raw/anual/`

Foram confirmados arquivos:

**COTAHIST_A1986.ZIP → COTAHIST_A2026.ZIP**

A sequência anual observada é contínua de 1986 a 2026.

## 3. NORMALIZED / MANIFESTS

Diretório:

`dados/cotahist/normalized/manifests/`

A estrutura contém, para cada ano observado:

- checksum do CSV normalizado;
- quality manifest;
- em vários anos, auditoria de duplicidades.

Os manifests contêm:

- status;
- ano;
- versão do parser;
- fonte;
- RAW SHA-256;
- arquivo normalizado;
- NORMALIZED SHA-256;
- quantidade de linhas;
- quantidade de campos;
- primeira data;
- última data;
- datas inválidas;
- datas fora do ano.

## 4. Evidência amostrada

| Ano | Status | Linhas normalizadas | Primeira data | Última data |
|---:|---|---:|---|---|
| 1986 | VALIDADO | 177.981 | 1986-01-02 | 1986-12-30 |
| 1990 | VALIDADO | 108.626 | 1990-01-02 | 1990-12-28 |
| 2000 | VALIDADO | 153.682 | 2000-01-03 | 2000-12-28 |
| 2005 | VALIDADO | 181.408 | 2005-01-03 | 2005-12-29 |
| 2010 | VALIDADO | 287.480 | 2010-01-04 | 2010-12-30 |
| 2011 | VALIDADO | 298.370 | 2011-01-03 | 2011-12-29 |
| 2012 | VALIDADO | 330.633 | 2012-01-02 | 2012-12-28 |
| 2015 | VALIDADO | 414.177 | 2015-01-02 | 2015-12-30 |
| 2020 | VALIDADO | 1.251.646 | 2020-01-02 | 2020-12-30 |
| 2024 | VALIDADO | 2.635.561 | 2024-01-02 | 2024-12-30 |
| 2025 | VALIDADO | 3.174.698 | 2025-01-02 | 2025-12-30 |
| 2026 | VALIDADO | 2.904.013 | 2026-01-02 | 2026-09-22 |

**Nota:** esta tabela é uma amostragem de evidência, não uma certificação estatística independente de todos os 41 anos.

## 5. Workflows

A auditoria identificou **479 execuções históricas** do GitHub Actions no endpoint consultado.

Há forte concentração em workflows de investigação de 1986.

Também existem workflows gerais para:

- normalização controlada;
- catálogo B3;
- Copom;
- captura/pesquisa de pregão;
- classificação BVBG.028;
- inventário BVBG.028;
- validação BVBG.028.

### 5.1 Ponto crítico

As execuções históricas dos workflows:

- `cotahist-normalizacao-2011-2026.yml`
- `cotahist-normalizacao-2011-2026-v2.yml`
- `cotahist-normalizacao-2011-2026-v3.yml`

apresentaram falhas nas execuções consultadas.

Entretanto, esses caminhos não aparecem atualmente na listagem de workflows presentes no diretório `.github/workflows/`.

Portanto, **não devemos interpretar essas falhas históricas como prova de que a base 2011–2026 atual esteja inválida**.

A existência dos manifests atuais e seus status deve ser analisada separadamente das execuções antigas.

## 6. Workflow de normalização atualmente presente

O workflow:

`.github/workflows/cotahist-normalizacao-controlada-v7.yml`

executa:

RAW ZIP → `normalize_cotahist.py` → CSV → SHA-256 → `validar_normalized.py` → quality manifest

e publica os manifests no repositório.

Contudo, atualmente ele está configurado com **workflow_dispatch**, recebendo explicitamente o ano.

Isso significa que a normalização controlada V7 é reproduzível, mas **não é, neste momento, um processo automático periódico para todos os anos**.

Essa distinção é importante.

## 7. 1986

A auditoria confirma a existência de evidência NORMALIZED para 1986 com status VALIDADO.

Paralelamente, o histórico de commits registra o encerramento operacional da FASE 09C de 1986 como exceção histórica.

Portanto, devemos separar:

**validade estrutural do arquivo normalizado**

de

**resolução completa de todas as questões semânticas históricas investigadas em 1986**.

Não devemos transformar um status de normalização em certificado absoluto de toda a semântica histórica.

## 8. Diagnóstico

O estado atual deve ser classificado como:

### BASE HISTÓRICA
**SUBSTANCIALMENTE CONSTRUÍDA**

### NORMALIZAÇÃO
**OPERACIONALMENTE DISPONÍVEL**

### EVIDÊNCIA DE QUALIDADE
**DISPONÍVEL PARA TODOS OS ANOS 1986–2026 NA ESTRUTURA DE MANIFESTS**

### AUTOMAÇÃO
**PARCIALMENTE CONSOLIDADA**

### WORKFLOWS ANTIGOS
**EXISTEM FALHAS HISTÓRICAS QUE NÃO DEVEM SER CONFUNDIDAS COM O ESTADO ATUAL**

### 1986
**EXCEÇÃO HISTÓRICA CONTROLADA**

### CERTIFICAÇÃO GLOBAL
**AINDA NÃO CONCLUÍDA**

## 9. Próxima ação obrigatória

Não criar outro conjunto de workflows de investigação.

A próxima frente deverá ser:

**CONSOLIDAÇÃO DO PIPELINE COTAHIST**

com quatro objetivos:

1. identificar o workflow canônico;
2. definir se a normalização anual deve ser automática;
3. separar workflows históricos de workflows operacionais;
4. criar uma matriz oficial de certificação por ano.

## 10. Critério de encerramento desta auditoria

Esta auditoria estabelece o ponto zero da fase de consolidação.

A partir dela, decisões posteriores deverão usar este diagnóstico como referência e não repetir investigações já encerradas sem nova evidência.

---

**Conclusão:** o projeto não está diante de uma base inexistente ou de uma ingestão ainda embrionária. Existe uma base RAW anual de 1986–2026 e uma camada de manifests de qualidade cobrindo os mesmos anos. O principal problema agora é transformar essa infraestrutura existente em um pipeline operacional único, automático, auditável e claramente certificado.
