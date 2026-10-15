# Classificação estrutural do inventário B3

| Campo | Valor |
|---|---|
| **ID** | B3-ATIVOS-CLASSIFICACAO-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | README_METODOLOGIA |
| **Fase** | Catálogo B3 — classificação estrutural |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | cd940ea5ebc58971872800f5d50d35e28372460e72753e8545d960a60aa2786b |
| **Commit de referência (versão anterior)** | N/A — primeira normalização do cabeçalho |
| **Data de criação** | N/A — data original não registada no documento |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação metodológica e aprovação humana |
| **Origem** | Cadastro de instrumentos B3, BVBG.028.02 e regras de classificação estrutural |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Camadas

1. **OFICIAL_B3** — quando houver campo/tabela oficial B3.
2. **ESTRUTURAL** — determinada diretamente por atributos do cadastro, principalmente AsstDesc, CFICd, OptnTp, XprtnDt, Undrlyg, SgmtNm e MktNm.
3. **HIPOTESE** — padrão identificado, mas que exige confirmação externa.
4. **NAO_CLASSIFICADO** — evidência insuficiente.

## Prioridade

`SctyCtgy oficial > descrição oficial > atributos estruturais > CFI > ticker/ativo-base`.

Ticker nunca será usado isoladamente para classificar instrumento.

## Primeiros grupos estruturais

- Ações / participações
- ETFs
- Fundos
- BDRs / recibos
- Opções
- Futuros
- Índices
- Moedas / FX
- Juros / taxas
- Commodities
- Renda fixa
- Certificados / outros instrumentos
- Indicadores econômicos
- Instrumentos não classificados

## Regra de auditoria

Toda classificação derivada deverá registrar:

`instrumento | regra aplicada | evidência | nível de confiança | fonte`.

A classificação estrutural não representa recomendação de investimento nem liquidez.
