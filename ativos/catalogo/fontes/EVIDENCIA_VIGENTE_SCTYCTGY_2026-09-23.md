# EVIDÊNCIA VIGENTE — SctyCtgy

**Arquivo:** EVIDENCIA_VIGENTE_SCTYCTGY_2026-09-23.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Situação atual da classificação SecurityCategory  
**Data:** 2026-09-23  
**Repositório:** carlos-andrade/B3

## 1. Evidência oficial B3

O Catálogo de Taxonomia UP2DATA da B3 define:

- `SctyCtgy` = SecurityCategoryName;
- representa o terceiro nível da classificação de mercado no pós-negociação;
- requer uma lista externa;
- a lista indicada pela documentação é `ExternalSecurityCategoryCode`, no arquivo `ExternalCodeLists_BVMF.xls`.

Fonte: B3, Catálogo de Taxonomia UP2DATA. citeturn0search16turn0search17

## 2. Consequência para o inventário 2026-09-22

O inventário BVBG.028.02 possui 120.973 registros e contém códigos numéricos em `SctyCtgy`.

A documentação pública localizada confirma a existência e a natureza da lista externa, mas **não disponibilizou nesta pesquisa o arquivo vigente completo com a tabela código → descrição**.

Assim:

- não é permitido converter automaticamente todos os códigos atuais;
- a lista histórica de 2013 permanece apenas como referência temporal;
- códigos presentes no inventário atual e ausentes na lista histórica permanecem sem tradução oficial.

## 3. Mudança futura relevante

A B3 publicou em setembro de 2026 uma alteração prevista para o 4º trimestre de 2026 no BVBG028, incluindo a tag `SctyCtgy` para opções sobre disponível e futuros.

Fonte: B3 — Próximas entregas para o mercado | Negociação. citeturn2search0turn0search4

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

