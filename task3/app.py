import csv
import sqlite3

def csv_to_sql(csv_file_path, database_name, table_name):
    print(table_name)
    # Connect to SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (column1 TEXT, column2 TEXT, column3 INTEGER);")
    # Read the CSV file and insert data into the SQLite database
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header if exists

        for row in csv_reader:
            # Assuming your CSV has three columns: id, name, and age
            cursor.execute(f"INSERT INTO {table_name} (id, name, age) VALUES (?, ?, ?);", row)

    # Commit changes and close the database connection
    conn.commit()
    conn.close()

# Replace these values with your CSV file path, SQLite database name, and table name
csv_file_path = 'data.csv'
database_name = 'scb.db'
table_name = 'sample_table'

# Call the function to perform the operation
csv_to_sql(csv_file_path, database_name, table_name)
