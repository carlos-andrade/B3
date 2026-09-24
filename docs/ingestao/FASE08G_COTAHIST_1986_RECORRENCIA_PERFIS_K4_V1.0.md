# FASE 08G — Recorrência Histórica de Perfis Estatísticos sob K4 Idêntica

**Arquivo:** FASE08G_COTAHIST_1986_RECORRENCIA_PERFIS_K4_V1.0.md
**Projeto:** B3 - A BOLSA DO BRASIL
**Tema:** teste de recorrência da colisão K4 e de perfis estatísticos
**Data:** 24/09/2026
**Repositório:** carlos-andrade/B3

## 1. Objetivo
Testar se a coexistência de duas linhas com K4 idêntica em 10/10/1986 é recorrente no arquivo ou se constitui ocorrência isolada, separando recorrência de K4 de recorrência de perfil estatístico.

## 2. Método
Foram executados três testes:
1. repetição exata da K4;
2. repetição de perfil estatístico normalizado por FATCOT, incluindo TOTNEG, preços ajustados e VOLTOT/QUATOT;
3. comparação de registros do mesmo dia, mercado, CODNEG e TPMERC.

Nenhuma recorrência de perfil é tratada como prova de mesma origem econômica.

## 3. Escopo
Arquivo RAW: COTAHIST_A1986.ZIP.
Registros tipo 01: 177.981.

## 4. Critério
**FATO:** repetição literal dos campos da K4.
**DERIVADO:** perfil estatístico calculado.
**PADRÃO:** recorrência observada no conjunto.
**HIPÓTESE:** interpretação ainda não documentalmente comprovada.

## 5. Resultado
O JSON publicado pelo workflow contém:
- contagem de grupos K4 duplicados;
- linhas e perfis de cada grupo;
- recorrência exata dos perfis estatísticos;
- correspondências relaxadas das linhas 140808 e 140809;
- registros do mesmo contexto diário;
- SHA-256 do RAW.

## 6. Regra de interpretação
Se K4 duplicada ocorrer somente uma vez, isso caracteriza a colisão de 10/10/1986 como **isolada dentro do COTAHIST 1986**. Se perfis estatísticos semelhantes ocorrerem muitas vezes, isso demonstra apenas que os números estatísticos não são identificadores únicos.

Uma recorrência de perfil semelhante não autoriza consolidar, excluir ou reclassificar registros.

## 7. Governança
- RAW intocado;
- nenhum registro removido;
- nenhuma consolidação;
- nenhuma correção dos valores originais;
- nenhuma identidade econômica inferida.

## 8. Status inicial
IMPLEMENTADO: aguardando execução.
EXECUTADO: aguardando JSON.
VALIDADO: aguardando conferência.

## 9. Próxima frente
Após a validação, decidir se a investigação precisa ampliar o escopo para múltiplos anos COTAHIST ou se a evidência disponível em 1986 já é suficiente para manter a anomalia como caso histórico isolado.
