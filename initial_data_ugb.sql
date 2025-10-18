-- ============================================
-- DATOS INICIALES - SISTEMA ACADÉMICO UGB
-- ============================================

USE db_academico_ugb;

-- Usuario administrador
INSERT INTO login (usuario, clave, rol) 
VALUES ('admin', 'admin123', 'Administrador');

-- Docentes
INSERT INTO docentes (codigo, nombre, direccion, telefono, email, dui, escalafon) VALUES
('uss001', 'Alcir Gustavo Quintanilla', 'San Miguel', '2222-1111', 'alcir@ugb.edu.sv', '12345678-9', 'Titular'),
('uss002', 'Oscar Roberto Torres', 'Usulután', '2222-1112', 'oscar@ugb.edu.sv', '23456789-0', 'Asociado'),
('uss003', 'Alexia Marcela Martínez', 'San Salvador', '2222-1113', 'alexia@ugb.edu.sv', '34567890-1', 'Asistente'),
('uss004', 'Marvin Osmaro Parada', 'La Unión', '2222-1114', 'marvin@ugb.edu.sv', '45678901-2', 'Titular'),
('uss005', 'Luis Enrique Hernández', 'Morazán', '2222-1115', 'luis@ugb.edu.sv', '56789012-3', 'Asociado');

-- Materias
INSERT INTO materias (codigo, nombre, idDocente, horario, aula) VALUES
('ugb001', 'Estadística', 1, 'Lunes 7:00-9:00', 'A-101'),
('ugb002', 'Base de Datos II', 2, 'Martes 9:00-11:00', 'Lab-3'),
('ugb003', 'Inglés Básico', 3, 'Miércoles 11:00-13:00', 'B-205'),
('ugb004', 'Circuitos Digitales', 4, 'Jueves 14:00-16:00', 'Lab-1'),
('ugb005', 'Programación III', 5, 'Viernes 16:00-18:00', 'Lab-2');

-- Alumnos
INSERT INTO alumnos (codigo, nombre, direccion, telefono, email, dui) VALUES
('uss2023001', 'Carlos Antonio Gómez Martínez', 'San Miguel', '7777-0001', 'carlos@est.ugb.edu.sv', '11111111-1'),
('uss2023002', 'María Fernanda López Reyes', 'Usulután', '7777-0002', 'maria@est.ugb.edu.sv', '22222222-2'),
('uss2023003', 'José Roberto Hernández Díaz', 'San Salvador', '7777-0003', 'jose@est.ugb.edu.sv', '33333333-3'),
('uss2023004', 'Ana Cecilia Ramírez Castro', 'La Unión', '7777-0004', 'ana@est.ugb.edu.sv', '44444444-4'),
('uss2023005', 'Miguel Ángel Flores Sánchez', 'Morazán', '7777-0005', 'miguel@est.ugb.edu.sv', '55555555-5');