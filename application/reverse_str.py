#!/usr/bin/python
# coding:utf-8
''' reverse str '''

def function():
    input_str=input("Please input a str:")
    point=len(input_str)//2
    left=input_str[:point]
    print(left)
    right=input_str[:point-1:-1]
    print(right)
    if left == right:
        print("Good,done!")
    else:
        print("Not right,try again")
        function()

function()

                   
