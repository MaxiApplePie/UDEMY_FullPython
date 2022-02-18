import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text,
    age int
)
""")

d = {"a": "Paul", "b": "Durand", "c": "46"}
c.execute("INSERT INTO employees VALUES (:a, :b, :c)", d)

d = {"a": "Paul"}
c.execute("SELECT * FROM employees WHERE prenom = :a", d)
data = c.fetchall()
print(data)

conn.commit()
conn.close()

