import csv
import random


def get_student_results():
    student_details = []
    enrollment_nos = []

    with open('student_results.csv', 'rt')as sd:
        data = csv.reader(sd)
        for row in data:
            student_details += [row]
            enrollment_nos += [row[0]]
    enrollment_nos = enrollment_nos[1:]
    return student_details, enrollment_nos


def get_college_details(type):
    college_details = []
    college_code = []
    with open('college_details.csv', 'rt')as cd:
        data = csv.reader(cd)
        for row in data:
            college_details += [row]
            college_code += [row[0]]
    college_code = college_code[1:]
    college_details = college_details[1:]
    if type == 'details':
        return college_details
    elif type == 'code':
        return college_code
    else:
        return college_code, college_details


def create_dictionary(college_details):
    clg_seats = {}
    for clg in college_details:
        clg_seats[clg[0]] = clg[1:]
    return clg_seats


def fill_choice_filling():
    student_choices = [["EnrollmentNo", "choice1", "choice2", " choice3", "choice4", "choice5",
                        "choice6", "choice7", " choice8", "choice9", "choice10"]]
    with open('choice_filling.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        student_details, students = get_student_results()
        writer.writerow(student_choices[0])
        college_codes, college_details = get_college_details('details and code')
        clg_seats = create_dictionary(college_details)
        # print(clg_seats)
        branches = ["CSE", "IT", "ME", "EE", "EC", "IC", "CH", "Civil", "Auto"]
        # eno ==> enrollment number
        for eno in students:
            choices = []
            for choice_number in range(10):
                choice_code = random.randint(0, 49)
                branch_code = random.randint(0, 8)
                while choice_code in choices:
                    choice_code = random.randint(0, 49)
                    while clg_seats[college_codes[branch_code]] == 0:
                        branch_code = random.randint(0, 8)
                clg_choice = str(college_codes[choice_code]) + '-' + branches[branch_code]
                choices += [clg_choice]
            row = [eno] + choices
            student_choices += [row]
            writer.writerow(row)
        return student_choices
