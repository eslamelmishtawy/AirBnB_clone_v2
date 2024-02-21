--Prepare db for project
CREATE DATABASE IF NOT EXIST hbnb_dev_db;
CREATE USER IF NOT EXIST 'hbnb_deb'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVLIGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
