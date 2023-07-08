#!/usr/bin/python3.10.8

import random

#times=int(input(f"how many random number you need?"))

#for i in range(0,times):
#   i+=1
min=0
max=10
count=0
bomb= random.randint(min,max-1)
#    print (f"random number is {bomb}")
print("============終極密碼============")

cont=0

while True:
    count+=1
    keyin=input(f"請輸入一個{min}~{max}間的數字")
    
    if not keyin.isnumeric():
        print (f"這不是一個{min}~{max}間的數字")
        count-=1
        continue
    target=int(keyin)


    if bomb==target:
        print (f"GAME OVER! 終極密碼就是{bomb}")
        print (f"總共猜了{count}次")
        cont=input("是否還要繼續(Y/N)")
        if cont=="n" or cont=="N":
            break
        elif cont=="Y" or cont=="Y":
            count=0
            min=0
            max=10
            continue    
        else:
            print("byebye")
        break

    elif target<min or target>max:
        print (f"這不是一個{min}~{max}間的數字")
        count-=1
        continue
    elif target >bomb:
        max=target
        continue
    else:
        min=target
        continue
