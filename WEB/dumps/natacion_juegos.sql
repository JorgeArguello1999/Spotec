-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: natacion
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
-- Table structure for table `juegos`
--

DROP TABLE IF EXISTS `juegos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `juegos` (
  `idevento` int DEFAULT NULL,
  `serie` int DEFAULT NULL,
  `idjugador` int DEFAULT NULL,
  `tiempo_juego` time DEFAULT NULL,
  KEY `idevento` (`idevento`),
  KEY `idjugador` (`idjugador`),
  CONSTRAINT `juegos_ibfk_1` FOREIGN KEY (`idevento`) REFERENCES `informacion` (`idevento`),
  CONSTRAINT `juegos_ibfk_2` FOREIGN KEY (`idjugador`) REFERENCES `jugadores` (`idjugador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juegos`
--

LOCK TABLES `juegos` WRITE;
/*!40000 ALTER TABLE `juegos` DISABLE KEYS */;
INSERT INTO `juegos` VALUES (21,1,4,NULL),(22,1,4,NULL),(26,1,4,NULL),(21,1,5,NULL),(22,1,5,NULL),(24,1,5,NULL),(25,1,5,NULL),(19,1,6,NULL),(20,1,6,NULL),(24,1,6,NULL),(25,1,6,NULL),(16,1,7,NULL),(17,1,7,NULL),(18,1,7,NULL),(23,1,7,NULL),(4,1,8,NULL),(5,1,8,NULL),(7,1,8,NULL),(8,1,8,NULL),(4,1,9,NULL),(9,1,9,NULL),(10,1,9,NULL),(11,1,9,NULL),(5,1,10,NULL),(12,1,10,NULL),(13,1,10,NULL),(7,1,11,NULL),(9,1,11,NULL),(10,1,11,NULL),(12,1,11,NULL);
/*!40000 ALTER TABLE `juegos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-04  6:25:27
