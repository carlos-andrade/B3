# Provedores e Granularidade

**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Matriz de fontes para microestrutura  
**Caminho:** dados/market_data/PROVEDORES_E_GRANULARIDADE.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

## Matriz inicial

| Fonte | EOD | Negócio a negócio | Agressor explícito | Uso |
|---|---:|---:|---:|---|
| BVBG.086.01 | Sim | conforme conteúdo do arquivo | a validar | histórico |
| BVBG.186.01 | Sim | Não tratar como tick feed | Não presumir | ações |
| BVBG.187.01 | Sim | Não tratar como tick feed | Não presumir | derivativos |
| Market Data intradiário | a definir | a definir | a definir | microestrutura |

## Critério

A ausência de evidência sobre um campo significa **não confirmado**, e não zero.

## Próxima validação

Capturar efetivamente um arquivo histórico de cada tipo e inspecionar:

- campos;
- número de registros;
- chaves;
- timestamps, se presentes;
- volume;
- preço médio;
- preço de abertura/mínimo/máximo/último;
- posições em aberto;
- eventuais indicadores de compra/venda.

Somente depois dessa inspeção será definida a arquitetura final de ingestão.
