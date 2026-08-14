# Guia de Estudo — Amanda

### 🎤 Sua parte: **Login, segurança e níveis de acesso**

Você explica como o sistema **protege quem entra** e **controla o que cada pessoa pode fazer**. É uma parte que a banca adora, porque segurança é um assunto sério em qualquer sistema real.

---

## 1. Sua parte em uma frase

> "O Stock Flow protege o acesso com login seguro: as senhas nunca são guardadas em texto puro, o sistema entrega uma 'credencial digital' que expira sozinha, e cada usuário só faz o que o nível dele permite."

---

## 2. Explicação de verdade (para você entender)

### O login, passo a passo
1. O usuário digita **e-mail e senha**.
2. O sistema procura esse e-mail no banco.
3. Ele **compara a senha** digitada com a versão guardada (embaralhada).
4. Se bater, ele **libera o acesso** e entrega uma credencial digital.

### Ideia-chave 1: a senha nunca é guardada de verdade (**hash com bcrypt**)
No banco, **não** existe a senha "admin123". Existe algo assim:
`$2b$12$e2hlJgU2tHDJApv8xsz08...`

Isso é o **hash**: a senha passa por uma "máquina de picar" (o algoritmo **bcrypt**) que a transforma numa sequência embaralhada e **impossível de reverter**. Quando você faz login, o sistema pica a senha que você digitou e compara os dois picadinhos. Assim, **mesmo quem invadisse o banco não descobriria as senhas**.

> Analogia: é como transformar uma fruta em suco. Dá pra fazer suco e comparar dois sucos, mas ninguém consegue "desliquidificar" o suco de volta na fruta.

### Ideia-chave 2: a "pulseira de festa" (**token JWT em cookie**)
Depois do login, o sistema entrega um **token JWT** — uma espécie de **pulseira de festa**. Toda vez que você pede uma página, você "mostra a pulseira" e o sistema sabe que você já entrou, sem precisar digitar a senha de novo.

Detalhes importantes do nosso projeto:
- A pulseira fica guardada num **cookie HTTP-only**: ou seja, só o servidor mexe nela; **o JavaScript da página não consegue ler** o token. Isso protege contra um tipo comum de ataque (roubo de sessão).
- A pulseira **expira em 24 horas**. Depois disso, precisa logar de novo.

### Ideia-chave 3: níveis de acesso (**admin x operador**)
Nem todo mundo pode tudo:
- **Administrador**: pode cadastrar, editar, vincular, mandar pra manutenção, gerenciar usuários. Acesso total.
- **Operador**: só **visualiza** (dashboard, ativos, relatórios). Não altera nada.

Se um operador tentar acessar uma tela de administrador, o sistema **bloqueia** e mostra a página de erro **403 (acesso negado)**.

---

## 3. Por que fizemos assim (decisões que impressionam)

- **Por que hash de senha (bcrypt)?** Porque guardar senha em texto puro é um erro grave de segurança. Com hash, um vazamento do banco não expõe as senhas.
- **Por que cookie HTTP-only?** Para que o token não possa ser roubado por scripts maliciosos na página (ataque XSS).
- **Por que o token expira?** Se alguém deixar o computador aberto, o acesso não fica válido pra sempre.
- **Por que dois níveis de acesso?** Princípio de segurança: cada pessoa deve ter **só as permissões que precisa** (menor privilégio).

---

## 4. Glossário (fale com naturalidade)

| Termo | Tradução simples |
|-------|------------------|
| **Autenticação** | Provar quem você é (o login). |
| **Autorização** | Definir o que você pode fazer (os níveis de acesso). |
| **Hash** | Embaralhamento irreversível de uma informação (a senha). |
| **bcrypt** | O algoritmo específico que usamos para picar as senhas. |
| **Token JWT** | A "pulseira" digital que prova que você já logou. |
| **Cookie** | Um pequeno dado que o navegador guarda (aqui, o token). |
| **HTTP-only** | Um cookie que o JavaScript da página não consegue ler (mais seguro). |
| **Erro 403** | "Acesso negado" — você está logado, mas não tem permissão. |

---

## 5. Roteiro de fala (ensaie ~2 min)

> "Agora que sabemos onde os dados ficam, como a gente protege o acesso? Começa pelo **login**. Um detalhe importante: a senha do usuário **nunca é guardada de verdade** no banco. Ela passa por um processo chamado **hash**, com o algoritmo **bcrypt**, que embaralha a senha de um jeito impossível de reverter. É como fazer suco de uma fruta: dá pra comparar dois sucos, mas não dá pra voltar à fruta. Então, mesmo que alguém invadisse o banco, não descobriria as senhas.
>
> Depois do login, o sistema entrega uma espécie de **pulseira de festa**, que é o **token JWT**. A cada página, o usuário 'mostra a pulseira' e não precisa logar de novo. Essa pulseira fica num cookie protegido, que o JavaScript não consegue ler, e **expira em 24 horas**.
>
> Por fim, temos **dois níveis de acesso**: o administrador pode tudo, e o operador só visualiza. Se um operador tenta entrar numa área de admin, o sistema bloqueia com um erro 403. Agora o Nicholas vai mostrar o que o sistema faz na prática."

---

## 6. Perguntas que a banca pode fazer

**"Como a senha é armazenada?"**
→ "Nunca em texto puro. A gente guarda um *hash* gerado pelo bcrypt, que é irreversível. No login, comparamos os hashes."

**"O que é esse tal de JWT?"**
→ "É um token, tipo uma credencial digital que o sistema entrega após o login. A cada requisição o usuário apresenta esse token em vez de digitar a senha de novo."

**"E se roubarem o token?"**
→ "A gente reduz esse risco guardando em cookie HTTP-only, que o JavaScript não acessa, e o token ainda expira em 24 horas."

**"Qual a diferença entre admin e operador?"**
→ "O admin tem acesso total (cadastrar, editar, gerenciar usuários); o operador só consulta. Isso segue o princípio do menor privilégio."

---

## 7. Onde isso está no projeto

- [app/auth.py](../../app/auth.py) — o coração da segurança: hash de senha, criação/validação do token, verificação de admin.
- [app/routers/auth_routes.py](../../app/routers/auth_routes.py) — as telas de login e logout.
- [docs/1-requisitos.md](../1-requisitos.md) — veja os requisitos de segurança (RNF03, RNF04, RNF11) e as regras RN01/RN02/RN10.
</content>
