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

## Registos

- [Inventário local](registry/sistemas-monitorizados.json)
- [Controlos obrigatórios](registry/controlos-obrigatorios.json)
- [Norma central](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md)

## Próximos passos do piloto

1. Validar o workflow em execução agendada e testar cenários de falha.
2. Testar a publicação dos artefactos em execução real e verificar a retenção.
3. Adicionar confirmação de receção, responsáveis e escalonamento de alertas.
4. Garantir que a falha do próprio monitor é detetada por mecanismo independente.
5. Expandir cobertura a frescura, integridade e reconciliação de dados COTAHIST/BCB/BDI.
6. Registar critérios de aceitação e evidência antes de declarar o piloto operacional completo.
