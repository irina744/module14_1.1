import sqlite3

conn = sqlite3.connect('bd1.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY,
           username TEXT NOT NULL,
           email TEXT NOT NULL,
           age INTEGER,
           balance INTEGER NOT NULL
           )''')

c.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(10):
    c.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
              (f'User{i + 1}', f'example{i + 1}@gmail.com', f'{(i + 1)*10}', '1000'))

for i in range(1, 11, 2):
    c.execute('UPDATE Users SET balance = ? WHERE username = ?',(500, f'User{i}'))

for i in range(1, 11, 3):
    c.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))

c.execute('SELECT * FROM Users WHERE age != 60')
result = c.fetchall()
for user in result:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

conn.commit()
conn.close()