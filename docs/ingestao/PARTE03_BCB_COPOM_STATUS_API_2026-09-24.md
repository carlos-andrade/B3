# PARTE03 — BCB/COPOM — STATUS DA API EM 24/09/2026

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
