# Arquitetura Geral

## Visão em camadas

```text
FONTES
  ↓
AQUISIÇÃO
  ↓
RAW / PRESERVAÇÃO
  ↓
NORMALIZAÇÃO
  ↓
VALIDAÇÃO
  ↓
EVIDÊNCIAS / AUDITORIA
  ↓
DADOS PUBLICADOS
  ↓
ANÁLISE / BACKTEST / APLICAÇÕES
```

## Fontes

A arquitetura pode integrar dados da B3, BCB e outras fontes econômicas ou de mercado devidamente identificadas.

## Aquisição

Os processos de aquisição devem registrar período, origem, arquivo obtido, resultado da operação e eventuais falhas.

## RAW

A camada RAW preserva o material recebido antes das transformações.

## Normalização

Transformações devem ser determinísticas sempre que possível e possuir código ou documentação suficiente para reprodução.

## Validação

A validação deve cobrir estrutura, tipos, chaves, datas, campos semânticos, valores, volumes e quantidades, calendário e amostras comparativas com a origem.

## Auditoria

A arquitetura deve permitir responder: de onde veio este dado, o que foi feito com ele, qual versão do processo o produziu, quais testes foram executados e qual evidência comprova o resultado.

## Evolução

A arquitetura será ampliada conforme novos módulos forem validados. Alterações relevantes devem atualizar esta página.
