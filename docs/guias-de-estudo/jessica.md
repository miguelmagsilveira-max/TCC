# Guia de Estudo — Jéssica

### 🎤 Sua parte: **Banco de dados** (onde e como os dados ficam guardados)

Depois que o Miguel apresenta a visão geral, você explica **a "despensa" do sistema**: o banco de dados. É onde ficam guardados os ativos, colaboradores, usuários e todo o histórico.

---

## 1. Sua parte em uma frase

> "O banco de dados é a memória do sistema: são 7 tabelas conectadas entre si que guardam, de forma organizada, tudo o que o Stock Flow precisa lembrar."

---

## 2. Explicação de verdade (para você entender)

### O que é um banco de dados?
Pense numa **planilha de Excel muito organizada e inteligente**. Cada **tabela** é uma aba da planilha, com **colunas** (as informações) e **linhas** (cada registro). Nós usamos o **MySQL**, que é um dos bancos de dados mais usados no mundo.

### As 7 tabelas do Stock Flow
| Tabela | Guarda... | Analogia |
|--------|-----------|----------|
| **usuarios** | quem acessa o sistema (admin/operador) | a lista de funcionários com crachá |
| **colaboradores** | os funcionários que recebem equipamentos | as pessoas da empresa |
| **tipos_ativo** | os tipos de equipamento e o estoque mínimo | as categorias (Notebook, Monitor...) |
| **ativos** | cada equipamento em si (a tabela central) | o inventário |
| **historico_ativos** | tudo que já aconteceu com cada ativo | o "prontuário" do equipamento |
| **notificacoes** | os alertas gerados | os avisos |
| **opcoes_select** | as opções dos menus que dá pra adicionar/remover | uma lista de opções editável |

### O conceito mais importante: **relacionamento entre tabelas**
As tabelas **conversam entre si**. Exemplo real:
- Na tabela **ativos**, um notebook não guarda o nome do colaborador escrito. Ele guarda só o **número (id)** do colaborador — tipo "colaborador nº 3".
- Quando o sistema quer mostrar o nome, ele vai na tabela **colaboradores**, procura o nº 3 e pega "Carlos Lima".

Isso se chama **chave estrangeira** (o "id" que aponta para outra tabela). A vantagem: se o Carlos mudar de nome, muda **num lugar só**, e o sistema todo é atualizado. Não fica informação repetida e desatualizada espalhada.

### Rastreabilidade: a tabela `historico_ativos`
Toda vez que algo acontece com um ativo (cadastro, empréstimo, manutenção, devolução), o sistema grava uma linha no histórico: **o que foi feito, quando e por quem**. É como o **prontuário de um paciente** — dá para ver toda a "vida" do equipamento. Esse é um dos grandes diferenciais do projeto.

---

## 3. Por que fizemos assim (decisões que impressionam)

- **Por que MySQL?** É um banco relacional (tabelas conectadas), gratuito, confiável e amplamente usado no mercado.
- **Por que não apagar ativos de verdade (exclusão lógica)?** Quando um ativo é "desativado", ele não some do banco — a gente só marca ele como inativo. Assim o **histórico é preservado**. Apagar de verdade perderia a rastreabilidade.
- **Por que guardar id em vez de repetir o nome?** Para **não duplicar dados** e evitar informação desatualizada. Isso se chama *normalização*.
- **Por que a senha aparece como `senha_hash`?** Porque a gente **nunca guarda a senha real** — só uma versão embaralhada e irreversível (isso a Amanda detalha).

---

## 4. Glossário (fale com naturalidade)

| Termo | Tradução simples |
|-------|------------------|
| **Banco de dados** | Onde o sistema guarda todas as informações de forma organizada. |
| **Tabela** | Uma "aba de planilha" com um tipo de informação (ex.: ativos). |
| **Registro / linha** | Uma entrada na tabela (ex.: um notebook específico). |
| **Chave primária (PK)** | O número único que identifica cada linha (o "id"). |
| **Chave estrangeira (FK)** | Um id que aponta para outra tabela, ligando as duas. |
| **Relacionamento** | A ligação entre duas tabelas. |
| **Diagrama ER** | O desenho que mostra as tabelas e como elas se ligam. |
| **Exclusão lógica** | Marcar como inativo em vez de apagar de verdade. |

---

## 5. Roteiro de fala (ensaie ~2 min)

> "Como o Miguel falou, o banco de dados é a 'despensa' do sistema — é onde tudo fica guardado. A gente usou o **MySQL**, e organizou os dados em **7 tabelas**. Podem pensar numa tabela como uma aba de uma planilha bem organizada.
>
> A tabela principal é a de **ativos**, que guarda cada equipamento. Tem também colaboradores, usuários, tipos de ativo e, muito importante, a de **histórico**.
>
> O mais interessante é que as tabelas **se conectam**. Por exemplo: um notebook não guarda o nome do dono escrito — ele guarda o *número* do colaborador, e o sistema vai buscar o nome na tabela de colaboradores. Isso evita repetir informação e manter dado desatualizado.
>
> E a tabela de **histórico** funciona como um prontuário: toda ação num equipamento fica registrada — o que foi feito, quando e por quem. Isso dá **rastreabilidade total**. Agora a Amanda vai explicar como a gente protege o acesso a tudo isso."

---

## 6. Perguntas que a banca pode fazer

**"Por que MySQL e não outro banco?"**
→ "É um banco relacional consolidado, gratuito e muito usado no mercado — ideal para dados conectados como os nossos."

**"O que é uma chave estrangeira?"**
→ "É um campo numa tabela que aponta para o registro de outra. Por exemplo, o campo `id_colaborador` na tabela de ativos aponta para quem está com aquele equipamento."

**"Se eu apagar um colaborador, os ativos dele somem?"**
→ "Não. A gente configurou para o vínculo simplesmente ficar vazio (o ativo volta a ficar 'sem dono'), preservando o ativo e o histórico."

**"Quantas tabelas tem e qual a principal?"**
→ "São 7 tabelas. A principal é a `ativos`, que fica no centro e se liga a colaboradores, usuários e ao histórico."

---

## 7. Onde isso está no projeto

- [init_db.sql](../../init_db.sql) — o arquivo que **cria as 7 tabelas** e coloca dados de exemplo. Abra e mostre os `CREATE TABLE`.
- [app/database.py](../../app/database.py) — o código que conversa com o MySQL.
- [docs/3-banco-de-dados.md](../3-banco-de-dados.md) — documento completo, com o **diagrama ER** (o desenho das tabelas conectadas). **Estude o diagrama.**
</content>
