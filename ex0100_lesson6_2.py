#!/usr/bin/python3.10.8

import random

times=int(input(f"how many random number you need?"))

for i in range(0,times):
    i+=1
    min=1
    max=10
    target= random.randint(min,max)
    print (f"random number is {target}")
