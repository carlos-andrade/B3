# CARTA DE CONFIANÇA DOS DADOS
## Repositório B3 — A BOLSA DO BRASIL

**Arquivo:** CARTA_DE_CONFIANCA_DOS_DADOS.md  
**Projeto:** B3 — A BOLSA DO BRASIL  
**Repositório:** carlos-andrade/B3  
**Data de criação:** 24/09/2026  
**Finalidade:** estabelecer os critérios mínimos para considerar confiáveis, auditáveis e reproduzíveis os dados gravados neste repositório.

---

## 1. Princípio fundamental

Nenhum dado deste repositório deve ser considerado confiável apenas porque está armazenado no GitHub.

A confiança deve resultar de uma cadeia verificável:

**fonte → aquisição → arquivo bruto → integridade → parsing → normalização → validação → reconciliação semântica → versionamento → auditoria.**

Se qualquer elo dessa cadeia estiver ausente, quebrado ou não documentado, o dado deve ser classificado como **não validado** até que a pendência seja resolvida.

---

## 2. Hierarquia de confiança

Os dados devem ser classificados, no mínimo, em quatro estados:

### 2.1 RAW — DADO BRUTO
Arquivo obtido da fonte original, preservado sem alteração semântica.

Regras:
- não alterar o conteúdo original;
- preservar nome, período, origem e data de aquisição;
- registrar checksum quando possível;
- nunca substituir silenciosamente um arquivo bruto.

### 2.2 PARSED — DADO EXTRAÍDO
Conteúdo convertido de seu formato original para uma representação estruturada.

Regras:
- manter referência inequívoca ao arquivo RAW;
- documentar layout, offsets, campos e tipos;
- registrar erros de leitura;
- não descartar registros silenciosamente.

### 2.3 NORMALIZED — DADO NORMALIZADO
Dados transformados para um esquema comum.

Regras:
- toda transformação deve ser determinística e documentada;
- códigos de origem não podem ser reinterpretados sem uma regra registrada;
- campos transformados devem manter rastreabilidade para o valor original;
- mudanças de regra exigem nova versão.

### 2.4 VALIDATED — DADO VALIDADO
Dado submetido aos testes definidos pelo projeto.

Somente este estado pode ser utilizado como base para análises quantitativas sem ressalva adicional.

---

## 3. Regra de rastreabilidade

Todo dado derivado deve poder responder:

1. Qual foi a fonte?
2. Qual arquivo original foi utilizado?
3. Qual período ele cobre?
4. Quando foi adquirido?
5. Qual versão do parser o processou?
6. Qual versão da normalização foi aplicada?
7. Quais validações foram executadas?
8. Qual commit produziu o resultado?
9. Quais registros foram rejeitados, corrigidos ou descartados?
10. É possível reproduzir o resultado?

Se essas perguntas não puderem ser respondidas, a confiança deve ser reduzida.

---

## 4. Integridade dos arquivos

Sempre que tecnicamente possível, cada arquivo de entrada deve possuir:

- tamanho em bytes;
- checksum/hash;
- fonte;
- URL ou identificador da origem;
- data de aquisição;
- período de referência;
- formato;
- versão do layout;
- status de validação.

Um arquivo cujo checksum mudou deve ser tratado como uma nova entrada até que a alteração seja explicada.

---

## 5. Integridade temporal

Datas são dados críticos.

Devem ser verificadas:

- data inicial;
- data final;
- continuidade temporal;
- duplicidade;
- registros fora do período esperado;
- datas inválidas;
- inversões temporais;
- lacunas justificadas e não justificadas;
- coerência entre data de negociação e calendário de mercado.

Não se deve preencher lacunas automaticamente sem registrar a regra utilizada.

---

## 6. Integridade estrutural

Cada dataset deve ser testado quanto a:

- quantidade de registros;
- quantidade de campos;
- tamanho dos registros, quando aplicável;
- tipos de dados;
- campos obrigatórios;
- valores nulos;
- valores fora do domínio;
- duplicidades;
- ordenação;
- chaves;
- consistência entre campos relacionados.

Falhas estruturais não podem ser mascaradas por conversões silenciosas.

---

## 7. Reconciliação semântica

Códigos de mercado não devem ser interpretados por aproximação.

Para campos como **TPMERC, CODBDI, CODNEG, ESPECI, PRAZOT, MODREF, PREULT, PREABE, PREMAX, PREMIN, PREMED, VOLTOT e QUATITENS**, a interpretação deve ser baseada na documentação da fonte e em evidência verificável.

Quando uma interpretação não puder ser comprovada, ela deve ser marcada como:

**HIPÓTESE — NÃO VALIDADA.**

Hipótese não pode ser promovida a fato apenas porque produz resultados plausíveis.

---

## 8. Regras específicas para COTAHIST

Para arquivos históricos da B3/COTAHIST:

- preservar os arquivos originais;
- respeitar o layout correspondente ao período;
- não assumir que layouts históricos são idênticos entre anos;
- validar o tamanho e a estrutura dos registros;
- mapear códigos explicitamente;
- separar mercado à vista, opções, futuros e demais modalidades conforme o código documentado;
- validar campos numéricos e casas decimais;
- validar datas;
- investigar registros rejeitados;
- registrar mudanças de layout;
- impedir que um parser moderno seja aplicado cegamente a arquivos históricos.

Um resultado aparentemente correto não substitui a validação do layout.

---

## 9. Regras contra dados inventados

É proibido:

- inventar registros;
- completar preços ausentes com estimativas sem marcação explícita;
- criar volume inexistente;
- inferir negócios que não estão presentes na fonte;
- transformar hipótese em dado;
- corrigir valores sem registrar o valor original;
- eliminar outliers sem justificativa e rastreabilidade;
- alterar retrospectivamente o RAW.

Qualquer imputação deve ser identificada como **DADO DERIVADO/IMPUTADO**, nunca como dado original.

---

## 10. Regras contra perda silenciosa

Nenhuma etapa de ingestão pode descartar registros sem contabilização.

Toda pipeline deve procurar produzir, quando aplicável:

**entrada → processados → aceitos → rejeitados → duplicados → corrigidos → saída.**

A soma das categorias deve ser reconciliável com a entrada, salvo exceções explicitamente documentadas.

---

## 11. Controle de duplicidade

Duplicatas devem ser investigadas antes de serem removidas.

Uma duplicidade pode representar:

- repetição legítima;
- registro duplicado na fonte;
- erro de ingestão;
- erro de chave;
- evento de mercado legítimo com atributos semelhantes.

Não se deve deduplicar apenas por aparência.

---

## 12. Versionamento

Toda alteração relevante em:

- parser;
- schema;
- mapeamento;
- normalização;
- validação;
- fonte;
- calendário;
- regras de classificação;

deve gerar versão identificável e commit no Git.

O histórico do Git constitui parte da trilha de auditoria.

Nenhum resultado validado deve depender de código ou regra que não esteja versionado.

---

## 13. Reprodutibilidade

Uma análise deve ser reproduzível a partir de:

**fonte + versão do código + parâmetros + regras + commit.**

Se duas execuções com os mesmos insumos e a mesma versão produzirem resultados diferentes, o pipeline deve ser considerado **não determinístico** até investigação.

---

## 14. Testes mínimos

Antes de promover um dataset a VALIDATED, devem ser executados, conforme aplicabilidade:

- teste de existência;
- teste de leitura;
- teste de encoding;
- teste estrutural;
- teste de schema;
- teste temporal;
- teste de duplicidade;
- teste de domínio;
- teste de cardinalidade;
- teste de continuidade;
- teste de reconciliação;
- teste de invariantes;
- teste de consistência entre etapas;
- teste de reprodutibilidade.

Os resultados dos testes devem ser preservados.

---

## 15. Evidência negativa também é evidência

Uma validação que falha deve ser registrada.

Não é permitido apagar o histórico de falhas apenas porque uma versão posterior foi corrigida.

Falhas importantes devem permanecer auditáveis para permitir reconstrução da evolução do projeto.

---

## 16. Separação entre fato, transformação e inferência

Todo resultado deve distinguir:

**FATO:** diretamente observado na fonte.

**TRANSFORMAÇÃO:** resultado determinístico de uma regra documentada.

**INFERÊNCIA:** interpretação produzida a partir dos dados.

**HIPÓTESE:** explicação ainda não comprovada.

Essa distinção é obrigatória em análises de mercado.

---

## 17. Dados para pesquisa quantitativa

Antes de utilizar uma série em backtests, estudos estatísticos ou modelos quantitativos, deve-se verificar:

- cobertura temporal;
- sobrevivência de ativos;
- corporate actions;
- splits;
- bonificações;
- dividendos;
- mudanças de ticker;
- ativos deslistados;
- viés de sobrevivência;
- liquidez;
- gaps artificiais;
- mudanças de metodologia;
- qualidade dos volumes;
- consistência dos preços.

Uma série histórica não é automaticamente adequada para backtest apenas por possuir muitas observações.

---

## 18. Proibição de confiança absoluta

Nenhum dataset deve ser descrito como:

**“100% correto”**, **“infalível”** ou **“sem erros”**.

A classificação apropriada é:

- **VALIDADO** — passou nos testes definidos;
- **VALIDADO COM RESSALVAS** — passou, mas possui limitações documentadas;
- **NÃO VALIDADO** — evidência insuficiente;
- **REJEITADO** — apresentou falha incompatível com o uso pretendido.

---

## 19. Regra de confiança operacional

A confiança de um dado é função da evidência disponível, não da aparência do resultado.

**Fonte confiável + arquivo íntegro + parser validado + semântica comprovada + testes aprovados + rastreabilidade + reprodutibilidade = dado apto ao uso definido.**

A ausência de qualquer componente crítico deve reduzir o nível de confiança.

---

## 20. Regra de ouro do repositório B3

> **Não confiaremos no dado porque ele parece correto. Confiaremos somente naquilo que conseguirmos rastrear, testar, reproduzir e explicar.**

Este documento estabelece a política de confiança dos dados do projeto **B3 — A BOLSA DO BRASIL** e deve ser tratado como documento normativo para as futuras etapas de ingestão, normalização, validação e análise.

---

## Controle de versão

**Versão:** 1.0  
**Data:** 24/09/2026  
**Status:** VIGENTE  
**Escopo:** dados históricos, dados de mercado, dados econômicos, calendários, datasets derivados e resultados produzidos pelo repositório B3.
