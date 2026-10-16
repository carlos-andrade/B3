# B3 — A BOLSA DO BRASIL

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-B33563055168 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_RECALCULO_POS_AUDITORIA |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Repositório central de pesquisa, ingestão, normalização, certificação e disponibilização de dados relacionados ao mercado brasileiro.

> **Estado do projeto:** ativo e em evolução contínua.  
> **Branch principal:** `main`  
> **Última atualização deste README:** 16/10/2026

### Estado semântico e governança — 16/10/2026

- A divergência normativa GOV-DIV-001 tem decisão versionada em [DECISÃO GOV-DIV-001](./docs/governanca/decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md).
- A [matriz integral de revisão semântica](./docs/governanca/auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md) acompanha 303 documentos do snapshot inicial. A fila original de 281 documentos pendentes foi revista nos Lotes 05–26 e reconciliada no Lote 27; permanecem abertas a revalidação de 17 documentos previamente revistos após GOV-DIV-001, a revisão integral dos quatro relatórios antes amostrais e as ações residuais por domínio. Não declarar encerramento semântico global apenas com base no fecho da fila original.
- A auditoria SHA-256 comprova integridade canónica, não a validade semântica ou operacional do conteúdo.
- COTAHIST 1986–2025 permanece em consulta/read-only; 2026 mantém atualização diária.
- A proveniência RAW COTAHIST, a lista oficial ExternalSecurityCategoryCode e os controlos operacionais WATCHDOG permanecem frentes próprias, com estado explícito no roadmap.


---

## 1. Objetivo

O projeto **B3 — A BOLSA DO BRASIL** foi estruturado para construir uma base de dados de mercado **auditável, reproduzível e historicamente consistente**, reunindo dados de negociação, instrumentos, índices, calendário econômico e informações macroeconômicas.

A arquitetura prioriza:

- dados verificáveis e rastreáveis;
- separação entre dado bruto, normalizado e certificado;
- preservação da proveniência;
- validações automáticas;
- reconciliação entre fontes e camadas;
- automação por GitHub Actions;
- documentação das decisões e contratos de dados;
- disponibilização dos resultados para pesquisa quantitativa, análise de mercado e futuras aplicações.

O princípio central é simples:

> **Não transformar ausência de informação em informação.**

## WATCHDOG — monitorização transversal

O projeto adota o padrão central [WATCHDOG da GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/tree/main/WATCHDOG). O [monitor de execuções GitHub Actions](./WATCHDOG/README.md) e o [avaliador de atualidade](./.github/workflows/watchdog-data-freshness.yml) publicam evidências e alertas, mas os artefactos têm retenção limitada e não constituem arquivo imutável. A avaliação histórica de 8 PASS, 0 STALE e 0 UNKNOWN no [run 38387593511](https://github.com/carlos-andrade/B3/actions/runs/38387593511) descreve apenas aquela execução. Os limiares continuam provisórios; a supervisão externa depende de secrets e serviço externo, e ACK/escalonamento/retensão duradoura ainda exigem validação. Consulte [WATCHDOG — estado e limitações](./WATCHDOG/README.md), [fecho da Fase C](./WATCHDOG/FASE_C_FECHAMENTO_OPERACAO_GOVERNANCA_2026-10-15.md) e [Issue #11](https://github.com/carlos-andrade/B3/issues/11).

---

## 2. O que já existe

### Dados de mercado

A camada de dados está organizada em [`dados/`](./dados/), incluindo:

- [BCB/SGS](./dados/bcb_sgs)
- [BDI](./dados/bdi)
- [Calendário econômico](./dados/calendario_economico)
- [COTAHIST](./dados/cotahist)
- [Fontes](./dados/fontes)
- [Market Data](./dados/market_data)

### Universo de ativos

O catálogo de ativos está organizado em [`ativos/`](./ativos), contemplando, entre outras categorias:

- ações;
- BDRs;
- ETFs;
- FIIs;
- fundos;
- futuros;
- índices;
- juros;
- moedas;
- opções;
- renda fixa;
- termo;
- commodities;
- criptoativos;
- balcão;
- empréstimo de ativos;
- catálogo e classificação de instrumentos.

Consulte também o [README da camada de ativos](./ativos/README.md).

---

## 3. COTAHIST — base histórica

O **COTAHIST** é uma das camadas centrais do projeto.

O pipeline existente contempla etapas de:

1. captura/importação;
2. preservação do dado de origem;
3. análise estrutural;
4. identificação de calendário;
5. validação de chaves;
6. análise de quantidade, volume e preço;
7. análise de OHLC;
8. reconciliação RAW × NORMALIZED;
9. validação semântica;
10. certificação anual;
11. persistência de datasets normalizados;
12. atualização automática.

A importação diária já está integrada ao repositório por workflow automatizado.

Referências principais:

- [Dados COTAHIST](./dados/cotahist)
- [Scripts de ingestão](./scripts/ingestao)
- [Workflows COTAHIST](./.github/workflows)
- [Contrato de normalização anual](./governanca)
- [Carta de confiança dos workflows](./governanca/CARTA_DE_CONFIANCA_WORKFLOWS.md)

### Dataset Oficial

O projeto mantém uma camada específica para o **Dataset Oficial COTAHIST**, separada das análises exploratórias.

O objetivo dessa separação é impedir que uma hipótese de pesquisa seja confundida com dado certificado.

---

## 4-A. Política incremental permanente

A base B3 é atualizada por incrementos e não depende apenas de snapshots. Para COTAHIST, os incrementos diários são preservados, validados e incorporados sem substituir RAW histórico.

**Isolamento de projetos:** BLOOMBERG_MAIL está fora do âmbito operacional atual do repositório B3. A carta de recebimento incremental de 2026-10-08 é preservada apenas como histórico e foi marcada como não aplicável à execução corrente. Não há autorização vigente neste README para transferir dados, criar dependências de workflow ou integrar os dois repositórios. Qualquer integração futura exige decisão explícita, versionada e aprovada. A atualização diária COTAHIST de B3 é gerida pelos próprios workflows e contratos B3.

---

## 4. Ingestão automática

A automação está concentrada principalmente em:

[`.github/workflows/`](./.github/workflows)

e

[`scripts/ingestao/`](./scripts/ingestao)

Entre os processos existentes estão rotinas relacionadas a:

- importação diária do COTAHIST;
- normalização;
- certificação anual;
- reconciliação;
- BCB/SGS;
- COPOM;
- calendário econômico;
- índices B3;
- BDI;
- dados de pregão;
- negócio a negócio;
- análises históricas do COTAHIST.

Os workflows devem ser tratados como parte da infraestrutura do projeto, e não como scripts descartáveis.

---

### 4.1 Atualização automática do README

O próprio README possui uma rotina de manutenção automatizada para evitar que a documentação operacional fique defasada em relação ao repositório.

Componentes:

- [Workflow de atualização do README](./.github/workflows/atualizar-readme-b3.yml)
- [Rotina de sincronização](./scripts/ingestao/atualizar_readme_b3.py)

O mecanismo:

1. monitora alterações relevantes em workflows, governança, scripts de ingestão, catálogo de ativos, dados normalizados/certificados e dashboard;
2. executa também uma verificação programada diária;
3. recalcula o inventário operacional;
4. atualiza somente o bloco do README controlado pela automação;
5. não altera o conteúdo editorial fora desse bloco;
6. não cria commit quando o README já está sincronizado;
7. exclui dados RAW volumosos do gatilho automático para evitar commits desnecessários;
8. permite execução manual por workflow_dispatch.

A automação é **idempotente**: executar novamente sem mudança relevante não deve gerar novo commit.

---

## 5. Governança e confiança

A camada de governança está em [`governanca/`](./governanca).

Documento central:

**[Carta de Confiança dos Workflows](./governanca/CARTA_DE_CONFIANCA_WORKFLOWS.md)**

A governança também inclui mecanismos para:

- garantia de atualização dos dados;
- certificação de domínios;
- diagnóstico de frescor;
- matriz global de frescor;
- inventário dos índices B3;
- documentação da camada BCB/SGS;
- rastreabilidade das decisões de ingestão.

A regra operacional é:

> **Antes de usar um dado para análise, verificar sua origem, período, estado de atualização, transformação aplicada e evidência de validação.**

---

## 6. Índices B3

A composição dos índices possui camada própria de ingestão e governança.

Referências:

- [Governança dos índices B3](./governanca/indices_b3)
- [Inventário dos índices B3](./governanca/indices_b3/INVENTARIO_INDICES_B3_V1.md)
- [Workflow de composição dos índices](./.github/workflows/indices-b3-composicao-v1.yml)

As rotinas utilizam a fonte oficial da B3 quando aplicável e registram a evolução das carteiras, inclusive situações de pré-publicação da próxima carteira.

---

## 7. BCB, COPOM e núcleo macroeconômico

A camada macroeconômica inclui dados do Banco Central do Brasil e rotinas associadas ao COPOM.

Referências:

- [BCB/SGS](./dados/bcb_sgs)
- [Governança BCB/SGS](./governanca/bcb_sgs)
- [Workflow BCB/SGS — núcleo macro](./.github/workflows/bcb-sgs-nucleo-macro-v1.yml)
- [Workflow de captura COPOM](./.github/workflows/capturar-bcb-copom.yml)

Esses dados serão utilizados como contexto macroeconômico para análises posteriores de mercado, sempre mantendo separadas:

- observação;
- dado histórico;
- interpretação;
- hipótese;
- inferência.

---

## 8. Dashboard

O repositório possui uma interface web em:

**[`index.html`](./index.html)**

O painel, denominado **B3 Data Observatory**, lê a árvore pública do próprio repositório em tempo de execução e apresenta, entre outros elementos:

- quantidade de arquivos de dados;
- anos identificados;
- dados estruturados;
- arquivos de mercado;
- Dataset Oficial COTAHIST;
- snapshots/indicadores publicados;
- amostras de arquivos estruturados;
- informações de proveniência.

### Acesso direto

**[Abrir o B3 Data Observatory](./index.html)**

Quando o GitHub Pages estiver habilitado para este repositório, o mesmo arquivo poderá servir como ponto de entrada público do observatório.

---

## 9. Arquitetura conceitual

A arquitetura do projeto segue, de forma geral, este fluxo:

```text
FONTES
  │
  ├── B3
  ├── BCB
  ├── IBGE
  └── outras fontes documentadas
       │
       ▼
CAPTURA / INGESTÃO
       │
       ▼
DADO BRUTO / RAW
       │
       ▼
NORMALIZAÇÃO
       │
       ▼
VALIDAÇÃO
       │
       ├── estrutura
       ├── calendário
       ├── chaves
       ├── semântica
       ├── duplicidades
       └── reconciliação
       │
       ▼
CERTIFICAÇÃO
       │
       ▼
DATASETS PUBLICADOS
       │
       ├── pesquisa
       ├── análise quantitativa
       ├── dashboard
       └── futuras aplicações
```

---

## 10. Princípios de análise

O repositório não deve ser tratado como uma coleção de indicadores prontos.

A pesquisa futura deverá privilegiar, conforme disponibilidade dos dados:

- preço;
- retorno;
- volume financeiro;
- quantidade;
- volatilidade;
- VWAP;
- TWAP;
- fluxo;
- agressão;
- Cumulative Delta;
- liquidez;
- gaps;
- Fair Value Gaps (FVG);
- estrutura de mercado;
- calendário econômico;
- política monetária;
- Ibovespa;
- juros;
- câmbio;
- correlações entre mercados;
- comportamento institucional inferido a partir de dados observáveis.

**Indicadores e hipóteses não substituem o dado primário.**

---

## 11. Pesquisa quantitativa

A finalidade desta infraestrutura é permitir que hipóteses de mercado sejam transformadas em processos testáveis.

Para qualquer setup ou estratégia, a documentação deverá buscar especificar:

1. hipótese;
2. universo;
3. período;
4. fonte dos dados;
5. transformação aplicada;
6. regra de entrada;
7. regra de saída;
8. invalidação;
9. custos;
10. slippage;
11. tamanho da posição;
12. drawdown;
13. risco/retorno;
14. amostra;
15. período de teste;
16. resultados;
17. limitações;
18. possibilidade de reprodução.

**Nenhum backtest deve ser tratado como garantia de resultado futuro.**

---

## 12. Regras de qualidade

### Não fazer

- preencher lacunas com zeros sem justificativa;
- misturar dado bruto com dado normalizado;
- substituir fonte oficial por estimativa sem registrar a alteração;
- apagar evidência histórica para “corrigir” um problema;
- apresentar hipótese como fato;
- tratar ausência de dado como dado válido;
- alterar uma série histórica sem preservar a versão anterior;
- considerar um workflow concluído apenas porque foi criado;
- usar resultado não validado como referência definitiva.

### Fazer

- preservar a origem;
- registrar a transformação;
- validar;
- reconciliar;
- certificar quando aplicável;
- documentar exceções;
- registrar falhas;
- versionar decisões;
- manter evidência suficiente para reprodução.

---

## 13. Organização principal

```text
B3/
├── .github/
│   └── workflows/          # automações e pipelines
├── ativos/                 # universo e catálogo de instrumentos
├── dados/                  # dados e datasets
│   ├── bcb_sgs/
│   ├── bdi/
│   ├── calendario_economico/
│   ├── cotahist/
│   ├── fontes/
│   └── market_data/
├── governanca/             # contratos, confiança e certificação
├── scripts/
│   └── ingestao/           # captura, transformação e validação
├── index.html              # B3 Data Observatory
├── PROMPT_MESTRE_B3_799_CARACTERES.md
└── README.md
```

A estrutura acima é uma visão operacional. Novas camadas devem ser documentadas antes de se tornarem dependências permanentes.

---

## 14. Prompt mestre

O projeto mantém uma referência operacional em:

**[PROMPT_MESTRE_B3_799_CARACTERES.md](./PROMPT_MESTRE_B3_799_CARACTERES.md)**

Esse arquivo funciona como referência compacta para a orientação do projeto.

---

## 15. Estado atual

Em **28/09/2026**, o projeto já possui:

- infraestrutura de GitHub Actions;
- ingestão automática de dados;
- pipeline COTAHIST em evolução;
- camada de dados normalizados;
- certificação histórica em andamento;
- catálogo de instrumentos;
- ingestão de índices B3;
- camada BCB/SGS;
- captura relacionada ao COPOM;
- calendário econômico;
- governança de workflows;
- matriz de frescor dos dados;
- dashboard web;
- documentação de contratos e validações.

O projeto continua em desenvolvimento. **A existência de uma rotina no repositório não significa, por si só, que todo o domínio correspondente esteja definitivamente certificado.** O status de cada dataset deve ser determinado pelos seus próprios artefatos de validação e certificação.

---

## 16. Próxima evolução

A evolução do projeto deve seguir uma ordem controlada:

**Fonte → Captura → Persistência → Normalização → Validação → Reconciliação → Certificação → Publicação → Análise.**

Somente depois de uma camada atingir qualidade suficiente deverá ser utilizada como fundamento para modelos quantitativos, estudos de fluxo ou automações de decisão.

---

## 17. Regra permanente do projeto

Todo novo componente relevante deve:

1. possuir localização definida no repositório;
2. possuir nome e versão identificáveis;
3. possuir fonte documentada;
4. possuir método de atualização conhecido;
5. possuir validação compatível com seu propósito;
6. registrar limitações e exceções;
7. preservar a rastreabilidade;
8. atualizar a documentação quando alterar a arquitetura.

O repositório **B3 — A BOLSA DO BRASIL** é a fonte de organização e memória técnica do projeto.

---

<!-- B3_README_AUTO_BEGIN -->
## Atualização automática do README

> Este bloco é gerenciado pelo workflow `Atualizar README — B3`.

- **Última alteração relevante:** `ea2e5294f28c` — 16/10/2026 01:37 UTC
- **Commit de referência:** data(bcb): atualizar nucleo macro SGS
- **Workflows GitHub Actions:** 553
- **Scripts Python em `scripts/ingestao/`:** 119
- **Diretórios operacionais de primeiro nível:** 10

**Escopo monitorado:**

- workflows e automações;
- catálogo e universo de ativos;
- governança e certificação;
- scripts de ingestão;
- dados normalizados e certificados;
- dashboard e documentação operacional.

**Excluído do gatilho automático:** dados RAW volumosos, para evitar commits
desnecessários no README por simples alteração de arquivos brutos.

A automação não substitui a revisão editorial. Ela mantém o inventário operacional
e a trilha de atualização sincronizados com o estado efetivo do repositório.
<!-- B3_README_AUTO_END -->

## 17. Wiki técnica

A documentação técnica versionada do projeto está em WIKI/.

A estrutura atual inclui:

- visão geral e estado atual;
- governança e política de evidências;
- arquitetura;
- automação da Wiki nativa;
- documentação incremental dos pipelines e decisões.

A Wiki nativa do GitHub (/wiki) é tratada como camada de publicação, enquanto WIKI/ permanece como fonte de verdade versionada.

### Sincronização

- evento de push em WIKI/: publicação orientada a evento;
- reconciliação programada: a cada 5 minutos;
- execução manual: workflow_dispatch;
- credencial necessária para publicar na Wiki nativa: B3_WIKI_TOKEN.

O intervalo de 5 minutos é uma reconciliação, não um mecanismo de latência mínima. O caminho principal é o evento de alteração.

Referências:

- WIKI/README.md
- .github/workflows/sincronizar-wiki-b3.yml
- scripts/ingestao/sincronizar_wiki_b3.py
- WIKI/09-AUTOMACAO/WIKI_NATIVA.md


## 18. Regra de atualização após correções de auditoria

A documentação do projeto segue uma ordem obrigatória para evitar que o README registre um estado antes de a governança estar consolidada.

**Ordem vigente:**

**CORREÇÃO → CARTAS NORMATIVAS → EVIDÊNCIAS/INCIDENTES → VERIFICAÇÃO → README.**

As Cartas de Confiança, Carta Magna, Carta de Garantias e Modelo-Mestre devem refletir a correção antes de o README ser atualizado.

### Auditoria COTAHIST — próxima etapa

Antes da execução da próxima auditoria, o projeto deverá estabelecer o **layout aplicável ao período** e suas regras de interpretação. A definição de chave, cardinalidade, unicidade ou qualquer outro critério de bloqueio deverá nascer de:

**fonte oficial → layout → campos/offsets → semântica → hipótese → amostra → teste histórico → decisão normativa → implementação → evidência.**

Erros já corrigidos em auditorias anteriores não podem reaparecer como regras de validação. Os incidentes e suas correções devem ser consultados antes de cada nova fase.

O README documenta o estado consolidado; ele não substitui as cartas nem os artefatos de evidência.

## Licença e uso

Este repositório é destinado a pesquisa, engenharia de dados, análise de mercado e desenvolvimento de ferramentas.

Dados de terceiros permanecem sujeitos às respectivas fontes, licenças, termos de uso e condições de redistribuição.

---

**Projeto:** B3 — A BOLSA DO BRASIL  
**Repositório:** [carlos-andrade/B3](https://github.com/carlos-andrade/B3)  
**Branch principal:** `main`  
**Última revisão do README:** 01/10/2026

## Regra estrutural das fases — 2026-10-01

As fases COTAHIST são **unidirecionais, monotônicas e isoladas**.

- uma fase posterior **não retorna** para executar, corrigir ou reescrever uma fase anterior;
- uma fase anterior **não executa** responsabilidades pertencentes a fases posteriores;
- uma fase posterior consome evidências anteriores em modo somente leitura;
- uma correção permanece na fase que originou o erro;
- descoberta posterior gera incidente/impacto e revisão controlada, sem retrocertificação silenciosa;
- workflows de fases concluídas não devem disparar por alterações genéricas de README/documentação ou por fases posteriores.

**Fluxo obrigatório:** FASE N-1 → evidência → FASE N → evidência → FASE N+1.

A matriz vigente define, entre outras responsabilidades, **FASE06 = semântica/invariantes**, **FASE07 = identidade/chaves/cardinalidade** e **FASE08 = semântica/calendário/consistência**. O ciclo 1994 já fechado permanece preservado como histórico e não deve ser reexecutado apenas para alinhar nomenclatura; novas auditorias devem seguir o contrato atual.

