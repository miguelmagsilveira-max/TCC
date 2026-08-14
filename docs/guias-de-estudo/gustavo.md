# Guia de Estudo — Gustavo

### 🎨 Sua parte: **Identidade visual** — cores, tema claro/escuro, tipografia e layout

Você abre o bloco de design. Sua missão é explicar as **escolhas visuais** do Stock Flow: por que essas cores, como funciona o tema claro/escuro e como o layout foi pensado. Dica: **mostre na tela** enquanto fala.

---

## 1. Sua parte em uma frase

> "A identidade visual do Stock Flow foi pensada para transmitir confiança e profissionalismo: uma paleta sóbria em azul-marinho e cinza, com cores que têm significado, e um tema claro/escuro que o usuário escolhe."

---

## 2. Explicação de verdade (para você entender)

### A paleta de cores
A cor principal do sistema é um **azul-marinho** (código `#1e3a5f`), usado na barra lateral (menu) e nos títulos de relatório. Escolhemos azul porque transmite **confiança, seriedade e tecnologia** — é a cor mais usada em sistemas corporativos (bancos, empresas). O fundo é um **cinza-claro** suave (`#f1f5f9`) e os cartões são **brancos**, o que deixa a leitura leve e limpa.

### Cores com significado (cores semânticas)
Não usamos cor por enfeite — cada cor **comunica um estado**. As "etiquetas" de situação dos ativos seguem um padrão que qualquer pessoa entende na hora:
| Situação | Cor | Por quê |
|----------|-----|---------|
| Em estoque | 🟢 Verde | disponível, tudo certo |
| Em uso | 🔵 Azul | em atividade normal |
| Manutenção | 🟡 Amarelo | atenção, algo pendente |
| Desativado | ⚪ Cinza | inativo, "apagado" |

Isso se chama **design semântico**: a cor ajuda a entender sem precisar ler.

### Tema claro e escuro (dark mode)
O sistema tem **dois temas**, e o usuário troca num botão (☀️/🌙) no topo:
- **Tema claro**: fundo cinza-claro, texto escuro.
- **Tema escuro**: fundo azul-quase-preto (`#0f172a`), texto claro — mais confortável à noite e economiza a vista.

Três detalhes que mostram capricho:
1. A escolha do usuário fica **salva no navegador** — ao voltar, o tema continua o mesmo.
2. Se o usuário nunca escolheu, o sistema **respeita a preferência do computador dele**.
3. O tema é aplicado **instantaneamente**, antes da página aparecer, para **não dar aquele "flash" branco** irritante.

### Tipografia e layout
Usamos a fonte padrão do sistema (limpa e legível, sem exageros) e o layout tem sempre a **barra lateral fixa** à esquerda (o menu) e o conteúdo à direita, com bastante "respiro" (espaçamento). Isso dá **consistência**: o usuário sempre sabe onde as coisas estão.

### Como isso é feito, tecnicamente (só o suficiente)
Usamos o **Tailwind CSS**, um framework de estilos que trabalha com "classinhas" prontas (ex.: `bg-white`, `rounded-lg`). E o segredo do tema claro/escuro são as **variáveis de cor CSS**: definimos as cores uma vez e, ao trocar o tema, o sistema só troca os **valores** dessas variáveis — o resto se ajusta sozinho.

---

## 3. Por que fizemos assim (decisões que impressionam)

- **Por que azul-marinho?** Transmite confiança e seriedade, ideal para um sistema corporativo.
- **Por que cores semânticas?** Para o usuário **entender o estado num relance**, sem ler.
- **Por que tema claro/escuro?** Conforto visual e acessibilidade — cada um usa como prefere; à noite, o escuro cansa menos.
- **Por que Tailwind?** Acelera muito o desenvolvimento e garante **consistência** visual em todas as telas.

---

## 4. Glossário (fale com naturalidade)

| Termo | Tradução simples |
|-------|------------------|
| **Paleta de cores** | O conjunto de cores escolhido para o sistema. |
| **Cor semântica** | Cor que tem um significado (verde = ok, amarelo = atenção). |
| **Tema / dark mode** | A aparência clara ou escura da interface. |
| **Tailwind CSS** | Framework de estilos com classes prontas, usado no visual. |
| **Variável CSS** | Um "apelido" para uma cor, que facilita trocar o tema. |
| **Tipografia** | O estilo e a escolha das fontes (letras). |
| **Layout** | A organização dos elementos na tela. |

---

## 5. Roteiro de fala (ensaie ~2 min — mostrando na tela)

> "Agora vamos falar do visual. A identidade do Stock Flow foi pensada para passar **confiança e profissionalismo**. A cor principal é este **azul-marinho** da barra lateral — escolhemos azul porque é a cor de sistemas corporativos sérios, transmite tecnologia e seriedade. O fundo é um cinza bem clarinho, com cartões brancos, pra deixar a leitura leve.
>
> Um cuidado importante foi usar **cores com significado**: reparem que 'em estoque' é verde, 'em uso' é azul, 'manutenção' é amarelo de atenção e 'desativado' é cinza. Assim o usuário entende o estado só de bater o olho.
>
> E temos **tema claro e escuro** — [clica no botão ☀️/🌙] — o usuário troca aqui, e o sistema **lembra** a escolha na próxima vez, além de respeitar a preferência do computador. Tudo isso foi feito com o Tailwind CSS e variáveis de cor, o que garante que **todas as telas fiquem consistentes**. Agora o Caio vai mostrar as telas principais."

---

## 6. Perguntas que a banca pode fazer

**"Por que escolheram essas cores?"**
→ "O azul-marinho passa confiança e é padrão em sistemas corporativos. E usamos cores semânticas — verde, amarelo, azul, cinza — para comunicar o estado dos ativos visualmente."

**"O tema escuro é só enfeite?"**
→ "Não, é acessibilidade e conforto. Reduz o cansaço visual à noite e a preferência fica salva por usuário."

**"O que é Tailwind?"**
→ "É um framework de CSS que oferece classes de estilo prontas. Ele acelerou o desenvolvimento e manteve o visual consistente em todo o sistema."

**"Como o sistema lembra o tema escolhido?"**
→ "A preferência é salva no próprio navegador do usuário, então na volta o tema continua o mesmo."

---

## 7. Onde isso está no projeto

- [app/static/css/custom.css](../../app/static/css/custom.css) — as **variáveis de cor** e as regras dos temas (mostre o `:root` e o `html.dark`).
- [app/static/js/theme.js](../../app/static/js/theme.js) — o código que troca e **salva** o tema.
- [app/templates/base.html](../../app/templates/base.html) — o **layout base** (barra lateral + topo) que todas as telas usam.
</content>
