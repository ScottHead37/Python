import pyodbc
import csv

def import_csv_to_sql(csv_file, server, database, table, username, password):
    """
    Imports data from a CSV file and inserts it into a SQL Server table.

    Args:
        csv_file (str): Path to the CSV file.
        server (str): SQL Server name or IP.
        database (str): Database name.
        table (str): Table name to insert data into.
        username (str): SQL Server username.
        password (str): SQL Server password.
    """
    try:
        # Connect to SQL Server with username and password
        connection_string = (
            "DRIVER={SQL Server};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
        )
        
        # Establish connection
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Open the CSV file and read data
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Insert each row into the SQL table
            for row in reader:
                cursor.execute(f"""
                    INSERT INTO {table} (name, address, phone)
                    VALUES (?, ?, ?)
                """, (row['name'], row['address'], row['phone']))

        # Commit and close
        conn.commit()
        print(f"Data successfully imported from {csv_file} to table '{table}'.")
        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")
