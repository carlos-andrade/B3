# CONTRATO NORMALIZED ANUAL COTAHIST V2.0

**Projeto:** B3 — A Bolsa do Brasil  
**Data:** 2026-09-28  
**Status:** PROPOSTA TÉCNICA — AGUARDANDO IMPLEMENTAÇÃO CONTROLADA  
**Escopo:** COTAHIST anual 1986–2026 e novos anos futuros  
**Dependências:** RAW anual, parser NORMALIZED, manifests de qualidade, certificação anual, Dataset Oficial e dashboards.

## 1. Finalidade

Definir, de forma auditável e fail-closed, o comportamento da camada **NORMALIZED anual**.

O contrato elimina a ambiguidade existente entre:

- CSV NORMALIZED temporário de execução;
- CSV NORMALIZED permanentemente disponível;
- referência a CSV em manifest;
- capacidade de reconstrução a partir do RAW.

## 2. Princípio de autoridade

O RAW anual preservado é a fonte primária.

O NORMALIZED é uma representação determinística do RAW produzida pelo parser versionado.

O manifest deve identificar, no mínimo:

- ano;
- RAW;
- SHA-256 do RAW;
- parser;
- versão do parser;
- arquivo NORMALIZED;
- SHA-256 do NORMALIZED, quando materializado;
- quantidade de registros;
- primeira data;
- última data;
- status da validação;
- política de persistência;
- política de reconstrução.

## 3. Política adotada

**V2.0 adota NORMALIZED anual persistente no repositório para os anos certificados.**

Caminho canônico:

`dados/cotahist/normalized/anual/COTAHIST_A{ANO}.csv`

O CSV anual deixa de ser considerado apenas artefato temporário.

### 3.1 Por que esta política

A decisão privilegia:

1. reprodutibilidade imediata;
2. inspeção direta;
3. independência de retenção do GitHub Actions;
4. compatibilidade com o contrato do Dataset Oficial;
5. auditoria física do objeto de dados;
6. consumo simples por ferramentas e dashboards.

### 3.2 Restrição de infraestrutura

Antes da publicação em massa de 1986–2026, deve ser verificada a capacidade do repositório para arquivos grandes.

Se o tamanho dos arquivos ou os limites operacionais do Git impedirem a estratégia, a implementação deve parar em **fail-closed** e abrir uma revisão arquitetural para armazenamento versionado externo/Git LFS.

Não é permitido substituir a persistência por artefatos temporários sem atualizar este contrato.

## 4. Estado válido de um ano

Um ano pode assumir:

### NORMALIZED_PERSISTIDO

RAW existe + NORMALIZED existe + SHA NORMALIZED corresponde + validação aprovada.

### NORMALIZED_RECONSTRUIVEL

RAW existe + parser existe + manifest permite reconstrução, mas NORMALIZED físico não está disponível.

Este estado é permitido somente durante migração controlada e **não pode ser apresentado como NORMALIZED permanente no Dataset Oficial V2**.

### NORMALIZED_INVALIDO

Arquivo existe, mas falha SHA, schema, parser ou validação.

Deve bloquear publicação.

### NORMALIZED_AUSENTE

RAW existe, mas o NORMALIZED declarado não existe.

Deve bloquear a cadeia oficial quando a política persistente estiver vigente.

## 5. Regra fail-closed

A ausência do CSV nunca pode ser interpretada como:

- zero registros;
- arquivo vazio;
- SHA presumidamente válido;
- dado disponível;
- certificação física concluída.

Exemplo obrigatório:

`Path.exists() == false` → estado AUSENTE → publicação bloqueada.

## 6. Geração

O produtor anual continuará utilizando o parser versionado.

A saída deve ser gravada diretamente no caminho canônico ou produzida em área temporária e copiada para o caminho canônico após validação.

Sequência:

`RAW → NORMALIZED → SHA → validação → persistência → manifest → certificação → Dataset Oficial`

Nenhuma etapa posterior deve ocorrer se a anterior falhar.

## 7. Integridade

Após geração:

1. validar número de campos;
2. validar datas;
3. validar estrutura;
4. validar conteúdo conforme as regras existentes;
5. calcular SHA-256;
6. comparar com SHA esperado quando houver;
7. confirmar existência física do arquivo;
8. registrar tamanho;
9. registrar contagem;
10. atualizar manifest.

## 8. Certificação anual

A certificação anual V2 deve verificar o arquivo NORMALIZED físico.

Não será suficiente validar somente RAW + manifest.

Regra:

`certificação = RAW válido AND NORMALIZED físico válido AND manifest coerente`

A certificação de 1986 mantém sua exceção semântica já documentada, sem apagar a exigência física do NORMALIZED.

## 9. Dataset Oficial

O Dataset Oficial só poderá declarar um ano como disponível quando:

- RAW existir;
- NORMALIZED existir;
- manifest existir;
- SHA estiver coerente;
- certificação estiver aprovada.

O gerador deve verificar fisicamente:

`dados/cotahist/normalized/anual/COTAHIST_A{ANO}.csv`

antes de publicar o catálogo.

## 10. Reconstrução

A reconstrução continuará sendo obrigatória como capacidade de recuperação.

Teste mínimo:

`RAW + parser → NORMALIZED reconstruído → SHA esperado`

A reconstrução não substitui a persistência.

Ela existe para:

- disaster recovery;
- auditoria;
- reprodução histórica;
- recuperação após corrupção;
- validação de integridade.

## 11. Retenção

### Git

NORMALIZED anual certificado: permanente enquanto fizer parte do Dataset Oficial.

### GitHub Actions

Artefatos temporários: auxiliares, não fonte de verdade.

A retenção dos artefatos não pode ser utilizada como garantia de disponibilidade histórica.

## 12. Dashboard

O dashboard não deve inferir disponibilidade apenas do catálogo.

Quando a camada NORMALIZED for exibida como disponível, o pipeline deve ter validado a existência física e o SHA.

Ausência deve aparecer como estado explícito, nunca como zero.

## 13. Migração 1986–2026

A migração será executada em fases:

### Fase M1 — prova

Reconstruir e persistir um único ano representativo.

### Fase M2 — validação

Comparar:

- contagem;
- primeira/última data;
- SHA;
- manifest;
- certificação;
- Dataset Oficial.

### Fase M3 — lote histórico

Processar os anos restantes em lotes controlados.

### Fase M4 — certificação

Executar certificação física de todos os anos.

### Fase M5 — publicação

Atualizar Dataset Oficial somente após a matriz estar coerente.

## 14. Não permitido

É proibido:

- deduplicar registros econômicos sem regra semântica;
- alterar RAW para adequar NORMALIZED;
- escolher uma linha entre colisões K4 sem evidência;
- preencher ausência com zero;
- fabricar SHA;
- declarar arquivo existente apenas porque o manifest o referencia;
- publicar Dataset Oficial com NORMALIZED ausente;
- eliminar exceções históricas para obter uma matriz aparentemente limpa.

## 15. Controle de versões

Este contrato é V2.0.

Alterações de:

- política de persistência;
- localização;
- hash;
- reconstrução;
- retenção;
- critério de certificação

exigem nova versão do contrato e registro no changelog de governança.

## 16. Critério de conclusão

A arquitetura NORMALIZED anual será considerada implantada somente quando:

- 1986–2026 estiverem fisicamente disponíveis, ou houver uma exceção formalmente aprovada;
- cada arquivo tiver SHA;
- manifests forem coerentes;
- certificação verificar o CSV;
- Dataset Oficial validar existência;
- reconstrução de amostra for aprovada;
- workflow automático estiver validado;
- dashboard refletir o estado real.

## 17. Próxima ação

A implementação deve começar pela **Fase M1**, com um único ano representativo.

Nenhum lote de 41 anos deve ser executado antes da aprovação técnica da prova M1.

---

**Regra de integridade:** este contrato define a política. Ele não modifica, por si só, nenhum dado histórico.
