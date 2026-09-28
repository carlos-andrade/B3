# M3-1 — Decisão de armazenamento do NORMALIZED anual COTAHIST V1.0

**Arquivo:** M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** DECISÃO TÉCNICA — GIT LFS A VALIDAR/IMPLANTAR

## 1. Contexto

O Gate M3-0 de capacidade foi executado para o COTAHIST 2026.

Resultado físico:

- NORMALIZED: **392.044.266 bytes (~392,04 MB)**
- limite operacional adotado pelo gate: **100.000.000 bytes**
- SHA-256 NORMALIZED: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- registros tipo 01: **2.919.760**
- campos: **25**
- primeira data: **2026-01-02**
- última data: **2026-09-23**
- decisão M3-0: **GIT_STANDARD_LIMIT**

O gate falhou deliberadamente para impedir persistência inadequada. A falha não representa erro do parser.

## 2. Evidência de infraestrutura

O GitHub bloqueia arquivos superiores a **100 MiB** em Git normal. Para arquivos acima desse limite, a documentação oficial orienta Git LFS. O GitHub também recomenda considerar Git LFS para arquivos grandes ou armazenamento externo para arquivos gerados programaticamente.

Fonte: documentação oficial do GitHub.

## 3. Alternativas avaliadas

| Alternativa | Integridade | Reprodutibilidade | Acesso direto | Automação CI | Adequação ao contrato atual |
|---|---|---|---|---|---|
| Git normal | Falha para 392 MB | Alta | Alta | Alta | **Não atende** |
| Git LFS | Alta | Alta | Alta após checkout/LFS | Alta, com configuração | **Atende com alteração controlada** |
| Release asset | Alta | Alta | Média | Média | Exige mudança do contrato de persistência |
| Object storage externo | Alta, se versionado | Alta | Alta por API | Alta | Exige infraestrutura externa e novo contrato |

## 4. Decisão arquitetural

Para o M3, a solução candidata principal é **Git LFS**, porque preserva a semântica de arquivo versionado associado ao repositório, mantém o caminho lógico canônico e permite que o NORMALIZED continue sendo um objeto físico verificável por SHA-256.

A adoção definitiva depende de validação operacional do ambiente GitHub da conta/repositório, incluindo:

1. disponibilidade de Git LFS;
2. quota de armazenamento;
3. quota de bandwidth;
4. capacidade de CI para checkout de objetos LFS;
5. comportamento do Dataset Oficial;
6. comportamento dos validadores e certificadores;
7. política de arquivos futuros;
8. custo operacional.

## 5. Por que não usar Git normal

O NORMALIZED 2026 possui aproximadamente **392 MB**, portanto não deve ser persistido como blob Git convencional.

Também fica proibido tentar contornar o limite por:

- divisão arbitrária;
- compressão como substituto do objeto canônico;
- redução de campos;
- deduplicação econômica;
- alteração do RAW.

## 6. Regra de integridade

O objeto LFS será tratado como o mesmo NORMALIZED lógico definido pelo contrato.

A cadeia continuará sendo:

`RAW → NORMALIZE → SHA → VALIDATE → PERSIST → CERTIFY → RECONCILE`

O SHA-256 do conteúdo materializado deverá continuar registrado no manifest.

O ponteiro LFS não substitui a certificação do conteúdo físico.

## 7. Alteração necessária no contrato V2.0

O contrato atual determina persistência no repositório, mas não especifica o mecanismo físico.

A interpretação operacional proposta é:

> **Persistência no repositório = objeto versionado pelo repositório, podendo utilizar Git LFS quando o tamanho exceder o limite do Git convencional.**

A localização lógica permanece:

`dados/cotahist/normalized/anual/COTAHIST_A{ANO}.csv`

A política física será documentada em nova versão do contrato antes da migração em massa.

## 8. Plano M3-1

### M3-1A — Preparação

- criar regras de tracking LFS;
- não migrar ainda todos os anos;
- manter RAW intacto;
- manter M3 bloqueado para lote.

### M3-1B — Prova 2026

- gerar NORMALIZED 2026 novamente;
- validar 25 campos;
- validar datas;
- calcular SHA-256;
- persistir 2026 via LFS;
- materializar o arquivo;
- recalcular SHA-256;
- comparar com `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`.

### M3-1C — CI

Executar workflow que:

- obtém RAW;
- reconstrói NORMALIZED;
- valida SHA;
- confirma existência física;
- confirma que o arquivo não é apenas ponteiro;
- executa certificação V2;
- falha fechado em qualquer divergência.

### M3-1D — Dataset Oficial

Somente após M3-1C:

- validar o Dataset Oficial;
- confirmar que o consumidor consegue acessar o CSV;
- confirmar que ausência do objeto bloqueia publicação.

### M3-1E — Aprovação

Somente após a prova 2026 passar integralmente:

**M3-1 = APROVADO**

e M3 histórico poderá prosseguir em lotes.

## 9. Limites e governança

A documentação oficial atual do GitHub informa que Git LFS possui limites de tamanho por arquivo superiores ao necessário para os 392 MB observados, mas armazenamento e bandwidth dependem do plano e do uso.

Portanto, **não se deve declarar que toda a série 1986–2026 cabe na quota disponível antes de medir o tamanho agregado**.

O próximo gate deve calcular:

`SUM(size NORMALIZED anual)`

para todos os anos que serão persistidos.

## 10. Critério de aprovação

M3-1 só será aprovado quando todos forem verdadeiros:

- Git LFS disponível;
- quota suficiente ou política de orçamento definida;
- 2026 persistido;
- SHA materializado reproduzível;
- certificação V2 aprovada;
- Dataset Oficial validado;
- CI validado;
- documentação atualizada;
- nenhum RAW alterado.

## 11. Estado atual

**M3-0:** CONCLUÍDO — `GIT_STANDARD_LIMIT`  
**M3-1:** EM DECISÃO/PROVA — Git LFS  
**M3 histórico:** BLOQUEADO  
**RAW:** PRESERVADO  
**Parser:** 1.1.0  
**NORMALIZED 2026:** NÃO PERSISTIDO NO GIT STANDARD

## 12. Regra fail-closed

Enquanto M3-1 não for aprovado:

> **NENHUM ANO ADICIONAL DEVE SER PERSISTIDO COMO NORMALIZED ANUAL.**

Nenhum workflow pode interpretar o estado M3-1 como autorização para iniciar a migração histórica.

## 13. Fontes técnicas

- GitHub — Repository limits.
- GitHub — Adding a file to a repository.
- GitHub — About Git Large File Storage.
- GitHub — Git LFS billing.

Estas fontes foram consultadas em 2026-09-28 e devem ser revalidadas antes da implantação definitiva, pois limites e políticas comerciais podem mudar.
