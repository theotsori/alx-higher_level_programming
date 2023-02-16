-- A script that lists privileges of all my users

SELECT * FROM mysql.user WHERE User IN ('user_0d_1', 'user_0d_2');
