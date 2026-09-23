# Protocolo de Captura BDI

**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Captura e validação do Boletim Diário do Mercado  
**Caminho:** dados/bdi/PROTOCOLO_CAPTURA.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Captura

Para cada pregão, registrar a data e o capítulo/tabela selecionado na fonte oficial B3.

## 2. Preservação

Quando houver download:

- salvar o arquivo original em `raw/`;
- não editar o original;
- calcular SHA-256;
- registrar tamanho em bytes.

## 3. Estrutura

Registrar:

- formato;
- nome do arquivo;
- cabeçalho;
- delimitador, quando CSV;
- número de linhas/registros;
- campos encontrados.

## 4. Integridade

Verificar:

- duplicidade de chave;
- registros sem identificador;
- valores nulos em campos obrigatórios;
- inconsistência de data;
- alterações inesperadas de layout.

## 5. Normalização

A versão normalizada deve ser derivada do bruto. Nunca sobrescrever a fonte original.

## 6. Manifesto

Cada captura deve possuir manifesto contendo:

- data do pregão;
- fonte;
- capítulo;
- tabela;
- arquivo;
- SHA-256;
- quantidade de registros;
- validações executadas;
- observações.

## 7. Regra de evidência

Se o arquivo não foi efetivamente capturado, o projeto deve registrar somente a existência/documentação da fonte. Não estimar quantidade de registros nem inventar campos.

## 8. Microestrutura

BDI consolidado não deve ser confundido com dados intradiários. Estudos de agressão, Cumulative Delta, VWAP, TWAP e fluxo exigem dados com granularidade compatível.
