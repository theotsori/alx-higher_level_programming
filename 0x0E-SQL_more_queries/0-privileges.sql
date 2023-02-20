-- A script that lists privileges of all my users

SELECT
    grantee,
    privilege_type
FROM
    information_schema.user_privileges
WHERE
    grantee IN ('user_0d_1@localhost', 'user_0d_2@localhost');
