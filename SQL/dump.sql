-- MySQL dump 10.13  Distrib 5.7.26, for osx10.9 (x86_64)
--
-- Host: localhost    Database: simple_e_commerce
-- ------------------------------------------------------
-- Server version	5.7.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE simple_e_commerce CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use simple_e_commerce;

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Category` (
  `cate_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cate_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cate_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
INSERT INTO `Category` VALUES ('cate00001','CateA'),('cate00002','CateB'),('cate00003','CateC'),('cate00004','CateD'),('cate00005','CateE'),('cate00006','CateF'),('cate00007','CateG'),('cate00008','CateH'),('cate00009','CateI'),('cate00010','CateJ');
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer` (
  `cust_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cust_first_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cust_last_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES ('cust00001','Andy','Ho'),('cust00002','Roger','Lee'),('cust00003','Ethan','Hou'),('cust00004','Jesse','Hung'),('cust00005','Mike','Sun'),('cust00006','Peter','Sun'),('cust00007','Yuan','Chen'),('cust00008','Kevin','Huang'),('cust00009','Cathy','Lee');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OrderDetail`
--

DROP TABLE IF EXISTS `OrderDetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OrderDetail` (
  `ord_id` int(11) NOT NULL,
  `prod_id` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `amount` int(11) DEFAULT NULL,
  PRIMARY KEY (`ord_id`,`prod_id`),
  KEY `prod_id` (`prod_id`),
  CONSTRAINT `orderdetail_ibfk_1` FOREIGN KEY (`ord_id`) REFERENCES `ShoppingOrder` (`ord_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `orderdetail_ibfk_2` FOREIGN KEY (`prod_id`) REFERENCES `Product` (`prod_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrderDetail`
--

LOCK TABLES `OrderDetail` WRITE;
/*!40000 ALTER TABLE `OrderDetail` DISABLE KEYS */;
INSERT INTO `OrderDetail` VALUES (1,'prod00001',10),(1,'prod00002',5),(1,'prod00003',2),(1,'prod00004',1),(2,'prod00003',1),(2,'prod00006',2),(2,'prod00008',3),(2,'prod00009',4),(3,'prod00005',5),(3,'prod00010',5),(4,'prod00002',5),(4,'prod00005',5),(5,'prod00001',8),(5,'prod00002',6),(5,'prod00003',4);
/*!40000 ALTER TABLE `OrderDetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Product` (
  `prod_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `prod_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`prod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES ('prod00001','Product 1'),('prod00002','Product 2'),('prod00003','Product 3'),('prod00004','Product 4'),('prod00005','Product 5'),('prod00006','Product 6'),('prod00007','Product 7'),('prod00008','Product 8'),('prod00009','Product 9'),('prod00010','Product 10'),('prod00011','Product 11'),('prod00012','Product 12'),('prod00013','Product 13'),('prod00014','Product 14'),('prod00015','Product 15'),('prod00016','Product 16'),('prod00017','Product 17'),('prod00018','Product 18'),('prod00019','Product 19'),('prod00020','Product 20');
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProductCategory`
--

DROP TABLE IF EXISTS `ProductCategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProductCategory` (
  `prod_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cate_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`prod_id`,`cate_id`),
  KEY `cate_id` (`cate_id`),
  CONSTRAINT `productcategory_ibfk_1` FOREIGN KEY (`prod_id`) REFERENCES `Product` (`prod_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `productcategory_ibfk_2` FOREIGN KEY (`cate_id`) REFERENCES `Category` (`cate_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProductCategory`
--

LOCK TABLES `ProductCategory` WRITE;
/*!40000 ALTER TABLE `ProductCategory` DISABLE KEYS */;
INSERT INTO `ProductCategory` VALUES ('prod00001','cate00001'),('prod00003','cate00001'),('prod00006','cate00001'),('prod00007','cate00001'),('prod00011','cate00001'),('prod00001','cate00002'),('prod00002','cate00002'),('prod00006','cate00002'),('prod00007','cate00002'),('prod00012','cate00002'),('prod00001','cate00003'),('prod00003','cate00003'),('prod00007','cate00003'),('prod00013','cate00003'),('prod00002','cate00004'),('prod00004','cate00004'),('prod00014','cate00004'),('prod00002','cate00005'),('prod00005','cate00005'),('prod00015','cate00005'),('prod00002','cate00006'),('prod00006','cate00006'),('prod00016','cate00006'),('prod00004','cate00007'),('prod00007','cate00007'),('prod00017','cate00007'),('prod00004','cate00008'),('prod00008','cate00008'),('prod00018','cate00008'),('prod00005','cate00009'),('prod00007','cate00009'),('prod00009','cate00009'),('prod00019','cate00009'),('prod00005','cate00010'),('prod00007','cate00010'),('prod00010','cate00010'),('prod00020','cate00010');
/*!40000 ALTER TABLE `ProductCategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ShoppingOrder`
--

DROP TABLE IF EXISTS `ShoppingOrder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ShoppingOrder` (
  `ord_id` int(11) NOT NULL AUTO_INCREMENT,
  `cust_id` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`ord_id`),
  KEY `cust_id` (`cust_id`),
  KEY `timestamp` (`timestamp`),
  CONSTRAINT `shoppingorder_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `Customer` (`cust_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ShoppingOrder`
--

LOCK TABLES `ShoppingOrder` WRITE;
/*!40000 ALTER TABLE `ShoppingOrder` DISABLE KEYS */;
INSERT INTO `ShoppingOrder` VALUES (1,'cust00001','2019-08-24 22:25:55','Waiting for Delivery'),(2,'cust00002','2019-08-24 22:27:03','Waiting for Delivery'),(3,'cust00003','2019-08-24 22:28:20','On It\'s Way'),(4,'cust00001','2019-08-24 22:30:02','Delivered'),(5,'cust00006','2019-08-26 01:11:24','On It\'s Way');
/*!40000 ALTER TABLE `ShoppingOrder` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-26 18:04:07
