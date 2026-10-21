# DECISÃO DE GOVERNAÇÃO — REAVALIAÇÃO DO BLOQUEIO COTAHIST

| Campo | Valor |
|---|---|
| Projeto | B3 — A BOLSA DO BRASIL |
| Data | 2026-10-21 |
| Estado | APROVADA OPERACIONALMENTE |
| Escopo | Endpoint direto oficial de ficheiros históricos COTAHIST |
| Commit do registo atualizado | [c710245](https://github.com/carlos-andrade/B3/commit/c710245fecc8941792d355d0352263614c6c8a78) |

## Decisão

Reverter o bloqueio operacional geral aplicado ao endpoint direto de ficheiros históricos COTAHIST. A partir desta decisão, é permitida a aquisição controlada do ficheiro oficial para validação técnica e processamento interno, com proveniência integral e retries limitados.

A decisão aplica o princípio da política de aquisição do projeto: bloqueios devem ser específicos, proporcionais, documentados e reavaliáveis; não se deve estender automaticamente a proibição de uma interface a canais oficiais distintos.

## Limites

1. Esta é uma decisão interna de governação operacional, não uma licença emitida pela B3 nem um parecer jurídico.
2. O escopo não inclui a interface «Pesquisa por Pregão», nem autoriza endpoints B3 diferentes.
3. A aquisição controlada para validação não implica autorização para publicar o RAW num repositório público, redistribuir o ficheiro, usar comercialmente os dados ou desenvolver produto com eles.
4. Antes de publicar ou redistribuir o RAW, confirmar e registar os termos aplicáveis ao armazenamento público e à redistribuição.
5. Se for encontrada uma restrição oficial específica aplicável ao endpoint direto, suspender apenas a atividade afetada e reavaliar a decisão.

## Pipeline autorizado

1. Obter o ZIP oficial por canal direto, com retries limitados.
2. Registar URL, instante UTC, status HTTP, cabeçalhos relevantes, tamanho e SHA-256.
3. Validar integridade ZIP/CRC, membro(s), cabeçalho, trailer, comprimentos de 245 bytes e intervalo de datas.
4. Processar em ambiente controlado e reconciliar os 25 campos com NORMALIZED.
5. Reexecutar validações de calendário e semântica.
6. Não substituir manifestos canónicos nem publicar novo RAW até os controlos de qualidade passarem e a decisão de armazenamento/publicação estar documentada.

## Critério de conclusão

Esta decisão remove o bloqueio geral à aquisição controlada; não afirma que o COTAHIST 2026 já foi atualizado. O dataset só pode ser declarado atualizado após execução comprovada do pipeline e validação de todos os controlos aplicáveis.
