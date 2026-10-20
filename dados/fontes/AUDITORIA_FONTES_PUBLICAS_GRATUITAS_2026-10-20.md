# Auditoria e execução do roadmap — fontes públicas gratuitas

| Campo | Valor |
|---|---|
| **ID** | B3-AUD-FONTES-PUBLICAS-20261020 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Data de corte** | 2026-10-20 |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 5f7bdea42f148aa3d9823469cd651ad350f8f3ce69871c10eb411b98d1bb5235 |
| **Commit de referência (versão anterior)** | [3ed15bc](https://github.com/carlos-andrade/B3/commit/3ed15bc94ec0a6f31a638b490bfce86fe285ff21) |
| **Estado** | EXECUÇÃO PARCIAL COM EVIDÊNCIAS; pendências externas explicitadas |
| **Inventário** | [INVENTARIO_FONTES_PUBLICAS_GRATUITAS_V1.json](./INVENTARIO_FONTES_PUBLICAS_GRATUITAS_V1.json) |
| **Política** | [Política de aquisição de dados públicos gratuitos](../../WIKI/01-GOVERNANCA/POLITICA_AQUISICAO_DADOS_PUBLICOS_GRATUITOS_V1.md) |

## 1. Resultado executivo

O objetivo operacional é maximizar a cobertura dos dados públicos gratuitos relevantes ao projeto B3. Esta auditoria não afirma que tenha enumerado todos os dados da Internet: delimita fontes relevantes para instrumentos e mercado B3, companhias abertas, fundos, macroeconomia, câmbio e política monetária.

O inventário inicial contém **14 registos de fonte/conjunto de dados**:

| Estado de acesso/execução | Quantidade | Significado |
|---|---:|---|
| AUTORIZADO_COM_CONDICOES | 8 | Catálogo/licença oficial identificado; as condições e o âmbito continuam a aplicar-se |
| BLOQUEADO_RESTRICAO_DOCUMENTADA | 1 | O canal identificado tem restrição explícita à recolha automatizada |
| REVISAO_TERMO_ESPECIFICO | 2 | Método automatizado/uso previsto carece de prova documental específica |
| FONTE_NAO_CONFIRMADA | 1 | Descoberta por terceiro não demonstra canal oficial autorizado |
| PENDENTE_IMPLEMENTACAO | 2 | Fonte pública identificada; falta validar metadados/licença por conjunto e implementar captura |
| **Total** | **14** | Inventário inicial versionado |

Estes estados não são uma classificação de qualidade do conteúdo. Acesso, licença, captura, validação e certificação são dimensões separadas.

## 2. Execução das fases do roadmap

### Fase 1 — Formalizar a regra

**Concluída com evidência documental.**
- Política B3 publicada em `WIKI/01-GOVERNANCA/POLITICA_AQUISICAO_DADOS_PUBLICOS_GRATUITOS_V1.md`.
- Adenda transversal incorporada em [GOVERNANCA — governança de dados](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/05-dados-e-ia/governanca-de-dados.md).
- Política indexada em [WIKI/README.md](../../WIKI/README.md).

### Fase 2 — Inventariar fontes públicas

**Inventário inicial publicado; cobertura global continua aberta.**

Fontes confirmadas nos catálogos oficiais consultados:
- BCB — séries SGS elegíveis após preflight individual: https://dadosabertos.bcb.gov.br/
- BCB — Copom JSON, licença ODbL indicada no catálogo: https://dadosabertos.bcb.gov.br/dataset/documentos-do-copom
- BCB — PTAX/boletins diários, licença ODbL indicada no catálogo: https://dadosabertos.bcb.gov.br/dataset/taxas-de-cambio-todos-os-boletins-diarios
- CVM — DFP: https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp
- CVM — ITR: https://dados.cvm.gov.br/dataset/cia_aberta-doc-itr
- CVM — catálogo de fundos e recursos TXT/ZIP/CSV: https://dados.cvm.gov.br/dataset/
- IBGE/SIDRA e Tesouro Transparente permanecem candidatos públicos para validação de cada dataset/termo, não declarados ainda como plenamente autorizados.

### Fase 3 — Implementar captura e validação

**Parcial, com duas capturas novas verificadas.**
- O orquestrador BCB SGS + Copom passou nos [runs #16](https://github.com/carlos-andrade/B3/actions/runs/39412861864), [#17](https://github.com/carlos-andrade/B3/actions/runs/39413299122) e [#18](https://github.com/carlos-andrade/B3/actions/runs/39413806000): testes de governança/licença, preflight SGS, ingestão, gate de qualidade e captura/validação JSON Copom passaram. O preflight excluiu SGS 12 e 433 porque não demonstrou recurso/licença elegível; SGS 1, 11 e 432 ficaram `VALIDADO`.
- O inventário recebeu validador estrutural e testes unitários: `scripts/governanca/validar_inventario_fontes_publicas.py` e `scripts/governanca/test_validar_inventario_fontes_publicas.py`; no run #16, `valid=true` e `source_count=14`.
- O workflow do orquestrador foi ligado ao inventário e aos testes, para executar validação no CI.
- DFP e ITR da CVM foram capturados e publicados com sucesso no [run #2 do pipeline CVM](https://github.com/carlos-andrade/B3/actions/runs/39413170519). Ambos foram obtidos via CKAN oficial com licença `odc-odbl`, validados como ZIP, receberam SHA-256 e manifestos e foram persistidos em RAW. DFP 2026: 243.348 bytes, SHA-256 `b5a805d46cdb3c865eaff362013e2ff7df058b2112874d5be5e88cfe17dc50c6`; ITR 2026: 19.690.261 bytes, SHA-256 `56a82941d1c381b421a8075a584b498e4f183986ad526546e14682422773e6a1`.
- Foi criado workflow semanal para atualizar os conjuntos DFP/ITR e preservar os artefactos brutos e manifestos. A execução inicial #1 falhou apenas num teste que esperava exceção em vez de confirmar a filtragem segura de URL; o teste foi corrigido e a execução #2 passou. O histórico da falha foi preservado.
- PTAX BCB EUR/USD foi capturado e publicado com sucesso no [run #2 do pipeline PTAX](https://github.com/carlos-andrade/B3/actions/runs/39413690563). A janela de 30 dias (2026-09-21 a 2026-10-20) produziu 100 observações por moeda, 17.511 bytes por resposta. EUR SHA-256 `9f443bae283df16c25268c706be148fd3f7ed01d436d85c3a7c0a17d569d8757`; USD SHA-256 `e92f95a267cd0a10beb2946371a39441f42711bee219106a0acdd92982d8f282`. RAW e manifestos foram publicados após validação da API oficial OData, licença ODbL e checksums.
- A primeira execução PTAX (#1) falhou num teste unitário por formato esperado de data incorreto; o teste foi corrigido para `MM-DD-YYYY` e a execução #2 passou, incluindo a captura real. O histórico da falha foi preservado.
- Permanecem prioritários o backfill histórico PTAX e outros conjuntos CVM (informe diário de fundos e cadastros). A captura atual PTAX é incremental/móvel de 30 dias, não um backfill histórico completo.
- Não se devem descarregar arquivos históricos volumosos para Git sem avaliar o tamanho, retenção, Git LFS e política de redistribuição; isso é uma decisão de armazenamento, não motivo para omitir o inventário.

### Fase 4 — Corrigir bloqueios genéricos

**Classificação específica aplicada; pendências de acesso B3 mantidas onde faltam provas.**

- **BVBG.028.02:** o [workflow #20](https://github.com/carlos-andrade/B3/actions/runs/39403169556) comprovou que a captura técnica conseguiu 85.659 registos em 2026-10-20. Contudo, a página oficial Pesquisa por Pregão contém proibição de recolha automatizada nessa interface. O endpoint usado pelo importador está associado a essa via. Por isso, o workflow recorrente de captura foi substituído por um gate que não faz chamadas de rede, até ser documentado um canal oficial alternativo ou uma autorização aplicável. A captura histórica existente não foi apagada.
- **COTAHIST:** os ficheiros/layouts são identificáveis publicamente, mas a autorização específica para automação, armazenamento e redistribuição no âmbito previsto não está demonstrada no registo atual. Preservar dados históricos existentes; manter o gate fail-closed e 2026 em `BLOQUEADO_AUTORIZACAO_FONTE` até prova suficiente.
- **BDI:** endpoint identificado, mas licença/escopo específico de automação e redistribuição ainda não comprovado; não presumir que termos de outra página B3 resolvem ou proíbem automaticamente este canal.
- **DRP/Rapinegocios:** origem descoberta em implementação de terceiro; não executar sem confirmação oficial do endpoint e dos direitos de utilização.
- **BCB/CVM:** capturar apenas dentro do âmbito das licenças dos conjuntos identificados; a licença de um conjunto não se transfere automaticamente para anexos ou outros produtos.

### Fase 5 — Validar cobertura, qualidade e roadmap

**Estrutura de validação implementada; encerramento global ainda não comprovado.**
- Inventário versionado e validador estrutural adicionados.
- Orquestrador atualizado para testar o inventário no CI e executar as capturas BCB já existentes.
- A execução CI iniciada pela alteração deve ser verificada antes de declarar os testes aprovados.
- A cobertura ainda é incompleta: backfill histórico PTAX, informe diário/cadastro de fundos e cadastro de companhias CVM, IBGE/SIDRA e Tesouro Transparente requerem captura, teste, manifesto e estado de frescor próprios.
- A issue WATCHDOG #12 só deve ser encerrada após um novo snapshot independente posterior à correção e reconciliação das execuções relevantes.

## 3. Alterações de implementação

1. `dados/fontes/INVENTARIO_FONTES_PUBLICAS_GRATUITAS_V1.json` — 14 fontes/conjuntos, estado, URL, licença, evidência, prioridade e próxima ação.
2. `scripts/governanca/validar_inventario_fontes_publicas.py` — valida campos obrigatórios, IDs únicos, URLs HTTPS, estados permitidos, evidência de bloqueio e coerência de licença.
3. `scripts/governanca/test_validar_inventario_fontes_publicas.py` — testes para fontes válidas, duplicados, URLs inválidas, estados desconhecidos, evidência em falta e licença contraditória.
4. `.github/workflows/b3-fontes-gratuitas-orquestrador.yml` — passou a executar os testes/validação do inventário.
5. `.github/workflows/atualizar-catalogo-b3.yml` — a captura recorrente foi desativada e substituída por gate sem chamada de rede, porque o canal está associado à interface com restrição explícita à automação.

## 4. Critérios de aceitação pendentes

- [x] Confirmar o resultado do CI após a inclusão do validador do inventário — runs #16, #17 e #18 passaram.
- [x] Inspecionar logs e artefactos da execução de auditoria do catálogo/gate — runs #21 e #22 passaram sem chamada de rede.
- [ ] Documentar o canal oficial alternativo ou autorização específica para BVBG.028.02 antes de reativar captura automatizada.
- [ ] Confirmar escopo de uso para COTAHIST e BDI.
- [ ] Implementar e testar capturas PTAX e CVM com licença/recursos exatos, RAW, manifesto, SHA-256 e validação.
- [ ] Validar licença e periodicidade por dataset IBGE/SIDRA e Tesouro Transparente.
- [ ] Fazer novo snapshot WATCHDOG independente e atualizar a Issue #12.
- [ ] Atualizar o README global apenas depois da consolidação das cartas, evidências e validações.

## 5. Regra de fecho

A aquisição deve cobrir agressivamente dados gratuitos e públicos, sem bloqueios genéricos sem evidência. Não se deve, contudo, converter acessibilidade técnica em autorização legal/contratual, nem declarar concluída uma ingestão que não tenha artefacto e validação verificáveis. Todas as pendências acima têm causa concreta e condição de fecho observável.
