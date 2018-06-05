/*
Navicat MySQL Data Transfer

Source Server         : mysqlconn
Source Server Version : 50715
Source Host           : localhost:3306
Source Database       : news

Target Server Type    : MYSQL
Target Server Version : 50715
File Encoding         : 65001

Date: 2018-06-05 23:22:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_news
-- ----------------------------
DROP TABLE IF EXISTS `t_news`;
CREATE TABLE `t_news` (
  `url_link` varchar(120) NOT NULL,
  `news_title` varchar(100) DEFAULT NULL,
  `news_text` varchar(5000) DEFAULT NULL,
  `run_date` datetime DEFAULT NULL,
  PRIMARY KEY (`url_link`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_url
-- ----------------------------
DROP TABLE IF EXISTS `t_url`;
CREATE TABLE `t_url` (
  `id_no` int(11) NOT NULL AUTO_INCREMENT,
  `get_url_date` datetime DEFAULT NULL,
  `url_link` varchar(220) DEFAULT NULL,
  `url_title` varchar(80) DEFAULT NULL,
  `is_run` varchar(1) NOT NULL DEFAULT 'N',
  `website_from` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_no`)
) ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user_log
-- ----------------------------
DROP TABLE IF EXISTS `user_log`;
CREATE TABLE `user_log` (
  `id` int(11) NOT NULL,
  `user_ip` varchar(18) DEFAULT NULL,
  `uesr_agent` varchar(150) DEFAULT NULL,
  `login_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
