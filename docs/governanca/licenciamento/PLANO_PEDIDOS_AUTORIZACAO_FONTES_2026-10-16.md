# Plano de pedidos formais de autorização — fontes de dados B3

| Campo | Valor |
|---|---|
| **ID** | B3-LIC-PEDIDOS-FONTES-20261016 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Estado** | SUPERSEDIDO PELA POLÍTICA DE CUSTO ZERO; NÃO ENVIAR PEDIDOS COMERCIAIS |
| **Versão** | 1.0.1 |
| **Data** | 2026-10-16 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Proprietário do projeto — pendente |
| **SHA-256 (conteúdo canónico)** | 3f0f532cfc045bb20808d1aa6abed41f1b5942e97f595c0cd1cf7b9f5b43d8c6 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não registada |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |

## Aviso de governação — supersedido em 2026-10-16

**Não enviar os pedidos deste documento.** O proprietário definiu política de custo zero: não contratar feeds, licenças, subscrições ou autorizações pagas. Este ficheiro fica preservado como histórico de pesquisa, não como plano operacional. O trabalho prossegue com fontes gratuitas e licenças abertas verificadas; fontes gratuitas sem direitos de uso demonstrados permanecem bloqueadas. Não há pedidos enviados nem autorizações recebidas.

## 1. Resultado da pesquisa

A pesquisa identificou canais oficiais e orientações públicas, mas **não encontrou autorização específica já concedida ao projeto B3**. A existência de uma política pública, o acesso técnico a um arquivo, ou a licença de um dataset diferente não substituem uma autorização escrita específica.

### Canais oficiais

| Tema | Canal oficial | Uso recomendado |
|---|---|---|
| B3 Market Data / política comercial | produtos-marketdata@b3.com.br | Perguntar enquadramento, direitos e licença de dados históricos/BDI e confirmação do produto |
| B3 — contratação de serviços | contratacao@b3.com.br; +55 11 2565-5080 | Encaminhar pedido de avaliação comercial e contrato aplicável |
| B3 — termos de uso | https://www.b3.com.br/pt_br/termos-de-uso-e-protecao-de-dados/termos-de-uso/ | Confirmar as restrições publicadas para uso pessoal, comercial e redistribuição |
| B3 — política comercial e contratos | https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/distribuidores/politica-comercial-e-contratos/ | Consultar política vigente e contratos aplicáveis |
| B3 — FAQ de Market Data | https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/distribuidores/perguntas-frequentes/ | Verificar diferenças entre tempo real, delay e dados históricos D-1 |
| Banco Central — dúvida sobre dataset/API | https://www3.bcb.gov.br/faleconosco/#/login/registrar?natureza=1&tipo=3 | Pedir esclarecimento sobre a licença do conjunto Documentos do Copom e os ficheiros PDF |
| Banco Central — pedido de informação | https://falabr.cgu.gov.br/ | Canal alternativo formal quando for necessário pedido de informação; selecionar BACEN |

## 2. Evidência pública relevante e limites

1. Os Termos de Uso da B3 dizem que o uso dos dados do site é para fins pessoais e que reprodução, modificação, transmissão, comercialização, publicação e distribuição para fins comerciais exigem autorização prévia e escrita. A secção sobre Difusão de Dados de Mercado também exige consentimento expresso e instrumento contratual para os usos nela descritos.
2. A FAQ de Market Data da B3 informa que dados de fim de dia e históricos a partir de D-1 obtidos através das Plataformas de Market Data B3 podem ser distribuídos sem custo por distribuidores/redistribuidores, sem autorização prévia da B3. **Isto não demonstra, por si só, que essa exceção se aplica aos ficheiros públicos COTAHIST, às tabelas BDI, à API DRP/Rapinegócios, ao armazenamento em repositório GitHub público ou à redistribuição dos ficheiros brutos.** Pedir confirmação expressa.
3. O dataset “Documentos do Copom” no Portal de Dados Abertos do BCB apresenta a licença ODbL para o conjunto/API. Isso suporta o uso do dataset dentro dos termos ODbL; não se deve presumir sem confirmação que todos os PDFs anexos, a sua reprodução integral ou redistribuição isolada têm exatamente o mesmo enquadramento.
4. Não foi localizada uma autorização oficial específica para o endpoint identificado internamente como DRP/Rapinegócios. Solicitar à B3 confirmação do nome oficial, endpoint, finalidade, autenticação, limites e direitos antes de qualquer acesso automatizado.

## 3. Pedido à B3 — COTAHIST, BDI e DRP/Rapinegócios

**Destinatário principal:** produtos-marketdata@b3.com.br  
**CC sugerido:** contratacao@b3.com.br  
**Assunto:** Pedido formal de esclarecimento e autorização — COTAHIST histórico, BDI e endpoint DRP/Rapinegócios — projeto B3

Exmos. Senhores,

Solicito o encaminhamento à área responsável por Market Data, Dados Públicos e licenciamento da B3 de um pedido formal de esclarecimento e, quando necessário, autorização escrita para o projeto técnico de investigação denominado “B3 — A BOLSA DO BRASIL”.

O projeto é mantido no repositório https://github.com/carlos-andrade/B3 e destina-se a investigação quantitativa, análise histórica, validação de dados, desenvolvimento e teste de ferramentas de análise do mercado brasileiro. Antes de ativar novas recolhas automatizadas ou publicar/redistribuir ficheiros, pretendemos confirmar o âmbito de uso permitido.

Solicitamos resposta escrita, separada por produto/fonte, aos seguintes pontos:

**A. COTAHIST**
1. É permitido descarregar e armazenar localmente os ficheiros oficiais COTAHIST anuais e diários para investigação quantitativa interna, consultas históricas, validação de dados e backtests?
2. É permitido automatizar a recolha de ficheiros oficialmente publicados, com frequência limitada e respeito pelos limites técnicos?
3. É permitido guardar ficheiros RAW, hashes SHA-256, manifests e dados normalizados no repositório GitHub público? Se não, é permitido guardar apenas código, metadados, hashes, estatísticas de reconciliação e referências oficiais, mantendo os ficheiros brutos privados?
4. Quais são as condições de atribuição, retenção, redistribuição, utilização comercial e publicação de resultados agregados?
5. A regra da FAQ sobre dados históricos de fim de dia D-1 aplica-se aos ficheiros COTAHIST obtidos diretamente das páginas oficiais, ou apenas a dados distribuídos através das Plataformas de Market Data B3?
6. Existe produto, licença, política ou contrato específico aplicável a este caso? Favor indicar os documentos vigentes, custos e procedimento de contratação, se aplicável.

**B. Boletim Diário do Mercado (BDI)**
1. A consulta manual e o download dos capítulos/tabelas disponibilizados no site são permitidos para investigação interna?
2. A recolha automatizada limitada, o armazenamento de ficheiros e a extração/normalização das tabelas são permitidos? Em que condições?
3. Pode o projeto persistir o ficheiro RAW e os dados normalizados em repositório público, ou deve manter os dados brutos privados e publicar apenas metadados, hashes e resultados derivados?
4. Que termos, atribuições, limites de frequência ou contratos são aplicáveis à tabela DailyAverageStocks e às restantes tabelas do BDI?

**C. DRP/Rapinegócios**
1. Solicitamos confirmação do nome oficial do produto/serviço e do endpoint correto.
2. Existe API oficial documentada, mecanismo de autenticação, limites de utilização e política de acesso automatizado?
3. Que licença ou autorização é necessária para recolha, armazenamento, normalização e uso em investigação/backtests?
4. Existe proibição de automatização ou de redistribuição que deva ser refletida no nosso controlo técnico?

O projeto aplica atualmente uma política de autorização `FAIL_CLOSED`: as fontes permanecem bloqueadas para novas capturas automatizadas enquanto a permissão aplicável não for comprovada. Não pretendemos contornar restrições, reproduzir serviços pagos, redistribuir dados sem licença ou inferir autorização a partir da mera acessibilidade técnica.

Solicito que a resposta identifique o produto, os termos/contrato aplicáveis, o âmbito de utilização, as restrições, a vigência e o canal para formalização. Se este pedido tiver de ser apresentado através de formulário ou processo comercial específico, agradeço o respetivo encaminhamento.

Com os melhores cumprimentos,

Responsável pelo projeto B3 — A BOLSA DO BRASIL

## 4. Pedido ao Banco Central — API Copom e PDFs

**Canal:** https://www3.bcb.gov.br/faleconosco/#/login/registrar?natureza=1&tipo=3  
**Assunto:** Esclarecimento sobre ODbL e uso de PDFs — dataset Documentos do Copom

Prezados,

O projeto técnico “B3 — A BOLSA DO BRASIL” utiliza o conjunto “Documentos do Copom” publicado no Portal de Dados Abertos do Banco Central do Brasil:

https://dadosabertos.bcb.gov.br/dataset/atas-comunicados-copom

A página do conjunto apresenta a licença Open Data Commons Open Database License (ODbL). Pretendemos usar a API/JSON para indexação, reconciliação e análise histórica, com atribuição e cumprimento das obrigações da licença.

Solicitamos esclarecimento sobre o âmbito da licença relativamente a:
1. Consulta automatizada e armazenamento dos registos JSON retornados pela API.
2. Persistência de metadados, datas, identificadores, hashes e dados normalizados.
3. Download e armazenamento local dos PDFs das atas disponibilizados a partir das páginas oficiais.
4. Publicação de cópias integrais dos PDFs ou de conteúdos extraídos num repositório público GitHub.
5. Requisitos de atribuição, partilha sob a mesma licença, avisos de direitos autorais ou outras condições aplicáveis separadamente ao conjunto de dados e aos documentos PDF.

Até obtermos esclarecimento, distinguimos a API/JSON do PDF anexo e não presumimos que a licença apresentada para o dataset resolva automaticamente todos os direitos sobre cada documento.

Solicitamos resposta escrita ou indicação do instrumento oficial que determine as condições de reutilização e redistribuição.

Com os melhores cumprimentos,

Responsável pelo projeto B3 — A BOLSA DO BRASIL

## 5. Estado do processo

| Item | Estado |
|---|---|
| Identificação de canais oficiais B3 | CONCLUÍDO |
| Pesquisa de termos públicos B3 | CONCLUÍDO |
| Preparação de pedido COTAHIST | PREPARADO — ENVIO PENDENTE |
| Preparação de pedido BDI | PREPARADO — ENVIO PENDENTE |
| Preparação de pedido DRP/Rapinegócios | PREPARADO — ENVIO PENDENTE |
| Preparação de pedido BCB para JSON/PDF Copom | PREPARADO — ENVIO PENDENTE |
| Número de protocolo, e-mail enviado ou confirmação recebida | NENHUM REGISTADO |
| Autorização formal concedida ao projeto | NÃO DEMONSTRADA |

## 6. Regras de controlo até resposta

- Manter os gates existentes em `FAIL_CLOSED`.
- Não chamar endpoints proibidos nem tentar caminhos alternativos para contornar restrições.
- Não declarar que qualquer pedido foi enviado até existir mensagem de saída ou protocolo verificável.
- Ao receber resposta, preservar a mensagem original, anexos, data, remetente, escopo autorizado, vigência, condições e SHA-256; atualizar o registo de autorização apenas após revisão.
- Se a B3 autorizar apenas pesquisa interna, manter RAW fora do repositório público e publicar, se permitido, código, hashes e resultados agregados.
- A licença ODbL do dataset Copom deve ser cumprida na API/JSON; o uso dos PDFs será governado pela resposta/termos aplicáveis aos próprios documentos.
- Este documento é registo operacional e não substitui aconselhamento jurídico.

## 7. Fontes oficiais consultadas

- B3 — Termos de Uso: https://www.b3.com.br/pt_br/termos-de-uso-e-protecao-de-dados/termos-de-uso/
- B3 — Política comercial e contratos de Market Data: https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/distribuidores/politica-comercial-e-contratos/
- B3 — FAQ de Market Data: https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/distribuidores/perguntas-frequentes/
- BCB — Documentos do Copom: https://dadosabertos.bcb.gov.br/dataset/atas-comunicados-copom
- BCB — Contacto do Portal de Dados Abertos: https://dadosabertos.bcb.gov.br/pages/contato
