-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 06, 2020 at 01:50 PM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gamification-webshop`
--

-- --------------------------------------------------------

--
-- Table structure for table `available_code`
--

CREATE TABLE `available_code` (
  `id` int(11) NOT NULL,
  `min_score` int(11) NOT NULL,
  `max_score` int(11) NOT NULL,
  `catalog_coupon_id` int(11) NOT NULL,
  `shop_id` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `available_code`
--

INSERT INTO `available_code` (`id`, `min_score`, `max_score`, `catalog_coupon_id`, `shop_id`, `active`) VALUES
(1, 0, 100, 97, 1, 1),
(2, 101, 200, 98, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `high_score`
--

CREATE TABLE `high_score` (
  `id` int(11) NOT NULL,
  `mail` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `name` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `score` int(11) NOT NULL,
  `shop_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `high_score`
--

INSERT INTO `high_score` (`id`, `mail`, `name`, `score`, `shop_id`) VALUES
(1, NULL, NULL, 100, 1);

-- --------------------------------------------------------

--
-- Table structure for table `shop`
--

CREATE TABLE `shop` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `url` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `resource_owner_key` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `resource_owner_secret` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `client_key` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `client_secret` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `game_origin` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `shop`
--

INSERT INTO `shop` (`id`, `name`, `url`, `resource_owner_key`, `resource_owner_secret`, `client_key`, `client_secret`, `game_origin`) VALUES
(1, 'didi', 'http://localhost:8080', 'rtxojvqglcd2m4f8n3pg6nhi1dviil00', 'bhzrf9y224nc2rlonf5z6urr0499n8ih', 'm748bxohupsrer5hqvaynfkhy8nlpyz8', 'zz2z4zowvgyujqf38wcnzb0koqch7rx4', 'http://localhost:4000');

-- --------------------------------------------------------

--
-- Table structure for table `used_cart`
--

CREATE TABLE `used_cart` (
  `cart_id` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `shop_id` int(11) NOT NULL,
  `coupon_code` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `automatic_added` tinyint(1) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `used_cart`
--

INSERT INTO `used_cart` (`cart_id`, `shop_id`, `coupon_code`, `automatic_added`, `date`) VALUES
('1', 1, 'as34f1sdgj61b', 1, '2020-04-30 11:24:15');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `available_code`
--
ALTER TABLE `available_code`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ac_shop_id` (`shop_id`);

--
-- Indexes for table `high_score`
--
ALTER TABLE `high_score`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hs_shop_id` (`shop_id`);

--
-- Indexes for table `shop`
--
ALTER TABLE `shop`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `used_cart`
--
ALTER TABLE `used_cart`
  ADD PRIMARY KEY (`cart_id`,`shop_id`,`coupon_code`),
  ADD KEY `uc_shop_id` (`shop_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `available_code`
--
ALTER TABLE `available_code`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `high_score`
--
ALTER TABLE `high_score`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `shop`
--
ALTER TABLE `shop`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `available_code`
--
ALTER TABLE `available_code`
  ADD CONSTRAINT `ac_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `shop` (`id`);

--
-- Constraints for table `high_score`
--
ALTER TABLE `high_score`
  ADD CONSTRAINT `hs_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `shop` (`id`);

--
-- Constraints for table `used_cart`
--
ALTER TABLE `used_cart`
  ADD CONSTRAINT `uc_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `shop` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
