--database creationsql--
CREATE DATABASE student_db;

CREATE TABLE students (
    id SERIAL PRIMARY KEY,--
    ovog_ner VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    utas VARCHAR(20)

);