import csv

states = []
avgStudentRate = []
avgTeacherRate = []
freeLunchEligible = []
reducePriceLunchEligible = []
indivEduProgram = []
studentTeachRatio = []
publicSchoolSpending = []

def main():
    with open('./data/education.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for idx, row in enumerate(reader):

            # Will show you list of tuples (index, titleName)
            #
            # if (idx == 0):
            #     show = []
            #     for titleIdx, title in enumerate(row):
            #         show.append((titleIdx, title))
            #     print(show)

            if (idx != 0):
                avgStudentRate.append(row[3])
                avgTeacherRate.append(row[4])
                freeLunchEligible.append(row[9])
                indivEduProgram.append(row[11])
                reducePriceLunchEligible.append(row[17])
                states.append(row[21])
                studentTeachRatio.append(row[22])

    # This function will automatically add
    # data to 'publicSchoolSpending' global variable
    publicSpending()

    ########## STUDENT RATE ##########

    createNewFile('./bin/Free_Lunch_with_AVG_Student_Rate.csv', [
        states,
        avgStudentRate,
        freeLunchEligible
    ],
    [   "states",
        "avg_student_rate",
        "free_lunch_eligible"
    ])

    createNewFile('./bin/Reduced_Lunch_with_AVG_Student_Rate.csv', [
        states,
        avgStudentRate,
        reducePriceLunchEligible
    ],
    [   "states",
        "avg_student_rate",
        "reduced_lunch_eligible"
    ])

    createNewFile("./bin/Indiv_Educate_Prog_with_AVG_Student_Rate.csv", [
        states,
        avgStudentRate,
        indivEduProgram
    ],
    [   "states",
        "avg_student_rate",
        "individualized_education_programs"
    ])

    createNewFile("./bin/Student_Teacher_Ratio_with_AVG_Student_Rate.csv", [
        states,
        avgStudentRate,
        studentTeachRatio
    ],
    [   "states",
        "avg_student_rate",
        "student_teacher_ratio"
    ])

    createNewFile("./bin/State_Fund_Per_Pupil_with_AVG_Student_Rate.csv", [
        states,
        avgStudentRate,
        publicSchoolSpending
    ],
    [   "states",
        "avg_student_rate",
        "state_funding_per_pupil"
    ])

    ########## TEACHER RATE ##########

    createNewFile('./bin/Free_Lunch_with_AVG_Teacher_Rate.csv', [
        states,
        avgTeacherRate,
        freeLunchEligible
    ],
    [   "states",
        "avg_teacher_rate",
        "free_lunch_eligible"
    ])

    createNewFile('./bin/Reduced_Lunch_with_AVG_Teacher_Rate.csv', [
        states,
        avgTeacherRate,
        reducePriceLunchEligible
    ],
    [   "states",
        "avg_teacher_rate",
        "reduced_lunch_eligible"
    ])

    createNewFile("./bin/Indiv_Educate_Prog_with_AVG_Teacher_Rate.csv", [
        states,
        avgTeacherRate,
        indivEduProgram
    ],
    [   "states",
        "avg_teacher_rate",
        "individualized_education_programs"
    ])

    createNewFile("./bin/Student_Teacher_Ratio_with_AVG_Teacher_Rate.csv", [
        states,
        avgTeacherRate,
        studentTeachRatio
    ],
    [   "states",
        "avg_teacher_rate",
        "student_teacher_ratio"
    ])

    createNewFile("./bin/State_Fund_Per_Pupil_with_AVG_Teacher_Rate.csv", [
        states,
        avgTeacherRate,
        publicSchoolSpending
    ],
    [   "states",
        "avg_teacher_rate",
        "state_funding_per_pupil"
    ])


def createNewFile(name, listOfData, titles):
    # create sperate files
    with open(name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        # write title row
        writer.writerow(titles)
        idx = 0
        endLen = len(listOfData[0])
        # run through every element
        while (idx < endLen):
            # create new row
            row = []
            for data in listOfData:
                row.append(data[idx])
            # write to file
            writer.writerow(row)
            # increase index
            idx += 1

# helper function for public school spending
# will add data to global variable
def publicSpending():
    list_to_sort = []
    # read file
    with open("./data/public_school_spending.txt") as spending:
        reader = csv.reader(spending, delimiter='\t')
        for row in reader:
            list_to_sort.append(row)
    # sort by state (index: 0)
    list_to_sort.sort(key=lambda x: x[0])

    # add total per pupil to global
    for row in list_to_sort:
        str = row[1]
        publicSchoolSpending.append(str[1:])


if __name__ == '__main__':
    main()
