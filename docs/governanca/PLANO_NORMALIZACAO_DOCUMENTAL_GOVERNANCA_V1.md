# Plano de normalização documental — B3 segundo GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-PLANO-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | PLANO_DE_EXECUCAO |
| **Fase** | Adoção transversal da norma documental |
| **Estado** | EM_CURSO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — checksum existente não foi validado de forma independente |
| **Commit de referência (versão anterior)** | [16cb7f018923e42409f60ec685a339420ecbcd73](https://github.com/carlos-andrade/B3/commit/16cb7f018923e42409f60ec685a339420ecbcd73) |
| **Data de criação** | 2026-10-14 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente de aprovação específica deste plano |
| **Origem** | Norma de cabeçalho da [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Autoridade superior** | [Constituição GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md); [Layout Mestre B3](https://github.com/carlos-andrade/B3/blob/main/docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Escopo** | Documentação Markdown governada do repositório B3; não altera RAW, datasets, manifestos ou evidências de máquina |
| **Objetivo** | Aplicar cabeçalho canónico e rastreabilidade, preservar conteúdo e auditar por lotes |
| **Dependências** | Norma GOVERNANCA v1.0.3; inventário documental B3; links/commits reais |

## Contexto Histórico

A norma de cabeçalho documental padrão da GOVERNANCA v1.0.3 foi aprovada em 2026-10-13. O projeto B3 adota essa norma sem substituir a autoridade operacional específica do Layout Mestre B3.

## Estado

A fase de inventário estrutural foi concluída: 284 ficheiros Markdown enumerados a partir da árvore Git de `main` e classificados preliminarmente por caminho/nome. A classificação semântica e a conformidade continuam pendentes de revisão do conteúdo. Não se considera todo o repositório conforme com base num lote parcial.

## Evidências

- [Norma de cabeçalho padrão v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md)
- [Checklist de validação](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/CHECKLIST-VALIDACAO.md)
- [Layout Mestre Canónico B3](https://github.com/carlos-andrade/B3/blob/main/docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md)

## Validação

- Documento Markdown inicia com título H1.
- Tabela visível contém ID único, projeto, repositório, tipo, fase, estado, versão, SHA-256 canónico e commit de referência.
- Inclui datas ISO, responsável, aprovador, origem, autoridade, cadeia de autoridade, rastreabilidade/escopo/objetivo/dependências conforme aplicável.
- Hash canónico é calculado em UTF-8/LF, removendo apenas as linhas SHA-256 canónico e commit de referência antes do cálculo.
- Não inferir aprovação; distinguir estado do documento e estado do projeto.
- Preservar o conteúdo preexistente, os links e os limites de evidência.
- Não inserir cabeçalho em JSON, CSV, dados brutos, código ou artefactos gerados por máquina sem contrato próprio.

## Resultado

Lote inicial aplicado diretamente em `main`. Foram normalizados cabeçalhos e campos de autoridade nos seguintes documentos: cartas de confiança/garantias/carta magna, Plano Mestre de Execução, Carta de Incidente COTAHIST 1999, Modelo-Mestre de Governança, roadmaps COTAHIST de 1999–2005, PARTE18, PARTE20, PARTE23 e roadmap mestre 1986–2026, além da incidência Git LFS A1987. Os conteúdos históricos dos documentos foram preservados. A verificação de existência dos campos passou nos ficheiros reconsultados; os SHA-256 canónicos continuam explicitamente pendentes e a conformidade integral não é declarada.

## Estado do lote 1

| Métrica | Resultado |
|---|---:|
| Documentos Markdown no repositório | 284 |
| Documentos em `docs/` | 217 (referência anterior; reconfirmar no inventário atual por prefixo) |
| Documentos prioritários identificados no inventário inicial | 45 (conjunto inicial; classificação em revisão) |
| Documentos com cabeçalho normalizado e reconsultados nesta tranche | 11 |
| Incidente A1987 reconciliado e com cabeçalho normalizado | 1 |
| Hashes canónicos recalculados/verificados independentemente | 0 — pendentes |

Esta contagem reflete apenas os documentos explicitamente alterados e reverificados, não a conformidade do restante repositório.

## Inventário e próximo passo

- A fotografia inicial enumerou 284 ficheiros Markdown antes de criar a própria matriz. Na árvore atual, após publicar a matriz, existem 285 ficheiros Markdown, dos quais 218 em `docs/`; a matriz lista os 284 ficheiros que existiam no instante da captura e exclui-se a si própria para evitar autorreferência.
- Inventário estrutural completo: [Inventário e Matriz de Conformidade Documental B3 v1](https://github.com/carlos-andrade/B3/blob/main/docs/governanca/INVENTARIO_MATRIZ_CONFORMIDADE_DOCUMENTAL_B3_V1.md).
- A extração identificou 284 ficheiros Markdown na árvore Git; a classificação preliminar é baseada em caminho/nome e não equivale à classificação semântica.
- Classes preliminares: INGESTAO_DADOS 130; GOVERNANCA_CARTAS_LAYOUT 60; README_INDICE 35; OUTROS_MARKDOWN 24; DOCUMENTACAO_TEMATICA 14; INCIDENTES_AUDITORIAS 13; ROADMAP_PLANOS 8.
- Próximo passo obrigatório: validar a matriz por conteúdo e distinguir documentação humana, histórico, modelos e artefactos gerados antes de normalizar novos lotes.
- SHA-256 canónicos: continuam pendentes de cálculo independente; não declarar conformidade integral até existir evidência reprodutível.

## Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.0 | 2026-10-14 | Criação do plano de adoção documental B3 | Responsável técnico B3 | Commit inicial no repositório |
| 1.1.0 | 2026-10-15 | Inclusão do inventário estrutural inicial de 284 ficheiros Markdown e atualização do próximo passo | Responsável técnico B3 | [Inventário v1](https://github.com/carlos-andrade/B3/blob/main/docs/governanca/INVENTARIO_MATRIZ_CONFORMIDADE_DOCUMENTAL_B3_V1.md) |
| 1.1.1 | 2026-10-15 | Esclarecimento do snapshot e contagem atual de 285 ficheiros Markdown/218 em `docs/` | Responsável técnico B3 | Reconsulta da árvore Git após publicação da matriz |
