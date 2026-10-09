<!--
Projeto: B3 — A BOLSA DO BRASIL
Arquivo: WATCHDOG/README.md
Caminho: WATCHDOG/README.md
Data de criação: 2026-10-09
Versão: 1.0.0
Estado: proposta implementada em branch; ativação 24/7 depende de merge na main e execução verificada
Finalidade: documentar monitoramento contínuo, auditável e não destrutivo do código.
-->

# WATCHDOG B3 — Monitoramento contínuo de qualidade de código

## Objetivo

Monitorar continuamente a integridade estática do repositório B3, detectar regressões verificáveis e produzir evidências reproduzíveis. O watchdog complementa — não substitui — os contratos de dados, os testes de domínio, a Carta de Confiança dos Workflows e a revisão humana.

## Escopo da versão 1.0

- execução por evento de push e pull request;
- execução programada a cada 15 minutos, quando o workflow estiver ativo na branch padrão;
- execução manual por `workflow_dispatch`;
- compilação sintática de arquivos Python versionados, sem executar o código;
- verificação de arquivos normativos essenciais;
- inspeção estática dos workflows: presença de gatilhos, permissões explícitas e limites de tempo;
- relatórios Markdown e JSON como artefatos de cada execução;
- falha explícita em erros críticos; avisos separados de erros;
- nenhuma alteração automática de código, dados RAW, certificações ou histórico.

## Limite importante

GitHub Actions não é um serviço de tempo real com SLA. Agendamentos podem atrasar e podem ser desativados em repositórios públicos sem atividade prolongada. “24/7” significa tentativa de execução recorrente e orientada a eventos, não garantia de execução exatamente a cada 15 minutos. Para disponibilidade independente do GitHub, seria necessária uma segunda instância externa.

## Estrutura

```text
WATCHDOG/
├── README.md
├── CARTA_WATCHDOG_B3_V1.md
├── POLITICA_DE_ALERTAS_V1.json
├── scripts/
│   └── watchdog_b3.py
└── esquemas/
    └── README.md
.github/
└── workflows/
    └── watchdog-b3-24x7.yml
```

## Estados

- **PASS:** verificações críticas concluídas sem erro.
- **FAIL:** uma ou mais verificações críticas falharam; o job deve falhar.
- **WARN:** risco ou lacuna que precisa de avaliação, mas não é prova suficiente para bloquear por si só.
- **INFO:** contexto de execução.

## Evidência por execução

Cada execução publica `watchdog-report.md` e `watchdog-report.json` como artefatos. Os relatórios incluem commit, branch, timestamp UTC, contagens e verificações realizadas. Os artefatos do GitHub Actions têm retenção limitada pela configuração do repositório; não constituem arquivo permanente por si só.

## Roadmap

1. **V1 — integridade estática:** Python, contratos essenciais, política básica de workflows e relatórios.
2. **V1.1 — baseline controlada:** executar na branch principal, classificar falsos positivos e fixar limites aprovados.
3. **V1.2 — testes por domínio:** conectar verificadores COTAHIST, calendário, chaves, normalização e reconciliação sem duplicar suas regras.
4. **V2 — observabilidade de execuções:** detectar falhas repetidas, ausência de execuções e workflows críticos sem evidência recente.
5. **V3 — redundância externa:** monitor independente para alertar sobre indisponibilidade do próprio GitHub Actions.

Nenhuma etapa posterior deve ser considerada concluída sem execução real, evidência e revisão.
