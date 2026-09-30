# Ordem Operacional de Atualização — COTAHIST

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
