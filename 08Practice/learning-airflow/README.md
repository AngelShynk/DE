# Overview
This project is modified project from Astronomer.
For more info about astronomer go to [Astronomer Quickstart page](https://www.astronomer.io/docs/astro/cli/get-started-cli).

# What was modified

## Dags added:
- mysql_to_duckdb_dag.py -> mysql_to_duckdb_dag dag
- simple_python_operator.py -> simple_python_operator dag

## Project settings:

- Added docker-compose.override.yml

This file overrides standard Dockerfile.
Thanks to this file, we have a synchronized directory between the local machine and the Docker container.
- /data -> local directory
- /usr/local/airflow/data -> Docker container directory.

- Modified requirements.txt

Added some packages that are not in a part of Python standard library.

