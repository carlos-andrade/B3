# PARTE03 — B3 INTRADAY: TESTE DOS CANDIDATOS DE DOWNLOAD 2026-09-24

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-8033065400AD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 733d7e29058138d37a4c667a26c7ef1eec6a869d88f1cc95a1bd18441abfd76f |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** PARTE03_B3_INTRADAY_TESTE_CANDIDATOS_DOWNLOAD_2026-09-24.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Validação dos candidatos de download dos pregões 16/09/2026 e 17/09/2026  
**Caminho:** docs/ingestao/PARTE03_B3_INTRADAY_TESTE_CANDIDATOS_DOWNLOAD_2026-09-24.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Resultado

Foram testados, por pesquisa web e acesso direto à URL, os candidatos:

- SPRD260916.zip
- PRA260916.zip
- IN260916.zip

Não foi possível obter o conteúdo binário. A ferramenta web retornou a URL como inacessível e a busca textual não encontrou cópias indexadas dos arquivos.

## Situação

Nenhum dos três candidatos deve ser marcado como RAW capturado.

SPRD260916 = PENDING_BINARY_CAPTURE  
PRA260916 = PENDING_BINARY_CAPTURE  
IN260916 = PENDING_BINARY_CAPTURE

Os candidatos de 17/09 permanecem também pendentes de captura.

## Integridade

Não há:

- SHA-256;
- tamanho de arquivo;
- conteúdo ZIP;
- XML;
- registro de negócios;
- identificação de contrato.

Consequentemente, não há base para calcular métricas de mercado desses arquivos.

## Decisão

O pipeline B3 mantém a regra:

**URL candidata != arquivo capturado.**

A análise Copom 281 permanece bloqueada na etapa de microestrutura até que os bytes primários sejam obtidos.

## Próxima rota

A investigação deve migrar para:

1. mecanismo de sessão/cookies da página Pesquisa por Pregão;
2. identificação do serviço que popula o campo filelist;
3. fontes oficiais B3 alternativas que disponibilizem o mesmo conteúdo;
4. somente em último caso, fonte licenciada, explicitamente identificada como secundária.

