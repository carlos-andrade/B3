# PARTE03 — MATRIZ DE FONTES DO CALENDÁRIO ECONÔMICO V1.0

**Arquivo:** PARTE03_FONTES_CALENDARIO_ECONOMICO_V1.0.md  
**Projeto:** B3 — A BOLSA DO BRASIL  
**Tema:** Fontes oficiais e política de precedência  
**Caminho:** docs/ingestao/PARTE03_FONTES_CALENDARIO_ECONOMICO_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Matriz inicial

| Evento | Fonte primária | Histórico | Uso |
|---|---|---|---|
| IPCA | IBGE | conforme disponibilidade oficial | inflação |
| IPCA-15 | IBGE | conforme disponibilidade oficial | inflação antecipada |
| INPC | IBGE | conforme disponibilidade oficial | inflação |
| PNAD Contínua | IBGE | conforme disponibilidade oficial | trabalho |
| PIB | IBGE | conforme disponibilidade oficial | atividade |
| Produção Industrial | IBGE | conforme disponibilidade oficial | atividade |
| Comércio | IBGE | conforme disponibilidade oficial | atividade |
| Serviços | IBGE | conforme disponibilidade oficial | atividade |
| Copom/Selic | Banco Central | conforme calendário/histórico oficial | política monetária |
| Ata do Copom | Banco Central | conforme disponibilidade oficial | comunicação |
| Relatório de Política Monetária | Banco Central | desde a disponibilidade oficial | macro/juros |

## Evidência atual verificada em 24/09/2026

O calendário conjuntural do IBGE informa, entre outras divulgações, IPCA-15 em 25/09/2026, PNAD Contínua mensal em 29/09/2026 e IPCA em 09/10/2026. citeturn0search1turn0search7

O IBGE também disponibiliza calendários específicos por indicador; para o IPCA, por exemplo, a próxima divulgação indicada é 09/10/2026 para a referência 09/2026. citeturn0search2

Para o Banco Central, o histórico oficial do Copom registra que o comunicado da decisão é divulgado após a segunda sessão da reunião, a partir das 18h, e que a ata é divulgada às 8h da terça-feira da semana seguinte, dentro do prazo regulamentar. citeturn0search8

O Banco Central também disponibiliza um recurso de calendário de divulgação do Relatório de Política Monetária no Portal de Dados Abertos. citeturn0search4

## Política

A fonte oficial é a autoridade de referência do evento. Agregadores podem ajudar na descoberta, mas não substituem a evidência oficial.

O dataset deve separar:

1. **scheduled** — evento originalmente programado;
2. **released** — divulgação efetivamente realizada;
3. **revised** — alteração posterior;
4. **cancelled** — evento cancelado;
5. **unknown** — informação incompleta que não pode ser resolvida com segurança.

Nenhum consenso de mercado será inserido sem origem identificável e timestamp de disponibilidade.
