-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-03-2025 a las 04:07:40
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tiendamotos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `idcarrito` int(11) NOT NULL,
  `idproducto` int(11) DEFAULT NULL,
  `iduser` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`idcarrito`, `idproducto`, `iduser`, `cantidad`) VALUES
(1, 1, 2, 1),
(2, 3, 2, 5),
(4, 4, 2, 9),
(5, 2, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `idcategoria` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `img1` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`idcategoria`, `nombre`, `img1`) VALUES
(1, 'FRENOS', 'categoria.png'),
(2, 'ACEITES', 'categoria.png'),
(3, 'GUAYAS', 'categoria.png'),
(4, 'GENERICO', 'categoria.png'),
(5, 'bujias', 'categoria.png'),
(30, 'guantes', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `idproducto` int(11) NOT NULL,
  `precio` float NOT NULL,
  `descripcion` varchar(300) DEFAULT NULL,
  `img1` varchar(300) DEFAULT NULL,
  `img2` varchar(300) DEFAULT NULL,
  `img3` varchar(300) DEFAULT NULL,
  `img4` varchar(300) DEFAULT NULL,
  `idcategoria` int(11) DEFAULT NULL,
  `nombre` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`idproducto`, `precio`, `descripcion`, `img1`, `img2`, `img3`, `img4`, `idcategoria`, `nombre`) VALUES
(1, 50000, 'PASTILLAS ', 'fe2ec5ed72014bd0ac4f1e0e975b9235.jfif', 'productos.png', 'productos.png', 'productos.png', 1, ''),
(2, 3000, '', 'd154be17d578460f8964690d3a52160e.jfif', 'productos.png', 'productos.png', 'productos.png', 3, ''),
(3, 25000, 'BOMBA DE AIRE PARA MOTO Y BALONES', 'productos.png', '0153a0f33db34d66a3ad47c4a34c16d1.jfif', 'productos.png', 'productos.png', 1, ''),
(4, 12000, 'bujia temperatura', '5d9fec73f3034520a78f40e589ae5c07.jfif', '69fa727f5b3748768d721df0ac4f072b.jfif', 'productos.png', 'productos.png', 5, ''),
(1000, 6000, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA BLANCO REFUERZO PALMA\r'),
(1001, 5700, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO PALMA\r'),
(1002, 5300, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA SENCILLO\r'),
(1003, 7500, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO COMPLETO VAQUETA\r'),
(1004, 6700, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO COMPLETO CARNAZA\r'),
(1005, 6000, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO EN PALMA VAQUETA CON REFUERZO DEDO INDICE Y PULGAR\r'),
(1006, 5900, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO EN PALMA MANGA CORTA EN VAQUETA\r'),
(1007, 8500, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO EN PALMA MANGA LARGA EN VAQUETA\r'),
(1008, 7000, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO PALMA EN VAQUETA MANGA LARGA EN CARNAZA\r'),
(1009, 5200, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO PALMA EN CARNAZA\r'),
(1010, 6200, 'AnDy', '', '0', '0', '', 30, 'GUANTE VAQUETA EXTRA LARGO REFUERZO COMPLETO EN VAQUETA\r'),
(1011, 5500, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO MIXTO REFUERZO EN PALMA CARNAZA\r'),
(1012, 6200, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO EXTRA GRANDE MIXTO REFUERZO COMPLETO EN VAQUETA\r'),
(1013, 7500, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO REFUERZO EN PALMA Y MANGA EN VAQUETA 3/4\r'),
(1014, 7200, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO SENCILLO MANGA 3/4 VAQUETA\r'),
(1015, 6700, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO REFORZADO EN PALMA VAQUETA Y MANGA EN CARNAZA 3/4\r'),
(1016, 5500, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO CARNAZA REFUERZO EN VAQUETA COMPLETO\r'),
(1017, 5120, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO CARNAZA REFUERZO COMPLETO TRANSEJES\r'),
(1018, 4000, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO CARNAZA REFUERZO PALMA EN CARNAZA\r'),
(1019, 6500, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO SENCILLO MANGA 3/4 CARNAZA\r'),
(1020, 14700, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO SENCILLO PEGADO A LA MANGA SOLDADOR\r'),
(1021, 5900, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO BARRIDO\r'),
(1022, 7500, 'AnDy', '', '0', '0', '', 30, 'GUANTE INGENIERO RECOLECCION\r'),
(1023, 12000, 'AnDy', '', '0', '0', '', 30, 'GUANTE ESPECIAL PALMERO VAQUETA REFUERZO COMPLETO Y MANGA EN VAQUETA\r'),
(1024, 6000, 'AnDy', '', '0', '0', '', 30, 'GUANTE PALMERO CARNAZA REFUERCO COMPLETO VAQUETA CORTO\r'),
(1025, 7500, 'AnDy', '', '0', '0', '', 30, 'GUANTE PALMERO CARNAZA REFUERZO COMPLETO EN VAQUETA MANGA LARGA\r'),
(1026, 7000, 'AnDy', '', '0', '0', '', 30, 'GUANTE PALMERO CARNAZA REFUERZO COMPLETO EN VAQUETA MANGA 3/4\r'),
(1027, 8700, 'AnDy', '', '0', '0', '', 30, 'GUANTE PALMERO CARNAZA REFUERZO COMPLETO EN TULA\r'),
(1028, 5500, 'AnDy', '', '0', '0', '', 30, 'GUANTE CARNAZA PALMERO REFUERZO COMPLETO EN CARNAZA MANGA CORTA\r'),
(1029, 6000, 'AnDy', '', '0', '0', '', 30, 'GUANTE CARNAZA REFUERZO COMPLETO CARNAZA MANGA LARGA\r'),
(1030, 9500, 'AnDy', '', '0', '0', '', 30, 'GUANTE SOLDADOR SENCILLO EN CARNAZA\r'),
(1031, 12000, 'AnDy', '', '0', '0', '', 30, 'GUANTE SOLDADOR CARNAZA REFUERZO COMPLETO EN VAQUETA\r'),
(1032, 4800, 'AnDy', '', '0', '0', '', 30, 'GUANTE CICLISTA MIXTO\r'),
(1033, 8000, 'AnDy', '', '0', '0', '', 30, 'GUANTE CICLISTA EN VAQUETA\r'),
(1034, 7500, 'AnDy', '', '0', '0', '', 30, 'GUANTE CICLISTA VAQUETA REFUERZO VAQUETA CON ESPUMA\r'),
(1035, 10000, 'AnDy', '', '0', '0', '', 30, 'GUANTE PANADERO\r'),
(1036, 15000, 'AnDy', '', '0', '0', '', 30, 'GUANTE PARA MOTO\r'),
(1037, 9500, 'AnDy', '', '0', '0', '', 30, 'POLAINA EN CARNAZA CORTA\r'),
(1038, 12000, 'AnDy', '', '0', '0', '', 30, 'POLAINA EN CARNAZA LARGA\r'),
(1039, 34000, 'AnDy', '', '0', '0', '', 30, 'POLAINA TULA\r'),
(1040, 9500, 'AnDy', '', '0', '0', '', 30, 'PETO CARNAZA 90 X 60\r'),
(1041, 19000, 'AnDy', '', '0', '0', '', 30, 'PETO VAQUETA 90 X 60\r'),
(1042, 25000, 'AnDy', '', '0', '0', '', 30, 'PETO VAQUETA 60 X 120\r'),
(1043, 12000, 'AnDy', '', '0', '0', '', 30, 'PETO CARNAZA 60 X 120\r'),
(1044, 28000, 'AnDy', '', '0', '0', '', 30, 'PETO EN TULA 90 X 60\r'),
(1045, 19000, 'AnDy', '', '0', '0', '', 30, 'PETO CARNAZA DOBLE 90 X 60\r'),
(1046, 29000, 'AnDy', '', '0', '0', '', 30, 'CHAQUETA VAQUETA SOLDADOR\r'),
(1047, 300, 'AnDy', '', '0', '0', '', 30, 'TAPABOCAS COMPUTELL\r'),
(1048, 9000, 'AnDy', '', '0', '0', '', 30, 'MANGA CARNAZA\r'),
(1049, 19000, 'AnDy', '', '0', '0', '', 30, 'MANGA VAQUETA\r'),
(1050, 28000, 'AnDy', '', '0', '0', '', 30, 'MANGA TULA\r'),
(1051, 5000, 'Administrador d', '', '0', '0', '', 30, 'PETICION HORUN MOTORIZADO\r'),
(1052, 40000, 'Administrador d', '1000', '0', '0', 'a12', 30, 'BODIARMO\r'),
(1053, 130000, 'Administrador d', '', '0', '0', 'I1', 30, 'OSOS\r'),
(1054, 11000, 'Administrador d', '', '0', '0', '', 30, 'CAJAS ZAPATERA\r'),
(1055, 10000, 'Administrador d', '', '0', '0', '', 30, 'GLOBOS\r'),
(1056, 3000, 'Administrador d', '', '0', '0', '', 30, 'BOMBAS\r'),
(1057, 70000, 'Administrador d', '', '0', '0', '', 30, 'EXTINTIOR DE 10 LIBRAS\r'),
(1058, 30000, 'DAVID ALEJANDRO', '', '0', '0', 'P1I2', 30, 'ACEITE MOTUL\r'),
(1059, 14000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'DIRECCIONALES MOTOS\r'),
(1060, 28000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'ACEITE DICXOIL\r'),
(1061, 28000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'ACEITE ADVANCE\r'),
(1062, 28000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'ACEITE SUPER MOVIL\r'),
(1063, 25000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'ACEITE CASTROL\r'),
(1064, 36000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'ACEITE YAMALUBE\r'),
(1065, 35000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'ACEITE HAVOLINE\r'),
(1066, 40000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'ACEITE HONDA\r'),
(1067, 37000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'ACEITE MOTUL\r'),
(1068, 25000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'ACEITE CELERITY\r'),
(1069, 22000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'CERA BRILLA MAX\r'),
(1070, 22000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'LLANTYL\r'),
(1071, 15000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'LIQUIDO DE FRENOS\r'),
(1072, 25000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'ACEITE HIDRAULICO\r'),
(1073, 10000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'GRASA DE CADENA\r'),
(1074, 120000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'FRENO DE DISCO  PULSAR 180\r'),
(1075, 180000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'RELACION COMPLETA PLATO, CADENA, PI?ON PULSAR 180\r'),
(1076, 115000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'RELACION COMPLETA PULSAR 135\r'),
(1077, 150000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'RELACION COMPLETA DT\r'),
(1078, 120000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'FRENO DE DISCO 135\r'),
(1079, 40000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'PLATO GENERICO\r'),
(1080, 33000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'CADENA  428\r'),
(1081, 35000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'CADENA 520\r'),
(1082, 25000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'PASTILLAS DE FRENO DELANTERA\r'),
(1083, 25000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'PASTILLA DE FRENO TRASERO\r'),
(1084, 25000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'BANDAS DE FRENO\r'),
(1085, 12000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'CAUCHOS CAMPANA FRENO\r'),
(1086, 55000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'BOMBAS DE FRENO\r'),
(1087, 60000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'DISCOS DE CLOSH\r'),
(1088, 12000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'MANILARES\r'),
(1089, 25000, 'ANDRES PE?A VEL', '', '0', '0', '', 30, 'MANIGUETA\r');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `iduser` int(11) NOT NULL,
  `nameuser` varchar(90) NOT NULL,
  `passworduser` varchar(300) NOT NULL,
  `nombre` varchar(90) DEFAULT NULL,
  `telefono` varchar(90) DEFAULT NULL,
  `correo` varchar(90) DEFAULT NULL,
  `cedula` varchar(90) DEFAULT NULL,
  `imgper` varchar(300) DEFAULT NULL,
  `feccre` date DEFAULT NULL,
  `tipousu` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`iduser`, `nameuser`, `passworduser`, `nombre`, `telefono`, `correo`, `cedula`, `imgper`, `feccre`, `tipousu`) VALUES
(1, 'andy', '1234', 'andy', 'None', 'ANDETAZZ@GMAIL.COM', 'None', NULL, NULL, NULL),
(2, 'andres', '1234', 'andres123', '12345', 'ANDETAZZ87@GMAIL.COM', '12356', 'usuario.png', NULL, NULL),
(3, 'andres1', '123', 'andres1', '1234', 'ANDETAZZ@GMAIL.COM', '1234', 'usuario.png', NULL, NULL),
(5, 'andy1', '123', 'andy1', '123', 'ANDETAZZ@GMAIL.COM', '123', NULL, NULL, NULL),
(6, 'paco', '1234', 'DD', '123', 'ANDETAZZ@GMAIL.COM', '123', 'usuario.png', NULL, NULL),
(7, 'pepe', '1234', 'DD', '123', 'ANDETAZZ@GMAIL.COM', '123', 'usuario.png', NULL, NULL),
(8, 'rosa', '1234', NULL, NULL, NULL, NULL, 'usuario.png', NULL, NULL),
(9, 'miguel1', '1234', NULL, NULL, NULL, NULL, 'usuario.png', NULL, NULL),
(10, 'manolo', '1234', NULL, NULL, NULL, NULL, 'usuario.png', NULL, NULL),
(11, 'prueba', '1234', NULL, NULL, NULL, NULL, 'prueba.jpg', NULL, NULL),
(12, 'PEDROP', '1234', 'DD', '123', 'ANDETAZZ@GMAIL.COM', '123', '123.png', NULL, NULL),
(13, 'PEDROPI', '1234', '123', '123', 'ANDETAZZ@GMAIL.COM', '123', 'usuario.png', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_d`
--

CREATE TABLE `ventas_d` (
  `idventas` int(11) NOT NULL,
  `iduser` int(11) DEFAULT NULL,
  `idproducto` int(11) DEFAULT NULL,
  `nro_docu` varchar(90) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `cantidad` int(11) NOT NULL,
  `iva` int(11) DEFAULT NULL,
  `descuento` float DEFAULT NULL,
  `total` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_t`
--

CREATE TABLE `ventas_t` (
  `idventa` int(11) NOT NULL,
  `iduser` int(11) DEFAULT NULL,
  `nro_docu` varchar(90) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `f_vto` date DEFAULT NULL,
  `subtotal` float NOT NULL,
  `iva` float NOT NULL,
  `descuento` float NOT NULL,
  `total` float NOT NULL,
  `observacion` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD PRIMARY KEY (`idcarrito`),
  ADD KEY `idproducto` (`idproducto`),
  ADD KEY `iduser` (`iduser`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`idcategoria`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`idproducto`),
  ADD KEY `idcategoria` (`idcategoria`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`iduser`),
  ADD UNIQUE KEY `nameuser` (`nameuser`);

--
-- Indices de la tabla `ventas_d`
--
ALTER TABLE `ventas_d`
  ADD PRIMARY KEY (`idventas`),
  ADD KEY `iduser` (`iduser`),
  ADD KEY `idproducto` (`idproducto`);

--
-- Indices de la tabla `ventas_t`
--
ALTER TABLE `ventas_t`
  ADD PRIMARY KEY (`idventa`),
  ADD KEY `iduser` (`iduser`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carrito`
--
ALTER TABLE `carrito`
  MODIFY `idcarrito` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `idcategoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `idproducto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1090;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `iduser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `ventas_t`
--
ALTER TABLE `ventas_t`
  MODIFY `idventa` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD CONSTRAINT `carrito_ibfk_1` FOREIGN KEY (`idproducto`) REFERENCES `producto` (`idproducto`),
  ADD CONSTRAINT `carrito_ibfk_2` FOREIGN KEY (`iduser`) REFERENCES `user` (`iduser`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`idcategoria`) REFERENCES `categoria` (`idcategoria`);

--
-- Filtros para la tabla `ventas_d`
--
ALTER TABLE `ventas_d`
  ADD CONSTRAINT `ventas_d_ibfk_1` FOREIGN KEY (`idventas`) REFERENCES `ventas_t` (`idventa`),
  ADD CONSTRAINT `ventas_d_ibfk_2` FOREIGN KEY (`iduser`) REFERENCES `user` (`iduser`),
  ADD CONSTRAINT `ventas_d_ibfk_3` FOREIGN KEY (`idproducto`) REFERENCES `producto` (`idproducto`);

--
-- Filtros para la tabla `ventas_t`
--
ALTER TABLE `ventas_t`
  ADD CONSTRAINT `ventas_t_ibfk_1` FOREIGN KEY (`iduser`) REFERENCES `user` (`iduser`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
