# Publicação automática da Wiki nativa

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-ECB2CA5C5465 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | bca61be441bf30dcd3f539134ef62dc76169827622beb48d635036ca7ff5bdda |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Arquitetura

A documentação versionada em `WIKI/` é a fonte de verdade.

O workflow detecta alterações relevantes, executa reconciliação periódica e publica os documentos selecionados no Wiki nativo, que é um repositório Git separado.

A documentação oficial do GitHub confirma que a Wiki pode ser clonada e atualizada localmente por Git.

## Frequência

O GitHub Actions permite agendamento mínimo de **5 minutos**, e execuções agendadas podem sofrer atraso sob alta carga.

Portanto:

- **evento `push`**: publicação imediatamente após alteração relevante;
- **`schedule` a cada 5 minutos**: reconciliação contra deriva;
- **`workflow_dispatch`**: publicação manual.

Não usamos polling de 1 minuto porque a plataforma não oferece esse intervalo por `schedule`.

## Segredo necessário

O workflow espera o segredo:

`B3_WIKI_TOKEN`

Esse segredo precisa ser uma credencial autorizada a fazer push no repositório da Wiki. O conector utilizado neste projeto não expõe gerenciamento de Secrets do GitHub; portanto, essa configuração precisa ser feita no GitHub.

## Regra de governança

O fluxo oficial é:

`WIKI/ → GitHub Actions → B3.wiki.git → https://github.com/carlos-andrade/B3/wiki`

A Wiki nativa é uma camada de publicação. A documentação auditável permanece no repositório principal.
