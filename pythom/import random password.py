import random

print("welcome to random password generator!")
randomchars ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&"
nbrofpwds = int(input("please enter the number of passwords to be generated:"))
pwdlen = int(input("please enter the length of password needed:"))

print("Here are your random passwords:")
for x in range(nbrofpwds):
    pwd=""
    for chars in range(pwdlen):
        pwd = pwd + random.choice (randomchars)
    print(pwd)    