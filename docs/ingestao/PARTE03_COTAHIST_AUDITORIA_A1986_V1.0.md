# AUDITORIA COTAHIST A1986 — V1.0

Arquivo: PARTE03_COTAHIST_AUDITORIA_A1986_V1.0.md
Projeto: B3 - A BOLSA DO BRASIL
Tema: Auditoria estrutural e de integridade do COTAHIST 1986
Caminho: docs/ingestao/PARTE03_COTAHIST_AUDITORIA_A1986_V1.0.md
Data de criação: 24/09/2026
Repositório: carlos-andrade/B3

## 1. Execução auditada

- Workflow: COTAHIST - normalizacao controlada V7
- Run ID: 36003846986
- Run: #1
- Evento: workflow_dispatch
- Commit de execução: ef9285e678308bfcc9c8c656ec7f36299774a01b
- Resultado: SUCCESS
- Job: normalize
- Job ID: 107646853280
- Artefato: cotahist-normalizacao-controlada-v7-1986
- Artifact ID: 10808548928
- Digest do artefato: f1bcfe917627addd45e9b1387d097397b8e9940788fdcb33bf3e459c9faf5dc6

## 2. Resultado estrutural

- Registros normalizados: 177.981
- Campos: 25
- Parser: 1.1.0
- Primeira data: 1986-01-02
- Última data: 1986-12-30
- Datas distintas: 248
- Datas inválidas: 0
- Datas fora do ano: 0
- Chave de negócio auditada: data_pregao + codneg + tpmerc + codbdi
- Duplicidades da chave: 5.189

### Interpretação das duplicidades

As 5.189 ocorrências de duplicidade dessa chave NÃO são classificadas como erro automaticamente. O arquivo contém múltiplos instrumentos/contratos para o mesmo ativo, mercado e código BDI, diferenciados por campos como prazo (prazot) e outras características do registro. Portanto, a chave acima é uma chave de diagnóstico, não uma chave primária definitiva.

## 3. Integridade do CSV

- Linhas: 177.981
- Colunas: 25
- codneg nulo: 0
- nomres nulo: 0
- Registros completos quanto aos campos-base de identificação: preservados.
- Preços principais negativos: 0
- Totneg negativo: 0
- Quatot negativo: 0
- Voltot negativo: 0
- Série temporal das datas: monotônica crescente.

## 4. Preços e OHLC

Os campos preabe, premax, premin e preult estão preenchidos em todos os 177.981 registros e não apresentam valores negativos.

Foi encontrada uma exceção importante para a regra simplificada de OHLC:

- 30 registros apresentam alguma relação aparentemente incompatível entre premax/premin e preabe/preult.

Esses registros NÃO devem ser removidos nem corrigidos automaticamente. O COTAHIST histórico pode conter situações relacionadas a ajustes, eventos corporativos, características do instrumento ou semântica histórica dos campos. A auditoria registra a anomalia para investigação, sem substituir o dado-fonte.

Foram observados exemplos envolvendo ITEC, LABA, VALE, CHAPECO, ALPA, MARVIN, PETR, WHMT, CPFL, BELG, CPNE, MEND, CIIT, BBAS e outros.

## 5. Valores nulos

Foram observados nulos principalmente em campos que podem ser não aplicáveis a determinados tipos de instrumento ou registro, especialmente campos como preco de oferta, vencimento e características específicas.

Conclusão: não utilizar preenchimento automático com zero ou interpolação sem uma regra semântica específica por campo e por tipo de mercado.

## 6. Distribuição por tipo de mercado

Quantidade de registros por tpmerc:

| tpmerc | registros |
|---:|---:|
| 10 | 96.479 |
| 30 | 36.596 |
| 20 | 36.021 |
| 70 | 7.027 |
| 12 | 835 |
| 80 | 761 |
| 13 | 152 |
| 17 | 99 |
| 60 | 11 |

Esses códigos devem ser mantidos como códigos-fonte até que a tabela histórica oficial de domínio seja reconciliada. Não atribuir rótulos por inferência.

## 7. Distribuição temporal

- Dias com registros: 248
- Média de registros por dia: aproximadamente 717,7
- Mínimo: 3
- Máximo: 936

A existência de dias com poucos registros deve ser investigada contra calendário de pregão, feriados, eventos de mercado e composição dos mercados cobertos pelo COTAHIST. Não é evidência suficiente, isoladamente, de perda de dados.

## 8. Hashes

RAW:
350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018

NORMALIZADO:
fbd00ff5b24075813132193dc794e29015df20b7dc6bedadba7e896b30406329

Os hashes acima foram obtidos durante a execução e registrados no quality manifest.

## 9. Veredito técnico da auditoria

STATUS: APROVADO PARA PRÓXIMA ETAPA, COM PENDÊNCIAS CONTROLADAS.

O processamento V7 de 1986 é reproduzível e o artefato normalizado é íntegro conforme os testes executados. Entretanto, antes de processar em massa 1987–2026, devem ser formalizadas:

1. chave lógica definitiva por registro;
2. dicionário histórico de tpmerc/codbdi;
3. tratamento semântico de nulos;
4. regra de auditoria OHLC que diferencie anomalia de ajuste/evento corporativo;
5. teste de continuidade por dia de pregão;
6. reconciliação de quantidade/volume;
7. validação amostral contra o arquivo RAW original;
8. política para registros de derivativos, opções e mercados especiais.

Nenhum registro anômalo deve ser apagado nesta fase.

## 10. Próxima etapa

Executar o mesmo V7 para 1987 somente após a auditoria estrutural de 1986 ser registrada. O processamento em massa 1986–2026 permanece bloqueado até a conclusão dessa etapa.
