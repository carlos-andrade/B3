# Plano de normalização documental — B3 segundo GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-PLANO-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | PLANO_DE_EXECUCAO |
| **Fase** | Adoção transversal da norma documental |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — checksum existente não foi validado de forma independente |
| **Commit de referência (versão anterior)** | [16cb7f018923e42409f60ec685a339420ecbcd73](https://github.com/carlos-andrade/B3/commit/16cb7f018923e42409f60ec685a339420ecbcd73) |
| **Data de criação** | 2026-10-14 |
| **Data de atualização** | 2026-10-14 |
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

A execução começa por documentos humanos de governança, cartas, planos e roadmaps ativos. Não se considerará todo o repositório conforme com base num lote parcial.

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

Plano publicado como marco de governação. A conclusão da normalização será declarada por lote e acompanhada de evidência verificável, não por presunção de cobertura integral.

## Próxima Ação

Normalizar os documentos prioritários em lotes pequenos, verificar conteúdo e referências, calcular os checksums canónicos e atualizar este registo com os commits reais.

## Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.0 | 2026-10-14 | Criação do plano de adoção documental B3 | Responsável técnico B3 | Commit do arquivo no repositório |
