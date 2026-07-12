#start
num=int(input("Enter a number: "))
if num>99 or num<10:
    print('number should be between 10-99')
else:
    if num%10==num//10:
        print('tens equal ones')
    else:
        print('tens not equal ones')
#stop