import csv
import math
from operator import itemgetter


def rank_students():
    student_results = []
    with open('student_details.csv', 'rt')as sd:
        data = csv.reader(sd)
        for row in data:
            student_results += [row]
        student_results[0] += ["Total", "Percentage"]
        for row_idx in range(1, 5001):
            row = student_results[row_idx]
            total = int(row[1]) + int(row[2]) + int(row[3]) + int(row[4]) + int(row[5])

            percentage = int(math.ceil(total / 5))
            student_results[row_idx] += [str(total), str(percentage)]
    cols = student_results[0]
    student_results = student_results[1:]
    student_results = sorted(student_results, key=itemgetter(6), reverse=True)
    student_results = [cols] + student_results
    with open('student_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in student_results:
            writer.writerow(row)
    return student_results


def create_dictionary(college_details):
    branches = ["CSE", "IT", "ME", "EE", "EC", "IC", "CH", "Civil", "Auto"]
    college_details = college_details[1:]

    def branch_dictionary(branch_seats):
        branch_seat = {}
        idx = 0
        for branch in branches:
            branch_seat[branch] = branch_seats[idx]
            idx += 1
        return branch_seat

    clg_details = {}
    for clg in college_details:
        clg_details[clg[0]] = branch_dictionary(clg[1:])

    return clg_details


def create_day_wise_admission(student_results, student_choices, college_details):
    college_details = create_dictionary(college_details)
    with open('day_wise_admission.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        with open('student_results.csv', 'rt')as sd:
            data = csv.reader(sd)
            count = 0
            for student in data:
                if count == 0:
                    day = 'Day'
                    allotted_clg = ["Allotted College/ Branch"]
                else:
                    day = math.ceil(count / 200)
                    allotted = False
                    choice_no = 1
                    student_no = student[0]
                    clg_choices = student_choices[count]
                    while not allotted and choice_no < 11:
                        clg_no = clg_choices[choice_no][:5]
                        branch_no = clg_choices[choice_no][6:]
                        # print('Student No = ', student_no, '\tCollege No = ', clg_no, ' and branch no ', branch_no)
                        clg_choice = college_details[clg_no]
                        seats_remaining = clg_choice[branch_no]
                        # print('\n College choice = ', clg_choice)
                        # print('Seats remaining in college ', clg_no, ' and branch ', branch_no, ' = ', seats_remaining)
                        if seats_remaining > 0:
                            allotted = True
                        else:
                            choice_no += 1

                    if allotted:
                        college_details[clg_no][branch_no] = seats_remaining - 1
                        allotted_clg = [clg_no + '-' + branch_no]
                    else:
                        allotted_clg = ["None"]
                    print('Day: ', day, '\tStudent: ', student_no, '\tclg: ', allotted_clg)
                writer.writerow([str(day)] + student + student_choices[count][1:] + allotted_clg)
                count += 1

        college_detail_rows = ["CollegeCode", "CSE", "IT", "ME", "EE", "EC", "IC", "CH", "Civil", "Auto"]
        branches = college_detail_rows[1:]
        with open('final_college_seat_status.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(college_detail_rows)
            for clg in college_details.keys():
                college_detail_rows[0] = clg
                seats = college_details[clg]
                for branch in seats.keys():
                    idx = branches.index(branch) + 1
                    college_detail_rows[idx] = seats[branch]

                writer.writerow(college_detail_rows)






