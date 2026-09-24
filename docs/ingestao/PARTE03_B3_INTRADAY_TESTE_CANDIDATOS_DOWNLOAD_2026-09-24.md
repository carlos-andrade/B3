# PARTE03 — B3 INTRADAY: TESTE DOS CANDIDATOS DE DOWNLOAD 2026-09-24

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

