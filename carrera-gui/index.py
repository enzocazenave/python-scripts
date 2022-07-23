from tkinter import ttk
from tkinter import *

import sqlite3
import threading

class CampusGUI:
    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title("Ingenieria en informatica")

        # Add subject frame
        frame = LabelFrame(self.wind, text = 'Agrega una nueva materia')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Name input
        Label(frame, text = 'Materia: ').grid(row = 1, column = 0)
        self.name_input = Entry(frame)
        self.name_input.focus()
        self.name_input.grid(row = 1, column = 1)

        # Grade input
        Label(frame, text = "Nota: ").grid(row = 2, column = 0)
        self.grade_input = Entry(frame)
        self.grade_input.grid(row = 2, column = 1)

        # Button add subject
        ttk.Button(frame, text = "Agregar materia", command = self.add_subject).grid(row = 3, columnspan = 2, sticky = W + E)

        # Info message
        self.message = Label(text = '', fg = "red")
        self.message.grid(row = 3, column = 0, sticky = W)

        # Quantity of subjects
        self.qtty_subjects = Label(text = '')
        self.qtty_subjects.grid(row = 4, column = 0, sticky = W)

        self.aprobadas = Label(text = "")
        self.aprobadas.grid(row = 5, column = 0, sticky = W)

        self.previo = Label(text = "")
        self.previo.grid(row = 6, column = 0, sticky = W)


        # Subjects table
        columns = ('id', 'name', 'grade', 'condition')

        self.tree = ttk.Treeview(height = 30, columns = columns, show = 'headings')
        self.tree.grid(row = 8, column = 0, sticky = W + E, columnspan = 2)
        self.tree.heading("id", text = "*", anchor = CENTER)
        self.tree.heading("name", text = "Nombre", anchor = CENTER)
        self.tree.heading("grade", text = "Nota", anchor = CENTER)
        self.tree.heading("condition", text = "Condicion", anchor = CENTER)

        self.tree.column("id", anchor = CENTER, width = 40)
        self.tree.column("name", anchor = CENTER, width = 250)
        self.tree.column("grade", anchor = CENTER, width = 70)
        self.tree.column("condition", anchor = CENTER, width = 100)

        # Table buttons
        ttk.Button(text = "Eliminar", command = self.delete_subject).grid(row = 8, column = 0, sticky = W + E)
        ttk.Button(text = "Editar", command = self.edit_subject).grid(row = 8, column = 1, sticky = W + E)

        # Filling the table
        self.get_subjects()
    
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()

        return result

    def get_subjects(self):
        records = self.tree.get_children()

        for record in records:
            self.tree.delete(record)

        query = 'SELECT * FROM subjects ORDER BY name DESC'
        subjects = list(self.run_query(query))
        subjects_len = len(subjects)
        aprobadas = 0
        previas = 0

        for i in range(len(subjects)):
            condition = "Aprobada" if subjects[i][2] >= 4 else "Final previo"

            if condition == "Aprobada":
                aprobadas += 1
            else:
                previas += 1

            self.tree.insert('', 0, values = [subjects_len, subjects[i][1], subjects[i][2], condition])
            subjects_len -= 1

        self.qtty_subjects["text"] = f"Cantidad de materias: {len(subjects)}"
        self.aprobadas["text"] = f"Cantidad de materias aprobadas: {aprobadas}"
        self.previo["text"] = f"Cantidad de materias previas: {previas}"

    def validation(self):
        return len(self.name_input.get()) != 0 and len(self.grade_input.get()) != 0

    def show_message(self, text, color):
        self.message['text'] = text
        self.message['fg'] = color
        
        t = threading.Timer(6, self.delete_message)
        t.start()

    def delete_message(self):
        self.message['text'] = ''

    def add_subject(self):
        if self.validation() and self.grade_input.get().isdigit():
            query = 'INSERT INTO subjects VALUES(NULL, ?, ?)'
            parameters = (self.name_input.get(), self.grade_input.get())
            
            self.run_query(query, parameters)

            self.show_message(f"La materia ({self.name_input.get()}) ha sido agregada exitosamente.", 'green')

            self.name_input.delete(0, END)
            self.grade_input.delete(0, END)

            self.get_subjects()
        else:
            self.show_message('Debes completar todos los datos para ejecutar esta accion.', 'red')

    def delete_subject(self):
        try:
            self.tree.item(self.tree.selection())['values'][1]
        except IndexError as e:
            self.show_message('Selecciona una materia para ejecutar esta accion.', 'red')
    
            return

        name = self.tree.item(self.tree.selection())['values'][1]
        print(name)
        query = 'DELETE FROM subjects WHERE name = ?'

        self.run_query(query, (name, ))
        self.get_subjects()
        self.show_message(f"Materia ({name}) eliminada exitosamente.", 'red')

    def edit_subject(self):
        try:
            self.tree.item(self.tree.selection())['values'][1]
        except IndexError as e:
            self.show_message('Selecciona una materia para ejecutar esta accion.', 'red')
    
            return

        old_name = self.tree.item(self.tree.selection())['values'][1]
        old_grade = self.tree.item(self.tree.selection())['values'][2]

        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar materia'

        # Old name
        Label(self.edit_wind, text = 'Nombre actual: ').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_name), state = 'readonly').grid(row = 0, column = 2)

        # New name
        Label(self.edit_wind, text = 'Nombre nuevo: ').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        # Old grade
        Label(self.edit_wind, text = 'Nota actual: ').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_grade), state = 'readonly').grid(row = 2, column = 2)

        # New grade
        Label(self.edit_wind, text = 'Nota nueva: ').grid(row = 3, column = 1)
        new_grade = Entry(self.edit_wind)
        new_grade.grid(row = 3, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_name.get(), new_grade.get(), old_name, old_grade)).grid(row = 4, column = 2, sticky = W + E)

    def edit_records(self, new_name, new_grade, old_name, old_grade):
        query = 'UPDATE subjects SET name = ?, grade = ? WHERE name = ? AND grade = ?'
        parameters = (new_name, new_grade, old_name, old_grade)

        if len(new_name) != 0 and len(new_grade) != 0:
            self.run_query(query, parameters)
            self.edit_wind.destroy()
            self.show_message(f'La materia {old_name} ha sido actualizada exitosamente', 'green')
            self.get_subjects()
        else:
            self.show_message('Debes completar todos los datos para ejecutar esta accion', 'red')
            self.edit_wind.destroy()


if __name__ == "__main__":
    window = Tk()
    application = CampusGUI(window)
    
    window.resizable(False, False)
    window.mainloop()

    