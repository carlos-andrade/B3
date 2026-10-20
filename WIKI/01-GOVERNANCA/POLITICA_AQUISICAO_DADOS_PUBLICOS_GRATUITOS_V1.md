# Política de aquisição de dados públicos e gratuitos — B3

| Campo | Valor |
|---|---|
| **ID** | B3-POL-DADOS-PUBLICOS-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | POLITICA_OPERACIONAL |
| **Fase** | Governança de dados e ingestão |
| **Estado** | PROPOSTA_OPERACIONAL — sujeita à hierarquia normativa do projeto |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | c8c07d2d4bff5e8c9b4a6e0e57aed7ce448ab7666314b3bf93cea61595e3a7c9 | 
| **Commit de referência (versão anterior)** | N/A — criação inicial em 2026-10-20 |
| **Data de atualização** | 2026-10-20 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Proprietário do projeto, conforme governança aplicável |
| **Autoridade superior** | [GOVERNANCA — governança de dados](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/05-dados-e-ia/governanca-de-dados.md) |
| **Escopo** | Dados e metadados gratuitos disponibilizados publicamente por fontes oficiais ou outras fontes públicas identificadas |

## 1. Regra do projeto

O projeto B3 deve identificar, obter e preservar de forma sistemática os dados e metadados que estejam **gratuitamente disponíveis ao público em fontes públicas**, priorizando fontes primárias e oficiais. A finalidade é construir uma base abrangente, rastreável, reproduzível e atualizável para pesquisa quantitativa, análise de mercado e engenharia de dados.

A regra é **procurar e capturar o que estiver publicamente disponível e gratuito**, não presumir que a simples acessibilidade de uma página autoriza qualquer método de recolha ou qualquer forma de redistribuição.

## 2. Ordem de preferência das fontes

1. APIs, endpoints de dados, arquivos para download e feeds oficiais explicitamente disponibilizados.
2. Portais oficiais de dados abertos, catálogos e repositórios públicos.
3. Documentação técnica oficial, layouts, calendários, metadados e tabelas de referência.
4. Fontes secundárias públicas, quando a fonte primária não existir ou não cobrir a necessidade; a limitação deve ser documentada.

Não descartar uma fonte apenas porque uma primeira chamada falhou. Diagnosticar o erro, testar alternativas oficiais documentadas, distinguir falha transitória de mudança de contrato e registrar evidência.

## 3. Restrições objetivas e proporcionais

A aquisição só deve ser bloqueada ou limitada quando houver motivo concreto e documentado, por exemplo:

- autenticação, credencial, pagamento ou licença específica necessários e não disponíveis;
- termos aplicáveis que proíbam o método de recolha pretendido;
- restrição legal, contratual, de copyright, redistribuição ou proteção de dados;
- controle de acesso, CAPTCHA ou medida técnica que não deva ser contornada;
- risco operacional desproporcional, indisponibilidade persistente ou impacto indevido no serviço de origem.

Uma mensagem de erro HTTP, uma dúvida não investigada ou a mera ausência de uma rotina de ingestão não bastam para classificar todo um conjunto de dados como inacessível. Deve-se registrar o bloqueio específico, a evidência, a alternativa investigada, o responsável e a condição de reavaliação.

**Não contornar** autenticação, CAPTCHA, limites de acesso ou proibições explícitas. Quando um portal proibir coleta automatizada naquela interface, procurar um canal oficial próprio para download/API, uma licença aplicável ou autorização do fornecedor. Não transferir automaticamente a proibição de uma interface para todos os canais do fornecedor, nem presumir que outro endpoint está autorizado sem verificar os termos que o regem.

## 4. Pipeline obrigatório

Para cada fonte/dataset:

1. **Descoberta:** URL oficial, entidade publicadora, descrição, cobertura e periodicidade.
2. **Avaliação de acesso:** gratuito/pago, método permitido, termos/licença e restrições explícitas.
3. **Captura:** preferir API/download/feed oficial; respeitar limites publicados e usar retries controlados.
4. **RAW imutável:** preservar bytes originais quando permitido, data/hora UTC, URL/canal, parâmetros não secretos, status HTTP, cabeçalhos relevantes, tamanho e SHA-256.
5. **Manifesto:** formato, período de referência, quantidade de registros quando aplicável, checksum, versão do importador e estado de acesso.
6. **Validação:** estrutura, esquema/layout, encoding, datas, duplicidades, cobertura, integridade e reconciliação.
7. **Normalização/publicação:** separar RAW, normalizado e certificado; não promover dados não validados a certificados.
8. **Atualização:** definir frequência compatível com a fonte e detectar mudanças de esquema, desaparecimento ou obsolescência.
9. **Auditoria:** guardar logs, decisões, falhas e correções; nunca reescrever o histórico de incidentes para ocultar falhas.

Segredos, cookies de sessão, tokens e credenciais não podem ser publicados no repositório.

## 5. Estados padronizados

- `PUBLICO_GRATUITO_A_CONFIRMAR`: acesso observado; custo/licença/método ainda não documentados.
- `ACESSO_PUBLICO_CONFIRMADO`: canal e condições de aquisição documentados.
- `CAPTURA_OPERACIONAL`: captura concluída e evidenciada, sem implicar certificação dos dados.
- `VALIDADO`: verificações de qualidade definidas passaram.
- `CERTIFICADO`: satisfeitos os critérios formais do domínio.
- `BLOQUEADO_RESTRICAO_DOCUMENTADA`: existe restrição específica, com evidência e alternativa analisada.
- `INDISPONIVEL_TEMPORARIO`: falha transitória confirmada; requer nova tentativa conforme política.
- `DESCONTINUADO`: fonte retirou formalmente o produto/canal ou o substituiu.

Não usar `BLOQUEADO` genérico quando a restrição só afeta um método, uma página ou um período. Separar sempre **disponibilidade técnica**, **permissão de aquisição automatizada**, **permissão de uso/redistribuição** e **qualidade/certificação**.

## 6. Caso BVBG.028.02 / InstrumentsConsolidated

A existência do catálogo público da B3 e a execução bem-sucedida do importador são evidências de disponibilidade e funcionamento técnico do canal testado, mas não substituem a documentação dos termos aplicáveis à automatização e à redistribuição.

A página oficial “Pesquisa por pregão” contém aviso contra coleta automatizada naquela página. Portanto:

- não classificar o catálogo como tecnicamente bloqueado com base apenas em uma execução HTTP 400 já superada;
- não usar essa página como alvo de raspagem automatizada;
- verificar e registar as condições aplicáveis ao endpoint/download específico `arquivos.b3.com.br/api/download/requestname` e ao produto BVBG.028.02;
- preferir o canal oficial de download/API destinado a esse arquivo;
- manter a captura, o manifesto, o checksum e as validações separados da decisão sobre redistribuição;
- se os termos do canal específico forem ambíguos, abrir uma pendência documental delimitada, sem converter a dúvida em bloqueio técnico geral.

Referências iniciais:
- B3 — Pesquisa por pregão: https://b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/
- B3 — Dados disponíveis / UP2Data: https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/up2data/dados-disponiveis/

## 7. Critérios de auditoria

Uma fonte só pode ser declarada operacionalmente incorporada quando houver evidência verificável de: fonte identificada, método de acesso, execução, artefacto persistido, manifesto/checksum, validação e estado de atualização. Uma captura bem-sucedida não prova, por si só, a exatidão do conteúdo nem autoriza redistribuição irrestrita.

## 8. Roadmap de adoção

1. Inventariar fontes públicas gratuitas por domínio (mercado, instrumentos, índices, futuros, juros, câmbio, calendário, macroeconomia e dados institucionais).
2. Para cada fonte, registar URL, produto, periodicidade, formato, licença/termos, método permitido e estado.
3. Implementar captura priorizando canais oficiais de download/API.
4. Acrescentar RAW + manifesto + SHA-256 + validação automatizada.
5. Corrigir bloqueios genéricos para estados específicos, preservando histórico de incidentes.
6. Verificar cobertura, atualidade, duplicidade e qualidade do inventário.
7. Atualizar o roadmap global apenas com evidências dos passos executados.

**Regra de fecho:** a política é maximizar a cobertura de dados públicos gratuitos, com bloqueios específicos, proporcionais, documentados e reavaliáveis — nunca inventar uma restrição, e nunca ignorar uma restrição explícita.
