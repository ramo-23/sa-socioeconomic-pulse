\## Project Architecture

This project follows a modern ELT (Extract, Load, Transform) pattern using Python and dbt:



1\. \*\*Extraction:\*\* Programmatic API ingestion from World Bank Open Data.

2\. \*\*Storage:\*\* Google BigQuery (Bronze -> Staging -> Marts).

3\. \*\*Transformation:\*\* A three-layer dbt architecture ensuring modularity and auditability.



!\[Lineage Graph](lineage\_graph.png)



\## Engineering Decisions

\* \*\*Decoupled Extraction:\*\* API-first ingestion for reproducibility.

\* \*\*Modular Transformation:\*\* Staging/Intermediate/Mart layering for maintainability.

\* \*\*Auditability:\*\* Automated documentation and lineage generation.

