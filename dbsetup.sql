-- Creates that autolib_db, user for the db and grants privileges
-- Run this command to effect "cat dbsetup.sql | mysql -hlocalhost -uroot -p"

CREATE DATABASE IF NOT EXISTS autolib_db;
CREATE USER IF NOT EXISTS libadmin IDENTIFIED BY 'libadmin';
GRANT ALL ON autolib_db.* TO 'libadmin'@'%';
FLUSH PRIVILEGES;
