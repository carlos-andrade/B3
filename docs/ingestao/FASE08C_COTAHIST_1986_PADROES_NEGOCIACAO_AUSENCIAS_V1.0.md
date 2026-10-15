# FASE 08C — COTAHIST 1986: padrões internos em torno das ausências

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-0096FB6586FA |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 2c39904166f727c5df9a878f9ed61b0ed2eede618c0b3c2c1a8b4f3d0b96f5b8 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo
Reconstruir, exclusivamente a partir do RAW preservado, o padrão de atividade imediatamente antes e depois dos 12 dias úteis sem registros identificados na FASE 08A/08B.

## Regra metodológica
Esta fase mede evidência observacional. Ela não transforma ausência de registros em feriado, suspensão ou sessão perdida sem fonte histórica oficial.

Para cada data candidata são registrados:
- último dia observado anterior e primeiro posterior;
- distância calendárica;
- janela de ±3 dias corridos;
- quantidade de registros por data;
- quantidade de CODBDI, CODNEG e TPMERC distintos;
- continuidade de atividade antes/depois.

## Classificação
EVIDENCIA_COMPATIVEL_COM_CONTINUIDADE_DE_ATIVIDADE_AO_REDOR_DA_AUSENCIA significa somente que há atividade observável em datas vizinhas. O campo session_status permanece NAO_DETERMINADO_SEM_FONTE_HISTORICA_OFICIAL.

## Governança
- RAW não é alterado.
- Normalizado não é alterado.
- Nenhuma data é preenchida artificialmente.
- Nenhuma sessão é criada por inferência estatística.
- A fonte histórica institucional continua necessária para a reconciliação definitiva.

## Saída
dados/cotahist/quality/COTAHIST_1986_EVIDENCIA_PADROES_AUSENCIA_V1.json

## Próxima etapa
FASE 08D: confronto das evidências internas com fontes históricas institucionais recuperáveis para 1986.
