# CONTRATO DO DATASET OFICIAL COTAHIST — V1.0

**Projeto:** B3 — A Bolsa do Brasil  
**Arquivo:** CONTRATO_DATASET_OFICIAL_COTAHIST_V1.0.md  
**Status:** VIGENTE  
**Data:** 2026-09-25  
**Escopo:** COTAHIST anual 1986–2026

## 1. Objetivo

Definir, de forma auditável e reproduzível, qual conjunto de dados COTAHIST pode ser consumido pelo INDEX, dashboard e demais camadas analíticas do projeto.

O Dataset Oficial não substitui os arquivos RAW nem os manifests de qualidade. Ele é uma **camada de seleção e identificação** construída a partir deles.

## 2. Cadeia oficial

`RAW B3 → normalização → quality manifest → certificação anual → dataset oficial → aplicações`

Nenhuma aplicação deve selecionar arquivos COTAHIST por descoberta livre de diretórios quando o Dataset Oficial estiver disponível.

## 3. Fonte de verdade

A certificação anual é mantida em:

`dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv`

O manifesto do Dataset Oficial é:

`dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json`

A matriz de certificação e os manifests de qualidade permanecem como evidência primária.

## 4. Critério de inclusão

Um ano entra no Dataset Oficial quando:

- existe RAW anual;
- existe quality manifest;
- `status = VALIDADO`;
- `parser_version = 1.1.0`;
- `campos = 25`;
- `datas_invalidas = 0`;
- `datas_fora_do_ano = 0`;
- a certificação anual não é `NAO_CERTIFICADO`.

## 5. Exceções

### 1986

1986 é incluído com o estado:

`CERTIFICADO_NORMALIZACAO_COM_EXCECAO_SEMANTICA`

A inclusão significa certificação estrutural da normalização, **não** resolução de todas as questões semânticas históricas.

### 2026

2026 é incluído como ano corrente/parcial. Seu limite temporal é determinado pelo quality manifest vigente; não se presume que o ano esteja completo.

## 6. O que este contrato NÃO certifica

O Dataset Oficial não certifica automaticamente:

- equivalência semântica perfeita entre todas as décadas;
- cobertura econômica integral de todas as sessões;
- interpretação econômica dos campos;
- qualidade de microestrutura além dos testes existentes;
- adequação dos dados a uma estratégia específica;
- ausência de problemas não testados;
- resolução semântica completa de 1986.

## 7. Integridade

Cada ano deve manter referência ao:

- arquivo RAW;
- SHA-256 do RAW;
- arquivo normalizado;
- SHA-256 do normalizado;
- quality manifest;
- estado de certificação.

Alteração de qualquer evidência relevante exige regeneração do manifesto oficial.

## 8. Fail-closed

Se qualquer ano elegível deixar de satisfazer o contrato, a geração automática deve falhar e não publicar um Dataset Oficial silenciosamente degradado.

## 9. Não retroatividade

Uma nova versão do parser, do contrato ou da certificação deve gerar nova versão do Dataset Oficial. Nenhuma versão anterior deve ser sobrescrita conceitualmente.

## 10. Regra operacional

O dashboard/index deve consumir o manifesto oficial e seguir os caminhos declarados nele. O manifesto é o catálogo; os CSVs normalizados são os dados.

**Regra final:** se um arquivo não estiver identificado e certificado pelo Dataset Oficial vigente, ele não deve ser tratado como parte da base oficial de consumo automático.
