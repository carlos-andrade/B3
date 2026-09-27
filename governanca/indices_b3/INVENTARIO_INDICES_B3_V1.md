# INVENTÁRIO — ÍNDICES B3 V1

**Projeto:** B3 - A Bolsa do Brasil  
**Caminho:** governanca/indices_b3/INVENTARIO_INDICES_B3_V1.md  
**Data:** 27/09/2026  
**Repositório:** carlos-andrade/B3

## Escopo da fase 1

Certificação operacional da **composição diária das carteiras dos índices públicos de ações B3**, usando as páginas públicas oficiais da B3 como fonte primária.

A fase 1 cobre os códigos disponibilizados pela B3 no canal público/UP2DATA para índices de ações:

AGFS, BDRX, GPTW, IBBR, IBEE, IBEP, IBEW, IBHB, IBLV, IBOV, IBRA, IBRX, IBRX50, IBSD, ICO2, ICON, IDIV, IDVR, IEE, IFIL, IFIX, IFNC, IGCNM, IGCT, IGCX, IMAT, IMOB, INDX, ISE, ITAG, IVBX2, MLCX, SMLL, UTIL.

## Fonte primária

Endpoint público de carteira diária:

`https://sistemaswebb3-listados.b3.com.br/indexPage/day/{CODIGO}?language=pt-br`

A página oficial informa a carteira do dia, quantidade teórica, participação e, quando aplicável, o redutor.

A B3 informa que as carteiras de índices de ações são revisadas/rebalanceadas periodicamente; a carteira diária deve, portanto, ser tratada como uma observação temporal e não como um cadastro imutável.

## Evidências externas de 27/09/2026

- B3 informa que a carteira definitiva do Ibovespa válida de 08/09/2026 a 31/12/2026 possui 76 papéis de 74 empresas.
- A página oficial do Ibovespa descreve o rebalanceamento quadrimestral.
- A página pública de carteira diária da B3 expõe código, ação, tipo, quantidade teórica e participação.

## Contrato de certificação

Para cada código:

1. captura RAW da página oficial;
2. timestamp de captura;
3. data de referência extraída da própria página;
4. SHA-256 do RAW;
5. normalização para CSV;
6. SHA-256 do NORMALIZED;
7. número de componentes;
8. soma das participações;
9. duplicidade por código do ativo;
10. campos obrigatórios presentes;
11. redutor, quando publicado;
12. rejeição de página vazia, HTML de erro, data futura ou estrutura inválida;
13. manifesto individual;
14. manifesto global;
15. índice oficial corrente;
16. evidência do workflow.

## Regra fail-closed

Nenhum índice será certificado se qualquer validação crítica falhar.

**WORKFLOW SUCCESS != DATA CERTIFIED.**

A certificação do domínio só ocorrerá quando todos os índices do escopo tiverem manifesto `VALIDADO` para a mesma data de referência aplicável, ou quando uma exceção formal estiver documentada.

## Limite da fase 1

Esta fase certifica **composição de carteira**, não substitui:

- séries históricas completas de pontos do índice;
- ticks/intraday;
- dados proprietários UP2DATA;
- derivativos;
- metodologia histórica completa.

Esses domínios continuam separados até receberem sua própria camada de ingestão e validação.
