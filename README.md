# Stock Flow — Gestão de Ativos de TI

TCC — Curso Técnico em Desenvolvimento de Sistemas

## Tecnologias
- Python 3.12 com FastAPI
- MySQL 8.0+
- Jinja2 (templates HTML)
- Tailwind CSS (via CDN)
- Autenticação JWT em cookie HTTP-only

## Configuração e execução

### 1. Clonar e entrar na pasta
```bash
git clone https://github.com/miguelmagsilveira-max/TCC.git
cd TCC
```

### 2. Criar e ativar ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados
```bash
mysql -u root -p < init_db.sql
```

### 5. Configurar variáveis de ambiente
```bash
cp .env.example .env
# Abra o .env e preencha DB_PASSWORD e troque o JWT_SECRET
```

### 6. Iniciar o servidor
```bash
uvicorn app.main:app --reload
```

### 7. Acessar o sistema
- Sistema: http://localhost:8000
- Documentação da API (Swagger): http://localhost:8000/docs

### Credenciais de acesso
| Usuário | E-mail | Senha | Nível |
|---|---|---|---|
| Administrador | admin@stockflow.com | admin123 | Admin |
| Operador | operador@stockflow.com | operador123 | Operador |

## Execução com Docker

Alternativa à execução local: sobe a aplicação e o banco MySQL em containers, sem precisar instalar Python ou MySQL na máquina.

### 1. Configurar variáveis de ambiente
```bash
cp .env.example .env
```
O `docker-compose.yml` lê todos os valores do `.env` (senhas, `JWT_SECRET`, `MYSQL_ROOT_PASSWORD`). Nenhum segredo fica fixo no compose.

### 2. Subir a stack
```bash
docker compose up -d --build
```
Na primeira subida, o MySQL carrega automaticamente o banco a partir de `docker/mysql-init/dump.sql` (schema + dados).

### 3. Acessar
- Sistema: http://localhost:8000
- MySQL (host): porta `3307` (mapeada para o `3306` do container, evita conflito com um MySQL local)

### Comandos úteis
```bash
docker compose down        # para os containers (mantém os dados)
docker compose down -v     # para e apaga o volume (recarrega o dump do zero na próxima subida)
docker compose logs -f app # acompanha os logs da aplicação
```

> O arquivo `docker/mysql-init/` é executado apenas quando o volume de dados está vazio. Para regenerar o dump a partir de um banco existente:
> ```bash
> mysqldump -u siga -p --no-tablespaces --databases stockflow > docker/mysql-init/dump.sql
> ```

## Deploy (Railway)

O projeto inclui `railway.json` e `Procfile` para deploy no Railway.
Configure as variáveis de ambiente `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` e `JWT_SECRET` no painel do Railway.

## Estrutura do projeto
- `app/main.py` — ponto de entrada da aplicação
- `app/database.py` — conexão e queries MySQL
- `app/auth.py` — autenticação JWT
- `app/helpers.py` — funções auxiliares compartilhadas
- `app/routers/` — rotas organizadas por domínio
- `app/templates/` — páginas HTML (Jinja2)
- `app/static/` — arquivos estáticos (CSS, JS)
- `init_db.sql` — schema do banco + dados iniciais
- `Dockerfile` — imagem da aplicação (Python + uvicorn)
- `docker-compose.yml` — orquestração app + MySQL
- `docker/mysql-init/dump.sql` — dump carregado automaticamente pelo container MySQL
- `docs/` — documentação técnica do projeto (ver [docs/README.md](docs/README.md))

## Documentação

A documentação técnica completa (requisitos, arquitetura, banco de dados, casos de uso, manual do usuário e testes) está disponível na pasta [`docs/`](docs/README.md).
