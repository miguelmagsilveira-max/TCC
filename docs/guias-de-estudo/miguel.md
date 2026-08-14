# Guia de Estudo — Miguel

### 🎤 Sua parte: **Visão geral e arquitetura do sistema** (a abertura)

Você abre a apresentação. Sua missão é fazer a banca entender, em poucos minutos, **qual problema o projeto resolve** e **como ele é montado por dentro** — sem entrar nos detalhes (que os colegas aprofundam depois).

---

## 1. Sua parte em uma frase

> "O Stock Flow é um sistema web que controla todos os equipamentos de TI de uma empresa, e ele é construído em três camadas que separam a aparência, as regras e os dados."

---

## 2. Explicação de verdade (para você entender)

### O problema que resolvemos
Imagine uma empresa com 200 notebooks, monitores, headsets. Sem um sistema:
- Ninguém sabe **quem está com cada equipamento**.
- Não se sabe **quantos ainda tem em estoque** nem quando repor.
- **Garantias vencem** sem ninguém perceber.
- Quando um equipamento some ou quebra, não há **histórico** de por onde passou.

O Stock Flow organiza tudo isso num só lugar, acessível pelo navegador.

### Como o sistema é organizado: **arquitetura em 3 camadas**
Pense num **restaurante**:
- **Salão (o que o cliente vê)** = **Front-end**: as páginas, cores, botões. Feito com HTML + Tailwind CSS.
- **Cozinha (onde o trabalho acontece)** = **Back-end**: recebe o pedido, aplica as regras e prepara a resposta. Feito em **Python** com o framework **FastAPI**.
- **Despensa (onde ficam os ingredientes)** = **Banco de dados**: guarda todos os dados. É o **MySQL**.

O cliente nunca entra na cozinha nem na despensa — ele só faz o pedido no salão. No sistema é igual: o navegador pede uma página, o FastAPI processa e busca dados no MySQL, e devolve a página pronta.

Esse padrão de organização tem um nome: **MVC** (Model-View-Controller):
- **Model** = os dados (banco de dados).
- **View** = a visão, o que aparece na tela (templates).
- **Controller** = o controlador, que decide o que fazer (os *routers* do FastAPI).

Separar assim é importante porque **cada parte pode ser mexida sem quebrar as outras** — foi isso que permitiu o grupo dividir o trabalho: uns no visual, outros nas regras.

### O caminho de um clique (fluxo de uma requisição)
Quando o usuário clica em "Ativos":
1. O **navegador** envia o pedido para o servidor.
2. O **FastAPI** confere se o usuário está logado (isso a Amanda explica).
3. Ele pede os dados ao **banco MySQL** (isso a Jéssica explica).
4. Ele monta a **página HTML** com esses dados (isso o pessoal de design mostra).
5. Devolve a página pronta pro navegador.

---

## 3. Por que fizemos assim (as decisões que impressionam a banca)

- **Por que sistema web (e não um programa instalado)?** Para abrir em **qualquer dispositivo** (computador, celular) sem instalar nada — só o navegador.
- **Por que Python + FastAPI?** Python é uma linguagem simples e muito usada; o FastAPI é moderno, rápido e ainda gera uma documentação automática da aplicação.
- **Por que separar em camadas (MVC)?** Para **organizar** e permitir **trabalho em equipe**: o time de design mexe na View sem tocar nas regras, e vice-versa.

---

## 4. Glossário (fale com naturalidade)

| Termo | Tradução simples |
|-------|------------------|
| **Sistema web** | Programa que roda no navegador, sem instalar nada. |
| **Front-end** | A parte visual, o que o usuário vê. |
| **Back-end** | O "cérebro" que processa tudo por trás. |
| **Framework** | Um conjunto de ferramentas prontas que acelera o desenvolvimento (FastAPI é um). |
| **MVC** | Forma de organizar o sistema em 3 partes: dados, visão e controle. |
| **Requisição** | Um pedido que o navegador faz ao servidor (ex.: "me mostra os ativos"). |
| **Servidor** | O computador que roda o back-end e responde aos pedidos. |

---

## 5. Roteiro de fala (ensaie ~2 min)

> "Bom dia. Nosso projeto é o **Stock Flow**, um sistema de gestão de ativos de TI. Ele resolve um problema comum nas empresas: a dificuldade de controlar equipamentos como notebooks e monitores — quem está usando, quanto tem em estoque, e quais garantias estão vencendo.
>
> Para resolver isso, criamos um **sistema web**, que abre em qualquer navegador. Por dentro, ele é organizado em **três camadas**, como um restaurante: o *salão*, que é a parte visual que o usuário vê; a *cozinha*, que é o cérebro do sistema, feito em Python com FastAPI; e a *despensa*, o banco de dados MySQL, onde tudo fica guardado.
>
> Essa separação segue um padrão chamado **MVC**, e foi ela que permitiu que a gente dividisse bem o trabalho no grupo. Quando o usuário clica em algo, o pedido vai pro FastAPI, que confere o login, busca os dados no banco e devolve a página pronta. Agora a Jéssica vai mostrar como esses dados ficam organizados no banco."

---

## 6. Perguntas que a banca pode fazer

**"Por que vocês escolheram Python?"**
→ "Porque é uma linguagem simples de ler e muito usada no mercado, o que facilitou o aprendizado do grupo, e tem ótimos frameworks como o FastAPI."

**"O que é FastAPI exatamente?"**
→ "É um framework, ou seja, um conjunto de ferramentas prontas em Python para construir a parte de servidor de aplicações web de forma rápida e organizada."

**"O que ganha separando em camadas?"**
→ "Organização e trabalho em equipe: a gente consegue mexer na parte visual sem afetar as regras do sistema, e o código fica mais fácil de manter."

**"O sistema funciona no celular?"**
→ "Sim, é responsivo e web, então abre em qualquer dispositivo com navegador." (o pessoal de design detalha)

---

## 7. Onde isso está no projeto

- [app/main.py](../../app/main.py) — o "porteiro" que liga tudo e recebe os pedidos.
- [app/routers/](../../app/routers/) — os controllers (a lógica de cada área).
- [docs/2-arquitetura.md](../2-arquitetura.md) — documento completo da arquitetura (com os diagramas). **Vale muito abrir os diagramas na hora de estudar.**
</content>
