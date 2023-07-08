#!/usr/bin/python3.10.8

import random

#times=int(input(f"how many random number you need?"))

#for i in range(0,times):
#   i+=1
min=1
max=10
count=0
bomb= random.randint(min,max)
#    print (f"random number is {bomb}")
print("============終極密碼============")


while True:
    count+=1
    target=int(input(f"請輸入一個[{min}~{max}間的數字"))
    if bomb==target:
        print(f"你輸了! 終極密碼就是{bomb}")
        break
    elif target<min or target>max:5
    
        print(f"這不是一個[{min}~{max}間的數字")
        continue
    elif target >bomb:
        max=target
        continue
    else:
        min=target
        continue
