gradeList = []
sum = 0
highGrade = 0
lowGrade = 100
numGrades = int(input('Please enter your number of grades: '))
for i in range(0,numGrades,1):
    grade = float(input('What is your grade? '))
    gradeList.append(grade)
for i in range(0,numGrades,1):
    sum = sum + gradeList[i]
avg = sum/numGrades
for i in range(0,numGrades,1):
    if gradeList[i] > highGrade:
        highGrade = gradeList[i]
for i in range(0,numGrades,1):
    if gradeList[i] < lowGrade:
        lowGrade = gradeList[i]
print('Your average is', avg)
print('Lowest grade =',lowGrade)
print('Highest grade =', highGrade)

for i in range(0,numGrades,1):
    for i in range(0,numGrades-1,1):
        if gradeList[i] < gradeList[i+1]:
            swp = gradeList[i]
            gradeList[i] = gradeList[i+1]
            gradeList[i+1] = swp
print(gradeList)
