class student:
    def __init__(self,firstName,lastName,numberOfGrades):
        self.first = firstName
        self.last = lastName
        self.numGrades = numberOfGrades

    def askGrades(self):
        self.grades = []
        for i in range(0,self.numGrades,1):
            self.grade = float(input('What is your grade? ')) #use self. when you want to use the variable with other methods.
            self.grades.append(self.grade)
        return self.grades

    def avg(self):
        j = 0
        for i in range(0,self.numGrades,1):
            j = j + self.grades[i]
        avg = j/self.numGrades
        return avg

    def sort(self):
        for i in range(0,self.numGrades,1):
            for i in range(0,self.numGrades-1,1):
                if self.grades[i] < self.grades[i+1]:
                    swp = self.grades[i]
                    self.grades[i] = self.grades[i+1]
                    self.grades[i+1] = swp
        return self.grades

    def highLow(self):
        self.high = 0
        self.low = 100
        for i in range(0,self.numGrades,1):
            if self.high < self.grades[i]:
                self.high = self.grades[i]
            if self.low > self.grades[i]:
                self.low = self.grades[i]
        return self.high,self.low


numGrades = int(input("How many grades do you have? "))
student1 = student('Max','Fourie',numGrades)
grades = student1.askGrades()
avg = student1.avg()
sort = student1.sort()
high,low = student1.highLow()

print("your grades are:",grades)
print("Your average is:",avg)
print("Your high grade is:",high,"Your low grade is:",low)
print("Your grade's sorted are:",sort)

