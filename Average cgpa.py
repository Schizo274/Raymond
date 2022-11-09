#1： Write File 
PList = {
    "1": "Foundation in Engineering",
    "2": "Foundation in Arts",
    "3": "Foundation in Computing",
    "4": "Foundation in Business",
    "5": "Foundation in Science"}

def WriteFile(name,id,prog,marks,*file):
    if file != None:
        f = open("StudentData.txt","a")
        f.write(f"Name:{name}\tID:{id}\tProgramme:{prog}\tMarks:{marks}\n")
    else:
        file.a(f"Name:{name}\tID:{id}\tProgramme:{prog}\tMarks:{marks}\n")

StudentName = input("Enter your name: ")
ID = input("Enter your student id: ")
Program = input(f"Enter your program: {PList}")
SubjectNumber = input("Enter number of subjects：")
marks = []

for i in range(0,eval(SubjectNumber)):
    CurrentMarks = input("Enter marks: ")
    marks.append(CurrentMarks)

WriteFile(StudentName,ID,PList[Program],marks)



#2: Calculation
def  calculate_marks(gpa_list):
    total=0
    
    for GPAS in gpa_list:
        total+=float(GPAS)
    cgpa=total/len(gpa_list)
    
    return round(cgpa,2)
    
def calculate():
    with open("StudentData.txt") as file:
        lines=file.read().splitlines()

        for i in lines:
            split_lines=i.split("\t")
            GPAS=split_lines[3:][0][8:-2].split("', '")
            print(f" Marks: {calculate_marks(GPAS)} .")

calculate()
