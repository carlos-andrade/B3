# CARTA DE GARANTIAS DO PROJETO B3

**Versão:** 1.0  
**Data:** 2026-10-01  
**Status:** VIGENTE  
**Repositório:** carlos-andrade/B3

## 1. Finalidade

Esta carta consolida as garantias operacionais que o Projeto B3 assume para preservar integridade, rastreabilidade, continuidade e auditabilidade.

Ela complementa a Carta de Confiança dos Dados e o Modelo-Mestre de Governança.

## 2. Garantia de localização

Todo artefato governado deve possuir caminho determinístico.

Para COTAHIST anual:

- RAW: `dados/cotahist/raw/anual/COTAHIST_A<AAAA>.ZIP`
- manifesto: `dados/cotahist/manifests/COTAHIST_A<AAAA>.json`
- checksum: `dados/cotahist/checksums/COTAHIST_A<AAAA>.ZIP.sha256`
- evidências: `dados/cotahist/quality/`
- certificação: `dados/cotahist/certificacao/`

Uma busca incompleta não será tratada como prova de ausência.

## 3. Garantia de preservação do RAW

O RAW deve ser preservado e não sofrer alteração semântica silenciosa.

Correções devem ocorrer em camadas derivadas e manter vínculo com o original.

## 4. Garantia de checksum e manifesto

Quando aplicável, o RAW deve possuir checksum e manifesto coerentes.

Divergência de checksum bloqueia a promoção até investigação.

## 5. Garantia de execução linear

O COTAHIST anual segue:

**00 → 01 → 02 → 03–05 → 06 → 07 → 08 → GATE → 09 → GATE → 10 → GATE → 11 → GATE → 12 → transição.**

A regra é:

**pré-condição válida → execução → evidência → gate → próxima fase.**

Não haverá promoção por simples existência de arquivo.

## 6. Garantia fail-closed

Se uma fase crítica falhar:

- a fase dependente não deve ser promovida;
- o bloqueio deve aparecer na evidência;
- a execução deve permanecer auditável;
- a correção deve produzir nova execução verificável.

## 7. Garantia contra falso positivo

Nenhum indicador será alterado artificialmente para tornar um gate verde.

O contrato de correção distingue:

- `correction_required`;
- `correction_applied`;
- `correction_contract_valid`.

## 8. Garantia de preservação dos incidentes

Runs com falha relevante não serão apagados da narrativa operacional.

Os incidentes 1994 — Run #59, Run #8 e Run #10 — permanecem documentados como evidência das falhas encontradas e corrigidas.

## 9. Garantia de separação entre dado e pipeline

Falha de workflow não será automaticamente classificada como falha do dado.

A investigação deve determinar se o problema está em:

**fonte → RAW → parsing → normalização → evidência → gate → workflow.**

## 10. Garantia de não retrocertificação

Certificação e fechamento são específicos do período.

Fechamento de 1994 não certifica 1995.

A autorização de transição apenas libera o início da cadeia seguinte.

## 11. Garantia de continuidade

O fato de um período histórico possuir exceção não deve bloquear períodos independentes quando a análise de dependências demonstrar ausência de contaminação.

1986 permanece em trilha histórica própria.

## 12. Estado factual confirmado em 2026-10-01

A matriz anual registrada no repositório contém os anos **1986–2026** e marca RAW presente para todos.

O RAW de 1995 foi confirmado em:

`dados/cotahist/raw/anual/COTAHIST_A1995.ZIP`

Manifesto e checksum de 1995 registram SHA-256:

`de553f41a3ce15ec8a082ed1c2d451df58520a447d3f39417f45e7feb5a995fc`.

Portanto, 1995 não deve ser tratado como aquisição ausente.

## 13. Estado de 1994

A cadeia linear 1994 FASE06→FASE12 foi concluída com sucesso no Run #13, após correção dos gates.

Estado final registrado:

- FASE06: VALIDADO;
- FASE07: VALIDADO;
- FASE08: VALIDADO_COM_EXCECAO;
- FASE09: LIBERADO_PARA_FASE10;
- FASE10: VALIDADO;
- FASE11: VALIDADO/CERTIFICADO;
- FASE12: CONCLUIDA;
- transição para 1995: autorizada.

## 14. Garantia de memória operacional

Toda decisão relevante deve deixar:

- arquivo;
- versão;
- commit;
- evidência;
- workflow/run quando aplicável;
- estado;
- impacto;
- próximo passo.

O Git é parte da memória oficial do projeto.

## 15. Garantia final

> **O projeto pode avançar com incerteza controlada, mas não pode converter ausência de evidência em certeza.**

## 16. Histórico

| Versão | Data | Alteração | Status |
|---|---|---|---|
| 1.0 | 01/10/2026 | Criação da carta consolidando localização, preservação, execução linear, fail-closed, incidentes, não retrocertificação e estado confirmado da série COTAHIST. | VIGENTE |
