import json



def show_main_menu():
	print('Choose 1 for Patient menu')
	print('Choose 2 for Appointment menu')
	choice = int(input())
	match choice:
		case 1:
			show_patient_menu()
		case 2:
			show_appointment_menu()

def show_patient_menu():
	print('Choose 1 to add a new Patient')
	print('Choose 2 to update an existing patient')
	print('Choose 3 to delete an existing patient')
	choice = int(input())
	match choice:
		case 1:
			patient_data = load_data()
			add_patient(patient_data)
			save_data(patient_data)
		case 2:
			edit_patient()
		case 3:
			delete_patient()
		case default:
			print("Incorrect Input.")

def show_appointment_menu():
	print("1. Book an appointment")
	print("2. View appointment")
	print("3. Cancel an appointment")

	choice = int(input())
	match choice:
		case 1:
			dr_data = load_Doc_data()
			add_appointment(dr_data)
			save_save_appointment(dr_data)
		case 2:
			edit_patient()
		case 3:
			delete_patient()
		case default:
			print("Incorrect Input.")



def add_appointment(dr_data):
	patient_id = int(input("Enter the ID of the patient: "))
	name=input("enter name of patient")
	date = input("Enter the date of the appointment: ")
	time = input("Enter the time of the appointment: ")

	appointment = {}
	appointment["patient_id"] = patient_id
	appointment["name"] = name
	appointment["date"] = date
	appointment["time"] = time

	dr_data["appointment_list"].append(appointment)

def save_save_appointment(dr_data):
	with open('c:/python codes/smallprojets/doctors_data.json', 'w') as json_file_handle:
		json.dump(dr_data, json_file_handle, indent=8)
		print("information has been updated")

def add_patient(pdata):
	patient_id = int(input("Enter the ID of the patient: "))
	firstName =  input("Enter the first name of the patient: ")
	lastName = input("Enter the last name of the patient: ")
	gender = input("enter gender of patient")
	age = int(input("enter age of patient"))

	patient = {}
	patient["patient_id"] = patient_id
	patient["firstName"] = firstName
	patient["lastName"] = lastName
	patient["gender"] = gender
	patient["age"] = age

	pdata["patients_list"].append(patient)

def display_patient_data(pdata):
	plist = pdata["patients_list"]
	for p in plist:
		print(f"Patient ID: {p['patient_id']}")
		print(f"Patient Name: {p['firstName']}")

def edit_patient():
	pdata = load_data()
	display_patient_data(pdata)
	pid = int(input("Enter the ID of the patient to be edited: "))

	print("which information do you want to edit?")
	print("1. First Name")
	print("2. Last Name")
	print("3. Gender")
	print("4. Age")
	choice = int(input())
	match choice:
		case 1:
			name = input("enter first name")
			confirmation = input(f"Are you sure you want to edit the info of patient with ID {pid} (yes/ no)?")
			if confirmation == "yes":
				print("Editing info.")
				update_data(pid,1, name, pdata)
		case 2:
			lastname = input("enter last name")
			confirmation = input(f"Are you sure you want to edit the info of patient with ID {pid} (yes/ no)?")
			if confirmation == "yes":
				print("Editing info.")
				update_data(pid,2, lastname, pdata)
		case 3:
			Gender = input("enter Gender")
			confirmation = input(f"Are you sure you want to edit the info of patient with ID {pid} (yes/ no)?")
			if confirmation == "yes":
				print("Editing info.")
				update_data(pid,3, Gender, pdata)
		case 4:
			age=int(input("enter new age"))
			confirmation = input(f"Are you sure you want to edit the info of patient with ID {pid} (yes/ no)?")
			if confirmation == "yes":
				print("Editing info.")
				update_data(pid,4, age, pdata)

		case default:
			print("Incorrect Input.")

	
def delete_patient():
	pass

def load_data():
	with open('c:/python codes/smallprojets/patient_data.json', 'r') as json_file_handle:
		json_data = json.load(json_file_handle)
	return json_data

def load_Doc_data():
	with open('c:/python codes/smallprojets/doctors_data.json', 'r') as json_file_handle:
		json_data = json.load(json_file_handle)
	return json_data

def update_data(id,choice, data, pdata):
	for patient in pdata["patients_list"]:
		if (patient["patient_id"] == id and choice == 1):
			patient["firstName"] = data
			save_data(pdata)
		elif (patient["patient_id"] == id and choice == 2):
			patient["lastName"] = data
			save_data(pdata)
		elif (patient["patient_id"] == id and choice == 3):
			patient["gender"]=data
			save_data(pdata)
		elif (patient["patient_id"] == id and choice == 4):
			patient["age"]=data
			save_data(pdata)
		
			
def save_data(pdata):
	with open('c:/python codes/smallprojets/patient_data.json', 'w') as json_file_handle:
		json.dump(pdata, json_file_handle, indent=8)
		print("information has been updated")


show_main_menu()