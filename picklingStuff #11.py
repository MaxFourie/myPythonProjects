import pickle
names = []
grades = []
numStuds = int(input('How many students do you have? '))
for studs in range(0,numStuds,1):
    name = input('what is their name? ')
    names.append(name)
    grade = float(input('what is their average? '))
    grades.append(grade)
with open('myData.pkl','wb') as f:
    pickle.dump(numStuds,f)
    pickle.dump(names,f)
    pickle.dump(grades,f)

with open('myData.pkl', 'rb') as r:
    a = pickle.load(r)
    b = pickle.load(r)
    c = pickle.load(r)
print(a)
print(b)


