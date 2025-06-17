import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,        -- doctor or patient
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Optional: Create appointments table for future features
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    date TEXT,
    status TEXT
)
""")

# Save the changes and close the connection
conn.commit()
conn.close()

print("✅ Database and tables created successfully!")
