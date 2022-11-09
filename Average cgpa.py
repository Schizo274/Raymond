PList = {"1": "Foundation in Engineering",
         "2": "Foundation in Arts",
         "3": "Foundation in Computing",
         "4": "Foundation in Business",
         "5": "Foundation in Science"}

def WriteFile(name, id, prog, marks, *file):
    try:
        f = open(file, "a")
        f.write(f"\n{id}\t{prog}\t{name}\t{marks}")
    except:
        with open("StudentData.txt", "a") as out:
            out.write(f"\n{id}\t{prog}\t{name}\t{marks}")

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


StudentName = input("Enter your name: ")
ID = input("Enter your student id: ")
Program = input(f"Enter your program: {PList}: ")
SubjectNumber = input("Enter number of subjects: ")
marks = []
for i in range(0,eval(SubjectNumber)):
    CurrentMarks = input("Enter marks: ")
    marks.append(CurrentMarks)

WriteFile(StudentName,ID,PList[Program],marks)
Search()

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
            if i!="":
                split_lines=i.split("\t")
                ID=split_lines[0]
                Program=split_lines[1]
                name=split_lines[2]                
                GPAS=split_lines[3:][0][2:-2].split("', '")
                print(f" {name}\t{ID}\t{Program}\tMarks: {calculate_marks(GPAS)} .")

calculate()
