-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 172.26.131.251    Database: natacion
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `informacion`
--

DROP TABLE IF EXISTS `informacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `informacion` (
  `idevento` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(80) NOT NULL,
  `idestilo` int NOT NULL,
  `idgenero` int DEFAULT NULL,
  PRIMARY KEY (`idevento`),
  KEY `idestilo` (`idestilo`),
  CONSTRAINT `informacion_ibfk_1` FOREIGN KEY (`idestilo`) REFERENCES `estilos` (`idestilo`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `informacion`
--

LOCK TABLES `informacion` WRITE;
/*!40000 ALTER TABLE `informacion` DISABLE KEYS */;
INSERT INTO `informacion` VALUES (4,'50 metros varones',2,1),(5,'100 metros varones',2,1),(6,'200 metros varones',2,1),(7,'50 metros varones',3,1),(8,'100 metros varones',3,1),(9,'50 metros varones',4,1),(10,'100 metros varones',4,1),(11,'200 metros varones',4,1),(12,'50 metros varones',5,1),(13,'100 metros varones',5,1),(14,'200 metros varones',5,1),(16,'50 metros mujeres',2,2),(17,'100 metros mujeres',2,2),(18,'200 metros mujeres',2,2),(19,'50 metros mujeres',3,2),(20,'100 metros mujeres',3,2),(21,'50 metros mujeres',4,2),(22,'100 metros mujeres',4,2),(23,'200 metros mujeres',4,2),(24,'50 metros mujeres',5,2),(25,'100 metros mujeres',5,2),(26,'200 metros mujeres',5,2);
/*!40000 ALTER TABLE `informacion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-04 22:36:55
