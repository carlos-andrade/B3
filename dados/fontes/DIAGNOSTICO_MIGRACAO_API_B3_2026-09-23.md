# Diagnóstico e migração da captura B3 — 2026-09-23

## Fato verificado

O workflow `Capturar dados B3 - Pesquisa por Pregao` falhou nos runs #10 e #11 ao chamar:

`https://arquivos.b3.com.br/api/download/requestname`

para `InstrumentsConsolidated` na data de referência `2026-09-22`.

O endpoint retornou HTTP 400 com corpo RFC 9110 e `traceId`. A mesma chamada foi rejeitada mesmo com `recaptchaToken=`, portanto o problema não é mais a escolha da data nem a sintaxe do importador.

## Evidência externa

A B3 informa que as antigas páginas de Dados públicos de produtos listados e de balcão e Cotações foram desativadas em 31/03/2026 e que os dados anteriormente publicados passaram a ser disponibilizados no BDI desde 15/12/2025.

A documentação técnica atual encontrada para o ecossistema B3 confirma duas rotas relevantes:

1. **BDI:** API HTTP POST em `https://arquivos.b3.com.br/bdi/table/<Endpoint>/<data-inicial>/<data-final>/<pagina>/<pageSize>`, com corpo JSON `{}`.
2. **Pesquisa por Pregão:** download por `https://www.b3.com.br/pesquisapregao/download?filelist=...`.

Para BVBG.028.02, a implementação pública de referência usa `IN{aammdd}.zip`, por exemplo `IN260922.zip`.

## Decisão técnica

Não considerar a API legada `/api/download/requestname` como fonte operacional até nova evidência de disponibilidade.

A arquitetura passa a separar:

- `Pesquisa por Pregão` → arquivos de layout/cadastro, especialmente BVBG.028.02;
- `BDI` → tabelas diárias de mercado;
- outras fontes B3 → históricos, índices e arquivos especializados quando o BDI não reproduzir o dataset necessário.

## Regra de auditoria

Nenhum dado será considerado capturado somente porque a página existe. A entrada só passa para a camada de dados quando houver:

- resposta HTTP válida;
- arquivo/payload bruto preservado;
- data de referência;
- URL de origem;
- SHA-256;
- validação estrutural;
- contagem de registros quando aplicável;
- manifesto.

## Próxima implementação

1. Capturar BVBG.028.02 pela rota atual de Pesquisa por Pregão.
2. Criar adaptador genérico para BDI POST.
3. Mapear cada dataset prioritário para sua fonte operacional atual.
4. Testar uma fonte por vez antes de ativar a automação diária.
5. Manter a API legada apenas como histórico/diagnóstico, não como pipeline de produção.
