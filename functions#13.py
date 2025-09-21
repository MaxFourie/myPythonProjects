def highLow(numStuds,grades):
    high = 0
    low = 100
    for i in range(0,numStuds,1):
        if grades[i] < low:
            low = grades[i]
        if grades[i] > high:
            high = grades[i]
    print("your classes highest mark is:",high)
    print("Your classes lowest mark is:",low)
    return high,low
def classAvg(amount,grades):
    j = 0
    for i in range(0,amount,1):
        j = j + grades[i]
    avg = j/amount
    print("Your class's average is:",avg)
    return avg
def printGrades(amount,names,grades):
    print("print your student's grades are:")
    for i in range(0,amount,1):
        print(names[i],"'s grade is:",grades[i])
def studentArray(n):
    names = []
    x = []
    for i in range(0,n,1):
        name = input("What is your student's name? ")
        names.append(name)
        grade = float(input('What is your students grade? '))
        x.append(grade)

    return x,names

numStudent = int(input('how many students do you have? '))
grades,names = studentArray(numStudent)
printGrades(numStudent,names,grades)
avg = classAvg(numStudent,grades)
highLow(numStudent,grades)



