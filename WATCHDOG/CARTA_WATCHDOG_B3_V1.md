<!--
Projeto: B3 — A BOLSA DO BRASIL
Arquivo: CARTA_WATCHDOG_B3_V1.md
Caminho: WATCHDOG/CARTA_WATCHDOG_B3_V1.md
Data de criação: 2026-10-09
Versão: 1.0.0
Estado: proposta normativa para revisão
Natureza: contrato de monitoramento estático e evidências
-->

# CARTA DO WATCHDOG B3 — V1.0

## 1. Mandato

O Watchdog B3 observa a qualidade técnica dos códigos e a presença de salvaguardas operacionais. Deve ser determinístico, auditável, conservador e não destrutivo. Não pode declarar dados de mercado corretos apenas porque o código compila.

## 2. Hierarquia de confiança

1. fonte oficial e contrato aplicável;
2. carta normativa vigente;
3. layout e semântica documentados;
4. testes reproduzíveis e amostras rastreáveis;
5. implementação;
6. evidência de execução;
7. relatório consolidado.

O watchdog não altera essa hierarquia e não substitui a Carta de Confiança dos Workflows.

## 3. Regras de operação

- **Somente leitura:** a verificação não modifica arquivos, dados, RAW, datasets ou certificações.
- **Falha explícita:** erro sintático ou ausência de documento essencial resulta em estado FAIL.
- **Aviso não é erro:** riscos de configuração são apresentados separadamente, sem serem promovidos artificialmente a falhas críticas.
- **Sem aprovação automática:** nenhum resultado do watchdog autoriza sozinho merge, certificação ou publicação de dados.
- **Sem correção automática:** a V1 diagnostica; correções exigem mudança versionada e revisão.
- **Rastreabilidade:** registrar SHA do commit, branch, instante UTC, verificações, contagens e resultado.
- **Idempotência:** mesma árvore e ambiente equivalente devem produzir o mesmo resultado substantivo.
- **Fases COTAHIST:** respeitar fases monotônicas; nunca reexecutar nem reescrever fases históricas como efeito colateral.
- **Proteção de segredos:** nunca imprimir tokens, credenciais, variáveis secretas ou conteúdo sensível.
- **Dados ausentes:** ausência de evidência não pode ser convertida em sucesso.

## 4. Cobertura da V1

A V1 verifica sintaxe de Python sem executar módulos; presença de documentos essenciais; estrutura mínima de workflows; permissões explícitas e limites de tempo. As verificações são estáticas e não certificam a semântica financeira, a correção do COTAHIST nem a validade de dados externos.

## 5. Cadência

O workflow é acionado por push, pull request, despacho manual e agenda de 15 minutos. A agenda do GitHub Actions pode atrasar ou deixar de executar; portanto, não há SLA de tempo real. O monitoramento recorrente só fica ativo na branch padrão depois do merge.

## 6. Severidade

- **CRITICAL / FAIL:** sintaxe Python inválida ou contrato essencial ausente.
- **WARNING:** workflow sem timeout explícito, permissões excessivas ou referência de Action não fixada a SHA imutável.
- **INFO:** inventário e contexto de execução.

Avisos são indicadores de risco, não prova isolada de exploração ou defeito funcional.

## 7. Evidências

Cada execução deve publicar relatório Markdown e JSON como artefatos. A retenção do GitHub Actions é limitada; evidência crítica de certificação deve continuar no fluxo documental próprio e não depender apenas desses artefatos temporários.

## 8. Critérios de aceitação

A V1 só pode ser considerada operacionalmente aceita após:
1. merge aprovado na branch padrão;
2. primeira execução real concluída;
3. relatório verificado;
4. erros e avisos triados;
5. confirmação de que a rotina não altera dados nem arquivos;
6. revisão da política de alertas com base em evidências, não em suposições.

## 9. Fora de escopo

A V1 não monitora preços em tempo real, não garante disponibilidade do GitHub, não interpreta toda a lógica financeira, não executa backtests e não declara que uma estratégia é lucrativa.
