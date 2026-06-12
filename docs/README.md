# Documentação Técnica — Stock Flow

Sistema de Gestão de Ativos de TI

## Sobre o projeto

O **Stock Flow** é um sistema web para gestão de ativos de Tecnologia da Informação, desenvolvido como Trabalho de Conclusão de Curso (TCC). O sistema permite o controle completo do ciclo de vida de ativos de TI — cadastro, vinculação a colaboradores, manutenção, histórico de movimentações, alertas de estoque e garantia, relatórios em PDF e análise de inventário por Curva ABC.

- **Sistema em produção:** https://tcc-production-99b7.up.railway.app
- **Repositório:** https://github.com/miguelmagsilveira-max/TCC

## Índice da documentação

| # | Documento | Descrição |
|---|-----------|-----------|
| 1 | [Requisitos](1-requisitos.md) | Requisitos funcionais, não funcionais e regras de negócio |
| 2 | [Arquitetura](2-arquitetura.md) | Visão arquitetural, camadas, fluxo de requisição e tecnologias |
| 3 | [Banco de Dados](3-banco-de-dados.md) | Diagrama ER, descrição das tabelas e dicionário de dados |
| 4 | [Casos de Uso](4-casos-de-uso.md) | Atores, casos de uso detalhados e diagrama |
| 5 | [Manual do Usuário](5-manual-do-usuario.md) | Guia de utilização do sistema passo a passo |
| 6 | [Testes](6-testes.md) | Plano de testes, casos de teste e resultados |

## Informações do projeto

| Campo | Valor |
|-------|-------|
| Sistema | Stock Flow — Sistema de Gestão de Ativos de TI |
| Curso | Técnico em Desenvolvimento de Sistemas |
| Instituição | ETEC de São José dos Campos — Centro Paula Souza |
| Orientadora | Professora Patrícia Simões |
| Ano/Semestre | 2º Semestre de 2026 |

## Integrantes

- Amanda Braga
- Caio Gonçalves
- Eduardo De Paula
- Gustavo Abreu
- Jéssica Rodrigues
- Miguel Magalhães
- Nícolas Braga

## Stack tecnológica

- **Backend:** Python 3.12 + FastAPI
- **Banco de dados:** MySQL 8.0
- **Frontend:** HTML + Tailwind CSS + JavaScript
- **Templates:** Jinja2 (renderização server-side)
- **Autenticação:** JWT em cookie HTTP-only
- **Deploy:** Railway (integração com GitHub para deploy automático)
