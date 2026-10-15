# COTAHIST 2026 — Auditoria da promoção controlada FASE11

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-6537D19DD621 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_AUDITORIA |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | dab4a4dfb41af935ab1b33a2232fd456c2370def035dc0b1b565a6823c7e6d87 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Data da auditoria:** 2026-10-14  
**Repositório:** `carlos-andrade/B3`  
**Dataset canónico:** COTAHIST anual 2026

## Resultado executivo

A promoção do candidato oficial foi persistida no commit `3e4914638dedb5bec1935abd4a9821e5ddc4cfc6`. O workflow `38548092815` terminou com sucesso. Uma execução subsequente (`38548149197`) terminou com falha ao repetir a operação; a evidência disponível mostra que a etapa de preparação foi bem-sucedida e que a etapa de commit falhou. Como os ficheiros canónicos já estavam no estado-alvo, a falha é compatível com uma tentativa de commit sem alterações, mas a mensagem integral do log não estava disponível para confirmar a causa exata.

**Interpretação:** a falha da execução repetida não reverteu a promoção previamente persistida. A FASE11 deve, contudo, ser tornada idempotente para que uma segunda execução valide o estado existente e termine sem falhar quando não há alterações a gravar.

## Integridade verificada no branch `main`

| Elemento | Valor |
|---|---|
| RAW SHA-256 | `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e` |
| NORMALIZED SHA-256 | `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc` |
| Linhas NORMALIZED | 3.142.910 |
| Campos | 25 |
| Primeira data | 2026-01-02 |
| Última data | 2026-10-13 |
| Datas inválidas / fora do ano | 0 / 0 |
| Deduplicação | Não executada |

Os valores acima foram comparados com os manifestos e sidecars de checksum publicados no branch `main`.

## Execuções relevantes

- FASE10 validação do candidato: [run 38546769668](https://github.com/carlos-andrade/B3/actions/runs/38546769668) — sucesso.
- FASE11 promoção controlada: [run 38548092815](https://github.com/carlos-andrade/B3/actions/runs/38548092815) — sucesso.
- FASE11 repetição subsequente: [run 38548149197](https://github.com/carlos-andrade/B3/actions/runs/38548149197) — falha na etapa de commit e na persistência da evidência.
- Publicação do dataset oficial: [run 38549492463](https://github.com/carlos-andrade/B3/actions/runs/38549492463) — sucesso.
- Revalidação FASE04/05 após promoção: [run 38550406921](https://github.com/carlos-andrade/B3/actions/runs/38550406921) — execução iniciada; resultado final ainda por confirmar no momento desta auditoria.

## Próximas ações obrigatórias

1. Concluir e verificar a nova execução FASE04/05 com os hashes promovidos.
2. Executar sequencialmente FASE06, FASE07 e FASE08, sem deduplicar nem reordenar os dados.
3. Recalcular o gate 06–08 e reavaliar a atualidade/calendário na FASE09.
4. Corrigir a FASE11 para verificar `git diff --cached --quiet` antes de `git commit`, persistir a evidência com rebase/push idempotente e só declarar promoção após verificar o estado remoto efetivo.
5. Confirmar que cada evidência persistida corresponde aos hashes presentes no branch `main`.

## Limitações

Esta auditoria confirma os hashes e metadados publicados, não substitui a reconciliação semântica integral RAW → NORMALIZED. A liberação final depende da execução bem-sucedida das fases subsequentes e do gate atualizado.
