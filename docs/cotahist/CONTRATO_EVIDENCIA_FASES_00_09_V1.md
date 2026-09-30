# CONTRATO DE EVIDÊNCIA — FASES 00–09 COTAHIST V1

**Data:** 2026-09-30  
**Escopo:** cadeia retrospectiva anual COTAHIST  
**Repositório:** carlos-andrade/B3  
**Status:** VIGENTE

## 1. Regra fundamental

A existência de NORMALIZED, manifesto, FASE10, certificação ou fechamento anual não retrocertifica automaticamente uma fase anterior.

Cada fase obrigatória deve possuir evidência específica ou equivalência retrospectiva explicitamente documentada.

## 2. Cadeia canônica

00 -> 01 -> 02 -> 03 -> 04 -> 05 -> 06 -> 07 -> 08 -> 09 -> 10 -> 11 -> 12

## 3. Contrato mínimo por fase

| Fase | Função | Evidência mínima |
|---|---|---|
| 00 | Governança / pré-condições | identificação do ano, fonte, escopo, ordem, regras e pré-condições |
| 01 | Aquisição / RAW | RAW, origem, SHA-256, integridade ZIP e membro esperado |
| 02 | Integridade da fonte | ZIP/TXT e estrutura da fonte |
| 03 | Parsing | regras e resultado do parsing |
| 04 | Normalização | transformação reproduzível |
| 05 | Manifesto / checksum | fingerprints e manifesto |
| 06 | Reconciliação | RAW x NORMALIZED |
| 07 | Identidade / chaves | chave, cardinalidade, duplicidades e campos |
| 08 | Semântica / calendário | códigos, calendário, OHLC e exceções |
| 09 | Pré-release | consolidação das FASES 00–08 |
| 10 | Validação independente | validação independente |
| 11 | Certificação | promoção formal |
| 12 | Fechamento | fechamento do ano e transição |

## 4. Regra de promoção

A FASE09 somente pode produzir LIBERADO_PARA_FASE10 se:

- FASE00 e FASE01 tiverem evidência válida;
- FASE02 tiver estado VALIDADO ou VALIDADO_COM_EXCECAO;
- FASE03–05 tiverem evidência válida conforme o catálogo aplicável;
- FASE06–08 tiverem estado VALIDADO ou VALIDADO_COM_EXCECAO;
- RAW, NORMALIZED e manifestos estiverem presentes;
- não existir bloqueio não classificado.

## 5. Retrospectiva

Para 1987–1993, quando uma fase não foi originalmente registrada, a classificação correta é inicialmente NAO_COMPROVADO. Uma nova auditoria retrospectiva pode converter o estado somente após executar o teste correspondente e publicar sua evidência.

## 6. Não-circularidade

Não usar a própria FASE09, FASE10, certificação ou fechamento como prova primária das FASES00–08.

## 7. Rastreabilidade

Toda evidência deve registrar, no mínimo:

- ano;
- fase;
- entrada;
- procedimento/versão;
- checks;
- resultado;
- falhas/exceções;
- decisão;
- commit/workflow quando disponível.

## 8. Regra de segurança

Em caso de dúvida entre VALIDADO e NAO_COMPROVADO, prevalece NAO_COMPROVADO.

**Princípio:** melhor bloquear uma promoção do que promover um histórico sem prova suficiente.


## 9. ESCOPO ATUALIZADO — FASES 00–12

Embora o caminho histórico deste arquivo permaneça docs/cotahist/CONTRATO_EVIDENCIA_FASES_00_09_V1.md para preservar referências existentes, o contrato agora cobre formalmente **FASE00 a FASE12**.

A cadeia canônica é:

**00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12**

A partir desta versão, a identificação normativa interna deste documento é **CONTRATO DE EVIDÊNCIA — FASES 00–12 COTAHIST V2.0**.

### 9.1 FASE10 — Validação independente
Deve confirmar a integridade final do RAW e do NORMALIZED, a coerência dos manifests e as condições de release definidas para o período.

### 9.2 FASE11 — Certificação
Deve registrar formalmente o resultado de certificação do período e seu escopo. Certificação não retrocertifica outros períodos.

### 9.3 FASE12 — Fechamento e transição
Deve confirmar a existência das evidências obrigatórias, a passagem dos gates anteriores, a certificação aplicável, a ausência de bloqueios não declarados e a decisão de **fechar ou bloquear** o período. Quando todos os gates forem atendidos, deve registrar a autorização controlada para iniciar o próximo período.

### 9.4 Regra de existência
A docs/cotahist/REGRA_GERAL_EXISTENCIA_E_VALIDACAO_V1.md é a regra regente para existência física, identificabilidade, validação, registro Git e avanço de fase. Este contrato detalha os requisitos específicos da cadeia COTAHIST e não pode reduzi-los.

### 9.5 Não retrocertificação
Nenhuma fase posterior, certificação ou fechamento pode ser usada como prova automática de uma fase anterior quando o contrato exigir evidência específica. Equivalências retrospectivas devem ser explicitamente documentadas e testadas.

## 10. Histórico de versões

| Versão | Data | Alteração | Status |
|---|---|---|---|
| 2.0 | 30/09/2026 | Ampliação formal do contrato de FASES 00–09 para FASES 00–12; inclusão de certificação, fechamento, transição controlada e precedência da regra regente de existência/validação. | VIGENTE |

**Nota de compatibilidade:** o nome físico do arquivo não foi alterado para evitar quebra de referências existentes. O escopo normativo interno foi atualizado para FASES 00–12.
