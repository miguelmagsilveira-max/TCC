CREATE DATABASE IF NOT EXISTS stockflow CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE stockflow;

-- Usuários do sistema
CREATE TABLE IF NOT EXISTS usuarios (
  id           INT AUTO_INCREMENT PRIMARY KEY,
  nome         VARCHAR(100) NOT NULL,
  email        VARCHAR(100) UNIQUE NOT NULL,
  senha_hash   VARCHAR(255) NOT NULL,
  nivel        ENUM('admin', 'operador') NOT NULL DEFAULT 'operador',
  ativo        TINYINT(1) NOT NULL DEFAULT 1,
  criado_em    DATETIME NOT NULL DEFAULT NOW(),
  ultimo_acesso DATETIME
);

-- Colaboradores (funcionários da empresa)
CREATE TABLE IF NOT EXISTS colaboradores (
  id           INT AUTO_INCREMENT PRIMARY KEY,
  nome         VARCHAR(100) NOT NULL,
  email        VARCHAR(100),
  cargo        VARCHAR(100),
  departamento VARCHAR(100),
  status       ENUM('ativo', 'desligado') NOT NULL DEFAULT 'ativo',
  criado_em    DATETIME NOT NULL DEFAULT NOW()
);

-- Tipos de ativo com estoque mínimo configurável
CREATE TABLE IF NOT EXISTS tipos_ativo (
  id             INT AUTO_INCREMENT PRIMARY KEY,
  nome           VARCHAR(100) UNIQUE NOT NULL,
  estoque_minimo INT NOT NULL DEFAULT 0
);

-- Ativos de TI
CREATE TABLE IF NOT EXISTS ativos (
  id                 INT AUTO_INCREMENT PRIMARY KEY,
  codigo             VARCHAR(20) UNIQUE NOT NULL,
  nome               VARCHAR(100) NOT NULL,
  marca              VARCHAR(100),
  modelo             VARCHAR(100),
  numero_serie       VARCHAR(100),
  tipo               VARCHAR(100),
  situacao           ENUM('Em estoque','Em uso','Manutenção','Desativado') NOT NULL DEFAULT 'Em estoque',
  id_colaborador     INT,
  tipo_aquisicao     VARCHAR(50),
  preco              DECIMAL(10,2),
  data_aquisicao     DATE,
  data_garantia      DATE,
  data_vinculacao    DATETIME,
  fornecedor         VARCHAR(100),
  numero_nota_fiscal VARCHAR(50),
  localizacao        VARCHAR(100),
  ativo              TINYINT(1) NOT NULL DEFAULT 1,
  criado_em          DATETIME NOT NULL DEFAULT NOW(),
  criado_por         INT,
  FOREIGN KEY (id_colaborador) REFERENCES colaboradores(id) ON DELETE SET NULL,
  FOREIGN KEY (criado_por) REFERENCES usuarios(id) ON DELETE SET NULL
);

-- Histórico de movimentações dos ativos
CREATE TABLE IF NOT EXISTS historico_ativos (
  id                      INT AUTO_INCREMENT PRIMARY KEY,
  id_ativo                INT NOT NULL,
  acao                    VARCHAR(50) NOT NULL,
  id_colaborador_anterior INT,
  id_colaborador_novo     INT,
  detalhes                TEXT,
  realizado_por           INT,
  realizado_em            DATETIME NOT NULL DEFAULT NOW(),
  FOREIGN KEY (id_ativo) REFERENCES ativos(id) ON DELETE CASCADE,
  FOREIGN KEY (realizado_por) REFERENCES usuarios(id) ON DELETE SET NULL
);

-- Notificações e alertas
CREATE TABLE IF NOT EXISTS notificacoes (
  id        INT AUTO_INCREMENT PRIMARY KEY,
  tipo      VARCHAR(50) NOT NULL,
  titulo    VARCHAR(200) NOT NULL,
  mensagem  TEXT NOT NULL,
  lida      TINYINT(1) NOT NULL DEFAULT 0,
  criada_em DATETIME NOT NULL DEFAULT NOW()
);

-- ──────────────────────────────────────────────
-- DADOS INICIAIS
-- ──────────────────────────────────────────────

-- Usuário admin padrão (senha: admin123)
INSERT INTO usuarios (nome, email, senha_hash, nivel) VALUES (
  'Administrador',
  'admin@stockflow.com',
  '$2b$12$e2hlJgU2tHDJApv8xsz08.HRyXcHXtyArXJE48u31NSq3c7CpOcFG',
  'admin'
);

-- Usuário operador de exemplo (senha: operador123)
INSERT INTO usuarios (nome, email, senha_hash, nivel) VALUES (
  'Operador',
  'operador@stockflow.com',
  '$2b$12$wl/vWkOVK1cWXH27/BV0eelClQQHA9/0ydyCr6nY5IsViG7Ere4Ki',
  'operador'
);

-- Tipos de ativo padrão
INSERT INTO tipos_ativo (nome, estoque_minimo) VALUES
  ('Notebook', 2),
  ('Monitor', 2),
  ('Teclado', 3),
  ('Mouse', 3),
  ('Headset', 2),
  ('Webcam', 2),
  ('Nobreak', 1),
  ('Switch', 1),
  ('Impressora', 1),
  ('Cabo HDMI', 5);

-- Colaboradores de exemplo
INSERT INTO colaboradores (nome, email, cargo, departamento) VALUES
  ('João Silva',   'joao@empresa.com',   'Desenvolvedor Backend',  'TI'),
  ('Maria Santos', 'maria@empresa.com',  'Analista de Sistemas',   'TI'),
  ('Carlos Lima',  'carlos@empresa.com', 'Designer UX',            'Marketing'),
  ('Ana Costa',    'ana@empresa.com',    'Gerente de TI',          'TI');

-- Ativos de exemplo
INSERT INTO ativos (codigo, nome, marca, modelo, tipo, situacao, preco, data_aquisicao, data_garantia, id_colaborador, data_vinculacao, criado_por) VALUES
  ('AST-001', 'Notebook Dell Inspiron', 'Dell', 'Inspiron 15', 'Notebook', 'Em uso', 3500.00, '2024-01-10', '2026-01-10', 1, NOW(), 1),
  ('AST-002', 'Monitor LG 24"', 'LG', '24MK430H', 'Monitor', 'Em uso', 950.00, '2024-01-10', '2026-01-10', 1, NOW(), 1),
  ('AST-003', 'Notebook Lenovo ThinkPad', 'Lenovo', 'ThinkPad E14', 'Notebook', 'Em uso', 4200.00, '2024-02-15', '2026-02-15', 2, NOW(), 1),
  ('AST-004', 'Notebook Dell XPS', 'Dell', 'XPS 13', 'Notebook', 'Em estoque', 6800.00, '2024-03-01', '2026-03-01', NULL, NULL, 1),
  ('AST-005', 'Monitor Samsung 27"', 'Samsung', 'F27T450', 'Monitor', 'Em estoque', 1200.00, '2024-03-01', '2026-03-01', NULL, NULL, 1),
  ('AST-006', 'Headset Logitech H390', 'Logitech', 'H390', 'Headset', 'Em uso', 280.00, '2024-01-20', '2025-01-20', 3, NOW(), 1),
  ('AST-007', 'Switch TP-Link 8P', 'TP-Link', 'TL-SG108', 'Switch', 'Manutenção', 320.00, '2023-06-01', '2025-06-01', NULL, NULL, 1);

-- Histórico inicial para os ativos de exemplo
INSERT INTO historico_ativos (id_ativo, acao, id_colaborador_novo, detalhes, realizado_por) VALUES
  (1, 'Cadastro', NULL, 'Ativo cadastrado no sistema', 1),
  (1, 'Vinculação', 1, 'Vinculado ao colaborador João Silva', 1),
  (2, 'Cadastro', NULL, 'Ativo cadastrado no sistema', 1),
  (2, 'Vinculação', 1, 'Vinculado ao colaborador João Silva', 1),
  (3, 'Cadastro', NULL, 'Ativo cadastrado no sistema', 1),
  (3, 'Vinculação', 2, 'Vinculado ao colaborador Maria Santos', 1),
  (4, 'Cadastro', NULL, 'Ativo cadastrado no sistema', 1),
  (5, 'Cadastro', NULL, 'Ativo cadastrado no sistema', 1),
  (6, 'Cadastro', NULL, 'Ativo cadastrado no sistema', 1),
  (6, 'Vinculação', 3, 'Vinculado ao colaborador Carlos Lima', 1),
  (7, 'Cadastro', NULL, 'Ativo cadastrado no sistema', 1),
  (7, 'Manutenção', NULL, 'Enviado para manutenção: falha na porta LAN 3', 1);

-- Notificação de exemplo
INSERT INTO notificacoes (tipo, titulo, mensagem) VALUES
  ('estoque_baixo', 'Estoque baixo: Notebook', 'O estoque de Notebooks está abaixo do mínimo configurado (mínimo: 2, atual: 1).');
