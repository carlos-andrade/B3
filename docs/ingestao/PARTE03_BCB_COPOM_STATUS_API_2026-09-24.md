# PARTE03 — BCB/COPOM — STATUS DA API EM 24/09/2026

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-6D2B115B7BE8 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | f032b5b8ba7c80128e599acc20dce063fd0d68598a5d51cc746f9737c3a478d8 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** PARTE03_BCB_COPOM_STATUS_API_2026-09-24.md
**Projeto:** B3 — A Bolsa do Brasil
**Tema:** Status operacional da API oficial do Copom
**Caminho:** docs/ingestao/
**Data de criação:** 24/09/2026
**Repositório:** carlos-andrade/B3

## Resultado

A API oficial do BCB foi confirmada e seus recursos JSON foram identificados.

### Recursos confirmados
- Lista de atas do Copom;
- Detalhes de uma ata;
- Lista de comunicados;
- Recurso de detalhes de comunicado.

### Evidência observada

A lista de atas consultada com quantidade=5 retornou 279ª a 275ª reuniões. A lista de comunicados retornou 280ª a 276ª reuniões.

O recurso de detalhes de ata foi validado com uma resposta JSON contendo texto HTML, PDF e metadados da reunião.

## Limitação registrada

A consulta direta pelo navegador aos endpoints com parâmetros diferentes dos links publicados pelo catálogo apresentou falha de acesso/cache. Portanto, não registrar como capturada a Ata/Comunicado da 281ª reunião nesta etapa.

O script de ingestão existente permanece o mecanismo de execução operacional. A captura definitiva deverá ser executada pelo pipeline HTTP, preservando resposta bruta, URL final, timestamp, Content-Type e SHA-256.

## Controle de integridade

Não foram inventados:
- URL da Ata 281;
- conteúdo do Comunicado 281;
- horário de publicação;
- hash;
- timestamp de disponibilidade.

## Próxima operação

Executar a captura operacional dos endpoints com quantidade suficiente, identificar a 281ª reunião e, somente após resposta válida:
1. salvar RAW;
2. calcular SHA-256;
3. normalizar;
4. validar schema;
5. reconciliar calendário;
6. registrar information_available_at;
7. integrar ao calendário B3.
