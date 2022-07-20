import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = "",
            db = "degree"
        )

        self.cursor = self.connection.cursor()

    
    def close(self):
        self.connection.close()


    def get_all_subjects(self):
        sql = "SELECT * FROM subjects"

        try:
            self.cursor.execute(sql)
            subjects = self.cursor.fetchall()

            return subjects

        except:
            print("Hubo un error al buscar tus materias")


    def add_subject(self, subject):
        sql = f"INSERT INTO subjects (name, grade) VALUES(%s, %s)"

        try:
            value = (subject[0], subject[1])
            self.cursor.execute(sql, value)
            self.connection.commit()

            print()
            print(f"Materia ({subject[0]}) agregada exitosamente!")

        except Exception as e:
            print(f"No se pudo añadir la materia {subject[0]}")


    def delete_subject(self, id):
        sql = f"DELETE FROM subjects WHERE id={id}".format(id)
        select = f"SELECT * FROM subjects WHERE id={id}".format(id)

        try:
            self.cursor.execute(select)
            subject = self.cursor.fetchone()

            self.cursor.execute(sql)
            self.connection.commit()

            print()
            print(f"Materia ({subject[1]}) eliminada exitosamente!")
        except:
            print("Esa materia no existe")

    
    def edit_subject(self, id, edit_type, new):
        if edit_type == 1:
            sql = "UPDATE subjects SET name=%s WHERE id=%s"
        else:
            sql = "UPDATE subjects SET grade=%s WHERE id=%s"

        try:
            values = (new, id)
            self.cursor.execute(sql, values)
            self.connection.commit()

            print()
            print(f"Se modifico la materia {id} | Nuevo dato: ({new}) ")

        except:
            print("Esa materia no existe")
