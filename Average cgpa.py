def  calculate_marks(mark_list):
    total=0
    
    for mark in mark_list:
        total+=float(mark)
    cgpa=((total/len(mark_list))/100)*4

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
                Marks=split_lines[3:][0][2:-2].split("', '")
                print(f" {name}\t{ID}\t{Program}\tCGPA: {calculate_marks(Marks)} .")

calculate()
