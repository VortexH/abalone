-- create database `hackday_abalone` and tables `users` and `comments`
CREATE DATABASE IF NOT EXISTS hackday_abalone;
use hackday_abalone;
CREATE TABLE IF NOT EXISTS `comments` (
  id INT(128) NOT NULL AUTO_INCREMENT,
  user_id INT(128) NOT NULL,
  video_id VARCHAR(256) NOT NULL,
  comment VARCHAR(1024) NOT NULL,
  timestamp VARCHAR(256) NOT NULL,
  PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS `users` (
  id INT(128) NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL UNIQUE,
  PRIMARY KEY (id)
);
