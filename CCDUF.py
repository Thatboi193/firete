import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

cred = credentials.Certificate("D:/firetest/firetest/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


db = firestore.client()
print("Database Connected")

def add_employee(employee_id, name, postition, department_id, email, dateOfJoining):
    employee_data = {
        "employee_id": employee_id,
        "name": name,
        "position": postition ,
        "department_id": department_id,
        "email": email,
        "dateOfJoining": dateOfJoining
    }

    db.collection("Employee").document(employee_id).set(employee_data)
    print("added employee")


def add_departments(department_id, department_name, manager_name):
    department_data = {
        "department_id": department_id,
        "department_name": department_name,
        "manager_name": manager_name
    }

    db.collection("Departments").document(department_id).set(department_data)

def add_projects(project_id, projectName, department_id, client_id, startDate, endDate):
    project_data = {
        "project_id": project_id,
        "projectName": projectName,
        "department_id": department_id,
        "client_id": client_id,
        "startDate": startDate,
        "endDate": endDate
    }
    
    db.collection("Projects").document(project_id).set(project_data)


def add_client(client_id, client_name, contact_email, phone_number, address):
    client_data = {
        "client_id": client_id,
        "client_name": client_name,
        "contact_email": contact_email,
        "phone_number": phone_number,
        "address": address
    }
    db.collection("Clients").document(client_id).set(client_data)


def add_task(task_id, task_name, assigned_to, project_id, due_date, status):
    task_data = {
        "task_id": task_id,
        "task_name": task_name,
        "assigned_to": assigned_to, 
        "project_id": project_id,
        "due_date": due_date,
        "status": status
    }
    db.collection("Tasks").document(task_id).set(task_data)


def add_meeting(meeting_id, title, date, attendees, meeting_notes):
    meeting_data = {
        "meeting_id": meeting_id,
        "title": title,
        "date": date,
        "attendees": attendees,  # Array of EmployeeIDs
        "meeting_notes": meeting_notes
    }
    db.collection("Meetings").document(meeting_id).set(meeting_data)

def listemployeebydepartment(department_id):
    bing = db.collection("Employee").where("department_id", "==", department_id).stream()
    for er in bing:
        er_data = er.to_dict()
        print(er_data)

def listtaskforemployee(employee_id):
    bing = db.collection("Tasks").where("assigned_to", "==", employee_id).stream()
    for er in bing:
        er_data = er.to_dict()
        print(er_data)

def lsitprojectsforclients(clinet_id):
    bing = db.collection("Projects").where("client_id", "==", clinet_id).stream()
    for er in bing:
        er_data = er.to_dict()
        print(er_data)

def updateTask(task_id, newStatus):
    db.collection("Tasks").document(task_id).update({"status" : newStatus})

if __name__ == "__main__":
    updateTask("T001", "Complete")
    #listemployeebydepartment("D001")
    #listtaskforemployee("C001")
    #lsitprojectsforclients("C002")

    #employee_id = input("id: ")
    #name= input("Name: ")
    #postition= input("Pos: ")
    #department_id= input("dep-id: ")
    #email= input("email: ")
    #dateOfJoining= input("date: ")
    #add_employee(employee_id, name, postition, department_id, email, dateOfJoining)

    # department_id = input("id: ")
    # department_name = input("nam: ")
    # manager_name = input("man name: ")
    # add_departments(department_id, department_name, manager_name)

    # project_id = input("pid: ")
    # projectName = input("Pname: ")
    # department_id = input("d_id: ")
    # client_id = input("Cid: ")
    # startDate = input("Sdate: ")    
    # endDate = input("eDate: ")

    # add_projects(project_id, projectName, department_id, client_id, startDate, endDate)

    # Input for adding a client
    # client_id = input("Client ID: ")
    # client_name = input("Client Name: ")
    # contact_email = input("Contact Email: ")
    # phone_number = input("Phone Number: ")
    # address_street = input("Street Address: ")
    # address_city = input("City: ")
    # address_state = input("State: ")
    # address_zip = input("Zip Code: ")
    # address = {
    # "street": address_street,
    # "city": address_city,
    # "state": address_state,
    # "zip": address_zip
    # }

    # add_client(client_id, client_name, contact_email, phone_number, address)

    # Input for adding a task
    # task_id = input("Task ID: ")
    # task_name = input("Task Name: ")
    # assigned_to = input("Assigned To (Employee ID): ")
    # project_id = input("Project ID: ")
    # due_date = input("Due Date (YYYY-MM-DD): ")
    # status = input("Status (Pending, In Progress, Completed): ")
    # add_task(task_id, task_name, assigned_to, project_id, due_date, status)

    # # Input for adding a meeting
    # meeting_id = input("Meeting ID: ")
    # title = input("Title: ")
    # date = input("Date (YYYY-MM-DD): ")
    # attendees = input("Attendees (comma-separated Employee IDs): ").split(",")
    # meeting_notes = input("Meeting Notes: ")
    # add_meeting(meeting_id, title, date, attendees, meeting_notes)

    #GET ALL EMPLOYE WITH DEPARTMENT
   