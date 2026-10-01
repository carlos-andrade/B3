# COTAHIST — CONTRATO DO GATE 06–08 — PROMOÇÃO TÉCNICA

**Versão:** 1.0.0  
**Data:** 2026-10-01  
**Status:** VIGENTE  
**Aplicação:** ciclos COTAHIST que utilizem FASE06, FASE07 e FASE08  
**Repositório:** carlos-andrade/B3

## 1. Finalidade

O GATE 06–08 é uma barreira formal entre as fases técnicas e a FASE09 — PRÉ-RELEASE.

Ele **não executa análise técnica, não corrige fases e não substitui evidências**. Sua única responsabilidade é decidir, de forma determinística e fail-closed, se o conjunto FASE06 + FASE07 + FASE08 satisfaz os contratos de promoção para a FASE09.

Fluxo:

**FASE06 → FASE07 → FASE08 → GATE 06–08 → FASE09**

## 2. Entradas autorizadas

O Gate somente pode consumir:

1. evidência persistida da FASE06;
2. evidência persistida da FASE07;
3. evidência persistida da FASE08;
4. identificação do ano/ciclo;
5. referência do commit que materializou cada evidência;
6. estado de execução dos workflows das três fases, quando disponível;
7. contratos normativos vigentes no repositório.

O Gate não pode usar README como fonte operacional de decisão.

## 3. Evidências obrigatórias

Para cada ano, o Gate deve localizar explicitamente as evidências correspondentes às três fases. Os nomes concretos podem variar por versão/ano, mas cada evidência deve ser identificável por contrato e não por inferência.

Referências canônicas previstas:

- 'dados/cotahist/quality/COTAHIST_<AAAA>_FASE06_SEMANTICA_V1.json'
- 'dados/cotahist/quality/COTAHIST_<AAAA>_FASE07_IDENTIDADE_CHAVES_V1.json'
- 'dados/cotahist/quality/COTAHIST_<AAAA>_FASE08_SEMANTICA_CALENDARIO_V1.json'

Quando um ciclo histórico possuir nomenclatura legada, o mapeamento deve ser registrado explicitamente em evidência ou contrato; o Gate não deve adivinhar equivalência.

## 4. Estados permitidos

### 4.1 Estados que permitem promoção

- 'VALIDADO'
- 'VALIDADO_COM_EXCECAO', desde que a exceção seja formalmente registrada e classificada como não bloqueadora.

### 4.2 Estados que bloqueiam

- 'AUSENTE'
- 'BLOQUEADO'
- 'FALHOU'
- 'INVALIDO'
- estado desconhecido ou não previsto no contrato.

'AGUARDANDO_RECONCILIACAO' e estados equivalentes de incerteza não são promoção automática; devem ser classificados como bloqueio até que exista decisão normativa explícita.

## 5. Contrato mínimo de cada evidência

Cada evidência consumida pelo Gate deve permitir verificar, no mínimo:

- 'year'/ano do ciclo;
- identificação da fase;
- 'status';
- 'decision' ou equivalente de promoção;
- timestamp de geração/validação;
- commit ou referência rastreável da versão que a produziu, quando o contrato da fase o exigir;
- indicação de correção/incidente quando aplicável;
- resultado dos testes necessários àquela fase;
- exceções e sua classificação, quando existirem.

A ausência de campo necessário para provar o contrato da própria fase é bloqueadora.

## 6. Verificação das três fases

O Gate deve avaliar separadamente:

### FASE06

- evidência presente;
- status permitido;
- responsabilidade limitada a semântica/invariantes;
- duplicidades de chave candidata podem estar registradas como diagnóstico;
- 'logical_key_uniqueness_assessment=DEFERRED_TO_FASE07' é aceitável na FASE06;
- não exigir unicidade de chave na FASE06.

### FASE07

- evidência presente;
- status permitido;
- contrato de identidade/chave/cardinalidade efetivamente decidido;
- colisões classificadas;
- hipótese de chave testada contra evidência histórica;
- decisão normativa registrada;
- limitações/exceções registradas.

### FASE08

- evidência presente;
- status permitido;
- calendário/consistência histórica avaliados;
- exceções classificadas;
- inconsistências bloqueadoras resolvidas ou formalmente classificadas como exceções não bloqueadoras.

## 7. Classificação de bloqueadores

É bloqueador qualquer condição que impeça provar uma das três fases ou que contradiga seu contrato.

São exemplos de bloqueadores:

- evidência ausente;
- status não permitido;
- evidência de outro ano/ciclo;
- decisão de promoção incompatível;
- campo contratual obrigatório ausente;
- exceção sem classificação;
- evidência marcada como inválida;
- fase ainda em execução quando sua evidência final é necessária;
- conflito entre evidência e contrato normativo vigente;
- tentativa de promover FASE09 sem FASE06–08 válidas.

Não são bloqueadores, por si só:

- duplicidades de chave candidata já quantificadas pela FASE06 e transferidas à FASE07;
- 'correction_applied=false' quando 'correction_required=false' e o contrato de correção é válido;
- exceção explicitamente classificada como controlada e não bloqueadora;
- existência de documentação adicional que não altere a evidência normativa.

## 8. Prova de isolamento das fases

O Gate deve confirmar que:

1. FASE06 não executou decisão normativa de FASE07;
2. FASE07 não reescreveu a evidência da FASE06;
3. FASE08 não redefiniu a identidade da FASE07;
4. FASE09 não foi executada como parte da responsabilidade do Gate;
5. nenhuma correção cruzada foi usada para mascarar erro de fase anterior.

Quando não for possível provar o isolamento, o resultado deve ser 'BLOQUEADO_PARA_FASE09'.

## 9. Regra fail-closed

O Gate somente pode liberar quando **todas** as condições obrigatórias forem verdadeiras.

Formalmente:

'LIBERADO_PARA_FASE09 = E06_OK AND E07_OK AND E08_OK AND ISOLAMENTO_OK AND SEM_BLOQUEADORES'

Qualquer condição falsa, ausente ou indeterminada produz:

'BLOQUEADO_PARA_FASE09'

Não existe promoção por inferência, por coexistência de arquivos, por sucesso de workflow isolado ou por evidência de fase posterior.

## 10. Saída normativa

O Gate deve produzir uma evidência própria, por exemplo:

'dados/cotahist/quality/COTAHIST_<AAAA>_GATE_06_08_PROMOCAO_TECNICA_V1.json'

Schema mínimo:

- 'year'
- 'gate': 'GATE_06_08'
- 'status': 'LIBERADO' ou 'BLOQUEADO'
- 'decision': 'LIBERADO_PARA_FASE09' ou 'BLOQUEADO_PARA_FASE09'
- 'phase06_status'
- 'phase07_status'
- 'phase08_status'
- 'phase06_evidence'
- 'phase07_evidence'
- 'phase08_evidence'
- 'isolation_check'
- 'blockers[]'
- 'non_blocking_exceptions[]'
- 'validated_at'
- 'source_commits[]'
- 'contract_version'

## 11. Regras de correção

O Gate nunca corrige a FASE06, FASE07 ou FASE08.

Se houver problema:

**bloqueio → registro do incidente → correção na fase de origem → nova evidência da fase de origem → novo Gate.**

A correção não pode ser aplicada dentro do Gate para obter aprovação.

## 12. Reexecução

Um Gate já concluído não deve ser reexecutado por:

- alteração de README;
- documentação sem impacto no contrato;
- conclusão de fase posterior;
- reorganização visual de arquivos.

Uma nova execução é justificada por alteração real em uma entrada autorizada, mudança normativa que afete o contrato, correção de uma das fases 06–08 ou execução manual de auditoria controlada.

## 13. Relação com FASE09

A FASE09 somente pode consumir uma decisão 'LIBERADO_PARA_FASE09' emitida por este Gate ou por mecanismo histórico formalmente equivalente e documentado.

A FASE09 não pode substituir o Gate executando novamente as análises técnicas das FASE06–08.

## 14. Auditoria

O resultado do Gate deve ser reproduzível a partir das evidências referenciadas e deve permitir identificar:

**entradas → contratos avaliados → verificações → bloqueadores/exceções → decisão → commit.**

## 15. Estado do contrato

Este contrato passa a ser a referência normativa específica do GATE 06–08 para novas execuções COTAHIST.
