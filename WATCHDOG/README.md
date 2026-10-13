# WATCHDOG — Supervisão operacional do projeto B3

**Padrão central:** [GOVERNANCA/WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/tree/main/WATCHDOG)  
**Estado local:** piloto documental integrado; monitor de execuções GitHub Actions já existente; lacunas de alertas e evidências persistentes em aberto.

## Âmbito inicial

O projeto B3 tem um workflow de monitorização de execuções GitHub Actions:

- Workflow: [B3 - Monitor independente de execuções V1](../.github/workflows/b3-monitor-execucoes-v1.yml)
- Cadência declarada: a cada 15 minutos, além de execução manual.
- Janela analisada: últimas 24 horas.
- Sinais recolhidos: execuções desfavoráveis e execuções ainda ativas.
- Permissões declaradas: leitura de Actions e contents.

## Estado e limitações conhecidas

A existência do workflow e a sua configuração estão confirmadas no repositório. Isso não prova disponibilidade contínua nem cobertura de todos os pipelines. O workflow escreve um resumo de execução; este piloto ainda não demonstra envio de alerta fora do GitHub, armazenamento imutável de evidências, SLA de reconhecimento, nem supervisão externa do próprio GitHub Actions.

O resultado `FAVORAVEL` significa apenas que, na janela analisada pelo script, não foram encontrados resultados desfavoráveis nem execuções ativas. Não é certificação global da qualidade dos dados B3.

## Registos

- [Inventário local](registry/sistemas-monitorizados.json)
- [Controlos obrigatórios](registry/controlos-obrigatorios.json)
- [Norma central](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md)

## Próximos passos do piloto

1. Validar o workflow em execução agendada e testar cenários de falha.
2. Produzir artefacto persistente com data UTC, distribuição e IDs/URLs das execuções.
3. Adicionar canal de alerta com confirmação de receção e escalonamento.
4. Garantir que a falha do próprio monitor é detetada por mecanismo independente.
5. Expandir cobertura a frescura, integridade e reconciliação de dados COTAHIST/BCB/BDI.
6. Registar critérios de aceitação e evidência antes de declarar o piloto operacional completo.
