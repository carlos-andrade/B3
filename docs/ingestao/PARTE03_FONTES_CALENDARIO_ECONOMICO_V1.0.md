# PARTE03 — MATRIZ DE FONTES DO CALENDÁRIO ECONÔMICO V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-0F8FFC0BB0C3 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 3eb8defc60eb0fb46ac3554992a2d6908db3c54b7ac3bb3ae0c67bca87dc61bb |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
