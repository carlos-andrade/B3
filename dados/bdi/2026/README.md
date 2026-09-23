# BDI 2026

**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Arquivamento dos dados BDI de 2026  
**Caminho:** dados/bdi/2026/README.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

## Organização

Os arquivos de cada pregão deverão ser identificados pela data do pregão e pela tabela/capítulo de origem.

Padrão sugerido:

- `YYYY-MM-DD/`
- `raw/` — arquivo original baixado;
- `normalized/` — cópia normalizada sem alterar o conteúdo econômico;
- `manifest.json` — origem, data, hash, tamanho, registros e validações.

## Validações mínimas

1. data do pregão;
2. origem B3;
3. formato;
4. tamanho do arquivo;
5. SHA-256;
6. cabeçalho;
7. delimitador;
8. quantidade de registros;
9. duplicidades;
10. campos obrigatórios ausentes.

Nenhuma transformação deve substituir o arquivo bruto.
