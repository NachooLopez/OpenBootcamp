import sqlite3


def main():
    conn = sqlite3.connect("midb.db")
    create_table(conn)

    insert_students(conn, 1, "Nacho", "Lopez")
    insert_students(conn, 2, "Juan", "Perez")
    insert_students(conn, 3, "Sebastián", "Driussi")
    insert_students(conn, 4, "Julián", "Álvarez")
    insert_students(conn, 5, "Marcelo", "Gallardo")
    insert_students(conn, 6, "Enzo", "Francescoli")
    insert_students(conn, 7, "Ezequiel", "Palavecino")
    insert_students(conn, 8, "Miguel", "Borja")

    conn.commit()

    student = select_students(conn, "Nacho")
    conn.close()

    print(student)


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS alumnos(id INTEGER PRIMARY KEY, nombre STRING NOT NULL, apellido STRING NOT NULL);")
    cursor.close()


def insert_students(conn, id, nombre, apellido):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO alumnos(id, nombre, apellido) VALUES(?, ?, ?)", (id, nombre, apellido))
    cursor.close()


def select_students(conn, nombre):
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM alumnos WHERE nombre = ?", (nombre,))
    return rows.fetchone()


if __name__ == "__main__":
    main()
