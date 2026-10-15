# Revisão semântica documental — Lote 18: identidade histórica COTAHIST 1986

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-018 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; FASE07_FECHADA_COM_ANOMALIA_K4 |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão histórica; não autoriza alteração dos dados |
| **Origem** | Inspeção de 11 documentos de identidade histórica, campos e colisão K4 de 1986 |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | LAYOUT HISTÓRICO → ATRIBUTOS → CHAVES → REVISÃO SEMÂNTICA → EXCEÇÃO CONTROLADA |
| **Escopo** | FASE07B–07G, identidade histórica, CODNEG, TPMERC, CODBDI, CODISI, DIMES e K4 |
| **Objetivo** | Validar a distinção entre identidade observacional e identidade económica e preservar a anomalia sem correção artificial |
| **Dependências** | RAW/quality JSON de 1986, layout histórico B3 e evidências FASE07 |

## 1. Resultado executivo

Foram revistos 11 documentos da FASE07 para COTAHIST 1986. A metodologia separa corretamente identidade observacional, chave candidata e identidade económica; não presume CODNEG como chave permanente; trata CODISI de 1986 como código interno segundo o layout citado, não como ISIN; e não converte a colisão K4 automaticamente em duplicidade.

O estado consolidado mais recente dentro deste conjunto é: FASE07 fechada operacionalmente com anomalia residual K4 documentada. A anomalia não recebeu interpretação económica definitiva e deve continuar rastreável nas fases posteriores, sem alterar RAW ou NORMALIZED.

A referência temporária de citação no documento CODISI foi substituída por link para a página oficial de layouts da B3; a cópia exata da revisão 02 ainda deve ser preservada com data/hash para constituir evidência primária robusta.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/ingestao/FASE07B_COTAHIST_1986_TPMERC_V1.0.md | Análise de tipo de mercado | Usa a tabela B3 publicada, mas reconhece que a semântica posterior não prova automaticamente a semântica de 1986. TPMERC é atributo de mercado, não identidade permanente. | Manter os códigos desconhecidos sem significado inventado; a prova temporal contemporânea a 1986 permanece limitada. |
| docs/ingestao/FASE07C_COTAHIST_1986_CODBDI_V1.0.md | Análise de classificação BDI | Distingue código documentado de código não mapeado e não presume equivalência económica com CODNEG/TPMERC. | Preservar desconhecidos como não mapeados até haver fonte oficial adequada. |
| docs/ingestao/FASE07D_COTAHIST_1986_CODISI_V1.0.md | Análise de CODISI | Aplica a regra de que ISIN só é utilizado a partir de 15/05/1995; portanto, CODISI em 1986 não é automaticamente ISIN. Citação temporária foi substituída por link oficial de layouts. | Arquivar a revisão 02 do layout com hash/data para evidência primária; não presumir CODISI = CODNEG. |
| docs/ingestao/FASE07E_COTAHIST_1986_DIMES_V1.0.md | Análise de DIMES | Identifica a descrição documental como número de sequência relacionado com estado de direito vigente e explicita que a definição posterior pode não ser retroativamente idêntica. | Não tratar DIMES como identidade económica definitiva sem evidência contemporânea. |
| docs/ingestao/FASE07F_COTAHIST_1986_COLISAO_K4_V1.0.md | Investigação de colisão de chave | A K4 é chave contratual candidata; a colisão residual foi classificada REQUIRES_SEMANTIC_REVIEW e não apagou registos. | Preservar ambos os registos e a evidência; não rotular como duplicidade exata sem comparação dos 25 campos. |
| docs/ingestao/FASE07F_S_COTAHIST_1986_REVISAO_SEMANTICA_K4_V1.0.md | Revisão semântica da colisão | Distingue diferenças económicas entre os dois registos e conclui que a anomalia é rastreável sem correção dos dados. | Manter a exceção residual para auditoria posterior; não declarar identidade económica definitiva. |
| docs/ingestao/FASE07G_COTAHIST_1986_MATRIZ_IDENTIDADE_V1.0.md | Matriz final de identidade | Consolida K1–K4 e os papéis de CODNEG, TPMERC, CODBDI, CODISI e DIMES; não presume unicidade a partir de um campo. | Usar como evidência da análise de identidade, com a exceção K4 explícita. |
| docs/ingestao/FASE07_COTAHIST_1986_FECHAMENTO_IDENTIDADE_V1.0.md | Fechamento de fase | Afirma FASE07 fechada operacionalmente, não semanticamente definitiva, e transfere a anomalia K4 para as fases seguintes. | Estado coerente; não reabrir a fase apenas para eliminar a exceção documental. |
| docs/ingestao/FASE07_COTAHIST_1986_IDENTIDADE_HISTORICA_V1.0.md | Contrato/metodologia de identidade | Rejeita escolher uma chave apenas porque elimina duplicidades e exige evidência para CODNEG reutilizado, CODISI e DIMES. | Preservar distinção entre chave observacional e económica provisória. |
| docs/ingestao/FASE07_COTAHIST_1986_RESULTADO_IDENTIDADE_V1.1.md | Resultado de execução FASE07A | Reporta cardinalidades de atributos e mantém FASE07 global em execução até consolidação 07B–07G. | É um resultado intermédio; o fechamento posterior de FASE07G/status prevalece para estado da fase. |
| docs/ingestao/FASE07_COTAHIST_1986_STATUS_EXECUCAO_V1.0.md | Estado consolidado de execução | Declara FASE07 fechada com anomalia K4 documentada e lista evidências 07A–07G. | É a referência de estado dentro deste conjunto; a exceção continua explícita e não corrigida. |

## 3. Achados e decisões

### SEM-18-01 — CODNEG não é identidade permanente

A mesma designação pode ser reutilizada ao longo do tempo ou em mercados diferentes. A identidade histórica precisa de contexto temporal e de outros atributos documentados.

### SEM-18-02 — CODISI de 1986 não deve ser rotulado como ISIN

O documento usa a regra temporal declarada no layout B3: utilização de ISIN a partir de 15/05/1995. Esta regra deve manter referência a versão específica do layout; não se deve projetar retroativamente um significado posterior sem prova.

### SEM-18-03 — colisão K4 não é duplicidade por definição

Os dois registos partilham a composição K4, mas diferem em atributos que exigem interpretação. A fase preservou ambos e marcou a anomalia para revisão posterior.

**Decisão:** não excluir, corrigir ou substituir nenhum dos registos; manter a evidência JSON e a exceção nas fases subsequentes.

### SEM-18-04 — fechamento operacional não significa resolução económica

A FASE07 pode estar fechada no âmbito de identidade/chaves com exceção residual rastreável. Isso não prova a identidade económica final do instrumento nem elimina a análise semântica posterior.

## 4. Conclusão

O conteúdo dos 11 documentos foi revisto. A FASE07 de 1986 está fechada operacionalmente com anomalia K4 documentada; a identidade económica da colisão não é declarada definitivamente resolvida. Não foram alterados RAW, NORMALIZED ou evidências de máquina.

COTAHIST 1986–2025 permanece somente para consulta/read-only; qualquer nova análise requer decisão formal e não autoriza alteração retroativa dos dados.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Layout dos arquivos — B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/layout-dos-arquivos/)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
