# Publicação automática da Wiki nativa

## Arquitetura

A documentação versionada em `WIKI/` é a fonte de verdade.

O workflow detecta alterações relevantes, executa reconciliação periódica e publica os documentos selecionados no Wiki nativo, que é um repositório Git separado.

O GitHub documenta que cada Wiki pode ser clonado e atualizado por Git. citeturn0search10turn0search12

## Frequência

O GitHub Actions permite agendamento mínimo de **5 minutos**, e execuções agendadas podem sofrer atraso sob alta carga. citeturn0search0turn0search6

Portanto:

- **evento `push`**: publicação imediatamente após alteração relevante;
- **`schedule` a cada 5 minutos**: reconciliação contra deriva;
- **`workflow_dispatch`**: publicação manual.

Não usamos polling de 1 minuto porque a plataforma não oferece esse intervalo por `schedule`.

## Segredo necessário

O workflow espera o segredo:

`B3_WIKI_TOKEN`

Esse segredo precisa ser uma credencial autorizada a fazer push no repositório da Wiki. O conector utilizado neste projeto não expõe gerenciamento de Secrets do GitHub; portanto, essa configuração precisa ser feita no GitHub.

## Regra de governança

O fluxo oficial é:

`WIKI/ → GitHub Actions → B3.wiki.git → https://github.com/carlos-andrade/B3/wiki`

A Wiki nativa é uma camada de publicação. A documentação auditável permanece no repositório principal.
