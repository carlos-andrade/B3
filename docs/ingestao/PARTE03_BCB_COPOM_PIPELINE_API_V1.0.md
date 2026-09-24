# PARTE03 — BCB/COPOM — PIPELINE API V1.0

Arquivo: PARTE03_BCB_COPOM_PIPELINE_API_V1.0.md
Projeto: B3 - A BOLSA DO BRASIL
Tema: captura de Atas e Comunicados via API oficial
Caminho: docs/ingestao/
Data de criação: 24/09/2026
Repositório: carlos-andrade/B3

## Fonte

O Portal de Dados Abertos do Banco Central disponibiliza API para lista e detalhe de Atas e Comunicados do Copom. A documentação informa que as Atas estão disponíveis desde a 21ª reunião e os Comunicados desde a 46ª. A decisão é divulgada no mesmo dia por Comunicado; a Ata é normalmente publicada na terça-feira seguinte às 08:00.

## Arquitetura

API oficial → RAW original → metadados → SHA256 → parser → NORMALIZED → reconciliação por reunião → timestamp de informação → integração B3.

## Regra crítica

A data da reunião não é o timestamp de disponibilidade da informação.

Para backtest, usar a regra:
information_available_at <= bar_timestamp

scheduled_date representa calendário. published_at representa disponibilidade real. Nunca substituir um pelo outro.

## RAW

Cada resposta deve ser preservada sem alteração, acompanhada de URL solicitada, URL final, Content-Type, UTC de captura, SHA256 e tamanho em bytes.

## NORMALIZED

Separar metadados da reunião, decisão, votos, comunicado, ata, horário/data de publicação, conteúdo textual e referência à evidência RAW.

## Integridade

Não sobrescrever RAW. Nova captura gera novo snapshot versionado. Revisões posteriores são eventos novos e não devem corrigir retroativamente o estado histórico da informação disponível.