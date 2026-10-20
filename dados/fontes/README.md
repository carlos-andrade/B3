# Fontes públicas gratuitas — inventário e auditoria

| Campo | Valor |
|---|---|
| **ID** | B3-FONTES-PUBLICAS-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Estado** | EM EXECUÇÃO |
| **Data de atualização** | 2026-10-20 |
| **Autoridade normativa** | [Política de aquisição de dados públicos gratuitos](../../WIKI/01-GOVERNANCA/POLITICA_AQUISICAO_DADOS_PUBLICOS_GRATUITOS_V1.md) |

## Fonte de verdade

- [Inventário de fontes públicas gratuitas (JSON)](./INVENTARIO_FONTES_PUBLICAS_GRATUITAS_V1.json)
- [Auditoria e roadmap de execução (2026-10-20)](./AUDITORIA_FONTES_PUBLICAS_GRATUITAS_2026-10-20.md)
- [Registo de autorização de endpoints B3](../../docs/governanca/licenciamento/REGISTRO_AUTORIZACOES_ENDPOINTS_B3_2026-10-16.json)
- [Workflow de fontes gratuitas](../../.github/workflows/b3-fontes-gratuitas-orquestrador.yml)
- [Validador do inventário](../../scripts/governanca/validar_inventario_fontes_publicas.py)
- [Testes do validador](../../scripts/governanca/test_validar_inventario_fontes_publicas.py)

## Domínios

- **B3:** catálogo de instrumentos, COTAHIST, BDI e negócios; respetivos canais exigem avaliação específica de termos e autorização.
- **BCB:** SGS, Copom JSON e PTAX; licenças abertas aplicam-se ao conjunto/recursos identificados, com preflight onde definido.
- **CVM:** dados de fundos, cadastro de companhias abertas, DFP e ITR sob ODbL conforme os conjuntos oficiais identificados.
- **IBGE/SIDRA e Tesouro Transparente:** fontes públicas candidatas; falta confirmar o âmbito de cada conjunto e implementar captura.

## Regra

A fonte deve ser registada antes da implementação. O estado técnico da captura não substitui a licença. Toda ingestão deve preservar origem, data/hora, artefacto bruto, checksum, manifesto e validações, quando permitido. As fontes sem restrições documentadas não devem ser descartadas por bloqueios genéricos; as restrições explícitas devem ser respeitadas e delimitadas ao canal e escopo aplicáveis.
