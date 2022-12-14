SET NAMES utf8;

DROP TABLE IF EXISTS `User`;

CREATE TABLE
    `User` (
        `ID` int(11) NOT NULL AUTO_INCREMENT,
        `Email` text NOT NULL,
        `Password` text NOT NULL,
        `Status` tinyint(4) NOT NULL,
        `Creation_Date` date NOT NULL,
        `Las_update` timestamp NOT NULL,
        PRIMARY KEY (`ID`)
    ) ENGINE = InnoDB DEFAULT CHARSET = latin1;