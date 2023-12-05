-- MySQL dump 10.13  Distrib 8.0.31, for macos12.6 (x86_64)
--
-- Host: localhost    Database: hexa_suites
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.27-MariaDB

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
-- Table structure for table `accounting_applyto`
--

DROP TABLE IF EXISTS `accounting_applyto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounting_applyto` (
  `id` varchar(120) NOT NULL,
  `code` varchar(120) NOT NULL,
  `created_by` varchar(120) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_by` varchar(120) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `item_id` varchar(120) DEFAULT NULL,
  `pricing_rule_id` varchar(120) NOT NULL,
  `supplier_id` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounting_applyto_item_id_4ca18f26_fk_stock_item_id` (`item_id`),
  KEY `accounting_applyto_pricing_rule_id_8e334074_fk_accountin` (`pricing_rule_id`),
  KEY `accounting_applyto_supplier_id_bed5f6eb_fk_buying_supplier_id` (`supplier_id`),
  CONSTRAINT `accounting_applyto_item_id_4ca18f26_fk_stock_item_id` FOREIGN KEY (`item_id`) REFERENCES `stock_item` (`id`),
  CONSTRAINT `accounting_applyto_pricing_rule_id_8e334074_fk_accountin` FOREIGN KEY (`pricing_rule_id`) REFERENCES `accounting_pricingrule` (`id`),
  CONSTRAINT `accounting_applyto_supplier_id_bed5f6eb_fk_buying_supplier_id` FOREIGN KEY (`supplier_id`) REFERENCES `buying_supplier` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounting_applyto`
--

LOCK TABLES `accounting_applyto` WRITE;
/*!40000 ALTER TABLE `accounting_applyto` DISABLE KEYS */;
INSERT INTO `accounting_applyto` VALUES ('031afa671558457fa5c7ef51ed099754','APLY-PRC-RLE_000000004','shiela','2022-08-22 18:39:48.678832','shiela','2022-08-22 18:39:48.678930',NULL,'253ed2ed1d3c4b2fa0e5704f96aa50e6',NULL),('20e8b5aec7624c9ca1f48f708a3926f8','APLY-PRC-RLE_000000005','shiela','2022-08-22 18:40:08.607968','shiela','2022-08-22 18:40:08.608054',NULL,'a995714ba7c6498ba0a89483a9f01dd2','aba3687ce47b45eaa77a4d35a2177671'),('5557a44b6ce348568283ce39c566f87e','APLY-PRC-RLE_000000002','shiela','2022-08-22 18:29:44.076426','shiela','2022-08-22 18:29:44.076512',NULL,'3d96cd249b8449ddb223f14e344e213b',NULL),('6708ccbfa6bb4d35805369a080e22dd9','APLY-PRC-RLE_000000003','shiela','2022-08-22 18:39:00.709285','shiela','2022-08-22 18:39:00.709364',NULL,'213d034f357449359e0a3625fc835bc8',NULL),('e48a8ac373cb48b5a42e517197e4c868','APLY-PRC-RLE_000000001','shiela','2022-08-22 18:05:59.300131','shiela','2022-08-22 18:05:59.300239',NULL,'39817c935d614ae6945cb582b2a89c60',NULL);
/*!40000 ALTER TABLE `accounting_applyto` ENABLE KEYS */;
UNLOCK TABLES;
