import os
import pandas as pd
from time import sleep
from collections import Counter


college = {"CI": 110}

def grade_point(m, c):
    if m >= 90:
        return (c * 10)
    elif m >= 80:
        return (c * 9)
    elif m >= 70:
        return (c * 8)
    elif m >= 60:
        return (c * 7)
    elif m >= 45:
        return (c * 6)
    elif m >= 40:
        return (c * 4)
    else :
        return (c * 0)

def sgpa(marks):
    credits = [3, 3, 3, 3, 3, 1, 1, 2, 1]
    points = 0
    for x in range(len(marks)):
        points += grade_point(marks[x], credits[x])
    return (points / sum(credits))



exam = str(1)+ " Semester"
path = os.getcwd()
cs = ['A', 'B', 'C', 'D', 'E']
with pd.ExcelWriter(exam+".xlsx") as writer:
    for crs in cs:
        usn_arresult_percentage_array=[]
        name_arresult_percentage_array = []
        result_percentage_array = []
        sgpa_percentage_array = []
        total_percentage_array = []
        percentage_percentage_array = []
        for sa in range(10):
            usn = '1DB21CI001'
            response = ['University Seat Number ', '1DB21CS001', 'Student Name ', 'AAYUSH P NAIR', 'Semester1', 'Subject Code', 'Subject Name', 'Internal Marks', 'External Marks', 'Total', 'Result', 'Announced / Updated on', '21MAT11', 'CALCULUS AND DIFFERENTIAL EQUATIONS', '48', '34', '82', 'P', '2022-07-15', '21PHY12', 'ENGINEERING PHYSICS', '43', '29', '72', 'P', '2022-07-15', '21ELE13', 'BASIC ELECTRICAL ENGINEERING', '47', '20', '67', 'P', '2022-07-15', '21CIV14', 'ELEMENTS OF CIVIL ENGINEERING AND MECHANICS', '44', '41', '85', 'P', '2022-07-15', '21EVN15', 'ENGINEERING VISUALIZATION', '37', '48', '85', 'P', '2022-07-15', '21PHYL16', 'ENGINEERING PHYSICS LABORATORY', '48', '46', '94', 'P', '2022-07-15', '21ELEL17', 'BASIC ELECTRICAL ENGINEERING LABORATORY', '44', '47', '91', 'P', '2022-07-15', '21EGH18', 'COMMUNICATIVE ENGLISH', '45', '42', '87', 'P', '2022-07-15', '21IDT19', 'INNOVATION AND DESIGN THINKING', '48', '27', '75', 'P', '2022-07-15']
            frequency = Counter(response)
            frequency = dict(frequency)

            result = ("PASS" if frequency['P'] == 9  else "FAIL")




            usn_arresult_percentage_array.append(response[1])
            name_arresult_percentage_array.append(response[3])
            result_percentage_array.append(result)
            total = 0
            pos = 16
            marks = []
            for i in range(9):
                total = total + int(response[pos])
                marks.append(int(response[pos]))
                print(int(response[pos]))
                pos = pos+7
            total_percentage_array.append(total)
            percentage_percentage_array.append(total/9)
            if result == "PASS":
                sgpa_percentage_array.append(sgpa(marks))
            else:
                sgpa_percentage_array.append(0)


            #i = 0
            #for l in response:
            #    print(i, l)
            #    i=i+1
        df = pd.DataFrame({
                'USN':usn_arresult_percentage_array,
                'Name':name_arresult_percentage_array,
                'Result':result_percentage_array,
                'SGPA':sgpa_percentage_array,
                'Total':total_percentage_array,
                '%':percentage_percentage_array
        })
        df.to_excel(writer, sheet_name=crs, index=False)