-- Usar el plugin de autenticación recomendado para el usuario
ALTER USER 'user'@'%' IDENTIFIED WITH 'caching_sha2_password' BY 'password';
FLUSH PRIVILEGES;