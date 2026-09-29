# Modelo de Governança

## Objetivo

Estabelecer regras para que o projeto B3 permaneça rastreável, reproduzível, auditável e tecnicamente coerente ao longo do tempo.

## Camadas

1. **Fonte** — origem oficial ou identificada do dado.
2. **Aquisição** — registro do processo de obtenção.
3. **RAW** — preservação do conteúdo original.
4. **Normalização** — transformação documentada.
5. **Validação** — testes técnicos e semânticos.
6. **Evidência** — logs, checksums, relatórios e amostras.
7. **Publicação** — disponibilização da versão validada.
8. **Consumo** — pesquisa, análise e backtesting.

## Regras de governança

- Não sobrescrever evidência RAW sem justificativa e versionamento.
- Não promover dado normalizado sem validação.
- Não confundir ausência de erro de execução com validade do dado.
- Registrar mudanças estruturais em commits identificáveis.
- Preservar a relação entre origem, transformação e resultado.
- Documentar bloqueios em vez de mascará-los.

## Controle histórico

O marco inicial de reconstrução histórica é 1986. A progressão para novos períodos deve ocorrer somente após os critérios de validação definidos para a etapa precedente serem satisfeitos.

## Auditoria

Toda conclusão importante deve poder ser rastreada até arquivos, logs, testes ou fontes que permitam sua verificação independente.
