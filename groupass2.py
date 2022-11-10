PList = {"1": "Foundation in Engineering",
         "2": "Foundation in Arts",
         "3": "Foundation in Computing",
         "4": "Foundation in Business",
         "5": "Foundation in Science"}

# def WriteFile(name, id, prog, marks):
#     print(f"\n{id}\t{prog}\t{name}\t{marks}")
    # with open("StudentData.txt", "a") as out:
    #     out.write(f"\n{id}\t{prog}\t{name}\t{marks}")

def ReadFile(FileName):
    with open(FileName, "r") as file:
        Lines = file.readlines()
        for l in Lines:
            SplitLines = l.split(",")
            return Calculate([int(mark) for mark in SplitLines[3:]])

def Calculate(MarkList): #this needs to be changed to suit the new syntax 
    total = 0
    count = 0 
    for Marks in MarkList:
        if Marks >= 80:
            gpa = 4.0
        elif Marks >= 75 and Marks < 80:
            gpa = 3.67
        elif Marks >= 70 and Marks < 75:
            gpa = 3.33
        elif Marks >= 65 and Marks < 70:
            gpa = 3.0
        elif Marks >= 60 and Marks < 65:
            gpa = 2.67
        elif Marks >= 55 and Marks < 60:
            gpa = 2.33
        elif Marks >= 50 and Marks < 55:
            gpa = 2.0
        elif Marks >= 47 and Marks < 50:
            gpa = 1.67
        elif Marks >= 44 and Marks < 47:
            gpa = 1.33
        elif Marks >= 40 and Marks < 44:
            gpa = 1.00
        elif Marks >= 0 and Marks < 40:
            gpa = 0
        else: 
            print("Please enter a valid mark")
        total += gpa 
        count += 1
    return round(total / count,2)

def Search():   
    word = input("Enter a word to search >> ")
    word = word.lower()
    print("ID\tProgramme\tName\tMarks")
    with open("StudentData.txt") as file:
        lines = file.readlines()
    count = 0
    for i in range(len(lines)):
        if word in lines[i].lower():
            print(lines[i])
            count += 1
    print(count, "matches.")


def ManualInput(name, id, prog, SubjectNumber): #this fucntion no longer works
    marks = []
    for i in range(0,eval(SubjectNumber)):
        CurrentMarks = int(input("Enter marks >> "))
        marks.append(int(CurrentMarks))
        gpa = Calculate(marks)
        for mark in marks:
            print(mark)
    print(f"\n{id}\t{PList[prog]}\t{name}\t{marks}\t{gpa}")
    with open("StudentData.txt", "a") as out:
        out.write(f"\n{id}\t{PList[prog]}\t{name}\t{marks}\t{gpa}")

print("1 -> Enter data in a text file with format ID Programme Name Marks")
print("2 -> Enter data directly into the programme")
print("3 -> Calculate GPA of students (manually typed)")
print("4 -> Search for a specific entry in the data")
print("5 -> Export data to a text file")
print("6 -> End programme")

# while True:
#     try:
#         option = int(input("Enter your option >> "))
#         if option == 1:
#             FileName = input("Please enter the file name and ensure it is placed in the same folder as this programme >> ")
#             ReadFile(FileName)
#         elif option == 2:
#             StudentName = input("Enter the name of student >> ")
#             ID = input("Enter the student id >> ")
#             Program = input(f"Enter program: {PList} >> ")
#             SubjectNumber = input("Enter number of subjects >> ")
#             ManualInput(StudentName, ID, Program, SubjectNumber)
#         elif option == 3:
#             #activate cgpa calc
#             ReadFile("StudentData.txt")
#         elif option == 4:
#             #search function
#             Search()
#         elif option == 5:
#             #export f(x)
#             pass
#         elif option == 6:
#             break
#         else:
#             print("Please enter a valid option!")
#     except:
#         print("Please enter a valid option!")


FileName = input("Please enter the file name and ensure it is placed in the same folder as this programme >> ")
print(ReadFile(FileName))


# WriteFile(StudentName,ID,PList[Program],marks)
# Search()
