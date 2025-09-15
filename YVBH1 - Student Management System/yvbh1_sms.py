
#Variables und Data Types
className = 'Insight'
currentNumberOfStudent = 5
averageSuccessScore = 90.4
isClassActive = True

#Student Infos
student1 = {
    "name": "Fatih",
    "surname": "Aydin",
    "age": 32,
    "score": 87
}

student2 = {
    "name": "Sedef",
    "surname": "Kayran",
    "age": 27,
    "score": 93
}

student3 = {
    "name": "Malek",
    "surname": "Hoffman",
    "age": 30,
    "score": 95
}
student4 = {
    "name": "Maria",
    "surname": "Klein",
    "age": 28,
    "score": 85
}
student5 = {
    "name": "Viola",
    "surname": "Tzafai",
    "age": 30,
    "score": 92
}

students = [student1, student2, student3, student4, student5]
# print(students)

#Operators and String Process
# name = str(input("Enter Your Name: "))
# nameUpper = name.upper()

# surname = str(input("Enter Your Surname: "))
# surnameUpper = surname.upper()

# age = str(input("Enter Your Age: "))
# convAgeInt = int(age)

# score = str(input("Enter Your Score: "))
# convScoreInt =  int(score)

# if convScoreInt >= 85:
#     print(f"{name} Passed")
# else: 
#     print("Failed")

#Search and Listing
while True: 
    print("\n--- Öğrenci Yönetim Sistemi ---")
    print("1. Öğrenci Ekle")
    print("2. Öğrencileri Listele")
    print("3. Öğrenci Ara")
    print("4. İstatistik")
    print("5. Çıkış")

    selectedValue  = int(input("Select the process you want to perform: "))

    if selectedValue == 1:
        # newStudentName = str(input("Enter Your Name: ")).capitalize()
        # newStudentSurname = str(input("Enter Your Surname: ")).capitalize()
        # newStudentAge = int(input("Enter Your Age: "))
        # newStudentScore = int(input("Enter Your Score: "))
    
        # newStudent = {
        # "name": newStudentName,
        # "surname": newStudentSurname,
        # "age": newStudentAge,
        # "score" : newStudentScore 
        # }

        # for x in students:
        #     if newStudentName == x["name"] and newStudentSurname == x["surname"]:
        #         print("The Student is already exist.")    
        #         break
        # else:
        #     students.append(newStudent)
        #     print("The Student is added" , students)
        #     break
        print("x")  
    elif selectedValue == 2:
        print("\n--- Students ---")
        # for std in students:
        #     print(f"Name: {std['name']}, Surname: {std['surname']}, Age: {std['age']} Score: {std['score']}")

    elif selectedValue == 3:
        # searchValue = str(input("Search the Student: ")).capitalize()
        # for std in students: 
        #     if (std["name"] == searchValue or std["surname"] == searchValue):
        #         print(std)
        #         break
        # else:
            print("The Student could not be found")
    elif selectedValue == 4:
         #Average score of all students 
        sumScore =  sum(item['score'] for item in students)
        stdNumber = len(students)
        avrScore = sumScore / stdNumber
        print(avrScore)
        #The lowest and highest score
        maxScore =   max(std["score"] for std in students)
        print ("The highest score is:", maxScore)
    
    else:    
        break