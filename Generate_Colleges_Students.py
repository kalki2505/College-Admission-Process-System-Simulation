import csv
import random

branches = ["CSE", "IT", "ME", "EE", "EC", "IC", "CH", "Civil", "Auto"]
college_details = []


def college_details():
    colleges = []
    college_detail = [["CollegeCode", "CSE", "IT", "ME", "EE", "EC", "IC", "CH", "Civil", "Auto"]]
    with open('college_details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(college_detail[0])
        capacity = [0, 60, 120, 180, 240]

        for _ in range(50):
            college_code = "C"
            clg_code = random.randint(0, 9999)
            clg_code = "0" * (4 - len(str(clg_code))) + str(clg_code)
            while college_code in colleges:
                clg_code = random.randint(0, 9999)
            college_code += "0" * (4 - len(str(clg_code))) + str(clg_code)
            colleges += [college_code]
            clg_branch = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            while clg_branch == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
                clg_branch = []
                for _ in range(9):
                    clg_branch += [capacity[random.randint(0, 4)]]
            row = [college_code] + clg_branch
            college_detail += [row]
            writer.writerow(row)
        return college_detail


def student_details():
    students = []
    student_detail = []
    with open('student_details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["EnrollmentNo", "sub1", "sub2", "sub3", "sub4", "sub5"])

        for _ in range(5000):
            enrollment_no = "E"
            code = random.randint(0, 9999)
            code = "0" * (4 - len(str(code))) + str(code)
            while enrollment_no in students:
                code = random.randint(0, 9999)
            enrollment_no += "0" * (4 - len(str(code))) + str(code)
            students += [enrollment_no]

            subject_marks = []
            for _ in range(5):
                subject_marks += [random.randint(40, 100)]
            row = [enrollment_no] + subject_marks
            student_detail += [row]
            writer.writerow(row)
    return students, student_details

