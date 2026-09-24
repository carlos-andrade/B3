# PARTE03 — Negócio a Negócio DERIV — Layout V1.0

**Arquivo:** PARTE03_NEGOCIO_A_NEGOCIO_LAYOUT_DERIV_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Layout do feed tick-by-tick DERIV da B3  
**Caminho:** docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_LAYOUT_DERIV_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Evidência técnica

O layout foi confirmado por uma implementação pública independente que documenta a leitura do feed DERIV distribuído pela B3. A implementação referencia o Glossário de Negócios Listados da B3, versão 3, maio/2023.

Endpoint técnico identificado:
`https://drp.b3.com.br/rapinegocios/tickercsv/{YYYY-MM-DD}?type=1`

**Classificação da evidência do endpoint:** INDEPENDENT_PUBLIC_IMPLEMENTATION.  
A identificação do endpoint não equivale à captura dos arquivos.

## 2. Layout bruto — 12 campos

| # | Campo B3 | Tipo conceitual | Campo normalizado |
|---|---|---|---|
| 1 | DataReferencia | data | reference_date |
| 2 | CodigoInstrumento | texto | symbol |
| 3 | AcaoAtualizacao | inteiro | update_action |
| 4 | PrecoNegocio | decimal | price |
| 5 | QuantidadeNegociada | inteiro | quantity |
| 6 | HoraFechamento | HHMMSSmmm | time |
| 7 | CodigoIdentificadorNegocio | identificador | trade_id |
| 8 | TipoSessaoPregao | inteiro | session_type |
| 9 | DataNegocio | data | trade_date |
| 10 | CodigoParticipanteComprador | identificador | buyer_broker |
| 11 | CodigoParticipanteVendedor | identificador | seller_broker |
| 12 | TipoDoCanal | inteiro | channel_type |

## 3. Timestamp

O campo HoraFechamento é documentado como inteiro de 9 dígitos no formato HHMMSSmmm.

Exemplo estrutural:
`100000005` → `10:00:00.005`

O timestamp normalizado será construído por:

`trade_date + time`

Timezone de pesquisa: America/Sao_Paulo.

## 4. Microestrutura

O layout fornece **participante comprador** e **participante vendedor**, além do identificador do negócio.

Entretanto, este layout, isoladamente, **não fornece um campo explícito de agressor comprador/vendedor**. Portanto:

- não classificar automaticamente comprador como agressor;
- não classificar automaticamente vendedor como agressor;
- não calcular Cumulative Delta como se fosse agressão real;
- investigar a relação entre negócio, livro/cotações e regra de classificação antes do cálculo.

### Estado atual

**Aggressor side:** NÃO DETERMINADO.  
**Cumulative Delta:** NÃO CALCULADO.  
**Proxy de Delta:** NÃO incorporado ao dataset principal.

## 5. Integridade

Para cada captura deverão ser preservados:

- data de referência;
- URL utilizada;
- nome do ZIP;
- SHA-256 do ZIP;
- teste de integridade ZIP;
- listagem dos arquivos internos;
- nome do TXT;
- tamanho dos arquivos;
- quantidade de registros;
- primeira/última marca temporal;
- quantidade de símbolos WIN/WDO/DI identificados;
- duplicidade de trade_id;
- valores nulos/inválidos.

## 6. Datas Copom 281

Alvos:

- 16/09/2026 — primeiro dia da reunião;
- 17/09/2026 — primeiro pregão com a nova Selic efetiva.

Arquivos esperados:

- `20260916_NEGOCIOSAVISTA_DRV.zip`
- `20260917_NEGOCIOSAVISTA_DRV.zip`

A existência e o conteúdo desses arquivos continuam **PENDENTES DE CAPTURA**.

## 7. Regra de não-lookahead

A análise de janela Copom somente poderá utilizar registros cujo timestamp seja anterior ou igual ao instante de disponibilidade pública do evento correspondente.

Como o timestamp exato de publicação do Comunicado da 281ª reunião ainda não foi validado nesta ingestão, as janelas EVENTO deverão permanecer marcadas como dependentes de resolução temporal.

## 8. Fonte de evidência

Implementação pública independente consultada:

`gustavobjorgefo/b3-data-collector`

Arquivos técnicos consultados:

- `tick_by_tick/_feed.py`
- `tick_by_tick/_extractor.py`
- `tick_by_tick/_partitioner.py`

Este documento não transforma a implementação independente em fonte oficial. Ela serve como evidência técnica para reconstrução do layout e do endpoint, enquanto a validação final deverá ocorrer sobre o arquivo distribuído pela B3.

## 9. Conclusão

O **schema de 12 campos está tecnicamente identificado**.

O próximo estágio é a captura binária real de 16/09/2026 e 17/09/2026, seguida de validação do ZIP/TXT e inspeção dos registros.

Sem essa captura, nenhum número de negócios, volume, agressão ou Cumulative Delta será registrado como fato.
