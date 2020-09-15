#cerner_2^5_2020
a = int(__import__("sys").argv[1])
while a-1: print(a := int((a/2, 3*a+1)[a%2]))

'''
Prints the result of applying the iterated Collatz transition function on a given number.
Only works on Python 3.8+!

EXAMPLE:
> python collatz_conjecture.py 30
15
46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1

TROUBLESHOOTING:
Q. Help! The program is stuck in an infinite loop!
A. Congratuations, you just disproved the Collatz conjecture
'''
