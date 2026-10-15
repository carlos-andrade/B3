# Ordem Operacional de Atualização — COTAHIST

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-030--ATUALIZACAO-V1-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO_COTAHIST |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | c51d4685d2c4e0b498b843ebe9eeb3299ffe9780f4be4ff2f72d48fa947b3b1a |
| **Commit de referência (versão anterior)** | [b65ba085fcb987a4457198fc0d31e4e9f7364fbb](https://github.com/carlos-andrade/B3/commit/b65ba085fcb987a4457198fc0d31e4e9f7364fbb) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


**Versão:** V1.0  
**Data:** 2026-09-30

## Regra

O README não é fonte de estado operacional e **não deve ser atualizado antes da execução/verificação da fase**.

A ordem obrigatória é:

1. Alterar/criar o artefato técnico necessário.
2. Disparar a execução real.
3. Verificar o runner e seus resultados.
4. Produzir/atualizar a evidência da fase.
5. Validar os gates e o estado oficial.
6. Somente depois atualizar o README com o estado comprovado.
7. Registrar o commit final e o roadmap.

## Regra anti-falso-positivo

Uma alteração no README nunca pode ser usada como evidência de que uma execução ocorreu.

Se a execução não estiver comprovada, o README deve permanecer sem declarar a fase como concluída.

## Aplicação imediata

Para a FASE06/1994 em curso, a sequência passa a ser:

`EXECUÇÃO REAL → EVIDÊNCIA FASE06 → VALIDAÇÃO → README`

O README será atualizado **por último**, somente após a evidência existir e ser verificada.
