\# Architecture and Engineering Decisions



\## 1. Overview



This project is a data pipeline designed to collect, process, and provide access to macroeconomic indicators. The architecture was built with a focus on consistency, transparency, and data quality so that results can be trusted and reproduced.



\---



\## 2. Data Extraction and Ingestion



\### Decision



Data is collected automatically from the World Bank API using Python rather than through manual file uploads.



\### Reasoning



Manual uploads can introduce errors and make it difficult to keep the data up to date. By connecting directly to the World Bank API, the pipeline can refresh data automatically on a schedule using tools such as GitHub Actions or Cloud Scheduler.



\### Reliability



The ingestion process includes:



\* Basic schema validation

\* Logging of row counts during data loading



These checks help identify problems with the API or incoming data before they affect later stages of the pipeline.



\---



\## 3. Data Transformation (dbt)



The transformation process follows a three-layer structure.



\### Staging Layer (`staging/`)



\*\*Purpose\*\*



\* Convert data types into the correct format

\* Standardise column names using `snake\_case`



\*\*Reasoning\*\*



This layer separates the raw source data from the rest of the pipeline. If the structure of the source data changes, updates can usually be made here without affecting downstream models.



\### Intermediate Layer (`intermediate/`)



\*\*Purpose\*\*



\* Reshape data

\* Apply more complex SQL transformations

\* Convert data from long format to wide format



\*\*Reasoning\*\*



Keeping transformation logic in a separate layer makes the project easier to maintain and prevents the final reporting models from becoming overly complex.



\### Marts Layer (`marts/`)



\*\*Purpose\*\*



\* Create business-ready datasets

\* Support reporting tools such as Superset and Power BI



\*\*Reasoning\*\*



This layer provides the final datasets used for analysis and reporting. It serves as the project's single, trusted version of the data.



\---



\## 4. Materialisation Strategy



\### Views



\*\*Used for\*\*



\* Staging models

\* Intermediate models



\*\*Reasoning\*\*



Views reduce storage requirements and always reflect the latest source data without needing to rebuild datasets.



\### Tables



\*\*Planned for\*\*



\* Marts models as the project grows



\*\*Reasoning\*\*



Tables improve performance for dashboards and reports because the final datasets are already calculated and stored.



\---



\## 5. Future Scalability Considerations



\### Testing



The project includes dbt tests such as:



\* `not\_null`

\* `unique`



These tests help ensure that important data quality rules are met and that issues are detected early.



\### Observability



dbt documentation generates a lineage graph that shows how data moves through the pipeline.



This makes it easier to:



\* Understand data dependencies

\* Trace errors back to their source

\* Assess the impact of changes

\* Maintain the project as it grows



