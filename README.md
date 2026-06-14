\## Project Architecture



The project follows an ELT (Extract, Load, Transform) approach to collect, store, and transform macroeconomic data for analysis.



\### 1. Extraction

Data is extracted from the World Bank Open Data API using Python. This removes manual work and ensures the pipeline can run on a schedule.



\### 2. Storage

Data is stored in Google BigQuery using a layered structure:



\- Bronze: raw data from the API

\- Staging: cleaned and standardised data

\- Marts: final datasets for analysis and dashboards



\### 3. Transformation

dbt is used for transformations across three layers:



\- Staging: cleaning and standardisation

\- Intermediate: reshaping and transformation logic

\- Marts: final business-ready tables



\### Lineage



!\[Lineage Graph](./images/lineage\_graph.png)



The lineage graph shows how data moves through the pipeline and how models depend on each other.



\## Engineering Decisions



\- Decoupled extraction: data is pulled directly from the API using Python

\- Modular transformation: dbt layers keep logic separated and maintainable

\- Auditability: dbt documentation provides lineage and data tracking

