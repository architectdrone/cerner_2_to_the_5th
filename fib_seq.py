print((lambda iterations : [int((((1+__import__("math").sqrt(5))/2)**n - (1-((1+__import__("math").sqrt(5))/2))**n)/__import__("math").sqrt(5)) for n in range(iterations)])(int(__import__("sys").argv[1])))
'''
This abomination against programming is an attempt to get the fibbonacci sequence in one line.
I succeeded, but at what cost???

EXAMPLE:
PS C:\dev\personal> python .\fib_seq.py 10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''