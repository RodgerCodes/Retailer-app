import random
print('ec§ter the number of ypur choice between 0:20')
num =random.randrange(0,20)
value=int(input())
while value<num:
    print('the value is less')
    if value==num:
        print ('collect')
    else:
        print('try again')    