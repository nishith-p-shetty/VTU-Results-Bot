'''
SGPA CALCULATOR
Author : Nishith P Shetty
Ver 1.0
Run : Win   : py gpa.py
      Linux : python3 gpa.py
'''

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

def sgpa1():
    subjects = ["21MAT11", "21CHE12", "21PSP13", "21ELN14", "21EME15", "21CHEL16", "21CPL17", "21EGH18", "21SFH19"]
    credits = [3, 3, 3, 3, 3, 1, 1, 2, 1]
    marks = [67, 65, 89, 60, 70, 84, 99, 93, 80]
    obtained_credits = credits
    points = 0
    for x in range(len(subjects)):
        points += grade_point(marks[x], obtained_credits[x])
    sgpa = points / sum(obtained_credits)
    print("SGPA : ", sgpa)

def sgpa2():
    subjects = ["21MAT21", "21PHY22", "21ELE3", "21CIV4", "21EVN25", "21PHYL26", "21ELEL27", "21EGH28", "21IDT29"]
    credits = [3, 3, 3, 3, 3, 1, 1, 2, 1]
    marks = []
    obtained_credits = credits
    points = 0
    print("Enter the Total Obtained Marks for the following subjects : ")
    for s in subjects:
        marks.append(int(input(s + " : ")))
    if (input("All Passed ? (Y/N) : ") == "N"):
        print("Enter F if failed, else press enter")
        for s in subjects:
            if (input("s : ") == "F"):
                obtained_credits[subjects.index(s)] = 0
    for x in range(len(subjects)):
        points += grade_point(marks[x], obtained_credits[x])
    sgpa = points / sum(obtained_credits)
    print("SGPA : ", sgpa)

def sgpa3():
    subjects = ["21MAT31", "21CS32", "21CS33", "21CS34", "21CSL35", "21UH36", "21KSK37/21CIP37", "21CS38X/21CSL38X"]
    credits = [3, 4, 4, 3, 1, 1, 1, 1]
    marks = []
    obtained_credits = credits
    points = 0
    print("Enter the Total Obtained Marks for the following subjects : ")
    for s in subjects:
        marks.append(int(input(s + " : ")))
    if (input("All Passed ? (Y/N) : ") == "N"):
        print("Enter F if failed, else press enter")
        for s in subjects:
            if (input("s : ") == "F"):
                obtained_credits[subjects.index(s)] = 0
    for x in range(len(subjects)):
        points += grade_point(marks[x], obtained_credits[x])
    sgpa = points / sum(obtained_credits)
    print("SGPA : ", sgpa)

def sgpa4():
    subjects = ["21MAT41", "21CS42", "21CS43", "21CS44", "21BE45", "21CSL46", "21KSK47/21CIP47", "21CS48X/21CSL48X", "21INT49"]
    credits = [3, 4, 4, 3, 2, 1, 1, 1, 1, 2]
    marks = []
    obtained_credits = credits
    points = 0
    print("Enter the Total Obtained Marks for the following subjects : ")
    for s in subjects:
        marks.append(int(input(s + " : ")))
    if (input("All Passed ? (Y/N) : ") == "N"):
        print("Enter F if failed, else press enter")
        for s in subjects:
            if (input("s : ") == "F"):
                obtained_credits[subjects.index(s)] = 0
    for x in range(len(subjects)):
        points += grade_point(marks[x], obtained_credits[x])
    sgpa = points / sum(obtained_credits)
    print("SGPA : ", sgpa)

def sgpa5():
    subjects = ["21CS51", "21CS52", "21CS53", "21AI54", "21CSL55", "21XX56", "21CIV57", "21CS58X/21CSL58X"]
    credits = [3, 4, 3, 3, 1, 2, 1, 1]
    marks = []
    obtained_credits = credits
    points = 0
    print("Enter the Total Obtained Marks for the following subjects : ")
    for s in subjects:
        marks.append(int(input(s + " : ")))
    if (input("All Passed ? (Y/N) : ") == "N"):
        print("Enter F if failed, else press enter")
        for s in subjects:
            if (input("s : ") == "F"):
                obtained_credits[subjects.index(s)] = 0
    for x in range(len(subjects)):
        points += grade_point(marks[x], obtained_credits[x])
    sgpa = points / sum(obtained_credits)
    print("SGPA : ", sgpa)

def sgpa6():
    subjects = ["21CS61", "21AD62", "21AI63", "21XX64X", "21XX65X", "21AIL66", "21AIMP67", "21INT68"]
    credits = [3, 4, 3, 3, 3, 1, 2, 3]
    marks = []
    obtained_credits = credits
    points = 0
    print("Enter the Total Obtained Marks for the following subjects : ")
    for s in subjects:
        marks.append(int(input(s + " : ")))
    if (input("All Passed ? (Y/N) : ") == "N"):
        print("Enter F if failed, else press enter")
        for s in subjects:
            if (input("s : ") == "F"):
                obtained_credits[subjects.index(s)] = 0
    for x in range(len(subjects)):
        points += grade_point(marks[x], obtained_credits[x])
    sgpa = points / sum(obtained_credits)
    print("SGPA : ", sgpa)

def sgpa7():
    subjects = ["21AI71", "21CS72", "21XX73X", "21XX74X", "21XX75X", "21AIP76"]
    credits = [3, 2, 3, 3, 3, 10]
    marks = []
    obtained_credits = credits
    points = 0
    print("Enter the Total Obtained Marks for the following subjects : ")
    for s in subjects:
        marks.append(int(input(s + " : ")))
    if (input("All Passed ? (Y/N) : ") == "N"):
        print("Enter F if failed, else press enter")
        for s in subjects:
            if (input("s : ") == "F"):
                obtained_credits[subjects.index(s)] = 0
    for x in range(len(subjects)):
        points += grade_point(marks[x], obtained_credits[x])
    sgpa = points / sum(obtained_credits)
    print("SGPA : ", sgpa)

def sgpa8():
    subjects = ["21AI81", "21INT82", "21NS83/21PE83/21YO83"]
    credits = [1, 15, 0]
    marks = []
    obtained_credits = credits
    points = 0
    print("Enter the Total Obtained Marks for the following subjects : ")
    for s in subjects:
        marks.append(int(input(s + " : ")))
    if (input("All Passed ? (Y/N) : ") == "N"):
        print("Enter F if failed, else press enter")
        for s in subjects:
            if (input("s : ") == "F"):
                obtained_credits[subjects.index(s)] = 0
    for x in range(len(subjects)):
        points += grade_point(marks[x], obtained_credits[x])
    sgpa = points / sum(obtained_credits)
    print("SGPA : ", sgpa)


if __name__ == "__main__":
    sem = int(input("Enter the Semester Number of which SGPA should be calculated : "))
    match sem:
        case 1 :
            sgpa1()
        case 2 :
            sgpa2()
        case 3 :
            sgpa3()
        case 4 :
            sgpa4()
        case 5 :
            sgpa5()
        case 6 :
            sgpa6()
        case 7 :
            sgpa7()
        case 8 :
            sgpa8()
        case default :
            print("Wrong Semester Number : ")