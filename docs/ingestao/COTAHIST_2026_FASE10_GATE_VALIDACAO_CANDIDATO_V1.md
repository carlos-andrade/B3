# COTAHIST 2026 — FASE09/10: atualização da fonte e gate de promoção

**Projeto:** B3 — A Bolsa do Brasil  
**Data da auditoria:** 2026-10-14  
**Estado:** CANDIDATO ESTRUTURALMENTE VALIDADO; PROMOÇÃO CANÓNICA PENDENTE  
**Fonte oficial consultada:** https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2026.ZIP

## 1. Resultado verificado

O relatório persistido em `dados/cotahist/quality/COTAHIST_2026_FONTE_OFICIAL_REFRESH_PROBE_V1.json` identifica o estado `CANDIDATO_MAIS_RECENTE_VALIDADO_ESTRUTURALMENTE` e recomenda `REPROCESSAR_NORMALIZED_E_REEXECUTAR_FASES_04_08`.

| Verificação | Resultado |
|---|---:|
| SHA-256 do candidato | `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e` |
| Tamanho do ZIP | 85.075.031 bytes |
| Teste CRC/ZIP | OK |
| Membro ZIP | `COTAHIST_A2026.TXT` |
| Tipos 00 / 01 / 99 | 1 / 3.142.910 / 1 |
| Registos com comprimento diferente de 245 bytes | 0 |
| Data de geração do cabeçalho | 2026-10-13 |
| Primeira / última data de negociação | 2026-01-02 / 2026-10-13 |
| SHA-256 do RAW atualmente canónico | `4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768` |
| Última data do NORMALIZED atualmente canónico | 2026-09-23 |
| Alteração do dataset canónico pelo probe | Não |

## 2. Interpretação

A fonte candidata é mais recente e passou nas verificações estruturais executadas. Isso **não equivale** a uma reconciliação semântica dos 25 campos e não autoriza a substituição imediata do RAW, do NORMALIZED ou dos manifestos oficiais.

O probe é read-only quanto aos dados canónicos. A evidência técnica não declara o candidato como dataset oficial.

## 3. Gate obrigatório para promoção

1. Descarregar novamente a fonte oficial numa execução controlada e confirmar o SHA-256.
2. Executar `scripts/ingestao/normalize_cotahist.py` sobre o candidato, em área temporária.
3. Confirmar cabeçalho e ordem dos 25 campos; comparar cada registo tipo 01 do candidato com a linha NORMALIZED correspondente, em streaming e sem deduplicação.
4. Comparar o candidato com o NORMALIZED canónico anterior, identificando adições, alterações e ausências sem remover nem reordenar registos silenciosamente.
5. Gerar manifestos e checksums candidatos isolados.
6. Persistir evidência de reconciliação e auditar a diferença antes de promover os ficheiros canónicos.
7. Após promoção aprovada, executar novamente FASE04, FASE05, FASE06, FASE07, FASE08 e o gate 06–08. Não reutilizar evidências anteriores como se certificassem o novo hash.
8. Reabrir a FASE09 somente quando as evidências novas forem coerentes e o último pregão estiver confirmado.

## 4. Regras de integridade

- Não deduplicar.
- Não reordenar a sequência física da fonte.
- Não sobrescrever dados canónicos antes de passar todos os gates.
- Preservar o histórico através do versionamento do repositório.
- Se houver divergência semântica, falhar fechado e investigar.
- Não declarar promoção, atualização ou certificação enquanto a evidência não demonstrar esses estados.

## 5. Próximo passo operacional

Implementar um workflow de validação do candidato que normalize e reconcilie os 25 campos em área temporária, produza relatório versionado e mantenha o dataset canónico intacto. A promoção será uma etapa separada, condicionada à aprovação da reconciliação.

## 6. Referências internas

- [Relatório do probe da fonte oficial](../../dados/cotahist/quality/COTAHIST_2026_FONTE_OFICIAL_REFRESH_PROBE_V1.json)
- [Workflow do probe](../../.github/workflows/cotahist-refresh-probe-2026-v1.yml)
- [Contrato NORMALIZED anual V2.0](CONTRATO_NORMALIZED_ANUAL_COTAHIST_V2.0.md)
- [Auditoria de atualidade FASE09](COTAHIST_2026_FASE09_AUDITORIA_ATUALIDADE_CALENDARIO_V1.md)
