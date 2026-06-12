# 1. Documento de Requisitos

Sistema **Stock Flow** — Sistema de Gestão de Ativos de TI

Este documento especifica os requisitos funcionais, não funcionais e as regras de negócio que regem o sistema Stock Flow.

---

## 1.1. Requisitos Funcionais (RF)

Os requisitos funcionais descrevem as funcionalidades que o sistema deve oferecer aos seus usuários.

| Código | Requisito |
|--------|-----------|
| RF01 | O sistema deve permitir login com e-mail e senha. |
| RF02 | O sistema deve diferenciar usuários por nível de acesso (administrador e operador). |
| RF03 | O sistema deve permitir o cadastro de ativos de TI. |
| RF04 | O sistema deve gerar um código único automático para cada ativo (AST-001, AST-002, ...). |
| RF05 | O sistema deve permitir vincular um ativo a um colaborador. |
| RF06 | O sistema deve permitir desvincular um ativo de um colaborador. |
| RF07 | O sistema deve registrar o histórico de todas as movimentações de um ativo. |
| RF08 | O sistema deve permitir enviar um ativo para manutenção. |
| RF09 | O sistema deve permitir retornar um ativo da manutenção para o estoque. |
| RF10 | O sistema deve permitir desativar um ativo. |
| RF11 | O sistema deve exibir um dashboard com indicadores em tempo real. |
| RF12 | O sistema deve emitir alertas quando o estoque de um tipo de ativo estiver abaixo do mínimo configurado. |
| RF13 | O sistema deve emitir alertas de garantias vencendo nos próximos 30 dias. |
| RF14 | O sistema deve gerar relatórios exportáveis em PDF. |
| RF15 | O sistema deve calcular e exibir a Curva ABC do inventário. |
| RF16 | O sistema deve permitir o cadastro e o gerenciamento de colaboradores. |
| RF17 | O sistema deve permitir o gerenciamento de usuários do sistema (exclusivo para administradores). |
| RF18 | O sistema deve permitir adicionar e remover opções dos campos de seleção dinamicamente. |
| RF19 | O sistema deve suportar modo escuro e claro. |
| RF20 | O sistema deve manter a sessão autenticada por meio de JWT. |
| RF21 | O sistema deve exibir o detalhamento completo de um ativo, incluindo seu histórico de movimentações. |
| RF22 | O sistema deve permitir a edição dos dados cadastrais de um ativo. |
| RF23 | O sistema deve apresentar páginas de erro personalizadas para acessos não autorizados (403) e recursos inexistentes (404). |

---

## 1.2. Requisitos Não Funcionais (RNF)

Os requisitos não funcionais descrevem atributos de qualidade e restrições técnicas do sistema.

| Código | Requisito |
|--------|-----------|
| RNF01 | O sistema deve ser acessível via navegador web. |
| RNF02 | O sistema deve responder às requisições em menos de 3 segundos. |
| RNF03 | As senhas devem ser armazenadas com hash bcrypt. |
| RNF04 | O token JWT deve expirar em 24 horas. |
| RNF05 | O sistema deve estar disponível 24 horas por dia por meio da plataforma Railway. |
| RNF06 | O banco de dados deve ser MySQL 8.0. |
| RNF07 | O sistema deve funcionar nos navegadores Chrome, Firefox e Edge. |
| RNF08 | A interface deve ser responsiva, adaptando-se a diferentes tamanhos de tela. |
| RNF09 | O código-fonte deve estar versionado no GitHub. |
| RNF10 | O deploy deve ser automático a cada push no repositório GitHub. |
| RNF11 | O token de autenticação deve ser armazenado em cookie HTTP-only, mitigando ataques de roubo de sessão via JavaScript. |
| RNF12 | A interface deve seguir um padrão visual consistente em todas as telas. |

---

## 1.3. Regras de Negócio (RN)

As regras de negócio definem as restrições e políticas que governam o comportamento do sistema.

| Código | Regra |
|--------|-------|
| RN01 | Apenas usuários com nível administrador podem cadastrar, editar e desativar ativos. |
| RN02 | Apenas usuários com nível administrador podem cadastrar e editar colaboradores. |
| RN03 | Um ativo só pode ser vinculado a um colaborador por vez. |
| RN04 | Um ativo em manutenção não pode ser vinculado a um colaborador. |
| RN05 | Um ativo desativado não aparece no inventário ativo. |
| RN06 | O código do ativo é gerado automaticamente e não pode ser alterado. |
| RN07 | Todo evento de movimentação de ativo deve ser registrado no histórico. |
| RN08 | O estoque mínimo por tipo de ativo é configurável pelo administrador. |
| RN09 | A Curva ABC classifica os itens em três categorias: A (até 80% do valor acumulado), B (até 95%) e C (valor restante). |
| RN10 | O operador pode visualizar ativos e colaboradores, mas não pode realizar alterações. |
| RN11 | O alerta de estoque baixo é disparado quando a quantidade de ativos em estoque de um tipo for inferior ao estoque mínimo configurado. |
| RN12 | O alerta de garantia é disparado para ativos cuja data de garantia esteja dentro dos próximos 30 dias. |
