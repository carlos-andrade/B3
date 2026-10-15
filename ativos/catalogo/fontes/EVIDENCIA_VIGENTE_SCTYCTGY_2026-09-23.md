# EVIDÊNCIA VIGENTE — SctyCtgy

| Campo | Valor |
|---|---|
| **ID** | B3-CAT-FONTE-002 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | EVIDENCIA_DE_FONTE |
| **Fase** | CLASSIFICACAO_CADASTRAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | b9429435535988140fb7219627b365d3a9a04f9cab34547fa3c58abcf88ec529 |
| **Commit de referência (versão anterior)** | [1b0542c46918856832742ca82daa683cf665c3ac](https://github.com/carlos-andrade/B3/commit/1b0542c46918856832742ca82daa683cf665c3ac) |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório |
| **Origem** | Catálogo de Taxonomia UP2DATA da B3 e documentação do cadastro de instrumentos; correspondência vigente completa ainda não capturada |
| **Autoridade superior** | [Norma de cabeçalho documental da GOVERNANÇA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Evidência oficial B3

O Catálogo de Taxonomia UP2DATA da B3 define:

- `SctyCtgy` = SecurityCategoryName;
- representa o terceiro nível da classificação de mercado no pós-negociação;
- requer uma lista externa;
- a lista indicada pela documentação é `ExternalSecurityCategoryCode`, no arquivo `ExternalCodeLists_BVMF.xls`.

Fonte: B3, Catálogo de Taxonomia UP2DATA.

## 2. Consequência para o inventário 2026-09-22

O inventário BVBG.028.02 possui 120.973 registros e contém códigos numéricos em `SctyCtgy`.

A documentação pública localizada confirma a existência e a natureza da lista externa, mas **não disponibilizou nesta pesquisa o arquivo vigente completo com a tabela código → descrição**.

Assim:

- não é permitido converter automaticamente todos os códigos atuais;
- a lista histórica de 2013 permanece apenas como referência temporal;
- códigos presentes no inventário atual e ausentes na lista histórica permanecem sem tradução oficial.

## 3. Mudança futura relevante

A B3 publicou em setembro de 2026 uma alteração prevista para o 4º trimestre de 2026 no BVBG028, incluindo a tag `SctyCtgy` para opções sobre disponível e futuros.

Fonte: B3 — Próximas entregas para o mercado | Negociação.

Isso reforça que a tabela de códigos deve ser tratada como **versionada e dependente da data**, e não como uma enumeração histórica fixa.

## 4. Regra oficial do projeto

A classificação normalizada do snapshot 2026-09-22 só será publicada como oficial quando a lista vigente da B3 for capturada ou quando a própria documentação vigente fornecer a correspondência.

Até lá, o pipeline utilizará conjuntamente:

1. `Asst`;
2. `AsstDesc`;
3. `Desc`;
4. `SgmtNm`;
5. `MktNm`;
6. `SctyCtgy`;
7. `CFICd`;
8. demais atributos estruturais;

sem substituir a classificação oficial de `SctyCtgy`.

## 5. Status

**BVBG.028.02:** VALIDADO  
**SctyCtgy — existência/campo:** VALIDADO  
**SctyCtgy — tabela vigente código → descrição:** NÃO CAPTURADA  
**Classificação econômica final:** EM ANDAMENTO  
**BDI:** VALIDADO EM TESTE DE CAPTURA  
**Microestrutura:** PENDENTE DE CRUZAMENTO COM DADOS DE NEGÓCIOS
