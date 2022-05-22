#! /usr/bin/env python3

def func(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp


n1 = 10
n2 = 20
print("num1 = %d, num2 = %d" % (n1, n2))
func(n1, n2)
print("num1 = %d, num2 = %d" % (n1, n2))
