import sqlite3


def con():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name text, department text, year integer, sid integer)")
    conn.commit()
    conn.close()


def insert(name, department, year, sid):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?)",
                (name, department, year, sid))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(name="", department="", year="", sid=""):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM student WHERE name =? OR department =? OR year =? OR sid =? ", (name, department, year, sid))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, name, department, year, sid):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute(" UPDATE student SET name=?,department=?,year=?,sid=? WHERE id=?",
                (name, department, year, sid, id))

    conn.commit()
    conn.close()


con()

update(2, "prashant", "EEE", 2018, 204555)

print(view())
