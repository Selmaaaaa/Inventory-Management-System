-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: idkdb
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `produits`
--

DROP TABLE IF EXISTS `produits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produits` (
  `numSerie` int NOT NULL AUTO_INCREMENT,
  `nomProduit` varchar(20) NOT NULL,
  `descProduit` varchar(250) DEFAULT NULL,
  `prixUnitaire` int DEFAULT NULL,
  `quantiteProduit` int DEFAULT NULL,
  `seuilAlerteProduit` int DEFAULT NULL,
  `date_entree` date DEFAULT NULL,
  `date_sortie` date DEFAULT NULL,
  `imageProduit` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`numSerie`),
  CONSTRAINT `produits_chk_1` CHECK ((length(`nomProduit`) > 2))
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produits`
--

LOCK TABLES `produits` WRITE;
/*!40000 ALTER TABLE `produits` DISABLE KEYS */;
INSERT INTO `produits` VALUES (1,'Butterfly Bracelet','gold plated',320,9,3,'2022-05-02','2023-04-15',NULL),(2,'Butterfly Chain','gold plated',680,9,3,'2022-05-02','2023-04-15',NULL),(3,'Heart Earrings','gold plated with a touch of silver',740,8,4,'2023-05-01','2023-05-01',NULL),(4,'Heart Bracelet','Gold plated with a touch of silver',860,8,4,'2023-05-01','2023-05-01',NULL),(5,'Mermaid ring','Gold plated with stones',450,5,2,'2023-03-25','2023-05-01',NULL),(6,'Scorpio ring','Zodiac set , gold',360,5,2,'2023-05-01','2023-05-01',NULL),(10,'JEWL1','jew',14,5,2,'2023-05-04','2023-05-04','C:/Users/north/OneDrive/Desktop/PFA/fingerprint-scan.png');
/*!40000 ALTER TABLE `produits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `nomUser` varchar(20) NOT NULL,
  `passUser` varchar(20) NOT NULL,
  PRIMARY KEY (`idUser`),
  CONSTRAINT `users_chk_1` CHECK ((length(`nomUser`) > 2)),
  CONSTRAINT `users_chk_2` CHECK ((length(`passUser`) > 2))
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (7,'Admin','admin'),(8,'reda','190190'),(9,'dzD','123'),(10,'saa','aaaa'),(11,'aaa','aaa'),(12,'zaa','aaa');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-05  0:08:27
