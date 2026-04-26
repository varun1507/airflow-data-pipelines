# Airflow Data Pipelines

## 📌 Objective

Build and orchestrate data pipelines using Apache Airflow to automate ETL workflows.

---

## 🧩 Business Use Case

This project simulates an ETL pipeline where transactional data is processed daily to generate aggregated insights.

---

## 🧠 Architecture

Source Data
→ Transformation Script (Python)
→ Airflow DAG (Orchestration)
→ Output

---

## 🛠️ Tech Stack

* Apache Airflow (Orchestration)
* Python (Data Processing)
* Pandas (Transformation)

---

## 📥 Data Sources

* `orders.csv` → Transactional dataset

---

## 🔄 Pipeline Flow

1. Airflow triggers DAG on schedule
2. Python script processes data
3. Filter and aggregate data
4. Output results

---

## ⚡ Key Highlights

* Implemented Airflow DAG for scheduling
* Used PythonOperator for task execution
* Designed automated ETL workflow
* Simulated daily pipeline execution

---

## 📂 Project Structure

* `dags/` → Airflow DAG definitions
* `scripts/` → Data transformation logic
* `data/` → Input dataset

---

## 📊 Sample Output

| customer_id | total_amount |
| ----------- | ------------ |
| 101         | 350          |
| 102         | 300          |
| 103         | 500          |

---

## ▶️ How to Run

1. Install Apache Airflow
2. Place DAG file in Airflow `dags/` folder
3. Start Airflow scheduler and webserver
4. Trigger DAG from UI

---

## 🚀 Impact

Demonstrates orchestration of ETL pipelines using Airflow, enabling scheduling, automation, and workflow management.
