# Revisão semântica documental — Lote 19: calendário histórico e colisão K4 COTAHIST 1986

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-019 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; CALENDARIO_E_K4_MANTIDOS_COM_EXCECAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão histórica; nenhuma alteração dos dados autorizada |
| **Origem** | Inspeção de 15 documentos de FASE08A–08M sobre calendário, colisão K4 e mercado a termo |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | RAW OBSERVADO → FONTE HISTÓRICA → CLASSIFICAÇÃO → EXCEÇÃO CONTROLADA |
| **Escopo** | Dias úteis ausentes em 1986, colisão K4 VGO 2, códigos Cxx, DIMES e tabela histórica Mercado a Termo |
| **Objetivo** | Separar evidência interna de prova histórica e impedir inferências não suportadas |
| **Dependências** | RAW COTAHIST 1986, quality JSON, calendário histórico e fontes institucionais contemporâneas |

## 1. Resultado executivo

Foram revistos 15 documentos da investigação FASE08A–08M. O conjunto mantém a distinção correta entre observação no RAW, padrão estatístico, hipótese e prova histórica. Os 12 dias úteis sem registos tipo 01 permanecem candidatos cuja classificação histórica definitiva requer fonte institucional; atividade em datas vizinhas não prova que cada dia deveria conter negociação.

A colisão K4 de VGO 2 em 10/10/1986 não reaparece como classe recorrente no universo auditado segundo os relatórios, mas a ausência de recorrência não explica a sua origem económica. As fontes contemporâneas encontradas (publicação de 05/06/1986 e documentação histórica/regulatória) demonstram a existência de dimensões Tipo/Prazo e de códigos Cxx, mas não comprovam a regra específica que gerou os dois agregados em 10/10/1986.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/ingestao/FASE08A_COTAHIST_1986_MATRIZ_CALENDARIO_PROVISORIA_V1.0.md | Matriz provisória de calendário | Regista 248 datas distintas, 247 em dias úteis e uma observação em sábado (26/04/1986), sem criar calendário por inferência. | Preservar o snapshot; classificação final depende de fonte histórica por data. |
| docs/ingestao/FASE08B_COTAHIST_1986_EVIDENCIA_DIAS_UTEIS_AUSENTES_V1.0.md | Matriz de 12 dias candidatos | Distingue factos, evidência institucional, hipótese e desconhecido; mantém os 12 dias não resolvidos e o caso de sábado. | Não rotular ausências como feriados, suspensões ou falhas sem fonte primária verificável. |
| docs/ingestao/FASE08C_COTAHIST_1986_DUPLICIDADES_K4_V1.0.md | Análise estrutural de colisões K4 | Investiga colisões estruturais e diferenças de campos sem declarar automaticamente duplicidade económica. | Preservar as linhas e os JSON de evidência; a investigação histórica permanece sem causa definitiva. |
| docs/ingestao/FASE08C_COTAHIST_1986_PADRAO_NEGOCIACAO_ARREDORES_V1.0.md | Análise de atividade em datas vizinhas | Mede continuidade observável antes/depois dos dias candidatos, sem transformar padrão vizinho em prova de sessão. | Usar apenas como evidência interna; requer reconciliação institucional. |
| docs/ingestao/FASE08C_COTAHIST_1986_PADROES_NEGOCIACAO_AUSENCIAS_V1.0.md | Análise de padrões de ausências | Define corretamente que session_status permanece não determinado sem fonte histórica oficial. | Manter a classificação provisória e o gate de fonte primária. |
| docs/ingestao/FASE08D_COTAHIST_1986_RECONSTRUCAO_DOCUMENTAL_10101986_V1.0.md | Busca documental de 10/10/1986 | Separa fatos validados, hipóteses e não demonstrado; não afirma ter encontrado a página exata de BDI de 10/10. | Manter a causa K4 aberta; não completar a lacuna com hipótese. |
| docs/ingestao/FASE08E_COTAHIST_1986_CRONOLOGIA_CXX_DIMES_VGO2_V1.0.md | Análise estatística de cronologia | Testa DIMES, Cxx, CODBDI, TPMERC e VGO 2 antes de inferir causa económica. | Não atribuir causa sem evidência documental suficiente. |
| docs/ingestao/FASE08F_COTAHIST_1986_ESTRUTURA_ESTATISTICA_K4_V1.0.md | Análise estatística de duas linhas | Considera escala e fator de cotação (FATCOT), evitando comparar preços sem unidade. | Resultado estatístico caracteriza diferença, não explica a origem económica. |
| docs/ingestao/FASE08G_COTAHIST_1986_RECORRENCIA_PERFIS_K4_V1.0.md | Teste de recorrência em 1986 | Separa repetição de K4 de repetição de perfil estatístico e declara que recorrência não prova mesma origem económica. | Manter a exceção K4 rastreável. |
| docs/ingestao/FASE08H_COTAHIST_RECORRENCIA_K4_MULTIANOS_V1.0.md | Teste de recorrência multianual | Amplia o universo para verificar se a colisão de 1986 reaparece noutros anos, sem alterar RAW. | A conclusão limita-se ao universo e aos artefactos efetivamente auditados; não reabre anos fechados. |
| docs/ingestao/FASE08I_COTAHIST_1986_RECONSTRUCAO_REGRA_AGREGACAO_V1.0.md | Investigação da regra de agregação | Formula pergunta controlada sobre dimensão de mercado a termo que poderia distinguir linhas, sem assumir taxa como causa. | Manter a hipótese de agregação por testar documentalmente. |
| docs/ingestao/FASE08J_COTAHIST_1986_RECONSTRUCAO_DOCUMENTAL_TERMO_OUTUBRO_1986_V1.0.md | Pesquisa histórica/regulatória | Reúne Instrução CVM 36/1984, Decreto-Lei 2.286/1986, regulamento posterior e imprensa; distingue prova contemporânea de evidência posterior. | Não usar regulamento posterior como prova direta de regra de 1986. |
| docs/ingestao/FASE08K_COTAHIST_1986_ARQUEOLOGIA_BDI_TABELA_TERMO_V1.0.md | Arqueologia documental de BDI | Localiza publicação de 05/06/1986 com tabela Mercado a Termo e notação Vigor PP C05, mas não a página específica de 10/10. | Preservar cópia/URL/hash da publicação consultada; citações temporárias devem ser substituídas por referências persistentes. |
| docs/ingestao/FASE08L_COTAHIST_1986_DIMENSOES_OCULTAS_TERMO_V1.0.md | Teste de dimensões Tipo/Cxx | Conclui que Tipo e Prazo são dimensões distintas na publicação consultada e que Cxx não é sinónimo documental de Tipo. | Resultado estrutural validado; regra histórica para colisão K4 continua não validada. |
| docs/ingestao/FASE08M_COTAHIST_1986_BUSCA_DOCUMENTAL_TIPO_TERMO_V1.0.md | Busca dirigida por coluna Tipo | Compara evidências de 1986–1989 e mantém a possibilidade de dimensões ausentes do COTAHIST como hipótese, não facto. | A conclusão depende de fontes persistentes e não deve ser promovida sem a evidência contemporânea adequada. |

## 3. Achados e decisões

### SEM-19-01 — ausência de registros não identifica causa

Os 12 dias úteis sem registos são factos do arquivo observado. A classificação como feriado, suspensão, falha de captura ou dia sem negociação exige calendário/fonte histórica independente.

**Decisão:** manter status não determinado até existir fonte primária por data e hash verificável.

### SEM-19-02 — colisão K4 permanece exceção controlada

A análise não encontra recorrência que explique a colisão. A publicação histórica de 05/06/1986 demonstra estrutura de tabela a termo e códigos, mas não prova a causa exata dos dois agregados de 10/10/1986.

**Decisão:** não remover, corrigir, agregar ou reinterpretar os dois registos. Manter a anomalia para auditoria e preservar RAW/NORMALIZED.

### SEM-19-03 — evidência estatística não substitui evidência histórica

Padrões de DIMES, Cxx, CODBDI, TPMERC e valores estatísticos podem restringir hipóteses, mas não determinam sozinhos o significado económico de uma linha histórica.

### SEM-19-04 — referências temporárias de pesquisa

Alguns documentos citam identificadores temporários de pesquisa (por exemplo, turn3view0/turn1search0), que não são referências persistentes para leitores do repositório.

**Ação:** quando os documentos forem usados como evidência formal, substituir os identificadores por URL persistente, cópia arquivada ou referência bibliográfica com data e hash. Não inventar URLs nem reconstruir fontes ausentes.

## 4. Conclusão

O conteúdo dos 15 documentos foi revisto. A metodologia é conservadora e não cria fatos para preencher lacunas. O calendário histórico de 1986 e a causa económica da colisão K4 continuam sem resolução definitiva; isso deve permanecer explícito.

COTAHIST 1986–2025 permanece somente para consulta/read-only. Esta revisão não autoriza qualquer alteração aos dados históricos.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
