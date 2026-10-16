# Recuperação offline controlada — COTAHIST 2006

**Estado:** proposta em branch; validação operacional deve ocorrer nesta branch antes da integração.  
**Origem de dados:** exclusivamente `dados/cotahist/raw/anual/COTAHIST_A2006.ZIP`, já versionado.  
**Proibido nesta cadeia:** descarregar uma cópia nova da fonte externa, substituir RAW, corrigir manifestos silenciosamente ou declarar o CSV validado sem prova física.

## Motivo

A árvore `main` contém:
- RAW ZIP de 2006 e checksum/manifesto de origem;
- evidência FASE00 com `AUTORIZAR_FASE01`;
- manifesto normalizado `COTAHIST_A2006_quality.json` que declara 198.367 linhas, 25 campos e SHA-256 `d9025ebcc01413111c67a0bb573f4ff2676aae2105e8204f19d13f9a313ee69d`;
- sidecar `COTAHIST_A2006.csv.sha256` com o mesmo hash declarado;
- **ausência** do CSV canónico `dados/cotahist/normalized/anual/COTAHIST_A2006.csv`.

A presença do manifesto não substitui o conteúdo normalizado.

## Cadeia proposta

| Fase | Workflow | Gate principal |
|---|---|---|
| 01 | `cotahist-fase01-aquisicao-2006-v1.yml` | Verificar RAW armazenado, proveniência e SHA-256; não adquirir externamente |
| 02 | `cotahist-fase02-integridade-2006-v1.yml` | Confirmar hash, checksum e estrutura ZIP |
| 03 | `cotahist-fase03-parsing-2006-v1.yml` | Verificar membros ZIP, tipos de registo e comprimento de 245 bytes |
| 04A | `cotahist-fase04-recuperar-normalized-2006-v1.yml` | Regenerar CSV a partir do RAW sem alterar manifest/sidecar |
| 04B | `cotahist-fase04-validacao-independente-2006-v1.yml` | Verificar CSV regenerado, hash/contagem/datas e liberar a FASE05 |
| 05–09 | workflows de manifesto, reconciliação, identidade, calendário e pré-release | Executar gates já definidos nos templates de 2005, adaptados para 2006 |
| 10 | `cotahist-fase10-validacao-independente-2006-v1.yml` | Checkout LFS efetivo, hash físico e comparação independente dos 25 campos |
| 11 | `cotahist-fase11-certificacao-2006-v1.yml` | Certificar apenas depois da FASE10 aprovada |

As fases são sequenciadas pela evidência da fase anterior, evitando execuções paralelas prematuras. Para cumprir o fluxo feature → validação → principal, os gatilhos `push` e os commits de evidência ficam limitados à branch `feat/cotahist-2006-offline-recovery`; nenhum workflow desta cadeia deve escrever diretamente em `main`. Todas mantêm `workflow_dispatch` para intervenção manual auditável.

## Critérios de aceitação

1. RAW imutável; hash calculado igual ao manifesto de origem e checksum.
2. CSV gerado pelo parser versionado; hash calculado igual ao manifesto normalizado e sidecar existente.
3. 198.367 linhas e 25 campos apenas se confirmados pela execução; datas e tipos de registo reconciliados.
4. FASE10 deve descarregar o objeto LFS efetivo, recalcular SHA-256 e comparar o conteúdo, não apenas o ponteiro.
5. Em qualquer divergência, falhar fechado; não reescrever manifestos para fazer o teste passar.
6. Mesmo após certificação estrutural, não inferir que COTAHIST prova cobertura de futuros ou abertura de INDFUT/DOFUT/IND/DOL/WIN/WDO.

## Limites

Esta proposta não é evidência de execução. A cadeia deve ser executada e validada na branch de feature antes da revisão/integração em `main`; a integração só deve ocorrer após revisão do diff e evidências CI. A validação BRICKMASTER dos seis símbolos continua `UNKNOWN/BLOCKED` até que exista uma fonte que prove o contrato e o campo de abertura aplicável.
