# Classificação estrutural do inventário B3

**Projeto:** B3 - A Bolsa do Brasil  
**Fonte-base:** BVBG.028.02  
**Regra:** classificação estrutural auditável, sem substituir a classificação oficial B3.

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
