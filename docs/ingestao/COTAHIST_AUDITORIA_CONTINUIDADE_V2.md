# Auditoria COTAHIST B3 1986-2026 — Metodologia V2

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
