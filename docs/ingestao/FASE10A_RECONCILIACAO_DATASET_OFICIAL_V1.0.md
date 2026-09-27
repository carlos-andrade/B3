# FASE 10A — Reconciliação do Dataset Oficial COTAHIST V1.0

**Arquivo:** FASE10A_RECONCILIACAO_DATASET_OFICIAL_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_RECONCILIACAO_DATASET_OFICIAL_V1.0.md  
**Data de criação:** 27/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Verificar, antes de qualquer reprocessamento, se os artefatos declarados pelo Dataset Oficial existem no repositório e se a arquitetura publicada corresponde ao estado real dos dados.

## 2. Verificação executada

Foram consultados diretamente os seguintes componentes:

- `dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json`;
- `dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json`;
- `dados/cotahist/normalized/`;
- `dados/cotahist/normalized/anual/`;
- `dados/cotahist/normalized/diario/`;
- `dados/cotahist/normalized/manifests/`;
- `dados/cotahist/normalized/manifests/diario/`.

Nenhum arquivo de dados foi alterado nesta etapa.

## 3. Resultado principal

### 3.1 Dataset Oficial V1.0

O arquivo V1.0 declara, para 1987, entre outros campos:

- `normalized_file`: `dados/cotahist/normalized/COTAHIST_A1987.csv`;
- `normalized_sha256`: `5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`;
- `linhas_normalized`: 130665;
- primeira data: 1987-01-02;
- última data: 1987-12-30;
- 25 campos.

O manifesto de qualidade de 1987 confirma os mesmos valores.

Entretanto, o arquivo `dados/cotahist/normalized/COTAHIST_A1987.csv` **não está versionado nesse caminho**. Também não existe `dados/cotahist/normalized/anual/COTAHIST_A1987.csv`.

Portanto, o SHA-256 e a contagem estão documentados, mas o artefato CSV correspondente não está atualmente disponível no caminho declarado pelo V1.0.

### 3.2 Diretório anual normalizado

A pasta `dados/cotahist/normalized/anual/` contém apenas `.gitkeep`.

Isso confirma que os CSVs anuais normalizados não estão sendo mantidos nessa pasta no estado atual do repositório.

### 3.3 Dataset corrente V1.1

Existe um Dataset Corrente mais recente:

`dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json`

Ele está marcado como:

- `status: VIGENTE`;
- `status_frescor: VALIDADO`;
- `generated_at_utc: 2026-09-27T13:04:22.804727+00:00`;
- `ano_corrente: 2026`;
- `ultima_data: 2026-09-25`;
- `fail_closed: true`.

A composição declarada é:

**snapshot anual 2026 + incrementos diários posteriores ao snapshot**.

O snapshot anual 2026 registra:

- última data: 2026-09-22;
- 2.904.013 linhas;
- SHA-256 normalizado: `d97514f3224da3b70b5b890911c7383e86a6d69ffc5482eb610826d729b2a1fa`.

Os incrementos de 23, 24 e 25/09/2026 possuem CSVs normalizados versionados em `dados/cotahist/normalized/diario/`.

Os respectivos RAWs também estão presentes em `dados/cotahist/raw/diario/`.

## 4. Correção de interpretação

A ausência dos CSVs anuais em `normalized/anual/` não deve ser tratada automaticamente como falha da normalização.

A evidência disponível indica uma arquitetura em que:

1. RAW anual é preservado;
2. manifesto de normalização/qualidade registra o resultado;
3. CSV anual pode ter sido produzido como artefato de workflow, sem permanência no Git;
4. o Dataset Corrente V1.1 utiliza explicitamente um snapshot anual identificado por manifesto e incrementos diários versionados.

O ponto que permanece aberto é outro:

> **O Dataset Oficial V1.0 declara caminhos de CSV anual que não existem atualmente no repositório.**

Isso precisa ser reconciliado antes de qualquer camada downstream tratar esses caminhos como arquivos físicos disponíveis.

## 5. Estado da FASE 10A

**RESULTADO: RECONCILIAÇÃO PARCIALMENTE CONCLUÍDA.**

### Confirmado

- RAW 1987 preservado;
- SHA-256 RAW confirmado no manifesto;
- normalização 1987 documentada;
- SHA-256 normalizado documentado;
- contagem e intervalo de datas documentados;
- manifesto de qualidade presente;
- CSVs diários recentes de 2026 presentes;
- Dataset Corrente V1.1 existente e vigente.

### Pendente

- definir formalmente se CSVs anuais normalizados são artefatos permanentes ou artefatos de execução;
- corrigir ou versionar os caminhos declarados pelo Dataset Oficial V1.0;
- verificar todos os demais caminhos declarados pelo V1.0;
- verificar a integração do Dataset Corrente V1.1 com o dashboard;
- somente depois, decidir se o CSV anual de 1987 deve ser regenerado/versionado ou se o manifesto deve ser a referência oficial.

## 6. Regra de governança

Não será criado um CSV anual apenas para satisfazer um caminho declarado sem antes determinar a arquitetura oficial de persistência.

Não será alterado nenhum SHA-256 documentado.

Não será considerado que um arquivo está disponível apenas porque seu hash está registrado em manifesto.

A distinção entre **artefato reproduzível**, **artefato versionado** e **artefato oficial consumível** deve permanecer explícita.

## 7. Próxima frente

A próxima verificação deve ser uma **auditoria completa de referências do Dataset Oficial V1.0**, seguida da reconciliação com o Dataset Corrente V1.1.

Somente após essa auditoria deverá ser tomada a decisão de publicação/correção dos artefatos anuais.

**Status:** FRENTE 10A — RECONCILIAÇÃO INICIAL CONCLUÍDA; AUDITORIA DE REFERÊNCIAS PENDENTE.


## 8. Auditoria integral das referências V1.0

Foi realizada uma verificação sobre a árvore Git do branch `main), comparando as 41 entradas do Dataset Oficial V1.0 com os caminhos físicos declarados.

Resultado:

| Componente | Resultado |
|---|---:|
| Registros anuais declarados | 41 |
| RAW anual existente | 41/41 |
| Manifesto de qualidade existente | 41/41 |
| CSV normalizado anual no caminho declarado | 0/41 |
| CSV normalizado anual em `normalized/anual/` | 0/41 |

Portanto, a inconsistência não é exclusiva de 1987.

**Constatação:** o Dataset Oficial V1.0 declara 41 arquivos normalizados anuais como se fossem artefatos físicos permanentes do repositório, mas nenhum dos 41 está atualmente versionado nesses caminhos.

Isso altera a interpretação da FASE 10A: não estamos diante de um problema isolado do COTAHIST 1987, mas de uma **inconsistência arquitetural entre o manifesto do Dataset Oficial V1.0 e a camada física versionada do repositório**.

Os hashes normalizados continuam sendo evidência documental de resultados anteriormente produzidos, mas não podem ser tratados como prova de que os respectivos CSVs estão atualmente disponíveis para consumo direto no Git.

## 9. Decisão técnica provisória

Não regenerar 41 CSVs imediatamente.

Primeiro deve ser identificado qual é o contrato oficial de persistência:

**A.** CSV anual é artefato permanente e consumível → os 41 arquivos precisam existir e seus hashes precisam ser reconfirmados.

**B.** CSV anual é artefato transitório de workflow → o Dataset Oficial V1.0 deve deixar de apontar para arquivos inexistentes e passar a referenciar manifestos/artefatos reproduzíveis de forma explícita.

A decisão deve ser tomada antes da construção de qualquer camada analítica ou dashboard que dependa desses caminhos.

