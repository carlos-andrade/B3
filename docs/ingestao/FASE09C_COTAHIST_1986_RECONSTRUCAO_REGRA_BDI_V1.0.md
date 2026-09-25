# FASE 09C — Reconstrução documental da regra de agregação/publicação do BDI — Vigor 10/10/1986

**Arquivo:** FASE09C_COTAHIST_1986_RECONSTRUCAO_REGRA_BDI_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconstrução documental da origem de duas linhas estatísticas sob a mesma K4  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Ponto de partida

As FASES 08C, 08H e 09B convergem para uma única colisão K4 no COTAHIST 1986:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

As linhas RAW 140808 e 140809 possuem a mesma K4 e estatísticas diferentes.

FASE 09B demonstrou, no universo integral de 1986, que não existe uma população comparável de colisões. Portanto, a FASE 09C abandona a busca estatística genérica e passa a investigar a regra histórica de publicação/agregação do BDI.

## 2. Pergunta documental

Qual dimensão existente no processo de registro/publicação do Mercado a Termo da Bovespa em 10/10/1986 permitia que dois agregados estatísticos distintos fossem publicados para o mesmo ativo, prazo e demais campos hoje preservados na K4?

Dimensões a testar separadamente:

1. Tipo de operação a termo;
2. taxa/preço ou faixa de taxa;
3. comitente/participante/corretora;
4. posição de compra ou venda;
5. modalidade ou condição operacional;
6. regra de agregação do boletim;
7. correção/republicação/erro operacional;
8. qualquer outro campo existente no BDI e ausente no COTAHIST.

## 3. Evidência contemporânea já recuperada

O Jornal do Brasil de 05/06/1986 reproduz uma tabela do mercado a termo com as dimensões **Tipo** e **Prazo**, além de Quant, Fech, Máx, Mín, Méd e N°. A mesma publicação contém Vigor PP C05 e outros códigos Cxx. Isso demonstra que havia mais de uma dimensão de classificação/publicação além do prazo. citeturn0search0

A evidência, entretanto, não permite concluir que C05 seja o campo Tipo, nem que Tipo seja a dimensão que causou a colisão Vigor.

## 4. Evidência normativa e estrutural

O layout oficial do COTAHIST define DATA DO PREGÃO nas posições 03–10 e CODBDI como código utilizado para classificar os papéis na emissão do BDI. TPMERC identifica o mercado em que o papel está cadastrado. citeturn0search36

Regulamentação posterior da Bovespa documenta o BDI como boletim diário contendo operações dos mercados administrados pela Bolsa e informações dos mercados de liquidação futura. Essa fonte é posterior a 1986 e, portanto, serve como evidência de função institucional do BDI, não como prova direta da regra vigente em 1986. citeturn1search17

Manual posterior também registra que informações de taxas mínima, máxima e média das operações a termo para diferentes tipos de termo eram divulgadas no BDI. Novamente, a fonte é posterior e não deve ser retroprojetada automaticamente para 1986. citeturn0search37

## 5. Evidência institucional para recuperação primária

A B3 informa que o Centro de Memória preserva mais de 100.000 itens documentais e permite pesquisa no acervo digital ou presencial. A instituição disponibiliza atendimento a pesquisadores mediante agendamento. citeturn1search11

A página atual de pesquisa por pregão da B3 também informa que permite acesso a boletins diários e arquivos, inclusive retroativos, embora a interface atualmente disponível não tenha fornecido, nesta etapa, o BDI de 10/10/1986. citeturn1search1

## 6. Documento decisivo a recuperar

Prioridade máxima:

**Boletim Diário de Informações — Bovespa — pregão de 10/10/1986**, preferencialmente a seção **Mercado a Termo**, contendo Vigor / VGO 2 / PP C05 / prazo 060.

Prioridades secundárias:

- BDI de 09/10/1986;
- BDI de 13/10/1986;
- páginas imediatamente anteriores/posteriores da mesma série;
- legenda de Tipo/Cxx;
- manual/regulamento operacional vigente em 1986;
- tabela ou nota metodológica sobre agregação das operações a termo.

## 7. Campos que devem ser extraídos do BDI

Quando o exemplar for recuperado, registrar literalmente:

- título da publicação;
- data do pregão;
- número da edição, se existente;
- número da página;
- seção/capítulo;
- cabeçalho completo da tabela;
- título do ativo;
- Tipo;
- Prazo;
- Quant.;
- Fech.;
- Máx.;
- Mín.;
- Méd.;
- Volume, se presente;
- N° de negócios, se presente;
- código Cxx completo;
- qualquer coluna adicional;
- notas de rodapé;
- legenda da tabela;
- identificação/catalogação do acervo;
- URL, ID ou referência institucional do item;
- imagem/PDF, quando disponível.

## 8. Testes de decisão

### H1 — Tipo é a dimensão ausente

Somente será aceita se o BDI de 10/10/1986 demonstrar que as duas linhas Vigor possuem Tipos diferentes ou se documentação contemporânea estabelecer explicitamente que Tipo gera agregações separadas sob as demais condições do alvo.

### H2 — taxa/preço é a dimensão ausente

Somente será aceita se documentação contemporânea demonstrar agregação separada por taxa ou condição equivalente e os dois perfis do COTAHIST puderem ser reconciliados com essa regra.

### H3 — participante/comitente/posição é a dimensão ausente

Somente será aceita com documentação contemporânea que demonstre essa dimensão como chave de publicação/agregação.

### H4 — regra histórica de agregação/publicação do BDI

Será aceita se a documentação demonstrar que o BDI podia publicar mais de uma linha para o mesmo conjunto de campos hoje representado pela K4, por uma regra editorial/operacional de agregação.

### H5 — erro de processamento/publicação

Somente será aceita mediante evidência de correção, errata, inconsistência documental ou outra prova contemporânea.

## 9. O que NÃO será feito

- Não serão fundidas as linhas 140808 e 140809.
- Não será escolhido um dos dois registros como correto.
- Não será atribuído significado a C05 sem evidência.
- Não será retroprojetada uma regra moderna para 1986.
- Não será inferida identidade econômica apenas porque a K4 coincide.
- Não será alterado o RAW.

## 10. Estado

**IMPLEMENTADO:** protocolo documental definido.  
**EXECUTADO:** pesquisa pública inicial executada.  
**VALIDADO:** evidência estrutural/normativa disponível e limitações registradas.  
**CAUSA HISTÓRICA:** NÃO RESOLVIDA.  
**EVIDÊNCIA DECISIVA:** BDI de 10/10/1986 ainda não recuperado.

## 11. Próxima ação

Prosseguir exclusivamente na recuperação do exemplar primário do BDI de 10/10/1986 e, em paralelo, procurar o regulamento/manual Bovespa efetivamente vigente em 1986. A investigação será encerrada somente quando a regra puder ser demonstrada documentalmente ou quando a ausência do documento for formalmente registrada como limite da reconstrução.

## 12. Fontes externas consultadas

- Jornal do Brasil, 05/06/1986 — evidência contemporânea de tabela do mercado a termo e nomenclatura Cxx. citeturn0search0
- B3 — Layout oficial do COTAHIST. citeturn0search36
- B3 — Regulamento posterior sobre BDI. citeturn1search17
- B3 — Manual posterior de procedimentos do mercado a termo. citeturn0search37
- B3 — Centro de Memória. citeturn1search11
- B3 — Pesquisa por pregão/boletins retroativos. citeturn1search1
- Decreto-Lei nº 2.286/1986 — contexto normativo do mercado a termo. citeturn0search2