# Revisão semântica documental — Lote 01

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Classificação semântica e reconciliação |
| **Estado** | REVISAO_PARCIAL; DIVERGENCIA_ABERTA |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 1a4b58151d0571d999cbf3800c089f8682fcd0da955b26bc7f566e08d28167dc |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente de aprovação específica |
| **Origem** | Inspeção direta dos cinco documentos listados abaixo e norma GOVERNANCA v1.0.3 |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md); [Layout Mestre Canónico B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md) |
| **Cadeia de autoridade** | FONTES → CARTAS/DOCUMENTOS DE ENTRADA → LAYOUT MESTRE → CÓDIGO/WORKFLOWS → EVIDÊNCIAS → VALIDAÇÃO |
| **Escopo** | Revisão semântica de documentos prioritários de governança; sem alteração de dados ou código operacional |
| **Objetivo** | Confirmar classificação, identificar conflitos normativos e impedir normalização que perpetue contradições |
| **Dependências** | Inventário documental B3; Norma GOVERNANCA v1.0.3; Layout Mestre B3 |

## 1. Resultado executivo

Foram inspecionados cinco documentos prioritários. A finalidade desta etapa é a classificação semântica e deteção de divergências; não é uma certificação global nem validação de hashes. Quatro documentos são classificados de acordo com a sua função aparente. Foi identificada uma divergência normativa relevante entre a Carta Magna e o Layout Mestre quanto à precedência em caso de conflito. A divergência permanece aberta e não deve ser corrigida silenciosamente.

## 2. Matriz da revisão

| Documento | Classificação semântica | Resultado da inspeção | Próxima ação |
|---|---|---|---|
| [Layout Mestre Canónico B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md) | NORMA_OPERACIONAL_CANONICA | Declara-se a única especificação normativa operacional para criação, alteração e validação de código; define precedência do próprio Layout sobre evidência, fontes externas, cartas, procedimentos e implementação, na ordem descrita no seu §2. | Preservar como autoridade operacional para código; reconciliar documentos de entrada antes de novas mudanças normativas. |
| [Carta Magna de Governança B3](../../CARTA_MAGNA_GOVERNANCA_B3.md) | CARTA_GOVERNANCA_PROJETO | O §2 declara que, em caso de conflito, a própria Carta Magna prevalece. Isso contradiz a precedência declarada pelo Layout Mestre. | Abrir reconciliação versionada; não reescrever o texto até decisão autorizada. |
| [Carta de Confiança dos Dados](../../CARTA_DE_CONFIANCA_DOS_DADOS.md) | POLITICA_DE_CONFIANCA_DADOS | Define critérios de confiança, proveniência, integridade e uso dos dados. O seu cabeçalho remete para a norma GOVERNANCA e o Layout Mestre. | Revisar contra o Layout, preservando o histórico e sem promover regras paralelas. |
| [Carta de Garantias do Projeto B3](../../CARTA_DE_GARANTIAS_DO_PROJETO_B3.md) | CARTA_GARANTIAS_OPERACIONAIS | Estabelece garantias operacionais de localização, integridade, rastreabilidade e continuidade; contém contratos específicos que exigem revisão por seção. | Classificar as seções restantes e confirmar compatibilidade com contratos atuais antes de qualquer alteração. |
| [Modelo-Mestre de Governança para Projetos](../../MODELO_GOVERNANCA_PARA_PROJETOS.md) | MODELO_GOVERNANCA_REUTILIZAVEL | Apresenta-se como modelo de governança reutilizável para projetos; no contexto B3, o próprio cabeçalho subordina o documento ao Layout Mestre operacional. | Distinguir princípios reutilizáveis de regras específicas B3 e revisar referências de autoridade. |

## 3. Divergência normativa aberta — GOV-DIV-001

**Fato observado A:** o Layout Mestre Canónico B3, secção 2.2, determina que o próprio Layout Mestre prevalece operacionalmente em caso de divergência e trata cartas/documentos como fontes de entrada, não como autoridades paralelas.

**Fato observado B:** a Carta Magna de Governança B3, secção 2, estabelece que, em caso de conflito, a própria Carta Magna é a primeira autoridade.

**Impacto:** as duas regras não podem ser aplicadas simultaneamente quando a Carta Magna e o Layout Mestre divergirem. A cadeia de cabeçalho PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO descreve uma sequência de fluxo, mas não elimina por si só a contradição explícita de precedência.

**Decisão operacional provisória:** para geração, alteração e validação de código, aplicar a precedência operacional expressa no Layout Mestre, pois o próprio Layout define esse domínio e essa regra. Não inferir que a Carta Magna foi formalmente alterada ou revogada.

**Correção requerida:** uma decisão normativa versionada deve esclarecer se a Carta Magna é uma carta de princípios subordinada à autoridade operacional do Layout, ou se é necessário atualizar o Layout e a cadeia superior. Até haver essa decisão, a divergência fica aberta e a Carta Magna permanece em revisão.

## 4. Critérios preservados

- Nenhuma aprovação é inferida.
- Nenhum conteúdo histórico foi alterado nesta revisão.
- Não se declara conformidade integral com base em cinco documentos.
- SHA-256 canónico deste relatório e dos documentos inspecionados continua pendente de cálculo independente.
- COTAHIST 1986–2025 permanece fechado e apenas para consulta; 2026 mantém atualização diária.
- BLOOMBERG_MAIL permanece isolado e fora do escopo.

## 5. Próximos passos

1. Obter/confirmar decisão autorizada para resolver GOV-DIV-001 sem alterar retroativamente o histórico.
2. Continuar a revisão semântica dos contratos, políticas e procedimentos prioritários.
3. Separar documentos humanos de relatórios e artefactos gerados, respeitando contratos próprios.
4. Implementar cálculo canónico reprodutível e validar hashes em lote.
5. Atualizar o roadmap após a conclusão de cada fase e só então avançar.

## 6. Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-15 | Primeira revisão semântica prioritária; registada divergência de autoridade | Inventário atualizado e documentos-fonte citados |
