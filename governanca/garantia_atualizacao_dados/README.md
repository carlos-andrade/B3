# Garantia de Atualização dos Dados

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-6325FBE650C0 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | fce434cba3ac87b1d151a5a095a024f342c1e50d111fe59b49d071dff3780208 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Esta pasta contém os documentos de certificação da atualidade dos dados de mercado e macroeconômicos utilizados pelo projeto B3.

## Regra de emissão

Uma **Carta de Garantia de Atualização** somente pode declarar cobertura integral quando cada dataset sob escopo tiver:

1. fonte identificada e auditável;
2. última data de observação identificada;
3. última data de ingestão identificada;
4. validação de integridade concluída;
5. ausência de lacuna conhecida entre a última observação disponível na fonte e a última observação armazenada, salvo justificativa documental;
6. evidência do workflow responsável pela atualização;
7. status **APROVADO** em todos os datasets obrigatórios.

Se qualquer requisito falhar, a carta deve ser **PENDENTE** ou **NÃO CERTIFICADA**. É proibido transformar data de execução do workflow em data de mercado.

## Documento principal

- Carta de Garantia de Atualização dos Dados — status da verificação corrente.
