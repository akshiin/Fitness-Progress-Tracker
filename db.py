import sqlite3
import pandas as pd

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("fitness_data.db")
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS workout (
        date TEXT PRIMARY KEY,
        push_ups INTEGER,
        pull_ups INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
        date TEXT PRIMARY KEY,
        max_push_ups INTEGER,
        max_pull_ups INTEGER
    )
''')

# Load CSV data
workout_df = pd.read_csv("data.csv")
records_df = pd.read_csv("records.csv")

# Insert data into SQLite tables
workout_df.to_sql("workout", conn, if_exists="replace", index=False)
records_df.to_sql("records", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Data successfully migrated to SQLite!")
