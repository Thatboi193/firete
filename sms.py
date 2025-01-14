import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

cred = credentials.Certificate("D:/firetest/firetest/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


db = firestore.client()
print("Database Connected")



def add_student(student_id, name, age, class_id):
    student_data = {
        "name": name,
        "age": age,
        "class_id": class_id,
        "attendance": [],
        "grades": {}
    }


    db.collection("Students").document(student_id).set(student_data)

    class_ref = db.collection("Classes").document(class_id)
    class_ref.update({
        "students": firestore.ArrayUnion([student_id])
    })
    print(f"Student {name} added succesfully.")


#add teacher

def add_teacher(teacher_id, name, subject):
    teacher_data = {
        "name": name,
        "subject": subject
    }
    db.collection("Teachers").document(teacher_id).set(teacher_data)
    print(f"Teacher {name} added succesfully")


#create a class

def add_class(class_is, class_name, teacher_id):
    class_data = {
        "class_name": class_name,
        "teacher_id": teacher_id,
        "students": []
    }

    db.collection("Classes").document(class_is).set(class_data)
    print(f"Class {class_name} created successfully")


def record_attendance(student_id, date, status):
    student_ref = db.collection("Students").document(student_id)

    student = student_ref.get()
    if student.exists:
        attendance_record = {
            "date": date,
            "status": status
        }
    student_ref.update({
        "attendance": firestore.ArrayUnion([attendance_record])
    })
    print(f"Attendance recorded dor {student_id}.")

#assign grade

def assign_grade(student_id, subject, grade):
    student_ref = db.collection("Students").document(student_id)
    student = student_ref.get()
    if student.exists:
        student_ref.update({
            f"grades.{subject}": grade
        })
        print(f"Grade {grade} assigned for {subject} to {student_id}")

def list_students_in_class(class_id):
    class_ref = db.collection("Classes").document(class_id)
    class_doc = class_ref.get()
    if class_doc.exists:
        students = class_doc.to_dict().get("Students")
        for student_id in students:
            student = db.collection("Students").document(student_id).get()
        if student.exists:
            print(student.to_dict())
    else:
        print("Class not found")


if __name__ == "__main__":
    #add_teacher("T002","Nikolai", "Meth")
    for i in range(2,5):
        add_student(f"S00{i}", input("Name:"), input("Age: "), f"C00{i}")
    #list_students_in_class("C001")