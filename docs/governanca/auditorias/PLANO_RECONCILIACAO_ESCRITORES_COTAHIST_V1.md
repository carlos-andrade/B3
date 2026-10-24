# Plano de reconciliacao dos escritores COTAHIST

- Estado: PROPOSTA PARA REVISAO; nao constitui aprovacao nem prova de conclusao.
- Escopo: classificar os workflows, identificar branches, paths, referencias a credenciais e concorrencia.
- Categorias: escritor efetivo; escritor condicional; validador; falso positivo.
- Protecao: nao alterar dados canonicos nem desativar gates durante o inventario.
- Propriedade: o publicador central e candidato a proprietario da certificacao anual e dos datasets V1/V2; outros recursos exigem atribuicao especifica validada.
- Concorrencia: grupos devem ser definidos por recurso partilhado/operacao, com cancel-in-progress false para transacoes que nao podem ser interrompidas.
- Conflitos Git: refetch/reset/recompute/retry; nunca forcar push para main.
- Segredos: inventariar apenas nomes de referencias, nunca valores.
- Testes: executar inventario em workspace temporario, sem permissao de escrita no repositorio, e guardar JSON/Markdown como artefactos de CI.
- Aceitacao: inventario reconciliado com main, conflitos de escrita tratados, testes aprovados e revisao independente.
- Limitacao atual: os numeros anteriores (527 sinais estaticos, 65 sem grupo, 11 paths partilhados) sao indicativos e devem ser recalculados pelo inventario atualizado.
