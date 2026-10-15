# Revisão semântica documental — Lote 12: catálogos por classe de ativos

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-012 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; LISTAGEM_CORRENTE_EXIGE_FONTE_OFICIAL |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão semântica de documentação descritiva |
| **Origem** | Inspeção de 14 README de classes de ativos |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | FONTE OFICIAL → CAPTURA DATADA → CATÁLOGO → CLASSIFICAÇÃO → CONSUMO |
| **Escopo** | CEPAC, commodities, criptoativos, empréstimo de ativos, ETFs, FIIs, fundos, futuros, índices, juros, moedas, opções, renda fixa e termo |
| **Objetivo** | Verificar que a documentação por classe não se apresenta como prova de listagem ou negociabilidade atual |
| **Dependências** | Cadastro oficial de instrumentos B3, especificações por segmento e data de referência |

## 1. Resultado executivo

Foram revistos 14 README de classes de ativos. A maioria define o âmbito documental de uma pasta e exige origem oficial/data de captura; alguns enumeram exemplos de classes ou instrumentos. A presença de uma classe, exemplo ou diretório não demonstra que exista instrumento atualmente listado, ativo, elegível ou negociável na B3.

Os README são documentação de organização, não catálogo de instrumentos nem recomendação de investimento. A confirmação deve vir do cadastro oficial da B3 e das especificações aplicáveis, com data de referência, preservando distinção entre listado, registado, negociável e apenas referenciado.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| ativos/cepac/README.md | README de classe | Define CEPAC e documentação relacionada; exige confirmação oficial por data e separação entre factos e hipóteses. | Não inferir existência/negociabilidade a partir da pasta. |
| ativos/commodities/README.md | README de classe | Enumera exemplos (boi gordo, milho, cafés, soja, etanol, ouro) como escopo de commodities. A frase pode ser lida como afirmação geral de disponibilidade. | Interpretar como âmbito de catálogo; antes de publicar lista de instrumentos, validar cada contrato no cadastro e especificações oficiais para a data. |
| ativos/criptoativos/README.md | README de classe | Declara que não se deve presumir listagem ou negociação vigente sem evidência oficial. | Manter a regra; validar cada produto e vencimento/série na fonte. |
| ativos/emprestimo_ativos/README.md | README de serviço | Separa cadastro, posições e dados operacionais de empréstimo de ativos. | Não confundir o serviço de empréstimo com uma classe de título ou com disponibilidade atual de cada ativo. |
| ativos/etfs/README.md | README de classe | Descreve ETFs e classes subjacentes, mas não é evidência de listagem atual. | Confirmar cada ticker/ISIN e estado na fonte oficial. |
| ativos/fiis/README.md | README de classe | Delimita FIIs negociados/listados; a descrição não contém uma fotografia do cadastro. | Validar registo/listagem e data de referência por instrumento. |
| ativos/fundos/README.md | README de classe | Abrange fundos listados e outras classes conforme o cadastro aplicável. | Distinguir fundos negociados, registados e classes sem negociação secundária. |
| ativos/futuros/README.md | README de classe | Afirma que vigência/características dependem de evidência oficial datada e exige separação entre factos e hipóteses. | Manter essa regra; especificações e vencimentos não devem ser inferidos. |
| ativos/indices/README.md | README de classe | Distingue índices de instrumentos diretamente negociáveis. | Não tratar o índice de referência como ativo negociável; validar produtos ligados ao índice separadamente. |
| ativos/juros/README.md | README de classe | Enumera exemplos de taxas/séries e avisa que nem todos os exemplos estão listados na B3 na mesma data. | Tratar a lista como escopo conceptual; validar contrato e especificação oficial por instrumento. |
| ativos/moedas/README.md | README de classe | Declara que disponibilidade, ticker e especificações dependem do cadastro oficial datado. | Não inferir que todos os pares/moedas listados no texto são contratos vigentes. |
| ativos/opcoes/README.md | README de classe | Distingue série, ativo-objeto e data; exige confirmação oficial. | Não presumir que todos os ativos-objeto ou séries estejam disponíveis simultaneamente. |
| ativos/renda_fixa/README.md | README de classe | Distingue negociação, registo e serviços de infraestrutura. | Não tratar registo na infraestrutura como prova de negociação secundária ou direito de distribuição. |
| ativos/termo/README.md | README de classe | Exige confirmação de elegibilidade/disponibilidade em fonte oficial datada. | Validar as regras e ativos elegíveis antes de afirmar que uma operação é permitida. |

## 3. Achados e decisões

### SEM-12-01 — classes documentais não provam disponibilidade

A organização por classe é útil, mas pode induzir erro se for consumida como catálogo corrente. Isto é particularmente relevante para futuros, opções, moedas, juros e commodities, em que vencimento, série, ativo-objeto, especificação e data de vigência importam.

**Decisão:** qualquer listagem corrente deve derivar do cadastro oficial e conter data de captura. README não deve ser usado para construir tickers ou contratos por inferência.

### SEM-12-02 — distinguir listagem, registo e negociabilidade

Um instrumento pode estar registado ou ser suportado pela infraestrutura sem estar necessariamente disponível para negociação no mercado secundário. O estado deve vir da fonte e do contrato aplicável.

**Decisão:** manter campos de estado e fonte por instrumento; não inferir negociabilidade apenas pelo nome da classe.

### SEM-12-03 — classes e exemplos não são recomendação

Os documentos descrevem escopo de dados e infraestrutura, não adequação de investimento, liquidez ou retorno.

**Decisão:** não usar estas páginas como recomendação de investimento nem como fonte de métricas de liquidez.

## 4. Conclusão

O conteúdo dos 14 README foi revisto. O lote está concluído como revisão documental; a validação da listagem, vigência e negociabilidade de instrumentos continua dependente de fontes oficiais por data e não é certificada por este lote.

COTAHIST 1986–2025 permanece somente para consulta; 2026 mantém atualização diária. Não foram alterados dados RAW, catálogo ou manifestos.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Protocolo de captura do catálogo B3](../../ativos/catalogo/PROTOCOLO_CAPTURA.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
