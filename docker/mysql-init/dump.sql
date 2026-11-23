-- MySQL dump 10.13  Distrib 8.0.46, for Linux (x86_64)
--
-- Host: localhost    Database: stockflow
-- ------------------------------------------------------
-- Server version	8.0.46-0ubuntu0.24.04.5

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `stockflow`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `stockflow` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `stockflow`;

--
-- Table structure for table `ativos`
--

DROP TABLE IF EXISTS `ativos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ativos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `nome` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `marca` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `modelo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `numero_serie` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `situacao` enum('Em estoque','Em uso','Manutenção','Desativado') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'Em estoque',
  `id_colaborador` int DEFAULT NULL,
  `tipo_aquisicao` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  `data_aquisicao` date DEFAULT NULL,
  `data_garantia` date DEFAULT NULL,
  `data_vinculacao` datetime DEFAULT NULL,
  `fornecedor` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `numero_nota_fiscal` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `localizacao` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT '1',
  `criado_em` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `criado_por` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`),
  KEY `id_colaborador` (`id_colaborador`),
  KEY `criado_por` (`criado_por`),
  CONSTRAINT `ativos_ibfk_1` FOREIGN KEY (`id_colaborador`) REFERENCES `colaboradores` (`id`) ON DELETE SET NULL,
  CONSTRAINT `ativos_ibfk_2` FOREIGN KEY (`criado_por`) REFERENCES `usuarios` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ativos`
--

LOCK TABLES `ativos` WRITE;
/*!40000 ALTER TABLE `ativos` DISABLE KEYS */;
INSERT INTO `ativos` VALUES (1,'AST-001','Notebook Dell Inspiron','Dell','Inspiron 15',NULL,'Notebook','Em uso',1,NULL,3500.00,'2024-01-10','2026-01-10','2026-05-15 23:06:45',NULL,NULL,NULL,1,'2026-05-15 23:06:45',1),(2,'AST-002','Monitor LG 24\"','LG','24MK430H',NULL,'Monitor','Em uso',1,NULL,950.00,'2024-01-10','2026-01-10','2026-05-15 23:06:45',NULL,NULL,NULL,1,'2026-05-15 23:06:45',1),(3,'AST-003','Notebook Lenovo ThinkPad','Lenovo','ThinkPad E14',NULL,'Notebook','Em uso',2,NULL,4200.00,'2024-02-15','2026-02-15','2026-05-15 23:06:45',NULL,NULL,NULL,1,'2026-05-15 23:06:45',1),(4,'AST-004','Notebook Dell XPS','Dell','XPS 13',NULL,'Notebook','Em estoque',NULL,NULL,6800.00,'2024-03-01','2026-03-01',NULL,NULL,NULL,NULL,1,'2026-05-15 23:06:45',1),(5,'AST-005','Monitor Samsung 27\"','Samsung','F27T450',NULL,'Monitor','Em estoque',NULL,NULL,1200.00,'2024-03-01','2026-03-01',NULL,NULL,NULL,NULL,1,'2026-05-15 23:06:45',1),(6,'AST-006','Headset Logitech H390','Logitech','H390',NULL,'Headset','Em uso',3,NULL,280.00,'2024-01-20','2025-01-20','2026-05-15 23:06:45',NULL,NULL,NULL,1,'2026-05-15 23:06:45',1),(7,'AST-007','Switch TP-Link 8P','TP-Link','TL-SG108',NULL,'Switch','Manutenção',NULL,NULL,320.00,'2023-06-01','2025-06-01',NULL,NULL,NULL,NULL,1,'2026-05-15 23:06:45',1);
/*!40000 ALTER TABLE `ativos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colaboradores`
--

DROP TABLE IF EXISTS `colaboradores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colaboradores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cargo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `departamento` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` enum('ativo','desligado') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'ativo',
  `criado_em` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colaboradores`
--

LOCK TABLES `colaboradores` WRITE;
/*!40000 ALTER TABLE `colaboradores` DISABLE KEYS */;
INSERT INTO `colaboradores` VALUES (1,'João Silva','joao@empresa.com','Desenvolvedor Backend','TI','ativo','2026-05-15 23:06:45'),(2,'Maria Santos','maria@empresa.com','Analista de Sistemas','TI','ativo','2026-05-15 23:06:45'),(3,'Carlos Lima','carlos@empresa.com','Designer UX','Marketing','ativo','2026-05-15 23:06:45'),(4,'Ana Costa','ana@empresa.com','Gerente de TI','TI','ativo','2026-05-15 23:06:45');
/*!40000 ALTER TABLE `colaboradores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historico_ativos`
--

DROP TABLE IF EXISTS `historico_ativos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historico_ativos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_ativo` int NOT NULL,
  `acao` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_colaborador_anterior` int DEFAULT NULL,
  `id_colaborador_novo` int DEFAULT NULL,
  `detalhes` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `realizado_por` int DEFAULT NULL,
  `realizado_em` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_ativo` (`id_ativo`),
  KEY `realizado_por` (`realizado_por`),
  CONSTRAINT `historico_ativos_ibfk_1` FOREIGN KEY (`id_ativo`) REFERENCES `ativos` (`id`) ON DELETE CASCADE,
  CONSTRAINT `historico_ativos_ibfk_2` FOREIGN KEY (`realizado_por`) REFERENCES `usuarios` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historico_ativos`
--

LOCK TABLES `historico_ativos` WRITE;
/*!40000 ALTER TABLE `historico_ativos` DISABLE KEYS */;
INSERT INTO `historico_ativos` VALUES (1,1,'Cadastro',NULL,NULL,'Ativo cadastrado no sistema',1,'2026-05-15 23:06:45'),(2,1,'Vinculação',NULL,1,'Vinculado ao colaborador João Silva',1,'2026-05-15 23:06:45'),(3,2,'Cadastro',NULL,NULL,'Ativo cadastrado no sistema',1,'2026-05-15 23:06:45'),(4,2,'Vinculação',NULL,1,'Vinculado ao colaborador João Silva',1,'2026-05-15 23:06:45'),(5,3,'Cadastro',NULL,NULL,'Ativo cadastrado no sistema',1,'2026-05-15 23:06:45'),(6,3,'Vinculação',NULL,2,'Vinculado ao colaborador Maria Santos',1,'2026-05-15 23:06:45'),(7,4,'Cadastro',NULL,NULL,'Ativo cadastrado no sistema',1,'2026-05-15 23:06:45'),(8,5,'Cadastro',NULL,NULL,'Ativo cadastrado no sistema',1,'2026-05-15 23:06:45'),(9,6,'Cadastro',NULL,NULL,'Ativo cadastrado no sistema',1,'2026-05-15 23:06:45'),(10,6,'Vinculação',NULL,3,'Vinculado ao colaborador Carlos Lima',1,'2026-05-15 23:06:45'),(11,7,'Cadastro',NULL,NULL,'Ativo cadastrado no sistema',1,'2026-05-15 23:06:45'),(12,7,'Manutenção',NULL,NULL,'Enviado para manutenção: falha na porta LAN 3',1,'2026-05-15 23:06:45');
/*!40000 ALTER TABLE `historico_ativos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notificacoes`
--

DROP TABLE IF EXISTS `notificacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notificacoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `titulo` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `mensagem` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `lida` tinyint(1) NOT NULL DEFAULT '0',
  `criada_em` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificacoes`
--

LOCK TABLES `notificacoes` WRITE;
/*!40000 ALTER TABLE `notificacoes` DISABLE KEYS */;
INSERT INTO `notificacoes` VALUES (1,'estoque_baixo','Estoque baixo: Notebook','O estoque de Notebooks está abaixo do mínimo configurado (mínimo: 2, atual: 1).',0,'2026-05-15 23:06:45');
/*!40000 ALTER TABLE `notificacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opcoes_select`
--

DROP TABLE IF EXISTS `opcoes_select`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opcoes_select` (
  `id` int NOT NULL AUTO_INCREMENT,
  `contexto` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `valor` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `criado_por` int DEFAULT NULL,
  `criado_em` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `contexto` (`contexto`,`valor`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opcoes_select`
--

LOCK TABLES `opcoes_select` WRITE;
/*!40000 ALTER TABLE `opcoes_select` DISABLE KEYS */;
INSERT INTO `opcoes_select` VALUES (1,'tipo_ativo','Notebook',NULL,'2026-05-28 08:15:41'),(2,'tipo_ativo','Monitor',NULL,'2026-05-28 08:15:41'),(3,'tipo_ativo','Teclado',NULL,'2026-05-28 08:15:41'),(4,'tipo_ativo','Mouse',NULL,'2026-05-28 08:15:41'),(5,'tipo_ativo','Headset',NULL,'2026-05-28 08:15:41'),(6,'tipo_ativo','Webcam',NULL,'2026-05-28 08:15:41'),(7,'tipo_ativo','Nobreak',NULL,'2026-05-28 08:15:41'),(8,'tipo_ativo','Switch',NULL,'2026-05-28 08:15:41'),(9,'tipo_ativo','Impressora',NULL,'2026-05-28 08:15:41'),(10,'tipo_ativo','Cabo HDMI',NULL,'2026-05-28 08:15:41'),(11,'tipo_aquisicao','Compra',NULL,'2026-05-28 08:15:41'),(12,'tipo_aquisicao','Comodato',NULL,'2026-05-28 08:15:41'),(13,'tipo_aquisicao','Leasing',NULL,'2026-05-28 08:15:41'),(14,'tipo_aquisicao','Doação',NULL,'2026-05-28 08:15:41'),(15,'localizacao','Escritório',NULL,'2026-05-28 08:15:41'),(16,'localizacao','Sala de TI',NULL,'2026-05-28 08:15:41'),(17,'localizacao','Almoxarifado',NULL,'2026-05-28 08:15:41'),(18,'localizacao','Home Office',NULL,'2026-05-28 08:15:41'),(19,'cargo','Analista de TI',NULL,'2026-05-28 08:15:41'),(20,'cargo','Desenvolvedor',NULL,'2026-05-28 08:15:41'),(21,'cargo','Designer',NULL,'2026-05-28 08:15:41'),(22,'cargo','Gerente',NULL,'2026-05-28 08:15:41'),(23,'cargo','Estagiário',NULL,'2026-05-28 08:15:41'),(24,'departamento','TI',NULL,'2026-05-28 08:15:41'),(25,'departamento','RH',NULL,'2026-05-28 08:15:41'),(26,'departamento','Marketing',NULL,'2026-05-28 08:15:41'),(27,'departamento','Financeiro',NULL,'2026-05-28 08:15:41'),(28,'departamento','Operações',NULL,'2026-05-28 08:15:41');
/*!40000 ALTER TABLE `opcoes_select` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos_ativo`
--

DROP TABLE IF EXISTS `tipos_ativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_ativo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `estoque_minimo` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_ativo`
--

LOCK TABLES `tipos_ativo` WRITE;
/*!40000 ALTER TABLE `tipos_ativo` DISABLE KEYS */;
INSERT INTO `tipos_ativo` VALUES (1,'Notebook',2),(2,'Monitor',2),(3,'Teclado',3),(4,'Mouse',3),(5,'Headset',2),(6,'Webcam',2),(7,'Nobreak',1),(8,'Switch',1),(9,'Impressora',1),(10,'Cabo HDMI',5);
/*!40000 ALTER TABLE `tipos_ativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `senha_hash` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `nivel` enum('admin','operador') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'operador',
  `ativo` tinyint(1) NOT NULL DEFAULT '1',
  `criado_em` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ultimo_acesso` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Administrador','admin@stockflow.com','$2b$12$bMvtSTvfiSm2kkH7qCMmTe3Uah0lxazZX2ZTAr41.Jsqenfz1A0HK','admin',1,'2026-05-15 23:06:45','2026-11-23 07:41:24'),(2,'Operador','operador@stockflow.com','$2b$12$ofz1Mb8f8Bso.WoYH1X7neV6VbZrkhRXQDLOs3hpxOlfOO6iJSF1a','operador',1,'2026-05-15 23:06:45','2026-11-23 07:35:21');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-23  7:59:28
