# PARTE03 — BCB/COPOM — AUDITORIA V1.0

Arquivo: PARTE03_BCB_COPOM_AUDITORIA_V1.0.md
Projeto: B3 - A BOLSA DO BRASIL
Tema: auditoria da primeira carga BCB/Copom
Caminho: docs/ingestao/
Data de criação: 24/09/2026
Repositório: carlos-andrade/B3

## Resultado

Foi criada a primeira camada normalizada de eventos Copom 2026 a partir de fontes oficiais do Banco Central.

### Eventos modelados

- decisões da 276ª à 280ª reunião com metas Selic observadas;
- duas sessões da 281ª reunião;
- Ata da 281ª reunião;
- RPM do 3º trimestre de 2026;
- sessões e atas programadas das reuniões 282ª e 283ª.

### Evidência temporal

A página oficial do Copom registra 15–16/09/2026 para a 281ª reunião, Ata em 22/09/2026 às 11:00 e RPM do 3º trimestre em 24/09/2026 às 11:00. O BCB também disponibiliza API oficial para listas e detalhes de atas e comunicados.

### Controle de look-ahead

O dataset distingue eventos RELEASED de SCHEDULED. Uma estratégia histórica deve consumir apenas eventos cujo timestamp de publicação seja <= timestamp da barra. Datas futuras não podem contaminar o estado histórico.

### Próxima etapa

1. Capturar diretamente a API oficial de atas/comunicados.
2. Persistir RAW + metadados + SHA256.
3. Extrair decisão, Selic, votação e texto.
4. Reconciliar Ata/Comunicado com reuniões.
5. Integrar ao calendário IBGE e às sessões da B3.
