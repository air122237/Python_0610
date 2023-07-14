#!/usr/bin/python3.10.8

import random

#times=int(input(f"how many random number you need?"))

#for i in range(0,times):
#   i+=1
def ulti_pw():
    min=0
    max=10
    count=0
    bomb= random.randint(min,max-1) #隨機生成終極密碼
    print (f"random number is {bomb}")
    print("============終極密碼============")
    while True:
        count+=1
        keyin=input(f"請輸入一個{min}~{max}間的數字")
        
        if not keyin.isnumeric():
            print (f"這不是一個數字")
            count-=1
            continue
        target=int(keyin)

        if bomb==target: #遊戲結束了
            print (f"GAME OVER! 終極密碼就是{bomb}")
            print (f"總共猜了{count}次")
            break
        elif target<min or target>max: #非翻圍內
            print (f"這不是一個{min}~{max}間的數字")
            count-=1
            continue
        elif target >bomb:  #改上限
            max=target
            continue
        else: #改下限
            min=target
            continue


while True:
    ulti_pw()
    

    cont=input("是否還要繼續(Y/N)")
    print("\n\n")
    #+++++++++++++確認使用者要不要繼續++++++++++++++++++++++++++++++++++++++++
    if cont=="n" or cont=="N":#使用者不要繼續
        break
    elif cont=="y" or cont=="Y":#使用者要繼續
        count=0
        min=0
        max=10
        continue
    else:
        print("byebye")
    break
    #+++++++++++++確認使用者要不要繼續++++++++++++++++++++++++++++++++++++++++==>老師建議改兩層While