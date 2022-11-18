PList = {"1": "Foundation in Engineering",  #list of programmes for the manual input
         "2": "Foundation in Arts",
         "3": "Foundation in Computing",
         "4": "Foundation in Business",
         "5": "Foundation in Science"}

def ReadFile(FileName): #function to read from file
    with open(FileName, "r") as file:   #accepts the file name  
        Lines = file.readlines()
        print("Student ID\tProgramme\tName\tGPA")   #prints "header" in concole
        with open("GPAs.txt", "w") as out:  #opens a new file called GPAs.txt
            out.write("Student ID\tProgramme\tName\tGPA")   #prints "header" in file
        for l in Lines:
            SplitLines = l.split(",")   
            print(f"{SplitLines[0]}\t{SplitLines[1]}\t{SplitLines[2]}\t{Calculate([float(mark) for mark in SplitLines[3:]])}")  #prints student information as well as GPA by calling the Calculate function in console
            with open("GPAs.txt", "a") as out:
                out.write(f"\n{SplitLines[0]}\t{SplitLines[1]}\t{SplitLines[2]}\t{Calculate([float(mark) for mark in SplitLines[3:]])}") #appends student information and GPA to GPAs.txt
    print("This data has also been written to a file named GPAs.txt in the same folder as this programme.")

def Calculate(MarkList):
    total = 0
    count = 0 
    for Marks in MarkList:  #iterates through the list passed into the function 
        if Marks >= 80 and Marks <= 100:    #checks which GPA the marks fit into
            gpa = 4.0
        elif Marks >= 75 and Marks < 80:
            gpa = 3.67
        elif Marks >= 70 and Marks < 75:
            gpa = 3.33
        elif Marks >= 65 and Marks < 70:
            gpa = 3.00
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
        total += gpa    #sums all GPA values
        count += 1
    return round(total / count,2)   #returns the GPA divided by number of subjects

def Search(FileName):   #function to search for a specific word accepts a file name to search 
    word = input("Enter a word to search >> ")  #asks user to input the desired word to be found
    word = word.lower()
    print("ID\tProgramme\tName\tGPA")   #prints "header"
    with open(FileName) as file:    #opens the file to search
        lines = file.readlines()
    count = 0
    for i in range(len(lines)):
        if word in lines[i].lower():    #checks whether the word is contained in any of the entries
            print(lines[i])     #prints the entry containing the word
            count += 1
    print(count, "matches.")


def ManualInput(name, id, prog, SubjectNumber):     #function allowing the user to input directly into the programme
    marks = []  #defines a list to store the marks
    for i in range(0,eval(SubjectNumber)):  #repeats for n number of subjects to ask for the marks of each subject
        CurrentMarks = float(input(f"Enter marks for subject {i + 1} >> "))
        marks.append(float(CurrentMarks))
    gpa = Calculate(marks)  #calls function to calculate the GPA
    print(f"{id}\t{PList[prog]}\t{name}\t{marks}\t{gpa}")   #prints the information in the entry in the console
    with open("StudentData.txt", "a") as out:
        out.write(f"\n{id}\t{PList[prog]}\t{name}\t{marks}\t{gpa}") #prints the information in a file called StudentData.txt

def Sort(FileName):
    index = []
    with open(FileName, "r") as file:
        lines = file.readlines()
        for l in lines[1:]:
            split = l.split()
            for i in range(1, len(split)):
                gpa = (split[-1])
                if gpa not in index:
                    index += [gpa]
    hasSwap = True
    tempIndexList = []
    for i in range(len(index)):
        tempIndexList += [i]
    while hasSwap:
        hasSwap = False
        for i in range(len(index)):
            if i == len(index)-1:
                continue
            if index[i] > index[i+1]:
                hasSwap = True
                tempIndexList[i], tempIndexList[i+1] = tempIndexList[i+1], tempIndexList[i]
                index[i], index[i+1] = index[i+1], index[i]
    for i in tempIndexList:
        print(lines[i + 1])
    return tempIndexList

count = 0

#printing instructions for user
print("1 -> Enter data in a text file with format ID Programme Name Marks")
print("2 -> Enter data directly into the programme")
print("3 -> Search for a specific entry in the data")
print("4 -> Sort entries based on CGPA")
print("5 -> End programme")

while True:
    try:
        option = int(input("Enter your option >> "))
        if option == 1:
            FileName = input("Please enter the file name and ensure it is placed in the same folder as this programme >> ")
            ReadFile(FileName)
        elif option == 2:
            StudentName = input("Enter the name of student >> ")
            ID = input("Enter the student id >> ")
            Program = input(f"Enter program: {PList} >> ")
            SubjectNumber = input("Enter number of subjects >> ")
            if count == 0:
                with open("StudentData.txt", "w") as out:
                    out.write("Student ID\tProgramme\tName\tMarks\tGPA")
                count += 1
            ManualInput(StudentName, ID, Program, SubjectNumber)
            print("The entry has been successfully added to a file named StudentData.txt")
        elif option == 3:
            FileName = input("Input the name of the file you wish to search within >> ")
            Search(FileName)
        elif option == 4:
            FileName = input("Please input file that you wish to sort >> ")
            Sort(FileName)
        elif option == 5:
            print("Closing programme...")
            break
        else:
            print("Please enter a valid option!")
    except:
        print("Please enter a valid option!")
