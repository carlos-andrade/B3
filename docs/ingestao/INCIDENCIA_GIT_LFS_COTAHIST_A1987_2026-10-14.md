# Incidência — armazenamento Git LFS do COTAHIST A1987

**Data:** 2026-10-14  
**Repositório:** https://github.com/carlos-andrade/B3  
**Estado:** identificada; não bloqueia a geração do Dataset Oficial V2; correção de armazenamento pendente de plano controlado.

## Resumo

A execução do workflow [COTAHIST — Dataset Oficial V2, run 38577163285](https://github.com/carlos-andrade/B3/actions/runs/38577163285) terminou com sucesso. O workflow materializou seletivamente os CSV anuais, validou 41 anos contra a auditoria física global e publicou o dataset V2. Durante o checkout Git LFS foi emitido o aviso:

`Encountered 1 file that should have been a pointer, but wasn't: dados/cotahist/normalized/anual/COTAHIST_A1987.csv`

## Evidência verificável

A regra em `.gitattributes` é:

```gitattributes
dados/cotahist/normalized/anual/*.csv filter=lfs diff=lfs merge=lfs -text
```

A árvore Git de `main` mostrou:

| Ficheiro | Tamanho do blob Git | Observação |
|---|---:|---|
| `COTAHIST_A1986.csv` | 133 bytes | ponteiro LFS |
| `COTAHIST_A1987.csv` | 15.518.211 bytes | conteúdo CSV guardado diretamente como blob Git |
| `COTAHIST_A2026.csv` | 134 bytes | ponteiro LFS |

O conteúdo do CSV A1987 está acessível no repositório; a inconsistência é entre a regra declarada e a forma de armazenamento do blob. Não há evidência nesta incidência de divergência do SHA-256 de conteúdo: a auditoria física global está aprovada para 41/41 anos e o Dataset Oficial V2 contém A1987 como `VALIDADO`.

## Impacto

- **Dados:** nenhuma alteração feita nesta investigação.
- **Integridade:** sem bloqueio observado; a auditoria física e o gerador V2 passaram.
- **Armazenamento:** exceção ao padrão Git LFS para CSV anuais.
- **Operação:** aviso não bloqueante no checkout, deve ser eliminado por uma correção controlada.

## Plano de resolução

1. Não reescrever nem deduplicar o CSV.
2. Antes de qualquer migração, registar o SHA-256 atual do conteúdo, tamanho, contagem de linhas, 25 campos e intervalo de datas.
3. Converter apenas a representação de armazenamento do A1987 para LFS numa alteração isolada, sem alterar os bytes do conteúdo.
4. Confirmar que o ponteiro LFS foi criado e que o objeto LFS está disponível após push e novo checkout.
5. Recalcular o SHA-256 do conteúdo materializado e comparar com a auditoria física e manifesto; validar contagem, campos e datas.
6. Executar novamente a auditoria física global e o Dataset Oficial V2.
7. Fechar a incidência apenas quando o aviso desaparecer e todos os hashes/contagens continuarem coerentes.

## Restrições

- Não alterar RAW nem conteúdo NORMALIZED.
- Não regenerar manifestos para fazer coincidir hashes incorretos.
- Não marcar como corrigido apenas porque o workflow passa.
- Manter a geração fail-closed e preservar a evidência histórica.
