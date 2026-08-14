# Guia de Estudo — Caio

### 🎨 Sua parte: **Telas principais e experiência do usuário (UX)** — login, dashboard e navegação

Você faz o "passeio" pelo sistema. Sua missão é mostrar as **telas principais** e explicar como o usuário **navega e entende** o Stock Flow com facilidade. Dica: **abra o sistema ao vivo** e vá clicando enquanto fala.

---

## 1. Sua parte em uma frase

> "As telas do Stock Flow foram desenhadas para serem intuitivas: o usuário loga, cai num painel que resume tudo em segundos, e navega por um menu sempre visível."

---

## 2. Explicação de verdade (para você entender)

### O que é UX?
**UX** (do inglês *User Experience*, "experiência do usuário") é cuidar de como a pessoa **se sente usando** o sistema: se ela acha as coisas rápido, se entende o que está vendo, se não se perde. Um sistema pode ser poderoso, mas se for confuso, ninguém usa.

### Tela 1 — Login
É a porta de entrada. Simples de propósito: só **e-mail, senha e o botão Entrar**. Se errar a senha, aparece uma **mensagem clara** de erro (não deixa o usuário no escuro). Menos é mais: nada distrai do objetivo.

### Tela 2 — Dashboard (o painel principal)
Depois de logar, o usuário cai no **dashboard**, que é um **resumo visual** do sistema. A ideia é responder "como estão as coisas?" em **5 segundos**. Ele mostra:
- **Cartões com números** (os "KPIs"): total de ativos, em uso, em estoque, em manutenção, valor total do inventário.
- **Gráficos**: um de **barras** (ativos por tipo) e um de **rosca/pizza** (ativos por situação) — feitos com uma ferramenta chamada **Chart.js**.
- **Últimas movimentações**: as ações mais recentes.

Números "secos" cansam; **gráficos** contam a história de um jeito que o olho entende na hora.

### Tela 3 — Navegação (o menu lateral)
À esquerda tem uma **barra de menu fixa** com os atalhos: Dashboard, Ativos, Colaboradores, Relatórios, Alertas. Ela fica **sempre visível**, então o usuário nunca se perde. Dois detalhes de UX:
- O item da página atual fica **destacado** — o usuário sabe onde está.
- Em "Alertas" aparece uma **bolinha vermelha com número** quando há avisos pendentes (como as notificações do celular).

### Responsividade
O layout é **responsivo**: ele se **adapta ao tamanho da tela** — funciona tanto no computador quanto no celular. Isso é possível porque o Tailwind ajusta os elementos conforme o espaço disponível.

---

## 3. Por que fizemos assim (decisões que impressionam)

- **Por que um dashboard logo na entrada?** Para dar uma **visão geral instantânea** — o gestor vê o essencial sem procurar.
- **Por que gráficos?** Porque comunicam **tendências e proporções** muito mais rápido que uma tabela de números.
- **Por que o menu fixo e com destaque?** Para o usuário **sempre saber onde está** e ter tudo a um clique — reduz a "carga mental".
- **Por que a bolinha de alertas?** Um padrão que todo mundo já conhece do celular — chama atenção sem atrapalhar.

---

## 4. Glossário (fale com naturalidade)

| Termo | Tradução simples |
|-------|------------------|
| **UX** | Experiência do usuário — como é usar o sistema. |
| **Interface** | Tudo que aparece na tela para o usuário. |
| **Dashboard** | Painel com resumo visual das informações. |
| **KPI / indicador** | Um número importante em destaque (ex.: total de ativos). |
| **Gráfico** | Representação visual dos dados (barras, rosca). |
| **Chart.js** | A ferramenta que usamos para desenhar os gráficos. |
| **Responsivo** | Que se adapta ao tamanho da tela (PC ou celular). |
| **Navegação** | Como o usuário se move entre as telas (o menu). |

---

## 5. Roteiro de fala (ensaie ~2 min — abrindo o sistema ao vivo)

> "Agora vou mostrar como é **usar** o Stock Flow. Tudo começa na tela de **login** — bem simples de propósito, só e-mail e senha, pra não distrair. [faz login]
>
> Assim que entramos, caímos no **dashboard**, que é o coração visual do sistema. A ideia é responder 'como estão as coisas?' em poucos segundos. Aqui em cima temos os **cartões** com os números principais: total de ativos, quantos estão em uso, em estoque, e o valor total do inventário. Embaixo, estes **gráficos** — um de barras por tipo e um de rosca por situação — que mostram a proporção de um jeito fácil de entender.
>
> E reparem no **menu à esquerda**: ele fica sempre visível, o item da página atual fica destacado, então o usuário nunca se perde. Aqui em Alertas aparece uma **bolinha vermelha** quando tem aviso, igual às notificações do celular. Tudo isso é **responsivo**, ou seja, funciona no computador e no celular. Agora o Eduardo vai mostrar os detalhes de uso, como os formulários."

---

## 6. Perguntas que a banca pode fazer

**"O que é o dashboard e para que serve?"**
→ "É o painel inicial que resume o sistema em cartões e gráficos, para o gestor ter uma visão geral rápida assim que entra."

**"Como vocês fizeram os gráficos?"**
→ "Com uma biblioteca chamada Chart.js, que recebe os números do sistema e desenha os gráficos de barras e de rosca."

**"O sistema funciona no celular?"**
→ "Sim. O layout é responsivo — ele se adapta ao tamanho da tela, então dá pra usar no computador ou no celular."

**"Como o usuário sabe em que página está?"**
→ "O item correspondente no menu lateral fica destacado, dando essa referência visual o tempo todo."

---

## 7. Onde isso está no projeto

- [app/templates/login.html](../../app/templates/login.html) — a tela de login.
- [app/templates/dashboard.html](../../app/templates/dashboard.html) — o painel principal com cartões e gráficos.
- [app/templates/base.html](../../app/templates/base.html) — o menu lateral e a barra do topo (a navegação).
- [docs/5-manual-do-usuario.md](../5-manual-do-usuario.md) — o manual, útil pra estudar o passo a passo das telas.
</content>
