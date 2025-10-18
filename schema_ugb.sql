-- ============================================
-- BASE DE DATOS: SISTEMA ACADÉMICO UGB
-- Universidad Gerardo Barrios - El Salvador
-- ============================================

CREATE DATABASE IF NOT EXISTS db_academico_ugb;
USE db_academico_ugb;

-- ============================================
-- TABLA: login
-- ============================================
CREATE TABLE login (
    idLogin INT PRIMARY KEY AUTO_INCREMENT,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    clave VARCHAR(255) NOT NULL,
    rol VARCHAR(20) DEFAULT 'Administrador'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- TABLA: alumnos
-- ============================================
CREATE TABLE alumnos (
    idAlumno INT PRIMARY KEY AUTO_INCREMENT,
    codigo VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(200) NOT NULL,
    direccion TEXT,
    telefono VARCHAR(15),
    email VARCHAR(100),
    dui VARCHAR(10),
    INDEX idx_codigo (codigo),
    INDEX idx_nombre (nombre)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- TABLA: docentes
-- ============================================
CREATE TABLE docentes (
    idDocente INT PRIMARY KEY AUTO_INCREMENT,
    codigo VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(200) NOT NULL,
    direccion TEXT,
    telefono VARCHAR(15),
    email VARCHAR(100),
    dui VARCHAR(10),
    escalafon VARCHAR(50),
    INDEX idx_codigo (codigo),
    INDEX idx_nombre (nombre)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- TABLA: materias
-- ============================================
CREATE TABLE materias (
    idMateria INT PRIMARY KEY AUTO_INCREMENT,
    codigo VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    idDocente INT,
    horario VARCHAR(50),
    aula VARCHAR(20),
    FOREIGN KEY (idDocente) REFERENCES docentes(idDocente) ON DELETE SET NULL,
    INDEX idx_codigo (codigo),
    INDEX idx_nombre (nombre)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- TABLA: notas
-- ============================================
CREATE TABLE notas (
    idNota INT PRIMARY KEY AUTO_INCREMENT,
    idAlumno INT NOT NULL,
    idMateria INT NOT NULL,
    
    -- Computo 1
    lab1_c1 DECIMAL(5,2) DEFAULT 0,
    lab2_c1 DECIMAL(5,2) DEFAULT 0,
    parcial_c1 DECIMAL(5,2) DEFAULT 0,
    computo1 DECIMAL(5,2) DEFAULT 0,
    
    -- Computo 2
    lab1_c2 DECIMAL(5,2) DEFAULT 0,
    lab2_c2 DECIMAL(5,2) DEFAULT 0,
    parcial_c2 DECIMAL(5,2) DEFAULT 0,
    computo2 DECIMAL(5,2) DEFAULT 0,
    
    -- Computo 3
    lab1_c3 DECIMAL(5,2) DEFAULT 0,
    lab2_c3 DECIMAL(5,2) DEFAULT 0,
    parcial_c3 DECIMAL(5,2) DEFAULT 0,
    computo3 DECIMAL(5,2) DEFAULT 0,
    
    promedio_final DECIMAL(5,2) DEFAULT 0,
    ciclo VARCHAR(20),
    anio INT,
    
    FOREIGN KEY (idAlumno) REFERENCES alumnos(idAlumno) ON DELETE CASCADE,
    FOREIGN KEY (idMateria) REFERENCES materias(idMateria) ON DELETE CASCADE,
    UNIQUE KEY unique_alumno_materia (idAlumno, idMateria, ciclo, anio),
    INDEX idx_alumno (idAlumno),
    INDEX idx_materia (idMateria)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;