# REGRA GERAL — EXISTÊNCIA E VALIDAÇÃO DE EVIDÊNCIAS COTAHIST V1

**Status:** REGRA REGENTE  
**Aplicação:** B3 / COTAHIST / ingestão histórica e retrospectiva  
**Data de registro:** 2026-09-30

## Regra

Todo artefato, fase, evidência, transformação, validação ou decisão produzida neste projeto deve:

1. **Existir fisicamente no repositório** no caminho definido para sua função.
2. **Ser identificável** por nome, versão, ano/escopo e fase.
3. **Ser validável** por evidência objetiva, checksum, manifesto, teste, workflow ou outro mecanismo auditável apropriado.
4. **Ser registrado no Git**, com histórico de commit preservado.
5. **Não ser considerado concluído apenas porque um workflow terminou com sucesso**; o conteúdo da evidência e seus gates também devem ser verificados.
6. **Não permitir avanço silencioso de fase** quando uma pré-condição obrigatória estiver ausente, inválida ou não auditada.
7. **Manter separação entre fato, validação, exceção controlada e hipótese**.
8. **Preservar a imutabilidade do RAW** após sua validação, salvo procedimento explícito e auditado de correção/reprocessamento.
9. **Registrar bloqueios e exceções**, nunca ocultá-los para obter um status verde.
10. **Fechar formalmente cada ano antes da transição para o ano seguinte**, mediante evidência de fechamento e autorização de transição.

## Regra de avanço

Uma fase somente pode receber status de concluída/liberada quando:

- seus artefatos obrigatórios existem;
- suas pré-condições estão presentes;
- seus testes/gates definidos para a fase passam;
- a evidência da fase é persistida no repositório;
- o resultado pode ser reproduzido ou auditado;
- não existem bloqueios não declarados.

## Regra de transição anual

Para um ano YYYY, a transição para YYYY+1 somente pode ser autorizada quando:

- o RAW de YYYY estiver preservado e validado;
- a normalização e seu manifesto estiverem validados;
- as reconciliações e validações semânticas aplicáveis estiverem validadas;
- a pré-release estiver liberada;
- a integridade final estiver validada;
- a certificação estiver registrada;
- a FASE12 de fechamento/transição estiver concluída;
- a evidência da FASE12 estiver publicada no repositório.

**Princípio:** se não existe no repositório e não há evidência auditável de sua validação, para fins deste projeto o item não é considerado concluído.

## Auditoria

Esta regra deve ser usada como critério permanente nas futuras fases COTAHIST e nos demais fluxos de ingestão B3 que adotem este contrato.

## Registro de ativação FASE12

A criação da FASE12 deve provocar execução automática do workflow de fechamento/transição de 1993.


## Atualização normativa — 2026-10-01

### 1. Localização canônica

Para COTAHIST anual, a existência deve ser resolvida pelo caminho:

`dados/cotahist/raw/anual/COTAHIST_A<AAAA>.ZIP`

A ausência de resultado em busca ampla não constitui evidência de ausência.

### 2. Execução linear

A sequência de dependência é:

**00 → 01 → 02 → 03–05 → 06 → 07 → 08 → GATE → 09 → GATE → 10 → GATE → 11 → GATE → 12.**

### 3. Separação de estados

`EXISTE`, `ÍNTEGRO`, `VALIDADO`, `CERTIFICADO` e `FECHADO` são estados distintos.

### 4. Incidentes

Falha de workflow deve ser diagnosticada separadamente de falha do dado. Os incidentes de 1994 permanecem preservados como evidência.

### 5. Estado de referência

1994 está fechado e autorizou a transição para 1995.

1995 possui RAW, manifesto e checksum no caminho canônico e deve iniciar sua cadeia própria sem nova aquisição.

