beforeGPA=float(input("OLD GPA: "))
beforeHours=int(input("OLD HOURS: "))
AFTERGPA=float(input("NEW GPA: "))
AFTERHOURS=int(input("NEW HOURS: "))
TOTAL=AFTERHOURS+beforeHours
print(((beforeHours*beforeGPA)+(AFTERHOURS*AFTERGPA))/TOTAL)

