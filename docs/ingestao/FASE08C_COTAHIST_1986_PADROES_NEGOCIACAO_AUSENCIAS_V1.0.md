# FASE 08C — COTAHIST 1986: padrões internos em torno das ausências

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
