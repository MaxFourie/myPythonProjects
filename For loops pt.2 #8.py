gradeList = []
sum = 0
numGrades = int(input('Please input the number of grades you have: '))
for i in range(0,numGrades,1):
    grade = float(input('please enter your grade: '))
    gradeList.append(grade)
for g in gradeList:
    sum += g
avg = sum/numGrades
print('average is:')
print(avg)
print('your grades are:')
for i in gradeList:
    print(i)