# Guia de Estudo — Eduardo

### 🎨 Sua parte: **Componentes e usabilidade** — formulários, SmartSelect e páginas de erro (fechamento)

Você fecha a apresentação mostrando os **detalhes que fazem o sistema ser agradável de usar**: os formulários bem-feitos, o componente inteligente de seleção (SmartSelect) e até as telas de erro. Dica: **mostre na tela** um formulário e o SmartSelect funcionando.

---

## 1. Sua parte em uma frase

> "Cuidamos dos detalhes de usabilidade do Stock Flow: formulários claros, um componente de seleção que o próprio usuário pode alimentar, e até as páginas de erro foram desenhadas para não deixar ninguém perdido."

---

## 2. Explicação de verdade (para você entender)

### Formulários bem pensados
Formulário é onde o usuário **digita dados** (cadastrar um ativo, um colaborador). Um bom formulário evita erros e frustração. No Stock Flow eles têm:
- Campos **agrupados de forma lógica** (dados do equipamento juntos, dados de compra juntos).
- **Rótulos claros** em cada campo.
- Botões de ação evidentes (**Salvar**, **Cancelar**).
- Feedback visual: os campos mudam de aparência ao serem clicados, e no tema escuro se ajustam sozinhos.

### O destaque: o **SmartSelect** (seleção inteligente)
Esse é o componente mais legal da sua parte. Imagine que você está cadastrando um ativo e precisa escolher o **tipo** (Notebook, Monitor...). Num sistema comum, se o tipo que você quer não está na lista, você fica travado. No Stock Flow, o **SmartSelect** deixa o próprio usuário **adicionar uma opção nova ali na hora**, sem sair da tela — e ela já fica salva para todos os próximos cadastros. Também dá pra **remover** opções.

> Analogia: é como uma lista de contatos que se completa sozinha conforme você usa. Você não precisa "configurar tudo antes" — o sistema cresce junto com a empresa.

Isso aparece em vários campos: **tipo de ativo, tipo de aquisição, localização** (no cadastro de ativos) e **cargo, departamento** (no cadastro de colaboradores).

### Páginas de erro que não assustam
Quando algo dá errado, em vez daquela tela feia e técnica, o Stock Flow mostra páginas amigáveis:
- **Erro 404** ("página não encontrada"): quando o usuário tenta acessar um endereço que não existe.
- **Erro 403** ("acesso negado"): quando um operador tenta entrar numa área só de administrador.

Ambas têm visual caprichado e um **botão para voltar** ao lugar certo — o usuário nunca fica "preso".

### Consistência e acessibilidade
Todos os componentes seguem o **mesmo padrão visual** (mesmas cores, cantos arredondados, espaçamentos). Isso não é só bonito: deixa o sistema **previsível** — quando o usuário aprende uma tela, já sabe usar as outras.

---

## 3. Por que fizemos assim (decisões que impressionam)

- **Por que o SmartSelect?** Para o sistema **não engessar** o usuário. Ele se adapta à realidade de cada empresa sem precisar de um técnico para mexer no código.
- **Por que caprichar nos formulários?** Porque é onde o usuário mais erra; um bom formulário **previne erros** e economiza tempo.
- **Por que páginas de erro personalizadas?** Para **não perder o usuário**: em vez de uma tela técnica assustadora, ele recebe uma explicação amigável e um caminho de volta.
- **Por que consistência?** Porque um padrão visual único torna o sistema **fácil de aprender** — vale a mesma lógica em todas as telas.

---

## 4. Glossário (fale com naturalidade)

| Termo | Tradução simples |
|-------|------------------|
| **Componente** | Uma "peça" reutilizável da interface (um botão, um campo, o SmartSelect). |
| **Formulário** | A tela onde o usuário preenche e envia dados. |
| **SmartSelect** | Nosso campo de seleção que o usuário pode alimentar (adicionar/remover opções). |
| **Usabilidade** | O quanto o sistema é fácil e agradável de usar. |
| **Feedback visual** | As respostas visuais que a tela dá ao usuário (destaque, mensagens). |
| **Erro 404** | "Página não encontrada". |
| **Erro 403** | "Acesso negado" (sem permissão). |
| **Consistência** | Todas as telas seguirem o mesmo padrão. |

---

## 5. Roteiro de fala (ensaie ~2 min — mostrando na tela)

> "Para fechar, vou mostrar os **detalhes que fazem o sistema ser gostoso de usar**. Comecemos pelos **formulários** — por exemplo, o de cadastro de um ativo. Reparem que os campos estão agrupados de forma lógica e cada um tem um rótulo claro, o que evita erros.
>
> O destaque aqui é este componente, o **SmartSelect**. Olhem: quando vou escolher o tipo do equipamento, se o que eu quero não existe, eu mesmo **adiciono na hora** — [adiciona uma opção] — e ela já fica salva para os próximos cadastros. Isso deixa o sistema flexível, sem precisar de um técnico para configurar.
>
> E cuidamos até dos **erros**: se alguém tenta acessar uma página que não existe, aparece esta tela de erro 404 amigável, com um botão pra voltar — em vez de uma tela técnica assustadora. Tudo no sistema segue o **mesmo padrão visual**, então quando o usuário aprende uma tela, já sabe usar todas. E era isso: o Stock Flow une um back-end sólido a uma experiência simples e agradável. Obrigado!"

---

## 6. Perguntas que a banca pode fazer

**"O que o SmartSelect tem de diferente de um campo de seleção normal?"**
→ "Num campo normal, as opções são fixas. No SmartSelect, o próprio usuário adiciona ou remove opções na hora, e elas ficam salvas para os próximos cadastros."

**"Onde o SmartSelect é usado?"**
→ "Nos campos de tipo de ativo, tipo de aquisição e localização, no cadastro de ativos; e em cargo e departamento, no de colaboradores."

**"Por que fizeram páginas de erro personalizadas?"**
→ "Para não deixar o usuário perdido. Em vez de uma tela técnica, mostramos uma explicação amigável e um botão para voltar."

**"Como garantem que o sistema é fácil de usar?"**
→ "Mantendo consistência: todas as telas seguem o mesmo padrão visual e de comportamento, então o aprendizado de uma vale para as outras."

---

## 7. Onde isso está no projeto

- [app/static/js/smart-select.js](../../app/static/js/smart-select.js) — o código do componente SmartSelect.
- [app/templates/ativos/form.html](../../app/templates/ativos/form.html) — formulário de ativo (usa o SmartSelect em vários campos).
- [app/templates/errors/404.html](../../app/templates/errors/404.html) e [403.html](../../app/templates/errors/403.html) — as páginas de erro.
- [docs/4-casos-de-uso.md](../4-casos-de-uso.md) — veja o caso de uso UC16 (gerenciar opções do SmartSelect).
</content>
