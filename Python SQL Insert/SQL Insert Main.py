# --- Script Calls SQL_Insert function from Module 
# ----- SQL_Insert Moldule opens and inserts data
# ----- Uses SQL Authetication no Windows Accounts

# --- Import Custom SQL Module ---|
import csv
import sys
sys.path.append(r"C:\PYTHON\modules")
import SQL_Insert

# --- Set Parameters for SQL Connection and Insert ---
csv_file = 'C:/PYTHON/Sample/Insert_Customer_Info.csv'
server='MyServer'
database='MyDB'
table='Customer_Info'
username='sa'
password='xxxxxxxxx'

# --- Module Function Call ---
SQL_Insert.import_csv_to_sql(csv_file, server, database, table, username, password)
