# Setting Up MinIO as a Source for dbt with DuckDB

This guide explains how to install and configure **MinIO** as an **S3-compatible storage** and use it as a source in **dbt** through **DuckDB**.

## 1. Install MinIO Locally

### 1.1 Install MinIO Server

**For macOS (Homebrew):**
```sh
brew install minio/stable/minio
```

**For Linux:**
```sh
wget https://dl.min.io/server/minio/release/linux-amd64/minio
chmod +x minio
sudo mv minio /usr/local/bin/
```

**For Windows:**  
Download from [MinIO releases](https://min.io/download#/linux) and extract it.

### 1.2 Start MinIO Server
```sh
mkdir -p ~/minio-data
minio server ~/minio-data --console-address ":9001"
```

- **API:** `http://127.0.0.1:9000`
- **Console:** `http://127.0.0.1:9001`

### 1.3 Configure MinIO Credentials
```sh
export MINIO_ACCESS_KEY="minioadmin"
export MINIO_SECRET_KEY="minioadmin"
```

## 2. Install MinIO Client (`mc`)

```sh
brew install minio/stable/mc  # macOS
wget https://dl.min.io/client/mc/release/linux-amd64/mc  # Linux
chmod +x mc
sudo mv mc /usr/local/bin/
```
### For Windows
To install the MinIO client (mc) on Windows, follow these steps:

1. Download MinIO Client
Go to the official MinIO client downloads page:
👉 MinIO Client Downloads
Select Windows and download the executable file.

2. Install MinIO Client
After downloading, move the file (mc.exe) to a directory of your choice (e.g., C:\mc\).
Rename the file if needed to mc.exe.

3. Add MinIO Client to System Path
To use mc from any command prompt or PowerShell window, add it to your system's PATH:
Open Control Panel → System → Advanced system settings.
Click on Environment Variables.
Under System Variables, find the Path variable and click Edit.
Click New and add the folder path where mc.exe is located (e.g., C:\mc\).
Click OK and close all dialogs.

4. Verify Installation
Open Command Prompt or PowerShell and run:
```sh
mc --version
```
This should display the installed version of MinIO Client.

### 2.1 Configure MinIO Client
```sh
mc alias set local http://127.0.0.1:9000 minioadmin minioadmin
```

### 2.2 Create a Bucket
```sh
mc mb local/my-dbt-source
```

## 3. Store Data in MinIO

```sh
mc cp my_data.csv local/my-dbt-source/
```

## 4. Connect DuckDB to MinIO

### 4.1 Install DuckDB
```sh
pip install duckdb
```

### 4.2 Query Data in DuckDB
```sql
INSTALL httpfs;
LOAD httpfs;

SET s3_region='us-east-1';
SET s3_access_key_id='minioadmin';
SET s3_secret_access_key='minioadmin';
SET s3_endpoint='http://127.0.0.1:9000';

SELECT * FROM read_csv_auto('s3://my-dbt-source/my_data.csv');
```

## 5. Use DuckDB as a Source in dbt

### 5.1 Install dbt-DuckDB Adapter
```sh
pip install dbt-duckdb
```

### 5.2 Configure `profiles.yml`

```yaml
my_project:
  target: dev
  outputs:
    dev:
      type: duckdb
      database: my_duckdb.db
      schema: main
      threads: 4
      extensions:
        - httpfs
      settings:
        s3_region: 'us-east-1'
        s3_access_key_id: 'minioadmin'
        s3_secret_access_key: 'minioadmin'
        s3_endpoint: 'http://127.0.0.1:9000'
```

### 5.3 Define dbt Source
Create `models/sources.yml`:

```yaml
version: 2

sources:
  - name: minio_source
    schema: main
    tables:
      - name: my_data
        external:
          location: "s3://my-dbt-source/my_data.csv"
          format: "csv"
```

### 5.4 Create dbt model

Once the source is defined, you can use it in dbt models:
Create `models/my_model.sql`:
```sql
SELECT * FROM {{ source('minio_source', 'my_data') }}
```

Then, run dbt:
```sh
dbt run
```

### **Final Notes**
✅ MinIO stores data in an S3-compatible bucket.  
✅ DuckDB reads data directly from MinIO.  
✅ dbt can use DuckDB to query MinIO-stored files.  
✅ You can either use an in-memory DuckDB or a separate `.duckdb` file.  

Happy building! 🚀

