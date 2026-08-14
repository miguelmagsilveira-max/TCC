# Guias de Estudo para a Apresentação — Stock Flow

Este material foi feito para o grupo apresentar o TCC **Stock Flow** com segurança, mesmo para quem nunca programou. O objetivo **não é decorar**: é *entender* o que você vai falar, para conseguir responder qualquer pergunta com naturalidade.

> Leia primeiro este índice (o contexto abaixo vale para **todo mundo**). Depois vá direto para o **seu** guia.

---

## O que é o Stock Flow? (contexto que todos precisam saber)

**O problema.** Empresas têm muitos equipamentos de TI: notebooks, monitores, teclados, headsets, switches etc. Sem um sistema, ninguém sabe direito **quem está com o quê**, **quantos ainda tem em estoque**, **quais garantias estão vencendo** ou **o que já foi para manutenção**. Normalmente isso vira uma planilha bagunçada que se perde.

**A nossa solução.** O Stock Flow é um **sistema web** (abre no navegador, em qualquer dispositivo) que controla o **ciclo de vida completo** de cada equipamento: do cadastro à baixa, passando por empréstimo a um funcionário, manutenção e devolução — tudo com **histórico** e **alertas automáticos**.

**A frase de efeito do projeto:** *"O Stock Flow dá rastreabilidade total aos ativos de TI de uma empresa — a qualquer momento você sabe onde cada equipamento está, com quem, quanto vale e qual sua situação."*

**Como ele é feito, em uma linha por camada:**
- **O que o usuário vê (front-end):** páginas HTML estilizadas com **Tailwind CSS**, com tema claro/escuro.
- **O cérebro (back-end):** feito em **Python** com o framework **FastAPI**, que recebe os cliques, aplica as regras e decide o que mostrar.
- **A memória (banco de dados):** **MySQL**, onde ficam guardados todos os dados (ativos, colaboradores, histórico...).

---

## Divisão das 7 partes

O grupo se divide em dois blocos. Cada pessoa é "dona" de uma parte.

### 🎨 Bloco Design / Front-end (a cara do sistema)
| Pessoa | Parte | Arquivo |
|--------|-------|---------|
| **Gustavo** | Identidade visual: cores, tema claro/escuro, tipografia e layout | [gustavo.md](gustavo.md) |
| **Caio** | Telas e experiência do usuário: login, dashboard e navegação | [caio.md](caio.md) |
| **Eduardo** | Componentes e usabilidade: formulários, SmartSelect, páginas de erro | [eduardo.md](eduardo.md) |

### ⚙️ Bloco Back-end / Estrutura (o motor do sistema)
| Pessoa | Parte | Arquivo |
|--------|-------|---------|
| **Miguel** | Visão geral e arquitetura do sistema (abertura) | [miguel.md](miguel.md) |
| **Jéssica** | Banco de dados: como os dados são guardados e ligados | [jessica.md](jessica.md) |
| **Amanda** | Login, segurança e níveis de acesso | [amanda.md](amanda.md) |
| **Nicholas** | Funcionalidades de gestão, alertas e relatórios | [nicholas.md](nicholas.md) |

---

## Ordem sugerida de apresentação

Uma sequência que conta uma "história" e flui bem:

1. **Miguel** — abre: qual o problema, o que é o Stock Flow e como ele é organizado (visão geral).
2. **Jéssica** — mostra onde e como os dados ficam guardados (banco).
3. **Amanda** — explica como o sistema protege o acesso (login e permissões).
4. **Nicholas** — apresenta o que o sistema *faz na prática* (cadastro, alertas, relatórios).
5. **Gustavo** — mostra a identidade visual (cores, tema, layout).
6. **Caio** — passeia pelas telas principais (login, dashboard).
7. **Eduardo** — demonstra os detalhes de uso (formulários, SmartSelect, erros) e fecha.

> Dica: quem fala de back-end **explica**; quem fala de front-end **mostra na tela**. Combinem para o Caio/Eduardo abrirem o sistema ao vivo enquanto explicam.

---

## Como cada guia está montado

Todo guia segue a mesma estrutura, para você estudar do jeito certo:

1. **Sua parte em uma frase** — o que você "vende" na apresentação.
2. **Explicação de verdade** — o conteúdo explicado com analogias, para *entender*.
3. **Por que fizemos assim** — as decisões do projeto (é isso que impressiona a banca).
4. **Glossário** — os termos técnicos que você vai falar, em português simples.
5. **Roteiro de fala** — um "script" do que dizer, para ensaiar.
6. **Perguntas que a banca pode fazer** — com respostas prontas para adaptar.
7. **Onde isso está no projeto** — os arquivos, caso queira mostrar o código.

---

## 5 dicas de ouro para a apresentação

1. **Entenda, não decore.** Se você entende o *porquê*, responde qualquer pergunta. Decoreba trava na primeira pergunta fora do script.
2. **Fale como se explicasse para um amigo.** Traduza os termos técnicos ("JWT é tipo uma pulseira de festa que prova que você já entrou").
3. **Conecte com a parte do colega.** "Como a Jéssica falou do banco, é lá que esses dados ficam guardados."
4. **Se travar numa pergunta, seja honesto e raciocine em voz alta.** Melhor do que inventar.
5. **Ensaien juntos pelo menos 2 vezes** cronometrando. Cada um tem ~2 minutos.
</content>
</invoke>
