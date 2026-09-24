# PARTE03 — BCB/COPOM — ENDPOINTS DA API V1.0

**Arquivo:** PARTE03_BCB_COPOM_API_ENDPOINTS_V1.0.md
**Projeto:** B3 — A Bolsa do Brasil
**Tema:** Endpoints oficiais da API de documentos do Copom
**Caminho:** docs/ingestao/
**Data de criação:** 24/09/2026
**Repositório:** carlos-andrade/B3

## 1. Fonte oficial

O Portal de Dados Abertos do Banco Central disponibiliza recursos JSON para listas e detalhes de atas e comunicados do Copom. O conjunto é mantido pelo BCB/Depep.

## 2. Endpoints identificados

### Lista de atas
https://www.bcb.gov.br/api/servico/sitebcb/copom/atas?quantidade=N

Exemplo observado:
https://www.bcb.gov.br/api/servico/sitebcb/copom/atas?quantidade=5

Campos observados:
- nroReuniao
- dataReferencia
- dataPublicacao
- titulo

### Detalhes de ata
https://www.bcb.gov.br/api/servico/sitebcb/copom/atas_detalhes?nro_reuniao=N

Estrutura observada:
- identificação da reunião;
- data de referência;
- data de publicação;
- URL do PDF;
- texto integral da ata em HTML;
- informações da reunião;
- participantes;
- decisão e votos.

### Lista de comunicados
https://www.bcb.gov.br/api/servico/sitebcb/copom/comunicados?quantidade=N

Campos observados:
- nro_reuniao
- dataReferencia
- titulo

### Detalhes de comunicado
O recurso oficial foi identificado no catálogo. A URL exata deverá ser capturada do recurso antes da implementação final do parser; não será inferida por convenção.

## 3. Evidência atual

A lista de atas consultada retornou as reuniões 279, 278, 277, 276 e 275. A lista de comunicados retornou 280 a 276.

## 4. Regra de ingestão

O pipeline deve separar:
1. reunião agendada;
2. decisão realizada;
3. comunicado publicado;
4. ata publicada;
5. horário efetivo de publicação;
6. momento em que a informação tornou-se disponível para backtest.

## 5. Próximo passo

Capturar diretamente os recursos oficiais, preservar RAW imutável, calcular SHA-256, extrair a reunião 281 quando o recurso estiver disponível e reconciliar data da reunião, decisão Selic, comunicado, ata, publicação, information_available_at e sessão B3 afetada.
