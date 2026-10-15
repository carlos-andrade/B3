# Inventário estrutural COTAHIST — V1

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-024-OWS-COTAHIST-V1-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO_COTAHIST |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | f0641e36fe938d70a4c7e340299f70e7ba72305950b1e58b72f51a72659adc15 |
| **Commit de referência (versão anterior)** | [b65ba085fcb987a4457198fc0d31e4e9f7364fbb](https://github.com/carlos-andrade/B3/commit/b65ba085fcb987a4457198fc0d31e4e9f7364fbb) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


**Data:** 2026-09-29  
**Branch:** main

## Contagem

- Workflows totais em `.github/workflows`: **86**
- Workflows com prefixo `cotahist-`: **74**

## Classificação macro

### 1986 — exceção histórica
**32 workflows** relacionados diretamente à trilha 1986, incluindo FASE 07, FASE 08, FASE 09B, auditorias específicas e o gate histórico.

Tratamento: **pipeline excepcional controlado**. Não deve ser misturado automaticamente ao fluxo anual normal.

### 1987 — trilha histórica em reconciliação
Workflows específicos de calendário, OHLC, quantidade/volume, chave lógica, integridade de campos, semântica, PRAZOT, reconciliação RAW/NORMALIZED, normalização/matriz e certificação.

Tratamento: **pipeline histórico incompleto/heterogêneo**, com o problema LFS conhecido separado do fluxo 1988+.

### 1988 — trilha histórica auditada
Existem workflows independentes para calendário, OHLC, quantidade/volume, chave lógica, integridade de campos, semântica, exceções, reconciliação, reconciliação final, validação independente e FASE 10.

Tratamento: **pipeline histórico com evidências já produzidas**, mas com dependências majoritariamente implícitas.

### 1989–1993 — pipeline estrutural por ano
Há materialização NORMALIZED específica e FASE 10 específica para 1989–1993, além da certificação anual global.

Tratamento: **pipeline estrutural funcional, porém ainda sem DAG formal entre materialização → FASE10 → certificação**.

### Global / 2026
Existem workflows M2/M3 relacionados a capacidade, LFS, manifesto, CI, dataset oficial e aprovação global.

Tratamento: **camada de governança/infraestrutura**, não deve ser confundida com uma fase anual 00–12.

## Problema arquitetural identificado

A quantidade de workflows não é, por si só, o problema. O problema é que o repositório contém simultaneamente:

1. workflows de aquisição;
2. workflows de transformação;
3. workflows de auditoria;
4. workflows de certificação;
5. workflows de publicação;
6. workflows históricos específicos;
7. workflows de infraestrutura;

e muitos são acionados diretamente por `push`, sem uma relação formal de precedência.

## DAG alvo

```
00 GOVERNANÇA
      |
01 RAW
      |
02 INTEGRIDADE FONTE
      |
03 PARSING
      |
04 NORMALIZAÇÃO
      |
05 MANIFESTO/HASH
      |
06 RECONCILIAÇÃO
      |
07 IDENTIDADE
      |
08 SEMÂNTICA/CALENDÁRIO
      |
09 PRÉ-RELEASE
      |
10 VALIDAÇÃO INDEPENDENTE
      |
11 CERTIFICAÇÃO
      |
12 FECHAMENTO/PROMOÇÃO
      |
DATASET OFICIAL
```

## Regra de migração

Nenhum workflow histórico deve ser apagado ou renomeado em massa nesta etapa.

Primeiro:

- catalogar;
- classificar;
- definir dependências;
- marcar legado quando apropriado;
- criar o orquestrador canônico;
- executar testes;
- só depois desativar caminhos redundantes.

## Conclusão desta rodada

O inventário confirma que a reorganização deve ser feita **por arquitetura**, e não por simples renomeação de arquivos.

A próxima etapa é construir a **matriz workflow × fase × ano × trigger × saída × dependência**, que será a base do DAG definitivo.
