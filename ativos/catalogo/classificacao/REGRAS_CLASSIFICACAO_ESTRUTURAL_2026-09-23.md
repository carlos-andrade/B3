# REGRAS DE CLASSIFICAÇÃO ESTRUTURAL — BVBG.028.02

**Arquivo:** REGRAS_CLASSIFICACAO_ESTRUTURAL_2026-09-23.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Fonte:** BVBG.028.02 — snapshot 2026-09-22  
**Data:** 2026-09-23

## 1. Objetivo

Separar o universo cadastral de 120.973 registros em grupos econômicos e operacionais utilizando evidência presente no próprio cadastro.

## 2. Hierarquia

**Nível A — OFICIAL_B3:** campo ou tabela B3 explicitamente documentada.

**Nível B — ESTRUTURAL:** classificação diretamente sustentada por descrição ou atributos do instrumento.

**Nível C — HIPÓTESE:** padrão plausível que precisa de confirmação por fonte B3 adicional.

**Nível D — NÃO CLASSIFICADO:** sem evidência suficiente.

## 3. Regras de alta confiança

### Opções

Evidência principal: AsstDesc contendo termos explícitos de opção; CFICd iniciado por O quando combinado com descrição/atributos compatíveis; OptnTp preenchido.

Não classificar somente pelo primeiro caractere do CFI quando houver conflito com os demais campos.

### Futuros

Evidência principal: AsstDesc contendo FUTURO, Minicontrato ou Rolagem de Futuro; atributos de vencimento e/ou multiplicador compatíveis.

### Índices

Evidência principal: AsstDesc explicitamente identificando índice; Asst/descrição reconhecendo índice como referência.

### Moedas / FX

Evidência principal: AsstDesc explicitamente identificando moeda, dólar, euro, iene, libra, câmbio ou contrato cambial; combinação com vencimento e multiplicador quando aplicável.

### Juros / taxas

Evidência principal: AsstDesc contendo taxa, DI, FRA, cupom, DV01, PU ou instrumento de taxa; atributos compatíveis.

### Commodities

Evidência principal: AsstDesc identificando boi, milho, café, soja, ouro, etanol ou outra commodity; contrato futuro/opção deve ser separado do ativo físico subjacente.

### ETFs

Evidência principal: descrição explicitamente identificando ETF ou nome de fundo/índice compatível; nunca inferir ETF apenas pelo ticker.

### Fundos

Evidência principal: descrição explicitamente identificando fundo/FIC/FII ou categoria equivalente; validação adicional por CFI e SctyCtgy.

### Ações

Evidência principal: descrição/tipo de instrumento compatível com participação acionária; CFI de equity compatível; evitar classificar todo ticker de quatro caracteres como ação.

## 4. Conflitos

Quando regras produzirem grupos diferentes, registrar CONFLITO_CLASSIFICACAO. O registro permanece sem classificação final até validação.

## 5. Regra de liquidez

**Classificação não significa liquidez.** Um instrumento cadastrado como ação, ETF, futuro ou opção não será considerado líquido sem cruzamento com negócios, volume, volume financeiro, frequência, spread quando disponível e contratos em aberto quando aplicável.

## 6. Saída planejada

Arquivo futuro: ativos/catalogo/classificacao/CLASSIFICACAO_ESTRUTURAL_B3_2026-09-22.csv

Campos mínimos: Id, TckrSymb, Asst, AsstDesc, SctyCtgy, CFICd, CategoriaEstrutural, NivelConfianca, RegraAplicada, Evidencia.
