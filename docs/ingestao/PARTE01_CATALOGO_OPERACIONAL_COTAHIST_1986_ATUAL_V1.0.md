# PARTE 01 — CATALOGO OPERACIONAL DA SERIE HISTORICA B3

**Arquivo:** PARTE01_CATALOGO_OPERACIONAL_COTAHIST_1986_ATUAL_V1.0.md
**Projeto:** B3 - A BOLSA DO BRASIL
**Tema:** Aquisição, preservação e validação da série histórica de cotações
**Caminho:** docs/ingestao/PARTE01_CATALOGO_OPERACIONAL_COTAHIST_1986_ATUAL_V1.0.md
**Data de criação:** 23/09/2026
**Repositório:** carlos-andrade/B3

## Fonte oficial confirmada

A B3 informa oficialmente que a série histórica de cotações contém o histórico de preços dos títulos negociados na Bolsa desde **1986**.

Página:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/

## Produto

A B3 informa que os arquivos podem conter, entre outros:

- nome e código da empresa;
- código da ação;
- código ISIN;
- tipo de mercado;
- especificação ON/PN;
- preço anterior;
- abertura;
- mínimo;
- médio;
- máximo;
- fechamento;
- quantidade de negócios;
- volume negociado;
- outros campos disponíveis.

Os arquivos são distribuídos em ZIP e, após descompactação, os dados são interpretados por layout em TXT.

## Layout oficial

Documento:
https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf

O layout consultado especifica:

- arquivo anual: COTAHIST.AAAA.TXT;
- 245 bytes por registro;
- registro 00: header;
- registro 01: cotações históricas por papel-mercado;
- registro 99: trailer.

O registro 01 possui, entre outros, data do pregão, código BDI, código de negociação, tipo de mercado, nome resumido, especificação, moeda, abertura, máxima, mínima, média, último preço, melhores ofertas, número de negócios, quantidade, volume, vencimento e identificadores.

## Convenção operacional

A nomenclatura operacional esperada para os pacotes anuais é:

`COTAHIST_AAAAA.ZIP`

onde `AAAA` representa o ano.

Exemplo de padrão documentado por implementações independentes que consomem a fonte oficial:

- COTAHIST_A1986.ZIP
- COTAHIST_A1987.ZIP
- ...
- COTAHIST_A2025.ZIP
- COTAHIST_A2026.ZIP

**Observação:** a existência efetiva de cada pacote deverá ser confirmada durante a aquisição. O projeto não deve inferir que um arquivo existe apenas porque segue a convenção de nomenclatura.

## Estrutura de armazenamento

```
dados/
└── cotahist/
    ├── raw/
    │   └── anual/
    ├── normalized/
    │   └── anual/
    ├── metadata/
    ├── layouts/
    ├── checksums/
    └── manifests/
```

## Política de ingestão

1. Adquirir o arquivo oficial.
2. Preservar o ZIP RAW.
3. Calcular SHA-256.
4. Descompactar sem modificar o conteúdo original.
5. Validar header/trailer.
6. Validar tamanho de registro.
7. Contar registros.
8. Identificar primeira/última data de pregão.
9. Validar duplicidades por chave apropriada.
10. Registrar rejeições.
11. Gerar camada NORMALIZED.
12. Registrar versão do parser.
13. Atualizar manifesto do período.
14. Somente então marcar o ano como ingerido.

## Estado atual — 23/09/2026

**Catálogo:** confirmado.

**Layout:** confirmado.

**Escopo temporal:** 1986 → período mais recente disponibilizado pela B3.

**Arquivos RAW anuais:** ainda não declarados como ingeridos neste commit.

A aquisição física dos ZIPs deve ocorrer antes de qualquer declaração de cobertura efetiva. A página B3 disponibiliza o produto, mas o mecanismo de download atual é carregado por componente externo/iframe e não expôs os binários diretamente nesta etapa automatizada.

## Próxima ação operacional

Baixar e validar os pacotes anuais a partir de 1986, começando por 1986 e avançando cronologicamente, preservando cada arquivo e seu SHA-256.

Não substituir o escopo por 1990.

## Critério de conclusão

O período somente será considerado completo quando houver:

- arquivo RAW;
- checksum;
- metadata;
- validação estrutural;
- cobertura temporal registrada;
- parser reproduzível;
- camada NORMALIZED;
- manifesto atualizado.
