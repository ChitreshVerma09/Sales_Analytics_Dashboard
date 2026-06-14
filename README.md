# 📊End-to-End Sales Analytics & Data Pipeline System-

A professional production-grade data pipeline project that automates the transition of raw, un-cleaned transactional data into an enterprise-level interactive analytical dashboard. 
This project bridges the gap between **Data Engineering (Python ETL)**, **Database Architecture (SQL DB Core)**, and **Business Intelligence (Power BI)**.

#🚀 Key Project Capabilities-
- Automated Data ETL: Ingests raw data via Python Pandas, handles schema validations, drops noise, and exports highly structured business-ready CSV logs.
- Relational SQL Database Engine: Creates a dynamic local SQLite database instance using Python SQLAlchemy, structures indexing, and executes analytical queries for core metric reporting.
- Dynamic Executive Dashboarding: Fully integrated live Power BI Dashboard showcasing core retail KPIs, time-series distributions, and cross-filtered sliceable matrices.


#🛠️ Corporate Tech Stack-
- **Data Engineering & ETL:** Python 3.13, Pandas
- **Database Engine & ORM:** SQLite3, SQLAlchemy
- **Data Visualization & Analytics:** Power BI Desktop

#📂 Project Repository Architecture-
Sales_Analytics_Dashboard/
├── Dashboard/
│   └── Sales Dashboard.pbix      # Enterprise Interactive Power BI Visualization
├── Data/
│   ├── superstore_raw.csv        # Raw transaction data inputs
│   ├── superstore_cleaned.csv    # Preprocessed output from Python ETL
│   └── superstore_analysis.db    # Live production SQLite database instance
├── Scripts/
│   ├── data_cleaning.py          # Python custom automation pipeline code
│   └── sql_analysis.py           # SQL query scripts for aggregate extraction
└── .gitignore                    # Ensures environment dependencies are untracked


## ⚙️ How to Run & Execute the Pipeline-
1. Execute Data Preprocessing & Cleaning (ETL)
Run the script to execute rigorous parsing rules, timestamp alignment, and clear out data anomalies:
Bash
python Scripts/data_cleaning.py

2. Initialize Database and Execute Analytical Queries
Load the cleaned dataset seamlessly into active SQL tables and run advanced aggregate calculations:
Bash
python Scripts/sql_analysis.py

3. Open Interactive Reporting Dashboard
Launch the dashboard model from the Dashboard/ directory inside Power BI Desktop. Hit the Refresh button on the ribbon to stream real-time updates directly from the optimized SQL database engine!
PowerShell
Start-Process "Dashboard\Sales Dashboard.pbix"

## Developed by Chitresh Verma
