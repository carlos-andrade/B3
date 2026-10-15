# Decisão normativa — GOV-DIV-001: hierarquia por domínio no projeto B3

| Campo | Valor |
|---|---|
| **ID** | B3-DEC-GOV-DIV-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DECISAO_NORMATIVA |
| **Fase** | Governança — reconciliação normativa |
| **Estado** | DECISAO_REGISTADA; HASH_CANONICO_CALCULADO; AUDITORIA_GLOBAL_PENDENTE |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 010661d79963294938036a358f0966c683a461b48b55fa3d3683809fb6992b4f |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Proprietário do repositório — instrução de resolução registada nesta execução; confirmação formal no histórico Git |
| **Origem** | Divergência identificada na revisão semântica documental Lote 01 |
| **Autoridade superior** | [Carta Magna de Governança B3](../../CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre Canónico B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS → IMPLEMENTAÇÃO → EVIDÊNCIAS |
| **Escopo** | Resolver GOV-DIV-001 sem apagar o histórico nem criar autoridade paralela |
| **Objetivo** | Definir precedência por domínio e procedimento de reconciliação de conflitos normativos |
| **Dependências** | Norma GOVERNANCA v1.0.3; Carta Magna B3; Layout Mestre B3; Issue #11 |

## 1. Decisão

A divergência GOV-DIV-001 fica resolvida por **separação explícita de competências normativas**, e não por supremacia irrestrita de um documento sobre todos os demais.

1. **Carta Magna de Governança B3**: autoridade superior em princípios constitucionais, competências, limites de autoridade e processo de alteração normativa.
2. **Layout Mestre Canónico B3**: especificação operacional única para pipelines, workflows, dados, execução e geração/validação de código, dentro dos limites da Carta Magna.
3. **Cartas de domínio e políticas**: definem princípios/garantias do seu domínio, subordinadas à Carta Magna e reconciliadas com o Layout Mestre antes de gerar comportamento executável.
4. **Contratos técnicos**: concretizam regras específicas; não podem contradizer os níveis superiores.
5. **Procedimentos e implementação**: executam as regras aprovadas; não são fonte autónoma de autoridade normativa.
6. **Evidência factual e documentação oficial externa**: estabelecem factos/requisitos de origem, mas não alteram por si mesmas a hierarquia interna de autoridade.

## 2. Regra operacional de conflito

Quando uma regra operacional parecer contrariar um princípio da Carta Magna:

- não escolher silenciosamente uma das versões;
- bloquear apenas a decisão/alteração afetada (fail-closed), sem paralisar trilhas independentes;
- registar o conflito, documentos/versões/linhas afetadas, impacto e evidências;
- reconciliar a regra no Layout Mestre por alteração versionada;
- só depois alterar código/workflows e executar os testes aplicáveis.

A Carta Magna não substitui o Layout como especificação diretamente executável. O Layout não pode revogar nem redefinir unilateralmente princípios constitucionais. A evidência não altera retroativamente decisões ou certificações.

## 3. Aplicação aos textos em conflito

**Texto anterior da Carta Magna, §2:** atribuía à própria Carta Magna precedência geral sobre cartas, normas, contratos e procedimentos.

**Texto anterior do Layout Mestre, §2.2:** declarava precedência geral do Layout sobre evidência, documentação externa, cartas, procedimentos e implementação.

As duas listas pretendiam ser universais e eram incompatíveis. Esta decisão substitui a interpretação universal por uma hierarquia baseada em competência. As versões anteriores permanecem recuperáveis no Git; não são apagadas nem reescritas retroativamente.

## 4. Artefactos afetados

- [Carta Magna B3](../../CARTA_MAGNA_GOVERNANCA_B3.md), versão atualizada para 1.3.0.
- [Layout Mestre Canónico B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md), versão atualizada para 1.1.0.
- [Revisão semântica Lote 01](../auditorias/REVISAO_SEMANTICA_DOCUMENTAL_LOTE01_2026-10-15.md), que identifica a divergência original.
- [Plano Mestre de Execução](../../PLANO_MESTRE_DE_EXECUCAO.md), a atualizar com esta decisão e com o estado real da revisão semântica.

## 5. Critérios de validação e encerramento

- [ ] Os dois documentos normativos expressam a mesma hierarquia por domínio.
- [ ] O presente registo de decisão tem hash canónico validado pelo auditor.
- [ ] A auditoria SHA-256 posterior às alterações termina com sucesso e sem estados inválidos/divergentes.
- [ ] A Issue #11 regista decisão, commits e evidência.
- [ ] A revisão semântica integral dos 302 Markdown tem matriz por ficheiro, classe documental, autoridade, conflitos, estado e evidência; não basta a auditoria estrutural.

A decisão substantiva está registada; a validação criptográfica e o inventário semântico integral só serão considerados concluídos depois de produzidas as evidências correspondentes.

## 6. Limites e itens que não são resolvidos por esta decisão

- Esta decisão não certifica a semântica dos dados COTAHIST nem do catálogo BVBG.028.02.
- Não autoriza alterações a RAW, datasets históricos ou evidências de máquina.
- COTAHIST 1986–2025 permanece em consulta/read-only; 2026 continua com atualização diária.
- BLOOMBERG_MAIL permanece isolado e fora do âmbito B3.
- Outros conflitos encontrados na revisão documental devem receber IDs próprios; não se consideram resolvidos por extensão desta decisão.
- A revisão integral deve distinguir regra normativa, contrato técnico, runbook, relatório histórico, modelo, documento gerado e conteúdo de máquina; uma classificação por nome/caminho não é suficiente.

## 7. Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-15 | Registo da decisão GOV-DIV-001 por separação de autoridade constitucional e operacional | Commits das alterações à Carta Magna e ao Layout Mestre; auditoria pós-alteração pendente |
