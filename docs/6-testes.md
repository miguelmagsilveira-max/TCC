# 6. Documento de Testes

Sistema **Stock Flow** — Sistema de Gestão de Ativos de TI

Este documento apresenta o plano de testes, os casos de teste executados e a respectiva conclusão sobre a qualidade do sistema Stock Flow.

---

## 6.1. Plano de testes

O objetivo dos testes é verificar se o sistema atende aos requisitos funcionais e às regras de negócio definidos, garantindo o correto funcionamento das principais operações.

- **Tipo de teste:** funcional (caixa-preta), conduzido manualmente sobre a interface do sistema.
- **Ambiente de teste:** aplicação em produção (Railway), acessada via navegador.
- **Critério de aprovação:** o resultado obtido deve coincidir com o resultado esperado.
- **Critério de reprovação:** divergência entre o resultado obtido e o esperado.
- **Abrangência:** autenticação, controle de acesso, gestão de ativos, gestão de colaboradores, alertas, relatórios, Curva ABC, SmartSelect e preferências de interface.

---

## 6.2. Casos de teste

### CT01 — Login com credenciais válidas
- **Pré-condição:** Usuário cadastrado.
- **Passos:** 1. Acessar a tela de login. 2. Informar e-mail e senha válidos. 3. Clicar em Entrar.
- **Resultado esperado:** Acesso concedido e redirecionamento ao dashboard.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT02 — Login com credenciais inválidas
- **Pré-condição:** Nenhuma.
- **Passos:** 1. Informar e-mail ou senha incorretos. 2. Clicar em Entrar.
- **Resultado esperado:** Exibição de mensagem de erro; acesso negado.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT03 — Bloqueio de acesso de operador a funções administrativas
- **Pré-condição:** Usuário operador autenticado.
- **Passos:** 1. Tentar acessar a área de gerenciamento de usuários.
- **Resultado esperado:** Acesso negado (página de erro 403).
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT04 — Cadastro de ativo
- **Pré-condição:** Administrador autenticado.
- **Passos:** 1. Acessar Ativos > Novo ativo. 2. Preencher os dados. 3. Salvar.
- **Resultado esperado:** Ativo cadastrado com situação "Em estoque".
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT05 — Geração automática de código do ativo
- **Pré-condição:** Cadastro de ativo em andamento.
- **Passos:** 1. Cadastrar um novo ativo.
- **Resultado esperado:** Código gerado no padrão AST-NNN, sequencial e único.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT06 — Edição de ativo
- **Pré-condição:** Ativo existente.
- **Passos:** 1. Selecionar ativo. 2. Editar dados. 3. Salvar.
- **Resultado esperado:** Dados atualizados; código inalterado.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT07 — Vinculação de ativo a colaborador
- **Pré-condição:** Ativo disponível e colaborador cadastrado.
- **Passos:** 1. Selecionar ativo. 2. Vincular a um colaborador. 3. Confirmar.
- **Resultado esperado:** Situação alterada para "Em uso" e vínculo registrado.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT08 — Impedimento de vinculação de ativo em manutenção
- **Pré-condição:** Ativo com situação "Manutenção".
- **Passos:** 1. Tentar vincular o ativo a um colaborador.
- **Resultado esperado:** Vinculação não permitida.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT09 — Desvinculação de ativo
- **Pré-condição:** Ativo vinculado a um colaborador.
- **Passos:** 1. Selecionar ativo. 2. Desvincular. 3. Confirmar.
- **Resultado esperado:** Situação alterada para "Em estoque"; vínculo removido.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT10 — Envio de ativo para manutenção
- **Pré-condição:** Ativo não desativado.
- **Passos:** 1. Selecionar ativo. 2. Enviar para manutenção. 3. Confirmar.
- **Resultado esperado:** Situação alterada para "Manutenção".
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT11 — Retorno de ativo da manutenção
- **Pré-condição:** Ativo em manutenção.
- **Passos:** 1. Selecionar ativo. 2. Retornar ao estoque. 3. Confirmar.
- **Resultado esperado:** Situação alterada para "Em estoque".
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT12 — Desativação de ativo
- **Pré-condição:** Ativo existente.
- **Passos:** 1. Selecionar ativo. 2. Desativar.
- **Resultado esperado:** Ativo deixa de aparecer no inventário ativo.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT13 — Registro de histórico de movimentações
- **Pré-condição:** Ativo com operações realizadas.
- **Passos:** 1. Acessar o detalhamento do ativo.
- **Resultado esperado:** Todas as movimentações exibidas em ordem cronológica.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT14 — Cadastro de colaborador
- **Pré-condição:** Administrador autenticado.
- **Passos:** 1. Acessar Colaboradores > Novo. 2. Preencher dados. 3. Salvar.
- **Resultado esperado:** Colaborador cadastrado com status "ativo".
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT15 — Exibição de indicadores no dashboard
- **Pré-condição:** Usuário autenticado.
- **Passos:** 1. Acessar o dashboard.
- **Resultado esperado:** Indicadores e gráficos exibidos com dados corretos.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT16 — Alerta de estoque abaixo do mínimo
- **Pré-condição:** Tipo de ativo com quantidade inferior ao mínimo.
- **Passos:** 1. Acessar a área de alertas.
- **Resultado esperado:** Alerta de estoque baixo exibido.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT17 — Alerta de garantia a vencer
- **Pré-condição:** Ativo com garantia vencendo em até 30 dias.
- **Passos:** 1. Acessar a área de alertas.
- **Resultado esperado:** Alerta de garantia a vencer exibido.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT18 — Geração de relatório em PDF
- **Pré-condição:** Usuário autenticado.
- **Passos:** 1. Acessar Relatórios. 2. Exportar PDF.
- **Resultado esperado:** Arquivo PDF gerado e disponibilizado para download.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT19 — Cálculo da Curva ABC
- **Pré-condição:** Ativos com valores cadastrados.
- **Passos:** 1. Acessar a análise de inventário.
- **Resultado esperado:** Itens classificados nas categorias A, B e C.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT20 — Adição de opção via SmartSelect
- **Pré-condição:** Administrador em um formulário com SmartSelect.
- **Passos:** 1. Digitar novo valor. 2. Clicar em adicionar.
- **Resultado esperado:** Opção adicionada e disponível imediatamente.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT21 — Remoção de opção via SmartSelect
- **Pré-condição:** Opção previamente cadastrada.
- **Passos:** 1. Selecionar a opção. 2. Removê-la.
- **Resultado esperado:** Opção removida da lista.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT22 — Alternância de tema claro/escuro
- **Pré-condição:** Usuário autenticado.
- **Passos:** 1. Acionar o seletor de tema. 2. Recarregar a página.
- **Resultado esperado:** Tema alternado e preferência mantida após recarregar.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT23 — Expiração de sessão (JWT)
- **Pré-condição:** Usuário autenticado.
- **Passos:** 1. Aguardar a expiração do token (24h) ou efetuar logout.
- **Resultado esperado:** Acesso a páginas protegidas exige novo login.
- **Resultado obtido:** Aprovado.
- **Observações:** —

### CT24 — Acesso a recurso inexistente
- **Pré-condição:** Nenhuma.
- **Passos:** 1. Acessar uma URL inexistente.
- **Resultado esperado:** Exibição de página de erro 404 personalizada.
- **Resultado obtido:** Aprovado.
- **Observações:** —

---

## 6.3. Tabela resumo dos testes

| ID | Funcionalidade | Resultado |
|----|----------------|-----------|
| CT01 | Login válido | Aprovado |
| CT02 | Login inválido | Aprovado |
| CT03 | Bloqueio de operador | Aprovado |
| CT04 | Cadastro de ativo | Aprovado |
| CT05 | Geração de código | Aprovado |
| CT06 | Edição de ativo | Aprovado |
| CT07 | Vinculação | Aprovado |
| CT08 | Bloqueio de vinculação em manutenção | Aprovado |
| CT09 | Desvinculação | Aprovado |
| CT10 | Envio para manutenção | Aprovado |
| CT11 | Retorno da manutenção | Aprovado |
| CT12 | Desativação | Aprovado |
| CT13 | Histórico | Aprovado |
| CT14 | Cadastro de colaborador | Aprovado |
| CT15 | Dashboard | Aprovado |
| CT16 | Alerta de estoque | Aprovado |
| CT17 | Alerta de garantia | Aprovado |
| CT18 | Relatório PDF | Aprovado |
| CT19 | Curva ABC | Aprovado |
| CT20 | SmartSelect — adição | Aprovado |
| CT21 | SmartSelect — remoção | Aprovado |
| CT22 | Tema claro/escuro | Aprovado |
| CT23 | Expiração de sessão | Aprovado |
| CT24 | Erro 404 | Aprovado |

**Total:** 24 casos de teste — 24 aprovados (100%).

---

## 6.4. Conclusão dos testes

Os 24 casos de teste executados cobrem as principais funcionalidades e regras de negócio do sistema Stock Flow, incluindo autenticação, controle de acesso por nível de usuário, gestão completa do ciclo de vida dos ativos, alertas, relatórios e recursos de interface. Todos os casos foram **aprovados**, demonstrando que o sistema atende aos requisitos especificados e está apto para utilização. Recomenda-se a continuidade dos testes a cada nova funcionalidade incorporada, mantendo a cobertura e a confiabilidade do sistema.
