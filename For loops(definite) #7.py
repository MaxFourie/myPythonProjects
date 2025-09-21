gradeList = []
numGrades = int(input('please input the number of grades you have: '))
for grades in range(0,numGrades,1):
    grade = float(input('Enter grade: '))
    gradeList.append(grade)
print('Your Grades are')
for grades in range(0,numGrades,1):
    print(gradeList[grades])







