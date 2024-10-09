-- Crear la base de datos
CREATE DATABASE registro_db;

-- CREACION DE LAS TABLAS
CREATE TABLE tab_usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    celular VARCHAR(20) NOT NULL,
    tipo_documento VARCHAR(50) NOT NULL,
    numero_documento VARCHAR(50) UNIQUE NOT NULL,
    contrasena TEXT NOT NULL,
    esactivo BOOLEAN DEFAULT true NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- INSERT
INSERT INTO tab_usuarios (nombre, celular, tipo_documento, numero_documento, contrasena) VALUES ('Juan Camilo', '3001112233','Cédula Ciudadanía', '1011222333','123456789');

-- VISTAS
create view vw_usuarios as SELECT nombre, celular, tipo_documento, numero_documento, contrasena, esactivo, fecha_creacion::date as fecha_creacion
FROM public.tab_usuarios 
where esactivo = true  
