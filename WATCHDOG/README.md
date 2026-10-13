# WATCHDOG — Supervisão operacional do projeto B3

**Padrão central:** [GOVERNANCA/WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/tree/main/WATCHDOG)  
**Estado local:** piloto com evidências de execução em artefactos de 30 dias e alertas rastreáveis por GitHub Issues; supervisão externa do próprio monitor ainda pendente.

## Âmbito inicial

O projeto B3 tem um workflow de monitorização de execuções GitHub Actions:

- Workflow: [B3 - Monitor independente de execuções V1](../.github/workflows/b3-monitor-execucoes-v1.yml)
- Cadência declarada: a cada 15 minutos, além de execução manual.
- Janela analisada: últimas 24 horas.
- Sinais recolhidos: execuções desfavoráveis e execuções ainda ativas.
- Evidência: JSON e Markdown publicados como artefacto GitHub Actions, com retenção configurada de 30 dias.
- Alerta: cria ou atualiza uma issue aberta para execuções desfavoráveis.
- Permissões declaradas: leitura de Actions e contents; escrita de issues apenas para o fluxo de alertas.

## Estado e limitações conhecidas

A configuração do workflow e a execução da validação do inventário estão confirmadas. Os relatórios do monitor são publicados como artefactos com retenção configurada de 30 dias; os artefactos do GitHub não são um arquivo imutável nem uma garantia de retenção permanente. Os alertas são issues do GitHub, não notificações externas; confirmação de receção e SLA de escalonamento ainda não estão implementados. A supervisão externa do próprio GitHub Actions permanece pendente.

O resultado `FAVORAVEL` significa apenas que, na janela analisada pelo script, não foram encontrados resultados desfavoráveis nem execuções ativas. Não é certificação global da qualidade dos dados B3.

## Monitorização da atualidade dos dados

Foi adicionado o avaliador [check_data_freshness.py](engine/check_data_freshness.py), com catálogo explícito de limites em [datasets-monitorizados.json](registry/datasets-monitorizados.json). A verificação lê datas de observação declaradas nos manifestos; não transforma timestamps de ingestão em datas de mercado. O workflow [WATCHDOG de atualidade dos dados](../.github/workflows/watchdog-data-freshness.yml) executa testes, publica JSON/Markdown como artefacto de 30 dias e cria/atualiza uma issue quando identifica datasets fora do limite.

A primeira execução real é o teste de aceitação para confirmar quais datasets estão desatualizados. Limites de idade são política configurada e devem ser revistos pelo proprietário de cada série; estado `UNKNOWN` significa que o manifesto não declara uma data de observação suficiente.

## Registos

- [Inventário local](registry/sistemas-monitorizados.json)
- [Controlos obrigatórios](registry/controlos-obrigatorios.json)
- [Norma central](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md)

## Próximos passos do piloto

1. Rever os resultados reais do monitor de atualidade e calibrar limites por dataset.
2. Adicionar confirmação de receção, responsáveis e escalonamento de alertas.
3. Garantir que a falha do próprio monitor é detetada por mecanismo independente.
4. Expandir a reconciliação a integridade, hashes e continuidade de dados COTAHIST/BCB/BDI.
5. Testar recuperação, retenção e acesso aos artefactos.
6. Registar critérios de aceitação e evidência antes de declarar o piloto operacional completo.
