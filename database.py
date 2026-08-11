import sqlite3

conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    hours INTEGER,
    attendance INTEGER,
    previous_marks INTEGER,
    sleep_hours INTEGER,
    predicted_marks REAL
)
""")

conn.commit()

def add_student(name, hours, attendance, prev_marks, sleep, pred):
    cursor.execute("INSERT INTO students (name, hours, attendance, previous_marks, sleep_hours, predicted_marks) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, hours, attendance, prev_marks, sleep, pred))
    conn.commit()

def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()