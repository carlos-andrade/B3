# Inventário B3 — 2026-09-21

**Projeto:** B3 - A Bolsa do Brasil  
**Repositório:** `carlos-andrade/B3`  
**Data de referência:** 21/09/2026  
**Fonte:** B3 — BVBG.028.02 Instruments File / Cadastro de Instrumentos (Listado)

## Evidência da fonte

A página oficial de pesquisa por pregão da B3 registra o **BVBG.028.02 Instruments File — Cadastro de instrumentos** para a data de referência disponível, e a documentação da B3 define o BVBG.028.02 como o arquivo de identificação dos instrumentos.

## Regra de processamento

1. Baixar o arquivo oficial da B3.
2. Preservar o arquivo bruto sem alteração.
3. Validar encoding, delimitador, cabeçalho e quantidade de registros.
4. Normalizar somente em uma cópia derivada.
5. Classificar os instrumentos por categoria.
6. Criar diretório individual apenas para registros efetivamente presentes no cadastro.
7. Registrar contagens e inconsistências.
8. Não preencher campos ausentes por inferência.

## Situação

A fonte oficial está identificada, mas a interface pública consultada é dinâmica. A extração automatizada deve ser executada pelo coletor versionado em `ferramentas/importar_bvbg028.py`, preservando o arquivo original e seu hash.

**Importante:** este arquivo não declara uma quantidade de instrumentos sem que o CSV oficial tenha sido efetivamente capturado e validado.
