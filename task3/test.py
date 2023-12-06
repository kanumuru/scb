import sqlite3

# Replace 'your_database.db' with the name of your SQLite database file
database_name = 'scb.db'

# Connect to SQLite database
conn = sqlite3.connect(database_name)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Example: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sample_table (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Example: Insert data into the table
# cursor.execute("INSERT INTO sample_table (id, name, age) VALUES (?, ?, ?)", (4,'John Doe', 25))
# print(cursor.lastrowid)  # Print the ID of the last inserted row
# print(cursor.rowcount)  # Print the number of rows inserted
# print all the data in the table
print(cursor.execute("SELECT * FROM sample_table"))
# Commit changes and close the database connection
conn.commit()
conn.close()
