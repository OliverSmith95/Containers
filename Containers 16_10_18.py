# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:25:44 2018

@author: gy18os
"""
import matplotlib.pyplot
import random
#code for creating new number integers. Top agent is "agent 0", then the second one is 1. 
agents = []
agents.append([[random.randint(0,99),random.randint(0,99)],[random.randint(0,99),random.randint(0,99)]])
agents.append([[random.randint(0,99),random.randint(0,99)],[random.randint(0,99),random.randint(0,99)]])
agents.append([[random.randint(0,99),random.randint(0,99)],[random.randint(0,99),random.randint(0,99)]])
agents.append([[random.randint(0,99),random.randint(0,99)],[random.randint(0,99),random.randint(0,99)]])



#printing agents,
print (agents[0])
print (agents[1])
print (agents[2])
print (agents[3])
print(max(agents))



#abm practical start
y0 = 50
x0 = 50

print (y0, x0)
print (y0, x0)

#set up first set of vairables
if random.random () <0.5:
    y0 = y0 + 1 
else:
    y0 = y0 - 1

if random.random () <0.5:
    x0 = x0 + 1 
else:
    x0 = x0 - 1

print (y0, x0)
    
if random.random () <0.5:
    y0 = y0 + 1 
else:
    y0 = y0 - 1

if random.random () <0.5:
    x0 = x0 + 1 
else:
    x0 = x0 - 1

print (y0, x0)
#Set up second set
#x1=50
x1 = 50
y1 = 50

print (y1, x1)

#set up y1 and x1 - step 1
if random.random () <0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1  
    
if random.random() <0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print (y1, x1) 
#set up y1 and x1 twice - step 2 
if random.random () <0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

if random.random () <0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
#print the outcome, reason for printing twice is a 2 step code.
print (y1,x1)

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq 
distance1 = sum**0.5
print(distance1) 


import operator    # Do this line at the top of the code.
#add max agent to test the furthest east.
print(max(agents, key=operator.itemgetter(1)))    # Do this line at the bottom.
#to assign a colour, add with a comma at the end of the line.
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color='red')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='yellow')
matplotlib.pyplot.show()

