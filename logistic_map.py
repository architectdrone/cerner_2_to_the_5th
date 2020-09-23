#cerner_2^5_2020
current_x = float(__import__("sys").argv[2])
for i in range(int(__import__("sys").argv[3])): print(current_x := float(__import__("sys").argv[1])*current_x*(1-current_x))

'''
Behold, the strange behavior of the LOGISTIC MAP! Determine the location of BIFURCATIONS! Observe the onset of CHAOS!
The logistic map is a generalization of the logistic model of population. This model takes into account overcrowding.
The equation is x(i+1) = R*(x(i))*(1-x(i)). x is proportion of carrying capacity. R is rate of reproduction.
For R < 3, population trends towards a fixed point.
At R = 3, population bifurcates - that is, there is an oscillation between two different populations
At R = 3.4, it bifurcates again, into a quadruple oscillation. 
This bifurcation happens faster and faster until R is approximately 3.569946, at which point the population has effectively bifurcated infinitely.
After this point, no oscillation is observable, and the population is essentially random.
The population also shows sensitive dependence on initial conditions - that is, chaos.
In fact, this has even been used to generate random numbers! All from such a simple function - spoooOOOoooOOOoooky
I (obviously) didn't invent this function. Instead, I read about it in a book I am reading, called "Complexity: A Guided Tour". 
Also see this youtube video by Veritasium: https://www.youtube.com/watch?v=ovJcsL7vyrk&vl=en

USAGE: python logistic_map.py <R> <x_0> <number of iterations>
EXAMPLE:
PS C:\dev\personal> python .\logistic_map.py 4 0.2 10 
0.6400000000000001
0.9215999999999999
0.28901376000000045
0.8219392261226504
0.585420538734196
0.970813326249439
0.11333924730375745
0.40197384929750063
0.9615634951138035
0.14783655991331973
'''
