import pyodbc
import csv

def fetch_and_export_data(myQuery):
    try:
        # Static connection details
        server = "MyServer"  # Replace with your server name or IP
        port = "1433"         # Replace with your port number if different
        database = "test"     # Replace with your database name
        username = "sa"       # Replace with your username
        password = "PasswordHere"  # Replace with your password

        # Define the connection string
        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server},{port};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
        )
        # Connect to the database
        connection = pyodbc.connect(connection_string)
        print("Connected to MS SQL Server successfully.")

        # Create a cursor and execute the query
        cursor = connection.cursor()        
        cursor.execute(myQuery)

        # Fetch all results
        rows = cursor.fetchall()
        return rows
        
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
    finally:
        # Close the connection if it was successfully created
        if 'connection' in locals() and connection:
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    # Call the function
    fetch_and_export_data()
