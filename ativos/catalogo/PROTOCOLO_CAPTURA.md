# Protocolo de Captura do Cadastro B3

**Projeto:** B3 - A Bolsa do Brasil  
**Repositório:** `carlos-andrade/B3`  
**Data:** 23/09/2026  
**Fonte:** B3 — Cadastro de Instrumentos (Listado), BVBG.028.02

## Objetivo

Transformar o cadastro oficial diário em uma base versionada e auditável.

## Ordem obrigatória

1. Capturar o arquivo oficial.
2. Preservar o bruto.
3. Registrar SHA-256.
4. Validar cabeçalho e delimitador.
5. Contar registros.
6. Detectar códigos duplicados.
7. Detectar registros sem ticker/código.
8. Classificar por instrumento/mercado.
9. Gerar inventário derivado.
10. Registrar manifesto e log.
11. Publicar no GitHub.

## Regra de evidência

Nenhuma quantidade de ativos será apresentada como fato antes da captura e validação do arquivo correspondente à data. Estruturas de pastas criadas previamente são taxonomia do projeto, não inventário de mercado.

## Saída mínima

- CSV bruto
- CSV normalizado
- manifesto JSON
- log de validação
- SHA-256
- data de referência
- commit Git

## Próxima execução

Executar:

`python ferramentas/importar_bvbg028.py --date YYYY-MM-DD`

Depois validar os resultados antes de gerar estudos de mercado.
