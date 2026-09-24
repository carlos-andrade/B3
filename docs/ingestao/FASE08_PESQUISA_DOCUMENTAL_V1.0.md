# FASE 08 — Pesquisa Documental Histórica — COTAHIST 1986

**Arquivo:** FASE08_PESQUISA_DOCUMENTAL_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Pesquisa documental da colisão K4 de 10/10/1986  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Investigar fontes contemporâneas capazes de explicar:

1. a convenção histórica VGO 2;
2. o código C05 em ESPECI = PP *C05;
3. DATVEN = 99991231;
4. a coexistência de duas linhas com K4 idêntica e agregados de negociação diferentes;
5. a semântica histórica do mercado a termo no registro-alvo.

## 2. Registro-alvo

19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0

Linhas RAW: 140808 e 140809.

## 3. Evidência documental localizada

### 3.1 Jornal do Brasil — 05/06/1986

Foi localizada uma publicação contemporânea de 05/06/1986 contendo tabela de cotações da Bovespa. A tabela registra Vigor PP C05 e apresenta outras ocorrências do padrão Cxx, como Weg PP C35, Metal Duque PP C45 e Brahma OP C15. citeturn1search0

A evidência demonstra que:

- a identificação Vigor PP C05 existia publicamente antes do registro-alvo de outubro de 1986;
- a notação Cxx era usada para múltiplos papéis;
- portanto, PP *C05 no COTAHIST é compatível com uma convenção histórica de publicação de mercado.

A fonte não apresenta legenda suficiente para decodificar o número 05.

### 3.2 Evidência complementar sobre a persistência da convenção Cxx

Fonte de imprensa posterior preserva exemplos de papéis publicados com códigos Cxx, incluindo C05, C07, C15, C34, C35 e outros. Isso é apenas evidência corroborativa da existência da convenção; não deve ser usada para reconstruir retroativamente a semântica de C05 em 1986. citeturn1search41

## 4. O que a pesquisa NÃO resolveu

Não foi localizada, na busca pública realizada em 24/09/2026:

- cópia primária do Boletim Diário de Informações da Bovespa de 10/10/1986;
- legenda oficial contemporânea para C05;
- documento contemporâneo que associe VGO 2 a uma descrição cadastral completa;
- regra documental explicando duas linhas com K4 idêntica e agregados diferentes;
- fonte primária que estabeleça o significado de DATVEN = 99991231.

## 5. Semântica atualmente sustentada

| Elemento | Estado |
|---|---|
| CODBDI 62 | Mercado a termo — documentado pelo layout B3 |
| TPMERC 030 | Termo — documentado pelo layout B3 |
| PRAZOT 060 | Campo de prazo do termo; valor 60 — documentado |
| VGO 2 | Código histórico observado; sem decodificação completa |
| VGORACPP | Código interno histórico observado |
| DIMES 104 | Campo de distribuição/estado de direito; sem reconstrução histórica completa |
| PP C05 | Convenção histórica comprovada; significado do C05 não resolvido |
| DATVEN 99991231 | Placeholder aparente; sem definição histórica comprovada |
| duplicidade K4 | fato RAW comprovado; causa não determinada |

## 6. Regra de evidência

Não será feita nenhuma transformação de C05, VGO 2 ou DATVEN com base apenas em analogia moderna.

A colisão permanecerá preservada no RAW e será tratada como evento histórico observável até existir documentação primária suficiente.

## 7. Próxima frente

Prioridade máxima:

1. localizar Boletim Diário de Informações Bovespa de 10/10/1986;
2. localizar boletins dos dias úteis próximos, para acompanhar Vigor PP C05;
3. localizar regulamento/manual histórico do Mercado a Termo de 1986;
4. procurar documentos cadastrais/societários contemporâneos da Vigor;
5. comparar outros COTAHIST de 1986 com a mesma estrutura para verificar se duplicidades K4 ocorrem em outros papéis.

## 8. Status

**IMPLEMENTADO:** pesquisa documental executada.

**EXECUTADO:** fonte contemporânea com Vigor PP C05 localizada.

**VALIDADO:** existência histórica da notação Vigor PP C05; não validada a semântica do número 05.

**FASE 08:** ABERTA — investigação semântica continua.

## 9. Fontes

- Jornal do Brasil, 05/06/1986 — tabela de cotações Bovespa. citeturn1search0
- Evidência complementar em acervo de imprensa histórica. citeturn1search41
