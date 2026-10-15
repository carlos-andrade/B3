# Revisão semântica documental — Lote 13: documentos de entrada, Wiki, dashboards e roadmap

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-013 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; CORRECOES_DOCUMENTAIS_APLICADAS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente para validação final quando aplicável |
| **Origem** | Inspeção de oito documentos de entrada, Wiki, dashboard, diagnóstico histórico e roadmap |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS → IMPLEMENTAÇÃO → EVIDÊNCIAS |
| **Escopo** | Prompt mestre, README raiz, dashboard, Wiki, diagnóstico histórico e plano mestre |
| **Objetivo** | Corrigir conteúdo inequivocamente obsoleto, preservar incidentes históricos e alinhar o roadmap com a matriz atual |
| **Dependências** | Matriz semântica, Issue #11, evidências de workflows e commits atuais |

## 1. Resultado executivo

Foram revistos oito documentos. Dois problemas substantivos foram corrigidos neste lote:

1. O ficheiro PROMPT_MESTRE_B3_799_CARACTERES.md continha o texto literal de uma função nativa em vez do prompt, embora declarasse uma especificação de 799 caracteres. O prompt foi restaurado com instruções B3 coerentes com governança e medido em exatamente 799 caracteres.
2. O README raiz tinha data de atualização antiga e descrevia uma integração operacional com BLOOMBERG_MAIL incompatível com o limite de isolamento atual. A data e o estado WATCHDOG foram atualizados, e a integração foi substituída por uma declaração explícita de isolamento, preservando a carta histórica.

Os restantes documentos foram classificados de acordo com a sua natureza. O diagnóstico de 25/09 e o incidente de Wiki de 29/09 permanecem snapshots históricos, não estados correntes. A Wiki nativa continua a depender de credencial e prova de publicação no repositório wiki separado; a revisão semântica não confirma a configuração de secrets.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| PROMPT_MESTRE_B3_799_CARACTERES.md | Prompt mestre operacional | O corpo continha function () { [native code] }, incompatível com a especificação de prompt. Foi substituído por prompt B3 de exatamente 799 caracteres, incluindo espaços. | Correção aplicada no commit e tamanho medido por código; futuras alterações devem repetir a contagem e revisão de conteúdo. |
| README.md | Entrada e resumo do projeto | Data antiga 01/10 e texto que afirmava integração corrente com BLOOMBERG_MAIL contradiziam o escopo atual. O README foi atualizado em 15/10, a integração foi retirada do fluxo ativo e o estado WATCHDOG foi qualificado como histórico/pendente de gates. | Correção aplicada. A carta de 08/10 permanece apenas histórica; nenhuma integração é autorizada. |
| dashboards/README.md | Contrato descritivo do dashboard | Afirma que o HTML não contém observações embutidas e que o snapshot JSON é a fonte dos indicadores; a ausência de dados não deve virar zero. | Coerente. A interface pronta não prova que todos os dados reais estejam alimentados nem que o dashboard esteja aprovado funcionalmente. |
| WIKI/09-AUTOMACAO/INCIDENTE_PUBLICACAO_WIKI_2026-09-29.md | Registo histórico de incidente | Regista falha de secret e ausência de evidência de commit no repositório .wiki.git. O texto não declara publicação concluída sem prova. | Preservar como incidente datado. O estado atual exige consulta a um run e commit posteriores; não armazenar tokens no repositório. |
| WIKI/09-AUTOMACAO/WIKI_NATIVA.md | Runbook de publicação Wiki | Define WIKI/ como fonte de verdade e a Wiki nativa como camada de publicação separada, dependente de credencial com permissão de push. | A arquitetura está coerente; a ativação só pode ser confirmada por execução real e commit no repositório wiki. |
| WIKI/README.md | Índice da Wiki técnica | Define a Wiki como documentação auditável, marco 1986 e obrigação de atualizar estado/histórico após mudanças. | Coerente como índice. A página Estado Atual precisa de atualização separada para refletir o roadmap de 15/10. |
| docs/AUDITORIA_ESTADO_REPOSITORIO_2026-09-25.md | Diagnóstico de base histórico | A própria data e o estado de diagnóstico de base identificam uma fotografia de 25/09. Os números de anos e manifests são evidência daquele snapshot. | Preservar como baseline histórica; não usar como certificação atual nem reescrever retrospectivamente. |
| docs/PLANO_MESTRE_DE_EXECUCAO.md | Roadmap principal | Contém fases antigas e atualizações posteriores; as secções históricas devem ser interpretadas à data de cada registo. A secção semântica precisava refletir os Lotes 05–13. | Roadmap atualizado em versão própria para registar os lotes recentes e o saldo real, sem apagar histórico. |

## 3. Achados e decisões

### SEM-13-01 — prompt mestre corrompido

**Achado:** a descrição prometia 799 caracteres, mas o corpo não continha um prompt utilizável.

**Correção:** prompt B3 restaurado, 799 caracteres exatos. A formulação reforça fontes oficiais, separação entre factos/hipóteses/inferências, backtest reproduzível, preservação RAW, política COTAHIST e isolamento de BLOOMBERG_MAIL.

### SEM-13-02 — README contradizia o isolamento de projetos

**Achado:** a secção incremental afirmava um fluxo de integração entre BLOOMBERG_MAIL e B3 como regra ativa.

**Correção:** README atualizado para declarar BLOOMBERG_MAIL fora do âmbito operacional atual; a carta antiga permanece preservada como histórico e não deve ser executada como contrato corrente.

### SEM-13-03 — snapshots não são estado atual

O diagnóstico de 25/09 e o incidente de 29/09 preservam evidências válidas para as suas datas. O estado de publicação da Wiki e os dados atuais devem ser confirmados por evidência posterior, não inferidos da existência de documentação.

## 4. Conclusão

O conteúdo dos oito documentos foi revisto. O prompt mestre e o README raiz foram corrigidos; os demais foram classificados como documentos descritivos ou históricos, com limites explícitos. Não foram alterados dados de mercado, RAW, manifests ou workflows neste lote.

COTAHIST 1986–2025 permanece somente para consulta; 2026 mantém atualização diária. BLOOMBERG_MAIL permanece isolado e fora do âmbito operacional B3.

## 5. Referências

- [Matriz integral de revisão semântica](MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Plano Mestre de Execução](../../docs/PLANO_MESTRE_DE_EXECUCAO.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
