PList = {"1": "Foundation in Engineering",
         "2": "Foundation in Arts",
         "3": "Foundation in Computing",
         "4": "Foundation in Business",
         "5": "Foundation in Science"}
def WriteFile(name,id,prog,marks,*file):
    if file != None:
        f = open("StudentData.txt","a")
        f.write(f"Name:{name} \t ID:{id} \t Programme:{prog} \t, Marks:{marks}\n" )
    else:
        file.a(f"Name:{name} \t ID:{id} \t Programme:{prog} \t, Marks:{marks}\n")



StudentName = input("Enter your name: ")
ID = input("Enter your student id: ")
Program = input(f"Enter your program: {PList}")
SubjectNumber = input("Enter number of subjects")
marks = []
for i in range(0,eval(SubjectNumber)):
    CurrentMarks = input("Enter marks: ")
    marks.append(CurrentMarks)



WriteFile(StudentName,ID,PList[Program],marks)