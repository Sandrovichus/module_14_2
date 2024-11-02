import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@mail.ru", i * 10, 1000))

for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)

connection.commit()
connection.close()