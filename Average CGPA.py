def calculate_cgpa(gpa_list):
    if gpa_list == []:
        return 0

    total = 0

    for gpa in gpa_list:
        total += float(gpa)

    return total / len(gpa_list)


def main():
    lines = ""

    with open("student.txt") as file:
        lines = file.readlines()

    for l in lines:
        split_line = l.split("//")
        gpa_scores = split_line[2:]
        
        with open("student_results.txt", "a") as out:
            output_string = f"{split_line[1]} (Student ID: {split_line[0]}) has a CGPA of {'{:.2f}'.format(calculate_cgpa(gpa_scores))}"
            print(output_string)
            out.write(output_string + "\n")


if __name__ == "__main__":
    main()