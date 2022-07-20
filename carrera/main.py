from database import DataBase
import platform
import os

switched_on = True
db = DataBase()
option = ""

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def show_menu():
    print()
    print("------------------------------------------------------------------------------------------------------------------")
    print("1. Mostrar todas tus materias")
    print("2. Agregar materia")
    print("3. Eliminar materia")
    print("4. Editar materia")
    print("5. Salir")
    print()

def show_subjects():
    clear_console()
    subjects = db.get_all_subjects()
    len_subjects = len(subjects)
        
    print()
    print("MATERIAS")
    print("------------------------------------------------------------------------------------------------------------------")
    print()
    
    if len_subjects > 0:
        for i in range(len_subjects):
            index_list = i + 1
            condition = "Aprobada" if subjects[i][2] >= 4 else "Final previo"

            print(f"{index_list} | ID: {subjects[i][0]} - NAME: {subjects[i][1]} - NOTA FINAL: {subjects[i][2]} - CONDICION: {condition}")
    else:
        print("No hay materias guardadas")

def add_subjects():
    clear_console()
    
    print()
    print("AGREGAR MATERIA")
    print("------------------------------------------------------------------------------------------------------------------")
    print()

    subject_name = input("Ingrese nombre de materia: ")

    while subject_name == "" or subject_name == " ":
        subject_name = input("Ingrese nombre de materia: ")

    subject_grade = int(input("Ingrese nota final materia: "))

    while subject_grade >= 10:
        subject_grade = int(input("Ingrese nota final materia: "))

    subject = [subject_name, subject_grade]
    db.add_subject(subject)

def delete_subject():
    clear_console()

    print()
    print("ELIMINAR MATERIA")
    print("------------------------------------------------------------------------------------------------------------------")
    print()

    subject_id = int(input("Ingrese id de materia: "))

    while subject_id <= 0:
        subject_id = int(input("Ingrese id de materia: "))

    db.delete_subject(subject_id)

def edit_subject():
    clear_console()

    print()
    print("EDITAR MATERIA")
    print("------------------------------------------------------------------------------------------------------------------")
    print()

    subject_id = int(input("Ingrese id de materia: "))

    while subject_id <= 0:
        subject_id = int(input("Ingrese id de materia: "))

    print()
    print("1. Editar nombre")
    print("2. Editar nota")
    print()

    subject_edit__type = int(input("Elija que informacion editar: "))

    while subject_edit__type != 1 and subject_edit__type != 2:
        subject_edit__type = int(input("Elija que informacion editar: "))

    if subject_edit__type == 1:
        subject_name = input("Ingrese nuevo nombre de materia: ")

        while subject_name == "" or subject_name == " ":
            subject_name = input("Ingrese nuevo nombre de materia: ")

        db.edit_subject(subject_id, subject_edit__type, subject_name)
         
    else:
        subject_grade = int(input("Ingrese nueva nota de materia: "))

        while subject_grade >= 10:
            subject_grade = int(input("Ingrese nueva nota de materia: "))

        db.edit_subject(subject_id, subject_edit__type, subject_grade)

def execute_option(option):
    if option == 1:
        show_subjects()
    elif option == 2:
        add_subjects()
    elif option == 3:
        delete_subject()
    elif option == 4:
        edit_subject()


while switched_on:
    show_menu()
    
    if option.isdigit():
        if option == "5":
            switched_on = False     
            db.close()
            print("PROGRAMA TERMINADO")

        else:
            execute_option(int(option))
            option = ""

    else:
        while not option.isdigit():
            option = input("Escriba el número de acción que quiere usar: ")

        

