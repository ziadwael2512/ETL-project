ETL Project: Extract, Transform, Load Pipeline for Bank Market Capitalization Data
This project demonstrates the process of building an ETL (Extract, Transform, Load) pipeline using Python. The goal of the project is to scrape financial data (market capitalization of the largest banks) from Wikipedia, transform the data into multiple currencies, and load it into both a CSV file and an SQLite database for further analysis.

Project Overview
In this project, I:

Extracted market capitalization data of the largest banks from a Wikipedia page using web scraping techniques.
Transformed the data by converting market caps into multiple currencies (GBP, EUR, INR) based on predefined exchange rates.
Loaded the transformed data into a CSV file for easy sharing and an SQLite database for querying and storage.
This project provides an example of data engineering practices, including web scraping, data cleaning, transformation, and storage.

Technologies Used:
  Python (for scripting the ETL process)
  Pandas (for data manipulation and transformation)
  BeautifulSoup (for web scraping)
  SQLite (for data storage)
  Requests (for making HTTP requests)
File Structure:
  etl_process.py: Main Python script for ETL operations, including data extraction, transformation, and loading.
  log_file.txt: Log file that tracks the progress of the ETL process.
  transformed.csv: CSV file containing the transformed data with market capitalization in different currencies.
  Banks.db: SQLite database containing the transformed data in a table.
Steps:
1. Extract:
The script scrapes the Wikipedia page listing the largest banks in the world, specifically extracting their market capitalization data.

2. Transform:
The market capitalization data is converted into three currencies: GBP, EUR, and INR.
The conversion uses predefined exchange rates to ensure accurate data transformation.

3. Load:
The transformed data is loaded into a CSV file (transformed.csv) for easy access.
The data is also stored in an SQLite database (Banks.db), where it can be queried and analyzed further.
SQL Queries:
Once the data is loaded into the SQLite database, the following sample queries can be run:

View all data: SELECT * FROM Largest_banks;
Calculate the average market capitalization in GBP: SELECT AVG(MC_GBP_Billion) FROM Largest_banks;
View the top 5 banks by name: SELECT Bank FROM Largest_banks LIMIT 5;

How to Run:

Clone this repository:
 
  git clone https://github.com/yourusername/ETL-project.git

Install required dependencies:
  
  pip install requests pandas beautifulsoup4 sqlite3

Run the ETL script:
  
  python etl_process.py

View the results:
  Open the transformed.csv file to see the transformed data.
  Open the Banks.db SQLite database using a database viewer or run queries directly from the script.
License:
  This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements:
  BeautifulSoup: For parsing and extracting HTML content.
  SQLite: For lightweight data storage and SQL querying.
