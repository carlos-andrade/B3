# WATCHDOG — Supervisão operacional do projeto B3

**Padrão central:** [GOVERNANCA/WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/tree/main/WATCHDOG)  
**Estado local:** piloto operacional em teste; última avaliação de atualidade: **8 PASS, 0 STALE, 0 UNKNOWN**. Os limiares permanecem provisórios, e a supervisão externa do próprio monitor ainda está pendente.

## Âmbito inicial

O projeto B3 tem um workflow de monitorização de execuções GitHub Actions:

- Workflow: [B3 - Monitor independente de execuções V1](../.github/workflows/b3-monitor-execucoes-v1.yml)
- Guia de heartbeat externo: [heartbeat-supervisor-externo.md](heartbeat-supervisor-externo.md)
- Cadência declarada: a cada 15 minutos, além de execução manual.
- Janela analisada: últimas 24 horas.
- Sinais recolhidos: execuções desfavoráveis e execuções ainda ativas.
- Evidência: JSON e Markdown publicados como artefacto GitHub Actions, com retenção configurada de 30 dias.
- Alerta: cria ou atualiza uma issue aberta para execuções desfavoráveis.
- Permissões declaradas: leitura de Actions e contents; escrita de issues apenas para o fluxo de alertas.

## Estado e limitações conhecidas

A configuração do workflow e a execução da validação do inventário estão confirmadas. Os relatórios do monitor são publicados como artefactos com retenção configurada de 30 dias; os artefactos do GitHub não são um arquivo imutável nem uma garantia de retenção permanente. Os alertas são issues do GitHub, não notificações externas; confirmação de receção e SLA de escalonamento ainda não estão implementados. Os hooks de heartbeat externo estão preparados, mas a supervisão só ficará ativa depois de configurar as secrets `WATCHDOG_HEARTBEAT_WORKFLOWS_URL` e `WATCHDOG_HEARTBEAT_DATA_URL` e validar o serviço externo. Consulte o [guia de supervisão externa](heartbeat-supervisor-externo.md).

O resultado `FAVORAVEL` significa apenas que, na janela analisada pelo script, não foram encontrados resultados desfavoráveis nem execuções ativas. Não é certificação global da qualidade dos dados B3.

## Monitorização da atualidade dos dados

Foi adicionado o avaliador [check_data_freshness.py](engine/check_data_freshness.py), com catálogo explícito de limites em [datasets-monitorizados.json](registry/datasets-monitorizados.json). A verificação lê datas de observação declaradas nos manifestos; não transforma timestamps de ingestão em datas de mercado. O workflow [WATCHDOG de atualidade dos dados](../.github/workflows/watchdog-data-freshness.yml) executa testes, publica JSON/Markdown como artefacto de 30 dias e cria/atualiza uma issue quando identifica datasets fora do limite.

**Primeira avaliação real (2026-10-13): 5 PASS, 1 STALE e 1 UNKNOWN.** A primeira execução encontrou BDI DailyAverageStocks em 2026-09-22 (21 dias), acima do limite de 5 dias, e abriu a [issue de atualidade #8](https://github.com/carlos-andrade/B3/issues/8). A captura automática foi corrigida e encontrou registos válidos em **2026-10-09**, preservando RAW, SHA-256 e manifesto em [dados/bdi/manifests/DailyAverageStocks/2026-10-09_page_0001.json](../dados/bdi/manifests/DailyAverageStocks/2026-10-09_page_0001.json). [Execução da captura BDI](https://github.com/carlos-andrade/B3/actions/runs/38387032896).

O manifesto anual COTAHIST 2026 declara a última data de observação **2026-09-23**, suportada pelo manifesto de qualidade NORMALIZED e pelo registo de reconciliação. O catálogo monitoriza também os manifestos diários COTAHIST, separadamente do snapshot anual. A reavaliação concluiu **8 PASS, 0 STALE e 0 UNKNOWN**, dentro dos limites configurados. [Execução de reavaliação](https://github.com/carlos-andrade/B3/actions/runs/38387593511). A [issue #8](https://github.com/carlos-andrade/B3/issues/8) permanece aberta para revisão humana e aprovação dos limiares.

**Importante:** todos os limiares atuais estão marcados como **PROVISIONAL** e ainda precisam de aprovação dos proprietários das séries. Um resultado PASS significa apenas que as datas observadas ficaram dentro dos limites configurados; não certifica integralmente a qualidade do negócio.

## Registos

- [Inventário local](registry/sistemas-monitorizados.json)
- [Controlos obrigatórios](registry/controlos-obrigatorios.json)
- [Norma central](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md)

## Próximos passos do piloto

1. Aprovar os limiares provisórios por dataset com os respetivos proprietários e atualizar o catálogo com a decisão.
2. Configurar `WATCHDOG_HEARTBEAT_WORKFLOWS_URL` e `WATCHDOG_HEARTBEAT_DATA_URL` com serviço externo independente; testar heartbeat ausente.
3. Definir confirmação de receção, responsáveis, SLA e escalonamento dos alertas.
4. Rever o ruído de alertas das execuções falhadas no histórico e documentar a política de classificação.
5. Expandir a reconciliação de integridade, hashes e continuidade de dados COTAHIST/BCB/BDI.
6. Registar a aceitação humana antes de declarar o piloto operacional completo.
