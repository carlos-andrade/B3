# Fontes públicas gratuitas — inventário e auditoria

| Campo | Valor |
|---|---|
| **ID** | B3-FONTES-PUBLICAS-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Estado** | EM EXECUÇÃO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 274b3c862fecd361522be5b82abbc53ca90730d897912798c240d625b7ba14c0 |
| **Commit de referência (versão anterior)** | [90a35cd](https://github.com/carlos-andrade/B3/commit/90a35cd247ad3952a65497ea03ef433c2e7051c6) |
| **Data de atualização** | 2026-10-20 |
| **Autoridade normativa** | [Política de aquisição de dados públicos gratuitos](../../WIKI/01-GOVERNANCA/POLITICA_AQUISICAO_DADOS_PUBLICOS_GRATUITOS_V1.md) |

## Fonte de verdade

- [Inventário de fontes públicas gratuitas (JSON)](./INVENTARIO_FONTES_PUBLICAS_GRATUITAS_V1.json)
- [Auditoria e roadmap de execução (2026-10-20)](./AUDITORIA_FONTES_PUBLICAS_GRATUITAS_2026-10-20.md)
- [Registo de autorização de endpoints B3](../../docs/governanca/licenciamento/REGISTRO_AUTORIZACOES_ENDPOINTS_B3_2026-10-16.json)
- [Workflow de fontes gratuitas](../../.github/workflows/b3-fontes-gratuitas-orquestrador.yml)
- [Workflow de ingestão CVM DFP/ITR](../../.github/workflows/b3-cvm-dados-abertos.yml)
- [Importador CVM DFP/ITR](../../scripts/ingestao/importar_cvm_dados_abertos.py)
- [Testes do importador CVM](../../scripts/ingestao/test_importar_cvm_dados_abertos.py)
- [RAW CVM DFP 2026](../cvm/raw/cia_aberta-doc-dfp/dfp_cia_aberta_2026.zip)
- [Manifesto CVM DFP 2026](../cvm/manifests/cia_aberta-doc-dfp_2026.json)
- [RAW CVM ITR 2026](../cvm/raw/cia_aberta-doc-itr/itr_cia_aberta_2026.zip)
- [Manifesto CVM ITR 2026](../cvm/manifests/cia_aberta-doc-itr_2026.json)
- [Workflow PTAX BCB](../../.github/workflows/b3-ptax-bcb.yml)
- [Importador PTAX BCB](../../scripts/ingestao/importar_ptax_bcb.py)
- [Testes do importador PTAX](../../scripts/ingestao/test_importar_ptax_bcb.py)
- [Manifesto PTAX EUR 2026-10-20](../cambio/ptax/manifests/PTAX_EUR_2026-10-20.json)
- [RAW PTAX EUR](../cambio/ptax/raw/PTAX_EUR_2026-09-21_2026-10-20_20261020T111621Z.json)
- [Manifesto PTAX USD 2026-10-20](../cambio/ptax/manifests/PTAX_USD_2026-10-20.json)
- [RAW PTAX USD](../cambio/ptax/raw/PTAX_USD_2026-09-21_2026-10-20_20261020T111622Z.json)
- [Evidência da captura PTAX](https://github.com/carlos-andrade/B3/actions/runs/39413690563)
- [Evidência da captura CVM](https://github.com/carlos-andrade/B3/actions/runs/39413170519)
- [Validador do inventário](../../scripts/governanca/validar_inventario_fontes_publicas.py)
- [Testes do validador](../../scripts/governanca/test_validar_inventario_fontes_publicas.py)

## Domínios

- **B3:** catálogo de instrumentos, COTAHIST, BDI e negócios; respetivos canais exigem avaliação específica de termos e autorização.
- **BCB:** SGS, Copom JSON e PTAX; licenças abertas aplicam-se ao conjunto/recursos identificados, com preflight onde definido.
- **CVM:** dados de fundos, cadastro de companhias abertas, DFP e ITR sob ODbL conforme os conjuntos oficiais identificados.
- **IBGE/SIDRA e Tesouro Transparente:** fontes públicas candidatas; falta confirmar o âmbito de cada conjunto e implementar captura.

## Regra

A fonte deve ser registada antes da implementação. O estado técnico da captura não substitui a licença. Toda ingestão deve preservar origem, data/hora, artefacto bruto, checksum, manifesto e validações, quando permitido. As fontes sem restrições documentadas não devem ser descartadas por bloqueios genéricos; as restrições explícitas devem ser respeitadas e delimitadas ao canal e escopo aplicáveis.
