-- A script that prints the descritpion of the first_table

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA='hbtn_0c_0' AND TABLE_NAME='first_table';
