# Overview
This project is modified project from Astronomer.
For more info about astronomer go to [Astronomer Quickstart page](https://www.astronomer.io/docs/astro/cli/get-started-cli).

# What was modified

## Dags added:
- simple_python_operator.py -> simple_python_operator dag

- mysql_to_duckdb_dag.py -> mysql_to_duckdb_dag dag

For mysql_to_duckdb_dag dag you need to prepare your local Mysql database:

```
-- Create database
CREATE DATABASE test_db;
USE test_db;

-- Create table
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    price DOUBLE
);

-- Insert some sample data
INSERT INTO products (name, price) VALUES 
    ('Laptop', 1200.00),
    ('Phone', 600.00),
    ('Tablet', 300.00);
```

## Project settings:

- Added docker-compose.override.yml

This file overrides standard Dockerfile.
Thanks to this file, we have a synchronized directory between the local machine and the Docker container.
- /data -> local directory
- /usr/local/airflow/data -> Docker container directory.

- Modified requirements.txt

Added some packages that are not in a part of Python standard library.

