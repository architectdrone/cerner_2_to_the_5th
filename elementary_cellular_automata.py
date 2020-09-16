a, b = [int(i) for i in __import__("sys").argv[1:3]]
c = [(1 if n == b else 0) for n in range(2*b+1)]
for i in range(b):
    d = []
    print("".join([("#" if i == 1 else " ") for i in c]))
    for x in range(len(c)):
        d.append([int(i) for i in (lambda x, n: format(x, 'b').zfill(n))(a, 8)][::-1][(0 if x == 0 else c[x-1])*(2**2)+c[x]*(2)+(0 if x == len(c)-1 else c[x+1])]) #This is the worst line of code I have ever written
    c = d
'''
Thanks to this guy https://stackoverflow.com/questions/699866/python-int-to-binary-string/21732313#21732313 for the padded binary conversion
USAGE: python elementary_cellular_automata.py <rule> <iterations>

PS C:\dev\personal> python .\elementary_cellular_automata.py 90 10 
          #
         # #
        #   #
       # # # #
      #       #
     # #     # #
    #   #   #   #
   # # # # # # # #
  #               #
 # #             # # 
'''