# Auditoria de diagnóstico — COTAHIST de 22/10/2026

- **Data de auditoria:** 2026-10-26
- **Workflow:** [Importação diária, execução #86](https://github.com/carlos-andrade/B3/actions/runs/40338958410)
- **Ficheiro processado:** `COTAHIST_D22102026.ZIP`
- **Resultado:** falha fechada durante a normalização; nenhuma promoção do dataset foi executada.

## Evidência observada na CI

O normalizador parou no registo de linha 1485:

- Tipo: `01`
- Comprimento observado: 246 bytes
- Comprimento esperado pelo parser: 245 bytes
- Bytes não ASCII observados: offsets 36 e 37 (base zero), valores `C3 82`
- Último byte observado: offset 245, valor `39` (ASCII `9`)
- O byte excedente **não é um espaço final**. Portanto, a hipótese de simplesmente remover um espaço terminal foi rejeitada.

O [layout oficial da B3](https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf) especifica registos de 245 bytes e identifica `NOMRES` (nome resumido do emissor) nas posições 28–39. Os offsets zero-based 36–37 correspondem às posições 37–38, portanto o par `C3 82` está dentro de `NOMRES`, não no fim do registo. O par é uma sequência UTF-8 válida para `Â`, mas o layout consultado não determina por si só a codificação do ficheiro nem prova qual era o texto pretendido. A hipótese de incompatibilidade de codificação/conteúdo permanece por confirmar.

## Decisão

1. Não truncar o registo nem remover bytes.
2. Manter o parser fail-closed para comprimentos diferentes de 245 bytes.
3. Não aceitar genericamente bytes UTF-8 ou alterar offsets dos campos sem confirmar a codificação e o layout oficial aplicáveis ao ficheiro.
4. Obter a especificação oficial da codificação e verificar a origem do par de bytes antes de propor uma correção.
5. Depois da correção comprovada, repetir a importação e auditar SHA-256, contagens, 25 campos, manifesto, reconciliação anual e integridade do dataset canónico.

## Estado de validação

- Testes do normalizador: passaram na execução #86.
- Importação do dia 23/10/2026: normalizou 16.898 cotações; SHA-256 do ZIP reportado pela CI: `d90845b442f17f9d004bbe2739bc2a59f450e9c413bd4ead8bc22317aed135af`.
- Importação de 22/10/2026: falhou no registo 1485; manifesto e validação integral desse dia não foram produzidos.
- Reconciliação anual e persistência: ignoradas após a falha.
- Inventário de escritores: execução #24 encontrou colisão entre dois workflows para `dados/cotahist/quality/COTAHIST_1994_FASE06_RECONCILIACAO_V1.json`. A correção em revisão retira a permissão de escrita e a publicação Git do workflow de reconciliação isolado; a cadeia FASE06→FASE12 permanece como publicador canónico e o workflow isolado deverá guardar apenas artefacto de auditoria. A correção ainda requer CI verde.

