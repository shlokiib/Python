grade10 = int(input("ENTER 10th GRADE: "))
grade12 = int(input("ENTER 12th GRADE: "))
cgpa = int(input("ENTER CGPA: "))
hire = False
if grade10>= 80:
    if grade12>= 60:
        if cgpa >=8:
            hire = True
            print("Kudos you've been hired")
        else:
            hire = False
            print("College CGPA not enough")
    else: 
        hire = False
        print("Grade 12th not enough")
else :
    hire = False
    print("Grade 10th not enough")
    
