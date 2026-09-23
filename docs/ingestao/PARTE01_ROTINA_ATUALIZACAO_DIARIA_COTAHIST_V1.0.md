# Atualização Diária Contínua da Base COTAHIST

**Arquivo:** PARTE01_ROTINA_ATUALIZACAO_DIARIA_COTAHIST_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Atualização diária, auditoria e continuidade da base histórica COTAHIST  
**Caminho:** docs/ingestao/PARTE01_ROTINA_ATUALIZACAO_DIARIA_COTAHIST_V1.0.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Manter a base histórica COTAHIST atualizada diariamente a partir da fonte B3, preservando rastreabilidade, integridade e evidência de cada atualização.

A rotina não possui data final. A cada execução ela consulta o arquivo anual correspondente ao ano corrente, valida sua estrutura, calcula SHA-256, gera/atualiza o manifesto e persiste a nova versão no repositório somente quando houver alteração.

## 2. Automação

Workflow:

`.github/workflows/cotahist-atualizacao-diaria.yml`

Agendamento:

- frequência: diária;
- cron: `17 3 * * *` UTC;
- execução adicional: `workflow_dispatch`;
- concorrência: grupo único `cotahist-atualizacao-diaria`;
- `cancel-in-progress: false`.

A execução diária não depende de uma ação manual.

## 3. Fluxo

```
Agendamento diário
      ↓
Identificar ano UTC corrente
      ↓
Consultar COTAHIST anual B3
      ↓
Download com retries
      ↓
Validar ZIP
      ↓
Validar registros de 245 bytes
      ↓
Validar header 00
      ↓
Validar registros 01
      ↓
Validar trailer 99
      ↓
Calcular SHA-256
      ↓
Gerar manifesto
      ↓
Comparar alterações
      ↓
Se alterado → commit + push
Se igual    → registrar execução sem novo commit
```

## 4. Integridade

Nenhum arquivo é considerado atualizado sem:

1. download bem-sucedido;
2. arquivo não vazio;
3. ZIP contendo exatamente um arquivo COTAHIST;
4. registros de 245 bytes;
5. header `00`;
6. pelo menos um registro `01`;
7. trailer `99`;
8. SHA-256 calculado;
9. manifesto com `status: VALIDADO`;
10. persistência no `main`.

## 5. Evidência

A rotina mantém:

- RAW: `dados/cotahist/raw/anual/`;
- checksums: `dados/cotahist/checksums/`;
- manifestos: `dados/cotahist/manifests/`;
- artefato da execução no GitHub Actions por 90 dias.

O RAW não é sobrescrito silenciosamente fora do histórico Git. Alterações geram novos commits, permitindo auditoria pelo histórico do repositório.

## 6. Regra de atualização

A rotina não cria um commit quando o arquivo baixado é idêntico ao conteúdo já versionado.

Quando o arquivo B3 muda, o workflow:

- recalcula o SHA-256;
- atualiza checksum;
- atualiza manifesto;
- registra novo commit.

Isso evita commits diários artificiais quando não houve alteração na fonte.

## 7. Continuidade

A intenção operacional é execução indefinida, sem data de término.

Entretanto, nenhuma infraestrutura externa pode garantir literalmente disponibilidade infinita. GitHub Actions, rede, serviço B3, limites de execução, alterações de endpoint e indisponibilidades externas podem interromper uma execução.

Por isso, a regra de segurança é:

**falha de aquisição nunca deve ser interpretada como ausência de novos dados.**

Uma execução com erro deve permanecer como erro até nova execução bem-sucedida. O sistema não deve marcar uma atualização como válida por inferência.

## 8. Escopo temporal

A base histórica validada atualmente cobre:

**1986 → 2026**

A rotina diária passa a manter atualizado o ano corrente.

Quando um novo ano existir, a arquitetura deverá migrar automaticamente ou por revisão controlada para o novo ano, sem remover os anos anteriores.

## 9. Separação entre histórico e microestrutura

COTAHIST continua sendo fonte de cotações históricas/EOD.

A rotina diária não transforma COTAHIST em:

- agressão;
- fluxo;
- Cumulative Delta;
- livro de ofertas;
- negócios tick a tick;
- VWAP intradiário;
- TWAP;
- microestrutura.

Essas dimensões deverão utilizar fontes específicas quando forem incorporadas ao projeto.

## 10. Controle de versão

Versão inicial da rotina: **V1.0**

Commit de implementação:

`7ed1c1af4a06e6da12843d29f5ca26b7a526bfe8`

Workflow implementado:

`.github/workflows/cotahist-atualizacao-diaria.yml`

## 11. Critério de auditoria

Para cada atualização, deve ser possível responder:

- qual arquivo foi obtido;
- qual era a fonte;
- quando foi obtido;
- qual era seu SHA-256;
- se passou na validação estrutural;
- qual manifesto foi produzido;
- qual commit persistiu a alteração;
- qual versão física está atualmente no repositório.

## 12. Próxima evolução

Após estabilizar a atualização diária, a próxima camada será a normalização dos COTAHIST:

`RAW → VALIDATED RAW → NORMALIZED → INSTRUMENT MASTER → DATA QUALITY → DERIVED`

A camada RAW permanece imutável como evidência primária.
