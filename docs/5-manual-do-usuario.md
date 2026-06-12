# 5. Manual do Usuário

Sistema **Stock Flow** — Sistema de Gestão de Ativos de TI

Este manual orienta a utilização do sistema Stock Flow, descrevendo, passo a passo, as principais funcionalidades disponíveis aos usuários.

---

## 5.1. Acesso ao sistema

O sistema está disponível no endereço:

> **https://tcc-production-99b7.up.railway.app**

Basta abrir o endereço em um navegador web atualizado (Chrome, Firefox ou Edge). Não é necessária instalação de programas adicionais.

---

## 5.2. Tela de login

A primeira tela apresentada é a de login. Nela, o usuário deve:

1. Informar o **e-mail** cadastrado;
2. Informar a **senha**;
3. Clicar em **Entrar**.

Em caso de credenciais inválidas, o sistema exibe uma mensagem de erro e mantém o usuário na tela de login. Após o acesso bem-sucedido, a sessão é mantida por meio de um token seguro, válido por 24 horas.

---

## 5.3. Dashboard

Após o login, o usuário é direcionado ao **dashboard**, que apresenta indicadores em tempo real. Os principais indicadores são:

| Indicador | Significado |
|-----------|-------------|
| Total de ativos | Quantidade de ativos cadastrados no inventário ativo. |
| Ativos em uso | Ativos atualmente vinculados a colaboradores. |
| Ativos em estoque | Ativos disponíveis, sem vinculação. |
| Ativos em manutenção | Ativos enviados para reparo. |
| Alertas de estoque | Tipos de ativo com quantidade abaixo do mínimo. |
| Garantias a vencer | Ativos com garantia expirando nos próximos 30 dias. |

O dashboard também exibe gráficos que sintetizam a distribuição dos ativos por situação e por tipo.

---

## 5.4. Cadastro de um ativo (passo a passo)

> Funcionalidade disponível apenas para **administradores**.

1. No menu, acesse **Ativos**.
2. Clique em **Novo ativo**.
3. Preencha os campos do formulário (nome, marca, modelo, tipo, número de série, preço, datas de aquisição e garantia, fornecedor, localização etc.).
4. Clique em **Salvar**.
5. O sistema gera automaticamente o código do ativo (por exemplo, **AST-008**) e o registra com situação **Em estoque**.

---

## 5.5. Vinculação de um ativo a um colaborador

1. Acesse **Ativos** e selecione o ativo desejado.
2. Clique em **Vincular**.
3. Selecione o colaborador que receberá o ativo.
4. Confirme a operação.

O ativo passa para a situação **Em uso**, a data de vinculação é registrada e o evento é gravado no histórico do ativo.

> Observação: ativos em **Manutenção** não podem ser vinculados.

---

## 5.6. Envio para manutenção e retorno

**Enviar para manutenção:**
1. Selecione o ativo desejado.
2. Clique em **Enviar para manutenção**.
3. Informe os detalhes (motivo do reparo) e confirme.

O ativo passa para a situação **Manutenção**.

**Retornar da manutenção:**
1. Selecione o ativo em manutenção.
2. Clique em **Retornar ao estoque**.
3. Confirme a operação.

O ativo retorna à situação **Em estoque**. Ambas as operações são registradas no histórico.

---

## 5.7. Cadastro de um colaborador

> Funcionalidade disponível apenas para **administradores**.

1. No menu, acesse **Colaboradores**.
2. Clique em **Novo colaborador**.
3. Preencha nome, e-mail, cargo e departamento.
4. Clique em **Salvar**.

O colaborador é cadastrado com status **ativo** e passa a estar disponível para vinculação de ativos.

---

## 5.8. Relatórios e exportação em PDF

1. No menu, acesse **Relatórios**.
2. Visualize as informações apresentadas na tela.
3. Clique em **Exportar PDF**.
4. O arquivo será gerado e disponibilizado para download.

---

## 5.9. Interpretação da Curva ABC

A **Curva ABC** classifica os ativos conforme sua relevância financeira no inventário:

| Classe | Critério | Interpretação |
|--------|----------|---------------|
| **A** | Itens que representam até 80% do valor acumulado | Itens de maior valor; merecem maior controle. |
| **B** | Itens entre 80% e 95% do valor acumulado | Itens de valor intermediário. |
| **C** | Itens que representam os 5% finais | Itens de menor valor relativo. |

Essa análise auxilia na priorização da gestão dos ativos de maior impacto financeiro.

---

## 5.10. Utilização do SmartSelect

O **SmartSelect** é um componente de seleção dinâmica presente em diversos formulários (tipo de ativo, cargo, departamento, localização, tipo de aquisição). Com ele é possível:

- **Adicionar uma opção:** digite o novo valor no campo e clique no botão de adição (+). A opção passa a ficar disponível imediatamente.
- **Remover uma opção:** selecione a opção e utilize o botão de remoção.

As alterações são salvas automaticamente e refletem em todos os formulários que utilizam aquele campo.

---

## 5.11. Alternância entre tema claro e escuro

No topo da interface há um seletor de tema. Ao acioná-lo, a aparência do sistema alterna entre o **modo claro** e o **modo escuro**. A preferência escolhida é salva no navegador e mantida nos acessos seguintes.

---

## 5.12. Níveis de acesso

| Ação | Administrador | Operador |
|------|:-------------:|:--------:|
| Acessar dashboard | ✔ | ✔ |
| Visualizar ativos e colaboradores | ✔ | ✔ |
| Consultar histórico e alertas | ✔ | ✔ |
| Gerar relatórios e Curva ABC | ✔ | ✔ |
| Cadastrar/editar/desativar ativos | ✔ | ✗ |
| Cadastrar/editar colaboradores | ✔ | ✗ |
| Vincular/desvincular e manutenção | ✔ | ✗ |
| Gerenciar usuários do sistema | ✔ | ✗ |
| Gerenciar opções do SmartSelect | ✔ | ✗ |

> O operador possui acesso somente de leitura às informações cadastrais; não pode realizar alterações.

---

## 5.13. Perguntas frequentes (FAQ)

**1. Esqueci minha senha. O que fazer?**
Entre em contato com um administrador do sistema, que poderá redefinir o acesso.

**2. Por que não consigo cadastrar ou editar ativos?**
Provavelmente seu usuário possui nível **operador**, que tem acesso somente de leitura. Solicite a um administrador as permissões necessárias.

**3. O código do ativo pode ser alterado?**
Não. O código é gerado automaticamente pelo sistema e não pode ser modificado, garantindo a unicidade dos registros.

**4. Posso vincular um ativo que está em manutenção?**
Não. É necessário primeiro retornar o ativo da manutenção para o estoque e, em seguida, realizar a vinculação.

**5. Como sei que um item está com estoque baixo?**
O sistema emite alertas automáticos quando a quantidade de um tipo de ativo fica abaixo do mínimo configurado. Esses alertas aparecem no dashboard e na área de alertas.

**6. O tema escuro fica salvo após eu sair do sistema?**
Sim. A preferência de tema é armazenada no navegador e mantida nos próximos acessos a partir do mesmo dispositivo.
