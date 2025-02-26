#generate a marksheet using if else and elif statements

student_percentage = int(input("Enter student percentage: "))

if student_percentage >= 80:
    print("Grade A1")
elif student_percentage >= 70:
    print("Grade A")
elif student_percentage >= 60:
    print("Grade B")
elif student_percentage >= 50:
    print("Grade C")
elif student_percentage >= 40:
    print("Grade D")
elif student_percentage >= 33:
    print("Grade E")
else:
    print("Fail")