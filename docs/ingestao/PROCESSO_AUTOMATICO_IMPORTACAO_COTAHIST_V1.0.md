# PROCESSO AUTOMÁTICO DE IMPORTAÇÃO DO COTAHIST — V1.0

**Projeto:** B3 — A BOLSA DO BRASIL  
**Status:** VIGENTE  
**Data:** 25/09/2026

## 1. Objetivo

Manter uma camada automática de atualização corrente do COTAHIST, separada do backfill anual histórico.

## 2. Fonte

A fonte primária é a B3. A página oficial informa que a série histórica contém dados desde 1986 e é disponibilizada em arquivos ZIP interpretados pelo layout oficial. A B3 também disponibiliza o layout oficial do COTAHIST. citeturn0search0turn0search13

A aquisição incremental utiliza o padrão público de arquivo diário COTAHIST_D{DDMMAAAA}.ZIP. O endpoint direto deve ser tratado como mecanismo operacional sujeito a mudança, não como contrato permanente da B3. citeturn2view0

## 3. Fluxo

B3 → COTAHIST diário → validação ZIP → SHA-256 RAW → normalização → validação estrutural/temporal → manifest → commit.

## 4. Frequência

O workflow automático executa diariamente após o fechamento do mercado. Dias sem pregão são tratados como ausência operacional conhecida.

## 5. Fail-closed

Corrupção, ZIP inválido, conteúdo vazio inesperado, erro de parsing ou falha de validação impede a publicação do artefato.

## 6. Separação de camadas

- **Anual:** backfill histórico e certificação 1986–2026.
- **Diária:** atualização incremental corrente.
- **Oficial:** catálogo governado para consumo.

A camada diária não altera silenciosamente os RAW anuais históricos.

## 7. Evidências

Cada aquisição bem-sucedida deve preservar, conforme aplicável: nome do arquivo, data de referência, URL, SHA-256, tamanho, arquivo normalizado, quantidade de registros, primeira/última data, parser, status de validação e commit.

## 8. Fallback

Se a aquisição automática deixar de funcionar, o procedimento manual da página oficial da B3 poderá ser utilizado como contingência. A substituição não deve ocorrer silenciosamente. citeturn0search0
