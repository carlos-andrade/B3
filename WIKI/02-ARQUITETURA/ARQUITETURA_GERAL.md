# Arquitetura Geral

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-AA13047E0C4D |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | d7ce84b5b8ee10bdf6fb828aade68bcc3c0fff43749520cfc92566c8bc3b2fc6 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Visão em camadas

```text
FONTES
  ↓
AQUISIÇÃO
  ↓
RAW / PRESERVAÇÃO
  ↓
NORMALIZAÇÃO
  ↓
VALIDAÇÃO
  ↓
EVIDÊNCIAS / AUDITORIA
  ↓
DADOS PUBLICADOS
  ↓
ANÁLISE / BACKTEST / APLICAÇÕES
```

## Fontes

A arquitetura pode integrar dados da B3, BCB e outras fontes econômicas ou de mercado devidamente identificadas.

## Aquisição

Os processos de aquisição devem registrar período, origem, arquivo obtido, resultado da operação e eventuais falhas.

## RAW

A camada RAW preserva o material recebido antes das transformações.

## Normalização

Transformações devem ser determinísticas sempre que possível e possuir código ou documentação suficiente para reprodução.

## Validação

A validação deve cobrir estrutura, tipos, chaves, datas, campos semânticos, valores, volumes e quantidades, calendário e amostras comparativas com a origem.

## Auditoria

A arquitetura deve permitir responder: de onde veio este dado, o que foi feito com ele, qual versão do processo o produziu, quais testes foram executados e qual evidência comprova o resultado.

## Evolução

A arquitetura será ampliada conforme novos módulos forem validados. Alterações relevantes devem atualizar esta página.
