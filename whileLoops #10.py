grades = []
j = 0
numGrades = int(input('please enter the number of grades you have? '))
while j < numGrades:
    grade = float(input('Please enter your grade: '))
    grades.append(grade)
    j = j+1
print('your grades are')
j = 0
while j < numGrades:
    print(grades[j])
    j = j+1

