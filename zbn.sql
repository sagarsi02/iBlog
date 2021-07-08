-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 08, 2021 at 07:05 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zbn`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(100) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone_num` varchar(13) NOT NULL,
  `msg` varchar(250) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'Sagar Singh', 'sagarsi5353@gmail.com', '07320837863', 'Hello Sir.', '2021-06-10 11:57:40');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(100) NOT NULL,
  `title` varchar(50) NOT NULL,
  `tagline` text NOT NULL,
  `content` varchar(250) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `slug` varchar(45) NOT NULL,
  `img_file` varchar(30) NOT NULL,
  `img_path` varchar(30) NOT NULL,
  `contents` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `content`, `date`, `slug`, `img_file`, `img_path`, `contents`) VALUES
(2, 'Lern about stock market', 'Stocks can be categorized by the country', 'A stock market, equity market, or share market is the aggregation of buyers and sellers of stocks (also called shares), which represent ownership claims on businesses; these may include securities listed on a public stock exchange, as well as stock t', '2021-06-10 12:32:01', 'stock-post', 'add.jpg', 'sfb.jpg', 'A stock exchange is an exchange (or bourse)[note 1] where stockbrokers and traders can buy and sell shares (equity stock), bonds, and other securities. Many large companies have their stocks listed on a stock exchange. This makes the stock more liqui'),
(3, 'Welcome to the Python forumsjabcjhs', 'python forum', 'Python is an interpreted high-level general-purpose programming language. Python\'s design philosophy emphasizes code readability with its notable use of significant indentation.', '2021-07-08 22:27:41', 'py-forum', 'add.jpg', 'sfb.jpg', 'This is peer to peer this forums for sharing knowledge with each other. NoSpam / Advertising / Self-promote in the forums.Do not post copyright-infringing material.Do not post “offensive” posts, links or images.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
