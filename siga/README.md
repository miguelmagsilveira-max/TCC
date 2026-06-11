# Stock Flow — Gestão de Ativos de TI

TCC — Curso Técnico em Desenvolvimento de Sistemas

## Tecnologias
- Python 3.11+ com FastAPI
- MySQL 8.0+
- Jinja2 (templates HTML)
- Tailwind CSS (via CDN)

## Configuração e execução

### 1. Clonar e entrar na pasta
```bash
cd siga
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

## Deploy (Railway)

O projeto inclui `railway.json` e `Procfile` para deploy no Railway.
Configure as variáveis de ambiente `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` e `JWT_SECRET` no painel do Railway.

## Estrutura do projeto
- `app/main.py` — ponto de entrada da aplicação
- `app/database.py` — conexão e queries MySQL
- `app/auth.py` — autenticação JWT
- `app/routers/` — rotas organizadas por domínio
- `app/templates/` — páginas HTML (Jinja2)
- `app/static/` — arquivos estáticos (CSS, JS)
- `init_db.sql` — schema do banco + dados iniciais
