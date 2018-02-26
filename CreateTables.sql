DROP TABLE IF EXISTS `MoviesActor`;
DROP TABLE IF EXISTS `MoviesGener`;
DROP TABLE IF EXISTS `Actor`;
DROP TABLE IF EXISTS `Producer`;
DROP TABLE IF EXISTS `Writer`;
DROP TABLE IF EXISTS `Movie`;
DROP TABLE IF EXISTS `Director`;

CREATE TABLE `Movie` (
  `id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `releasedate` varchar(100) NOT NULL,
  `duration` varchar(100) NOT NULL,
  `directorid` varchar(100) NOT NULL,
  `producerid` varchar(100) NOT NULL,
  `writerid` varchar(100) NOT NULL,
  `imdb` varchar(10) NOT NULL,
  `budget` varchar(100) NOT NULL,
  `collection` varchar(100) NOT NULL,
  `certification` varchar(100) NOT NULL,
  `score` float(6,4) DEFAULT 00.0000,  
  PRIMARY KEY (`id`)
);


CREATE TABLE `MoviesActor` (
  `movieid` varchar(100) NOT NULL,
  `actorid` varchar(100) NOT NULL,  
  `rank` varchar(10) NOT NULL,
  CONSTRAINT  FOREIGN KEY (`movieid`) REFERENCES `Movie` (`id`)
);

CREATE TABLE `MoviesGener` (
  `movieid` varchar(100) NOT NULL,
  `gener` varchar(100) NOT NULL,  
  CONSTRAINT  FOREIGN KEY (`movieid`) REFERENCES `Movie` (`id`)
);



CREATE TABLE `Producer` (
  `id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `score` float(6,4) DEFAULT 00.0000,  
   PRIMARY KEY (`id`)
);

CREATE TABLE `Director` (
  `id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `score` float(6,4) DEFAULT 00.0000,  
   PRIMARY KEY (`id`)
);

CREATE TABLE `Writer` (
  `id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `score` float(6,4) DEFAULT 00.0000,  
   PRIMARY KEY (`id`)
);

CREATE TABLE `Actor` (
  `id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `a` float(6,4) DEFAULT 00.0000,
  `b` float(6,4) DEFAULT 00.0000,
  `c` float(6,4) DEFAULT 00.0000,
  `d` float(6,4) DEFAULT 00.0000,  
   PRIMARY KEY (`id`)
);

