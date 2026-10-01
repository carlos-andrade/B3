# CARTA MAGNA DE GOVERNANÇA — B3

**Versão:** 1.1  
**Data:** 2026-10-01  
**Status:** VIGENTE  
**Repositório:** carlos-andrade/B3

## 1. Autoridade

Esta Carta Magna adapta o Modelo-Mestre de Governança ao Projeto B3 — A BOLSA DO BRASIL.

Ela rege as decisões de ingestão, armazenamento, validação, certificação, publicação, automação e auditoria dos dados governados pelo projeto.

## 2. Hierarquia

Em caso de conflito, aplica-se:

1. esta Carta Magna;
2. Carta de Confiança dos Dados;
3. normas técnicas específicas;
4. contratos de pipeline;
5. procedimentos operacionais;
6. implementação.

Alterações desta Carta devem ser versionadas e preservar o histórico anterior.

## 3. Princípios

São obrigatórios:

- evidência;
- proveniência;
- rastreabilidade;
- reprodutibilidade;
- integridade;
- transparência;
- separação entre fato, transformação, inferência e hipótese;
- versionamento;
- automação governada;
- fail-closed;
- não retrocertificação;
- não contaminação;
- preservação das falhas relevantes;
- não invenção.

## 4. COTAHIST como cadeia governada

O ciclo anual canônico é:

**FONTE → RAW → INTEGRIDADE → PARSING → NORMALIZAÇÃO → MANIFESTO/CHECKSUM → RECONCILIAÇÃO → IDENTIDADE → SEMÂNTICA/CALENDÁRIO → PRÉ-RELEASE → VALIDAÇÃO INDEPENDENTE → CERTIFICAÇÃO → FECHAMENTO → TRANSIÇÃO.**

## 5. Execução linear

A sequência de fases é obrigatória:

**00 → 01 → 02 → 03–05 → 06 → 07 → 08 → GATE → 09 → GATE → 10 → GATE → 11 → GATE → 12 → próximo ano.**

A próxima fase somente é autorizada depois da evidência da fase anterior e do respectivo gate.

## 6. Existência versus validação

O projeto distingue:

- **EXISTE:** localizado no repositório;
- **ÍNTEGRO:** checksum/estrutura confirmados;
- **VALIDADO:** critérios técnicos atendidos;
- **CERTIFICADO:** certificação formal concluída;
- **FECHADO:** ciclo encerrado;
- **TRANSIÇÃO AUTORIZADA:** próximo ciclo liberado.

Nenhum estado deve ser inferido automaticamente de outro.

## 7. Caminho canônico

Para COTAHIST anual:

`dados/cotahist/raw/anual/COTAHIST_A<AAAA>.ZIP`

`dados/cotahist/manifests/COTAHIST_A<AAAA>.json`

`dados/cotahist/checksums/COTAHIST_A<AAAA>.ZIP.sha256`

`dados/cotahist/quality/`

`dados/cotahist/certificacao/`

Uma busca ampla que falhe não autoriza declarar ausência. O caminho canônico deve ser verificado primeiro.

## 8. Incidentes

Incidentes devem ser classificados por camada.

Uma falha do workflow não equivale automaticamente a falha do RAW.

Os incidentes de 1994 demonstraram três classes relevantes:

- erro de implementação do workflow;
- erro lógico de gate;
- correção e reexecução verificável.

Esses eventos permanecem no histórico.

## 9. Contrato de correção

`correction_required` e `correction_applied` não podem ser usados artificialmente para satisfazer um gate.

O estado do contrato é representado por `correction_contract_valid`.

## 10. Fechamento anual

Um ano não é fechado por existência de arquivos.

É fechado quando:

- fases obrigatórias foram executadas;
- gates foram satisfeitos;
- certificação aplicável foi registrada;
- exceções foram classificadas;
- FASE12 foi concluída;
- a transição foi explicitamente autorizada.

## 11. Não retrocertificação

A certificação de um ano não certifica outro.

A transição autoriza o início do próximo ciclo; não substitui suas próprias validações.

## 12. Estado de referência em 2026-10-01

A matriz de certificação registrada cobre 1986–2026 e indica RAW presente em todos esses anos.

1994 está fechado após a cadeia linear FASE06→FASE12 ter sido validada no Run #13.

1995 possui RAW, manifesto e checksum no caminho canônico e está autorizado a iniciar sua própria cadeia.

1986 continua tratado como exceção histórica controlada e não deve contaminar períodos posteriores.

## 13. Governança das mudanças

Toda alteração normativa relevante deve registrar:

- versão;
- data;
- motivo;
- impacto;
- artefatos afetados;
- commit;
- novo critério de validação quando aplicável.

## 14. Regra suprema

> **A velocidade do projeto nunca prevalece sobre a evidência.**

O projeto pode continuar avançando em trilhas independentes, mas somente dentro de limites que preservem integridade, rastreabilidade e não contaminação.

## 15. Histórico

| Versão | Data | Alteração | Status |
|---|---|---|---|
| 1.0 | 01/10/2026 | Criação da Carta Magna específica do Projeto B3, consolidando governança, localização canônica, execução linear, estados de confiança, incidentes e fechamento anual. | VIGENTE |


## ADITIVO DE GOVERNANÇA — 2026-10-01 — FASE06/1995

### Regra permanente de reconciliação de chaves

A experiência da FASE06/1995 demonstrou que uma chave candidata não pode ser promovida automaticamente a chave lógica única apenas por conveniência de implementação.

A partir deste aditivo:

1. **Existência de duplicidade de chave candidata não é, isoladamente, corrupção do dado.**
2. A FASE06 deve registrar duplicidades como **observação diagnóstica**, sem reprovar o dataset exclusivamente por esse motivo.
3. A definição e o teste de unicidade da chave lógica pertencem ao contrato de **identidade/chaves da FASE07**, onde devem ser reconciliados com o layout oficial, o período histórico e os campos efetivamente disponíveis.
4. Uma chave somente pode ser declarada **canônica/única** quando houver evidência documental e empírica suficiente.
5. O validador não pode transformar uma hipótese de chave em regra de rejeição.
6. Duplicidades observadas devem permanecer quantificadas e auditáveis na evidência.
7. Se uma regra nova de validação contradizer dados históricos já certificados, a regra deve entrar em **reconciliação** antes de bloquear o ciclo.
8. Uma certificação anterior não substitui a investigação atual, mas também não pode ser ignorada sem análise de compatibilidade.

### Regra anti-regressão

Nenhum novo validador COTAHIST poderá introduzir uma condição de bloqueio baseada em:
- chave candidata não documentada;
- cardinalidade presumida;
- unicidade presumida;
- interpretação semântica não reconciliada;

sem antes possuir:
**fonte/layout → hipótese → amostra → teste histórico → decisão normativa → implementação → evidência.**

A FASE06/1995 passa a ser referência de incidente para impedir a repetição desse padrão.

### Incidente de referência

A execução comprovada da FASE06/1995 no workflow **Run 36859032714** identificou duplicidades na chave candidata data+codbdi+codneg+tpmerc. O incidente foi classificado como **falha do contrato do validador**, não como prova de corrupção do RAW.

O incidente permanece preservado e deve ser considerado em futuras certificações.

### Regra de não repetição de certificação

Antes de criar uma nova regra de certificação, o processo deve consultar:
- certificações anteriores;
- evidências das fases anteriores;
- incidentes históricos;
- contratos de chaves;
- layouts aplicáveis;
- exceções controladas.

A ausência dessa consulta é considerada falha de governança.

**Atualização normativa:** 2026-10-01 — inclusão da regra anti-regressão de chaves, classificação de duplicidades e obrigação de reconciliação antes de promover uma hipótese a critério de certificação.

## ADITIVO DE GOVERNANÇA — 2026-10-01 — PRECEDÊNCIA DAS CARTAS E CONTRATO DE LAYOUT

A governança passa a estabelecer explicitamente uma ordem de precedência operacional para novas auditorias COTAHIST.

### 1. Ordem documental obrigatória

Toda correção que altere regra, workflow, contrato ou classificação deve seguir:

**CORREÇÃO → CARTAS → EVIDÊNCIA/INCIDENTE → VERIFICAÇÃO → README.**

As Cartas são documentos normativos. O README é documento de divulgação/inventário e nunca poderá ser utilizado como substituto de uma atualização normativa.

### 2. Auditoria orientada por layout

Nenhum validador poderá impor cardinalidade, chave, unicidade ou interpretação semântica sem identificar previamente o layout oficial aplicável ao período.

O contrato obrigatório é:

**layout oficial → campos/offsets → semântica documentada → hipótese → amostra → teste histórico → decisão normativa → implementação → evidência.**

### 3. Controle de regressão

Antes de executar uma nova fase, deve ser feita verificação explícita contra incidentes e correções anteriores. Um workflow novo não pode reintroduzir uma regra já rejeitada sem apresentar nova evidência e decisão normativa.

### 4. Estado de suspensão

Quando a regra de auditoria depender de layout ainda não reconciliado, o estado correto é **BLOQUEADO POR GOVERNANÇA / AGUARDANDO LAYOUT**, e não **DADO INVÁLIDO**.

Essa regra é permanente e passa a integrar a autoridade normativa da Carta Magna.

## CONTROLE DE VERSÃO — 2026-10-01

**Versão vigente:** 1.1  
**Alteração:** consolidação da regra de precedência documental, layout como pré-condição de auditoria e não repetição de erros já corrigidos.  
**Status:** VIGENTE

