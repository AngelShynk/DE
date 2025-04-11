# 06 Assignment

### Requirements (15 points):

#### Build your own dbt project for your business.
1. Create 20 data models as minimum.
2. Create raw, stage and mart layers.
3. Use window functions.
4. Follow this [style guide](https://docs.getdbt.com/best-practices/how-we-style/1-how-we-style-our-dbt-models).
5. Add tests.
6. Create 20 data models as minimum.
7. Add seeds.
8. Provide some useful data insights. 
9. Use an OLTP database as a data source when appropriate, especially for structured or transactional data.
(Avoid using seeds for large files—they’re not suitable for that use case.) 
Add ETL using Airflow. In Airflow DAG uses Spark or Pandas or Polars to transfer data from OLTP database to DuckDB. 
10. Orchestrate your project with Airflow:
Trigger the dbt build command through a dedicated Airflow DAG to automate your workflows and ensure reproducibility.

Be able to explain your solution using the correct terminology.

### Additional points (2 points):
1.For large CSV files, use MinIO as a source instead of dbt seeds.
(Seeds are not designed for handling large datasets.)



