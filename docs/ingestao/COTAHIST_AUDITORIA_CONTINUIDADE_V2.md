# Auditoria COTAHIST B3 1986-2026 — Metodologia V2

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-C6686D4BB2B2 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_AUDITORIA |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 2e38bd5e605f2f34f98d45255a458ac61c2e597735ded295e9ceee77167b82b3 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo
Auditar a integridade estrutural, continuidade temporal e identidade dos registros anuais COTAHIST da B3 entre 1986 e 2026.

## Critérios
- Registro COTAHIST: 245 bytes.
- Registro de negócio: tipo `01`.
- Linhas de cabeçalho/rodapé diferentes de tipo `01` não são, por si só, erro estrutural.
- Erro estrutural: somente registro com comprimento diferente de 245 bytes.
- Intervalo > 4 dias corridos: apenas **candidato a intervalo longo**. Não equivale a pregão ausente sem calendário oficial independente.
- Integridade bruta: SHA-256 do arquivo anual.
- OHLC: verifica `premax >= premin` e se abertura/último permanecem dentro do intervalo high-low quando os quatro valores estão presentes.

## Duplicidade — correção metodológica
A V1 usava uma chave candidata excessivamente ampla para instrumentos históricos e podia confundir evolução de instrumentos com duplicidade.

A V2 separa:
1. **Registro completo exato** — todos os 25 campos iguais.
2. **Identidade de instrumento repetida** — `data_pregao + codbdi + codneg + tpmerc + codisi + dismes` iguais, permitindo que valores/atributos de mercado sejam diferentes.

A segunda categoria é uma **anomalia candidata**, não uma conclusão de duplicação indevida. Instrumentos históricos, opções, direitos, ajustes de código e convenções antigas exigem investigação contextual.

## Interpretação
As listas `isin_com_multiplos_codneg`, `codneg_com_multiplos_isin` e `codneg_com_multiplos_nomres` são evidências de evolução de identidade e nomenclatura. Não devem ser convertidas automaticamente em erro.

## Próxima etapa
Depois da execução V2, os candidatos devem ser cruzados com:
- calendário oficial de pregões;
- regras históricas de negociação e códigos BDI/TPMERC;
- documentação de layout COTAHIST por período;
- eventos corporativos e mudanças de instrumentos.

**Status:** metodologia V2 armazenada; execução GitHub Actions em andamento/aguardando conclusão.
