import pickle
with open('myData.pkl','rb') as r:
    numStuds = pickle.load(r)
    names = pickle.load(r)
    grades = pickle.load(r)
while 1==1:
    which = input("which student"'s'" grade would you like to look at? ")
    for i in range(0,numStuds,1):
        if which == names[i]:
            print(names[i],"'s",'grade is',grades[i])



