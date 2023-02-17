-- A script that lists privileges of all my users

SELECT User, Host, Grant_priv, Create_priv, Alter_priv, Drop_priv, Select_priv, Insert_priv, Update_priv, Delete_priv
FROM mysql.user
WHERE User IN ('user_0d_1', 'user_0d_2')
AND Host = 'localhost';
