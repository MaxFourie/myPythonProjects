import pickle
username = input('Please pick a username: ')
password = input('Please create a password: ')
with open('userSecurity','wb') as D:
    pickle.dump(username.lower(), D)
    pickle.dump(password, D)
print('Your data has successfully been created')
