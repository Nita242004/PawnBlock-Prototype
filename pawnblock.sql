-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 06, 2021 at 07:17 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pawnblock`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_address`
--

CREATE TABLE `tbl_address` (
  `username` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_all_items`
--

CREATE TABLE `tbl_all_items` (
  `code` int(2) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `photo_path` varchar(100) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `pawnshop` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_all_items`
--

INSERT INTO `tbl_all_items` (`code`, `name`, `photo_path`, `price`, `pawnshop`) VALUES
(1, 'Buddha Amulet', '/Users/22NitaC/PycharmProjects/pawnshop/all/1.png', '12000 THB', 'Metro Pawnshop Branch 1'),
(2, 'Chanel Bag', '/Users/22NitaC/PycharmProjects/pawnshop/all/2.png', '40000 THB', 'Metro Pawnshop Branch 2'),
(3, 'Computer', '/Users/22NitaC/PycharmProjects/pawnshop/all/3.png', '10000 THB', 'Metro Pawnshop Branch 1'),
(4, 'Diamond Ring', '/Users/22NitaC/PycharmProjects/pawnshop/all/4.png', '105000 THB', 'Metro Pawnshop Branch 1'),
(5, 'Gold Bars', '/Users/22NitaC/PycharmProjects/pawnshop/all/5.png', '325000 THB', 'Metro Pawnshop Branch 3'),
(6, 'Gold Buddha', '/Users/22NitaC/PycharmProjects/pawnshop/all/6.png', '31000 THB', 'Metro Pawnshop Branch 4'),
(7, 'Gold Buddha Amulet', '/Users/22NitaC/PycharmProjects/pawnshop/all/7.png', '20000 THB', 'Metro Pawnshop Branch 3'),
(8, 'Gold Necklace', '/Users/22NitaC/PycharmProjects/pawnshop/all/8.png', '100000 THB', 'Metro Pawnshop Branch 1'),
(9, 'Gold Necklaces', '/Users/22NitaC/PycharmProjects/pawnshop/all/9.png', '88000 THB', 'Metro Pawnshop Branch 1'),
(10, 'Gold Ring', '/Users/22NitaC/PycharmProjects/pawnshop/all/10.png', '35000 THB', 'Metro Pawnshop Branch 4'),
(11, 'Gold Yak Amulet ', '/Users/22NitaC/PycharmProjects/pawnshop/all/11.png', '31000 THB', 'Metro Pawnshop Branch 4'),
(12, 'Sunglasses', '/Users/22NitaC/PycharmProjects/pawnshop/all/12.png', '1500 THB', 'Metro Pawnshop Branch 3'),
(13, 'Watch', '/Users/22NitaC/PycharmProjects/pawnshop/all/13.png', '250000 THB', 'Metro Pawnshop Branch 2');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_cart`
--

CREATE TABLE `tbl_cart` (
  `username` varchar(100) NOT NULL,
  `item` varchar(100) NOT NULL,
  `price` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_cart`
--

INSERT INTO `tbl_cart` (`username`, `item`, `price`) VALUES
('n', 'Gold Bars', 325000),
('n', 'Gold Necklaces', 88000),
('n', 'Watch', 250000),
('n', 'Chanel Bag', 40000);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_contracts`
--

CREATE TABLE `tbl_contracts` (
  `username` varchar(20) DEFAULT NULL,
  `contract` varchar(10) DEFAULT NULL,
  `owe` varchar(50) DEFAULT NULL,
  `pawneditem` varchar(111) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_electronics`
--

CREATE TABLE `tbl_electronics` (
  `code` int(10) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `photo_path` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `pawnshop` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_electronics`
--

INSERT INTO `tbl_electronics` (`code`, `name`, `photo_path`, `price`, `pawnshop`) VALUES
(1, 'Computer', '/Users/22NitaC/PycharmProjects/pawnshop/electronics/1.png', '10000 THB', 'Metro Pawnshop Branch 1');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_favorites`
--

CREATE TABLE `tbl_favorites` (
  `username` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_favorites`
--

INSERT INTO `tbl_favorites` (`username`, `name`) VALUES
('n', 'Chanel Bag');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_gold`
--

CREATE TABLE `tbl_gold` (
  `code` int(10) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `photo_path` varchar(100) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `pawnshop` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_gold`
--

INSERT INTO `tbl_gold` (`code`, `name`, `photo_path`, `price`, `pawnshop`) VALUES
(1, 'Buddha Amulet', '/Users/22NitaC/PycharmProjects/pawnshop/gold/1.png', '12000 THB', 'Metro Pawnshop Branch 1'),
(2, 'Gold Bars', '/Users/22NitaC/PycharmProjects/pawnshop/gold/2.png', '325000 THB', 'Metro Pawnshop Branch 3'),
(3, 'Gold Buddha', '/Users/22NitaC/PycharmProjects/pawnshop/gold/3.png', '31000 THB', 'Metro Pawnshop Branch 4'),
(4, 'Gold Buddha Amulet', '/Users/22NitaC/PycharmProjects/pawnshop/gold/4.png', '20000 THB', 'Metro Pawnshop Branch 3'),
(5, 'Gold Yak Amulet ', '/Users/22NitaC/PycharmProjects/pawnshop/gold/5.png', '31000 THB', 'Metro Pawnshop Branch 4');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_jewelry`
--

CREATE TABLE `tbl_jewelry` (
  `code` int(10) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `photo_path` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `pawnshop` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_jewelry`
--

INSERT INTO `tbl_jewelry` (`code`, `name`, `photo_path`, `price`, `pawnshop`) VALUES
(1, 'Diamond Ring', '/Users/22NitaC/PycharmProjects/pawnshop/jewelry/1.png', '105000 THB', 'Metro Pawnshop Branch 1'),
(2, 'Gold Necklace', '/Users/22NitaC/PycharmProjects/pawnshop/jewelry/2.png', '100000 THB', 'Metro Pawnshop Branch 1'),
(3, 'Gold Necklaces', '/Users/22NitaC/PycharmProjects/pawnshop/jewelry/3.png', '88000 THB', 'Metro Pawnshop Branch 1'),
(4, 'Gold Ring', '/Users/22NitaC/PycharmProjects/pawnshop/jewelry/4.png', '35000 THB', 'Metro Pawnshop Branch 4');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_others`
--

CREATE TABLE `tbl_others` (
  `code` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `photo_path` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `pawnshop` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_others`
--

INSERT INTO `tbl_others` (`code`, `name`, `photo_path`, `price`, `pawnshop`) VALUES
(1, 'Chanel Bag', '/Users/22NitaC/PycharmProjects/pawnshop/other/1.png', '40000 THB', 'Metro Pawnshop Branch 2'),
(2, 'Sunglasses', '/Users/22NitaC/PycharmProjects/pawnshop/other/2.png', '1500 THB', 'Metro Pawnshop Branch 3'),
(3, 'Watch', '/Users/22NitaC/PycharmProjects/pawnshop/other/3.png', '250000 THB', 'Metro Pawnshop Branch 2');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_pawnshops`
--

CREATE TABLE `tbl_pawnshops` (
  `code` varchar(4) DEFAULT NULL,
  `name` varchar(23) DEFAULT NULL,
  `telephone` varchar(11) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `address` varchar(81) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_pawnshops`
--

INSERT INTO `tbl_pawnshops` (`code`, `name`, `telephone`, `email`, `address`) VALUES
('1', 'Metro Pawnshop Branch 1', '02-224-1730', 'pawnmetro1@gmail.com', '39-40 ถนนอัษฎางค์ ตําบลศาลเจ้าพ่อเสือ อําเภอพระนคร กรุงเทพมหานคร 10200'),
('2', 'Metro Pawnshop Branch 2', '025850909', 'pawnmetro2@gmail.com', '407-409 ถนนประชาราษฏร์สาย1 แขวงบางซื่อ เขตบางซื่อ กรุงเทพมหานคร 10800'),
('3', 'Metro Pawnshop Branch 3', '022241754', 'pawnmetro3@gmail.com', '80/124 หมู่ 6 ถนนตลิ่งชัน-สุพรรณบุรี ตําบลบางเสาธงหิน อําเภอบางใหญ่ นนทบุรี 11140'),
('4', 'Metro Pawnshop Branch 4', '034-108-677', 'pawnmetro4@gmail.com', '99/1 ถ.ทรงพล ต.สนามจันทร์ อ.เมือง จ.นครปฐม 73000');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user_profile`
--

CREATE TABLE `tbl_user_profile` (
  `user_id` int(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_user_profile`
--

INSERT INTO `tbl_user_profile` (`user_id`, `username`, `password`, `firstname`, `lastname`, `email`, `address`) VALUES
(1, 'nita', 'nita', 'nita', 'chen', 'n@gmail.com', ''),
(2, 'n', 'n', 'nit', 'chen', '22nita@gmail.com', 'test');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
