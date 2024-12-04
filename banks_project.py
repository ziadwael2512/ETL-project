import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sqlite3

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./log_file.txt", "a") as f:
        f.write(timestamp + ':' + message + '\n') 


def extract(url, table_attr):
    page = requests.get(url).text
    data = BeautifulSoup(page, "html.parser")
    df = pd.DataFrame(columns=table_attr)
    table = data.find('table', class_='wikitable')
    rows = table.find_all('tr')[1:]  # Skip the header row
    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 0:
            data_dict = {"Bank": cols[1].text.strip(),
                        "Market cap": cols[2].text.strip()}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
    return df
#df = extract(url, table_attr)


def transform(df):
        mc_list = df['Market cap'].tolist()
        mc_list = [float("".join(x.split(',')))for x in mc_list]
        MC_GBP_list = [np.round(x*0.8,2)for x in mc_list]
        df["MC_GBP_Billion"]=MC_GBP_list 
        MC_EUR_list = [np.round(x*0.93,2)for x in mc_list]
        df["MC_EUR_Billion"]=MC_EUR_list
        MC_INR_list = [np.round(x*82.95,2)for x in mc_list]
        df["MC_INR_Billion"]=MC_INR_list 
        return df
#df = extract(url, table_attr)       
#df = transform(df)
#print(df)

def load_to_csv(df,csv_path):
    df.to_csv(csv_path)

def load_to_db(df,sql_connection, table_name):
    df.to_sql(table_name,sql_connection , if_exists='replace', index=False)

def run_query(query_statement,sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement,sql_connection)
    print(query_output)


url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'  
exchange_rate_file = '/home/project/exchange_rate.csv'
table_attr = ["Bank", "Market cap"]
table_name="Largest_banks"
db_name = 'Banks.db'


log_progress('Preliminaries complete. Initiating ETL process')
df = extract(url, table_attr)
log_progress('Data extraction complete. Initiating Transformation process')
df = transform(df)
log_progress('Data transformation complete. Initiating loading process')
load_to_csv(df,'./transformed.csv')
log_progress('Data saved to CSV file')
sql_connection = sqlite3.connect('banks.db')
log_progress('SQL Connection initiated.')
load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Running the query')
query_statement1 = f"SELECT * from {table_name} "
query_statement2 = f"SELECT AVG(MC_GBP_Billion) from {table_name} "
query_statement3 = f"SELECT Bank from {table_name} LIMIT 5 "
run_query(query_statement1, sql_connection)
run_query(query_statement2, sql_connection)
run_query(query_statement3, sql_connection)
log_progress('Process Complete.')
sql_connection.close()