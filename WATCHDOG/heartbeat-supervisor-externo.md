# Configuração de supervisão independente por heartbeat

| Campo | Valor |
|---|---|
| **ID** | B3-WD-HEARTBEAT-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | GUIA_OPERACIONAL |
| **Fase** | WATCHDOG — supervisão independente |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 4f2f87a87acca1fd71add4c13546cdc52e5f1c0d16b24d140e55159141894ce4 |
| **Commit de referência (versão anterior)** | [8c75b57e4d9c11b5ff3545ff25ad54b76018c583](https://github.com/carlos-andrade/B3/commit/8c75b57e4d9c11b5ff3545ff25ad54b76018c583) |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável operacional do projeto B3 |
| **Aprovador** | Pendente — teste de aceitação e aprovação humana necessários |
| **Origem** | Workflows WATCHDOG e configuração de heartbeat externo do repositório B3 |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) e [Carta WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Estado:** hooks de integração preparados; supervisão externa ainda inativa até configurar as duas URLs secretas.

## Objetivo

O heartbeat permite que um serviço de monitorização externo detete a ausência de execuções do GitHub Actions. O serviço externo deve estar fora do repositório e, idealmente, fora da mesma plataforma de execução monitorizada.

## Secrets necessários no repositório B3

Em **Settings → Secrets and variables → Actions → New repository secret**, configurar:

- `WATCHDOG_HEARTBEAT_WORKFLOWS_URL`: URL de ping exclusiva para o workflow de monitorização de execuções, executado a cada 15 minutos.
- `WATCHDOG_HEARTBEAT_DATA_URL`: URL de ping exclusiva para o workflow de atualidade de dados, executado diariamente às 07:15 UTC.

Cada URL deve pertencer a uma verificação separada no serviço externo. Não reutilizar a mesma URL nos dois workflows, pois o heartbeat de um poderia mascarar a falha do outro.

## Configuração do serviço externo

Para o monitor de workflows:
- Intervalo esperado: 15 minutos.
- Tolerância recomendada para ausência de heartbeat: 25–30 minutos.
- Notificar responsável primário e suplente após o limite.

Para a atualidade dos dados:
- Intervalo esperado: diário às 07:15 UTC.
- Tolerância recomendada: 30–36 horas.
- Notificar responsável primário e suplente após o limite.

A tolerância final depende das capacidades do serviço externo e da política de resposta acordada.

## Comportamento dos workflows

- Se a secret estiver configurada, o workflow chama a URL com timeout de 10 segundos e falha se a chamada HTTP não for bem-sucedida.
- Se a secret estiver ausente, o workflow emite um aviso; o pipeline não declara supervisão independente ativa.
- O heartbeat de atualidade indica que o monitor executou e publicou o resultado, não que todos os datasets estejam saudáveis. A saúde dos dados permanece no relatório próprio.
- O heartbeat não deve incluir dados pessoais, tokens ou conteúdo de mercado.

## Teste de aceitação

1. Configurar cada secret com URL de heartbeat distinta.
2. Executar manualmente cada workflow.
3. Confirmar receção de um ping no serviço externo.
4. Simular uma execução que não envia heartbeat e verificar que o serviço externo alerta após o limite.
5. Verificar o alerta, o destinatário, o escalonamento e o registo de recuperação.
6. Guardar a evidência do teste e a aprovação do proprietário.

**Até concluir estes passos, o estado da supervisão independente é PENDENTE.**
