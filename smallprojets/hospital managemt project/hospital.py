import sqlite3


def show_main_menu():
    print('\t \t \t ****************************************')
    print('\t \t \t Choose 1 for Patient menu :')
    print('\t \t \t Choose 2 for Appointment menu :')
    print('\t \t \t Choose 3 for exit() :')

    choice = int(input("\t\t\t enter your choice: "))
    match choice:
        case 1:
            show_patient_menu()
        case 2:
            show_appointment_menu()


def show_patient_menu():
    print('\t \t \t ****************************************')
    print('\t \t \t Choose 1 to add a new Patient :')
    print('\t \t \t Choose 2 to update an existing patient :')
    print('\t \t \t Choose 3 to delete an existing patient :')
    print('\t \t \t Choose 4 main menu :')
    print('\t \t \t Choose 5 exit() :')
    choice = int(input())
    match choice:
        case 1:
            con = load_data()
            add_patient(con)
        case 2:
            con = load_data()
            update_patient(con)
        case 3:
            con = load_data()
            delete_patient(con)
        case 4:
            show_main_menu()
        case 5:
            pass
        case default:
            print("Incorrect Input.")


def show_appointment_menu():
    print('\t \t \t ****************************************')

    print("\t \t \t 1. Book an appointment")
    print("\t \t \t 2. View appointment")
    print("\t \t \t 3. Cancel an appointment")
    print('\t \t \t Choose 4 main menu :')
    print('\t \t \t Choose 5 exit() :')

    choice = int(input())
    match choice:
        case 1:
            con = load_data()
            add_appointment(con)

        case 2:
            con = load_data()
            view_appointment(con)
        case 3:
            con = load_data()
            delete_appointment(con)
        case 4:
            show_main_menu()
        case 5:
            pass
        case default:
            print("Incorrect Input.")


def add_appointment(con):
    print('\t \t \t ****************************************')

    pid = int(input("\t \t \t Enter the ID of the patient: "))
    name = input("\t \t \t enter name of patient")
    date = input("\t \t \t Enter the date of the appointment: ")
    time = input("\t \t \t Enter the time of the appointment: ")

    con.execute("insert into appointment (pid, pname, date, time) values (?, ?, ?, ?)",
                (pid, name, date, time))

    con.commit()
    print("\t \t \t Records created successfully")
    con.close()
    go_to_appointment_menu()


def view_appointment(con):
    print('\t \t \t ****************************************')
    cursor = con.execute("select * from appointment")
    for row in cursor:
        print(row)
    con.close()
    go_to_appointment_menu()


def delete_appointment(con):
    print('\t \t \t ****************************************')

    pid = int(input("\t \t \t Enter the ID of the appointment to be deleted: "))
    confirmation = input(
        f"\t \t \t Are you sure you want to delete the appointment with ID {pid} (yes/ no)?")
    if confirmation == "yes":
        print("\t \t \t Deleting appointment.")
        con.execute("delete from appointment where pid = ?", (pid,))
        con.commit()
        print("\t \t \t Deleted successfully")
    else:
        print("\t \t \t Not deleting.")
    con.close()
    go_to_appointment_menu()


def add_patient(con):
    print('\t \t \t ****************************************')
    id = int(input("\t \t \t Enter the ID of the patient: "))
    Name = input("\t \t \t Enter the first name of the patient: ")

    gender = input("\t \t \t enter gender of patient: ")

    contact = int(input("\t \t \t enter contact no  of patient: "))
    age = int(input("\t \t \t enter age of patient: "))

    con.execute("insert into patient (id,name,gender,contact,age) values (?, ?, ?, ?, ?)",
                (id, Name, gender, contact, age))
    con.commit()

    print("\t \t \t patient details added successfully")
    print("\t \t \t will you like to go previous menu ?")
    confirmation = input("\t\t\t yes/no")

    if confirmation == "yes":
        show_patient_menu()

    else:
        show_main_menu()


def update_patient(con):
    print('\t \t \t ****************************************')
    pid = int(input("\t \t \t Enter the ID of the patient to be edited: "))

    print("\t \t \t which information do you want to edit? ")
    print("\t \t \t 1. Name")
    print("\t \t \t 2. Gender")
    print("\t \t \t 3. contact")
    print("\t \t \t 4. Age")
    choice = int(input("\t\t\t"))
    match choice:
        case 1:
            name = input("\t \t \t enter first name: ")
            confirmation = input(
                f"\t \t \t Are you sure you want to edit the info of patient with ID {pid} (yes/ no)?")
            if confirmation == "yes":
                print("\t \t \t Editing info.")
                con.execute(
                    "update patient set name = ? where id = ?", (name, pid))
                con.commit()
                print("\t \t \t Edited successfully")
            go_to_update_menu(con)

        case 2:
            gender = input("\t \t \t enter gender: ")
            confirmation = input(
                f"\t \t \t Are you sure you want to edit the info of patient with ID {pid} (yes/ no)?")
            if confirmation == "yes":
                print("\t \t \t Editing info.")
                con.execute(
                    "update patient set gender=? where id= ?", (gender, pid))
                con.commit()
                print("\t \t \t edited successfully")
            go_to_update_menu(con)
        case 3:
            contact = int(input("\t \t \t enter Contact no: "))
            confirmation = input(
                f"\t \t \t Are you sure you want to edit the info of patient with ID {pid} (yes/ no)?")
            if confirmation == "yes":
                print("\t \t \t Editing info.")
                con.execute(
                    "update patient set contact=? where id= ?", (contact, pid))
                con.commit()
                print("\t \t \t edited successfully")
            go_to_update_menu(con)
        case 4:
            age = int(input("\t \t \t enter new age: "))
            confirmation = input(
                f"\t \t \t Are you sure you want to edit the info of patient with ID {pid} (yes/ no)?")
            if confirmation == "yes":
                print("\t \t \t Editing info.")
                con.execute("update patient set age=? where id= ?", (age, pid))
            con.commit()
            print("\t \t \t edited successfully")
            go_to_update_menu(con)

        case default:
            print("Incorrect Input.")
            go_to_update_menu(con)


def delete_patient(con):
    print('\t \t \t ****************************************')

    pid = int(input("\t \t \t Enter the ID of the patient to be deleted: "))
    confirmation = input(
        f"\t \t \t Are you sure you want to delete the patient with ID {pid} (yes/ no)?")
    if confirmation == "yes":
        print("\t \t \t Deleting patient.")
        con.execute("delete from patient where id = ?", (pid,))
        con.commit()
        print("\t \t \t Deleted successfully")
    else:
        print("\t \t \t Not deleting.")
    con.close()
    print("\t \t \t will you like to go previous menu ?")
    confirmation = input("\t\t\t yes/no")

    if confirmation == "yes":
        show_patient_menu()

    else:
        show_main_menu()


def load_data():
    print('\t \t \t ****************************************')

    conn = sqlite3.connect('hospital.db')
    print("\t \t \t Opened database successfully")
    return conn


def go_to_update_menu(con):
    print("\t \t \t will you like update anather information ?")
    confirmation = input("\t\t\t yes/no: ")
    if confirmation == "yes":
        update_patient(con)
    else:
        show_main_menu()


def go_to_appointment_menu():
    print("\t \t \t will you like to add an appointment ?")
    confirmation = input("\t\t\t yes/no: ")
    if confirmation == "yes":
        show_appointment_menu()
    else:
        show_main_menu()


show_main_menu()
