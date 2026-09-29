# Incidente de publicação — Wiki nativa — 2026-09-29

## Estado

- Repositório: `carlos-andrade/B3`
- Workflow: `Sincronizar WIKI nativa`
- Run: `36592504062`
- Job: `publicar`
- Job ID: `109499288664`
- Resultado: `failure`
- Etapa da falha: `Verificar segredo da Wiki`
- Etapas seguintes: não executadas
- Fonte de verdade: `WIKI/`

## Evidência operacional

Após a configuração informada do segredo `B3_WIKI_TOKEN`, o job foi reexecutado. A execução continuou falhando na etapa que testa:

```
if [ -z "$WIKI_TOKEN" ]; then
  echo "::error::O segredo B3_WIKI_TOKEN não está configurado."
  exit 1
fi
```

Nesta execução, o GitHub Actions não disponibilizou um valor não vazio para `secrets.B3_WIKI_TOKEN`.

## Diagnóstico

Verificar no GitHub:

1. se o segredo está em **Settings → Secrets and variables → Actions → Repository secrets**;
2. se o nome é exatamente `B3_WIKI_TOKEN`;
3. se o segredo contém um token válido;
4. se o token possui autorização para escrever no repositório separado da Wiki: `carlos-andrade/B3.wiki`.

O valor do token nunca deve ser registrado no repositório ou enviado no chat.

## Arquitetura

O workflow publica em:

`https://github.com/carlos-andrade/B3.wiki.git`

A Wiki nativa é um repositório Git separado do repositório principal. A autorização do token precisa contemplar esse destino.

## Critério de encerramento

O incidente será encerrado somente quando uma execução:

- passar por **Verificar segredo da Wiki**;
- executar **Preparar conteúdo da Wiki**;
- executar **Publicar no Wiki nativo**;
- terminar com `success`;
- e permitir confirmar o commit dos arquivos na Wiki nativa.

## Histórico

- Execução anterior: falha por ausência de `B3_WIKI_TOKEN`.
- Após configuração informada pelo usuário: nova execução ainda falhou na mesma etapa.
- Nenhuma publicação na Wiki nativa foi considerada concluída sem evidência do commit no repositório `.wiki.git`.

## Segurança

Não armazenar tokens, PATs, valores de secrets ou credenciais neste repositório. Registrar somente metadados operacionais e evidências não sensíveis.
