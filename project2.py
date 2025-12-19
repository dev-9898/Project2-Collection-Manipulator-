print("Welcome to the student Data Organizer!")
students={}
while True:
    print("Select an option")
    print("1.Add student")
    print("2.Display all students")
    print("3.update student Informations")
    print("4.Delete Student")
    print("5.Display Subjects offered")
    print("6.Exit")

    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            stud_id=int(input("Student id:"))
            name=input("Name:")
            age=int(input("Age:"))
            Grade=input("Grade:")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ")

            students[stud_id]={
                "name":name,
                "age":age,
                "Grade":Grade,
                "dob":dob,
                "subjects":subjects
            }

            print("student added Successfully")
            print()

        case 2:
            print("---Display All Student---")
            for sid,i in students.items():
                print("student Id:",sid,
                      "| Name:",i["name"],
                      "| Age:",i["age"],
                      "| Grade:",i["Grade"],
                      "| Dob:",i["dob"],
                      "| Subject:",i["subjects"]
                      )
            print()
        case 3:
            while True:
                sid=int(input("Enter Student Id for Update:"))

                if sid in students:
                    print("Enter the Details..")

                    students[sid]["name"]=input("Enter the name:")
                    students[sid]["age"]=int(input("Enter the age:"))
                    students[sid]["Grade"]=input("Enter the Grade:")
                    students[sid]["dob"]=input("Enter the Date_of_birth:")
                    students[sid]["subjects"]=input("Enter the subjects:")

                    print("Student informations update Successfully!")
                    break
                else:
                    print("Student Not Found!")
        case 4:
            sid = int(input("Enter Student id for Delete:"))

            if sid in students:
                students.pop(sid)
                print("Student Record Deleted Successfully!")
            else:
                print("Student Not found!")
        case 5:
            print("--- Display Subjects Offered ---")

            subject=["hindi","Math","Science","English","Java","php"]

            for i in subject:
                print(i)

            print()
        case 6:
            print("Exit")
            break


            