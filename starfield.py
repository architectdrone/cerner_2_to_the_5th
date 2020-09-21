#cerner_2^5_2020
for _ in range(int(__import__("sys").argv[2])): print("".join([(__import__("random").choice([".", "*", "+", "o"] + [" " for _ in range(int(__import__("sys").argv[1]))])) for _ in range(int(__import__("sys").argv[2]))]))

'''
python starfield.py <emptiness> <size>
Set emptiness to 5 for Hubble deep field, 50 for night sky
PS C:\dev\personal> python .\starfield.py 5 20
o+.    +*o * * o  o*
  *  +  *  +   *+ o 
 o * .+   o+*  ..
 .    .  *o*    +*
+ +*     o   .   *+o
  +     o*   * +    
 o  * o**o    o .  .
  *  . .     ..  o.
o +*+o*.  *    ++ .
**o+ .  o *      +.
   o.+  .o....o   *
  +*  .o  .   *  *
 * ** ** .o .o   .
    *   *     +  . .
. +  *  o* .     ooo
   . .+*  o.+  * .o+
+ +.  * .      .   +
 o+.   o  +*. o ..*
      *  ++o     . *
  * *   .* *o * +. o
'''
