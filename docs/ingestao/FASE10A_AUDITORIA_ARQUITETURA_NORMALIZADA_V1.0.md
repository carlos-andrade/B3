# FASE 10A — Auditoria da Arquitetura NORMALIZED COTAHIST V1.0

**Arquivo:** FASE10A_AUDITORIA_ARQUITETURA_NORMALIZADA_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_AUDITORIA_ARQUITETURA_NORMALIZADA_V1.0.md  
**Data de criação:** 27/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Escopo

Auditoria dos workflows e scripts responsáveis por certificação anual e publicação do Dataset Oficial, para determinar se os CSVs normalizados anuais são artefatos permanentes ou artefatos de execução.

## 2. Evidências verificadas

### Workflow de certificação

`.github/workflows/cotahist-certificacao-anual-v1.yml`

O workflow:

1. executa `scripts/ingestao/certificar_cotahist_anual_v1.py`;
2. grava somente `dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv`;
3. publica a matriz como artifact por 30 dias.

Ele **não cria nem persiste CSVs anuais normalizados**.

### Script de certificação

`scripts/ingestao/certificar_cotahist_anual_v1.py`

O script consulta:

- RAW anual;
- quality manifest.

Não lê o CSV normalizado. A certificação estrutural é derivada do manifesto.

### Workflow do Dataset Oficial

`.github/workflows/cotahist-dataset-oficial-v1.yml`

O workflow executa:

`scripts/ingestao/gerar_dataset_oficial_cotahist_v1.py`

e persiste somente:

`dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json`

Também publica esse JSON como artifact por 30 dias.

### Script do Dataset Oficial

`scripts/ingestao/gerar_dataset_oficial_cotahist_v1.py`

O script lê a certificação e os quality manifests e gera referências para:

`dados/cotahist/normalized/COTAHIST_A{ANO}.csv`

Entretanto, ele **não verifica a existência desses CSVs** antes de gravar o caminho no manifesto.

## 3. Constatação arquitetural

Existe uma divergência objetiva entre:

**Contrato V1.0:**  
> “O manifesto é o catálogo; os CSVs normalizados são os dados.”

e a implementação:

**Gerador V1.0:**  
gera caminhos de CSV normalizado sem testar sua existência.

Além disso, o workflow de certificação não gera os CSVs normalizados e o workflow do Dataset Oficial também não os gera.

Portanto, a arquitetura atual demonstra:

**RAW → quality manifest → certificação → manifesto oficial**

mas **não demonstra no repositório**:

**RAW → NORMALIZED CSV persistente → Dataset Oficial**

## 4. Consequência

O problema identificado anteriormente não é um caso de 1987.

É uma lacuna de contrato/implementação que afeta os **41 anos de 1986–2026**.

Os hashes `normalized_sha256` presentes nos manifests continuam sendo evidência útil e auditável, mas não tornam o CSV fisicamente disponível.

## 5. Decisão

**NÃO REGENERAR OS 41 CSVs NESTA ETAPA.**

Antes disso, deve ser estabelecido o contrato definitivo da camada NORMALIZED.

A opção tecnicamente mais segura para o repositório, considerando o volume histórico, é separar explicitamente:

- **RAW versionado**;
- **manifesto/quality versionado**;
- **artefato normalizado reproduzível**;
- **dataset oficial consumível**.

Se os CSVs normalizados forem necessários para consumo direto do dashboard, devem ser publicados de forma controlada e com validação de existência + SHA-256.

Se forem artefatos de execução, o Dataset Oficial deve referenciar o mecanismo de recuperação/reprodução em vez de caminhos físicos inexistentes.

## 6. Correção que NÃO deve ser feita ainda

Não alterar o gerador V1.0 para simplesmente exigir `Path.is_file()` sem antes definir a política de persistência.

Isso faria o workflow começar a falhar corretamente, mas não resolveria o contrato arquitetural.

## 7. Próxima frente

A próxima etapa deve auditar o **produtor original da normalização** e seus workflows, identificando:

1. onde os CSVs são gerados;
2. se são publicados como artifacts;
3. retenção dos artifacts;
4. se são usados pelo Dataset Corrente;
5. se o dashboard lê CSV, artifact ou manifesto;
6. se existe mecanismo de reconstrução determinística.

**Status:** AUDITORIA ARQUITETURAL CONCLUÍDA — DECISÃO DE PERSISTÊNCIA PENDENTE.

**Regra:** nenhum CSV anual será recriado em massa antes dessa decisão.
