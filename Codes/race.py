import numpy as np
import matplotlib.pyplot as plt
import random

#likelihood function is based on the following race standings
print("\nRace 1 = B C A") #race 1 result 
print("Race 2 = C D B A") #race 2 result
print("Race 3 = C B") #race 3 result

#respective capacity parameter value initialization
a_cap = 1 #fixed 
b_cap = np.random.uniform(0,1)
c_cap = np.random.uniform(0,1)
d_cap = np.random.uniform(0,1)

print("\nModified Bradley Terry Approach")

#MM algorithm run until convergence
while 1<2:
    
    b_cap_1 = 2.0/ ((1.0/(b_cap+c_cap+1)) + (1.0/(c_cap+b_cap)) + (1.0/(d_cap+b_cap+1)) + (1.0/(c_cap+d_cap+b_cap+1)) + (1.0/(b_cap+1)))
    c_cap_1 = 3.0/ ((1.0/(b_cap+c_cap+1)) + (1.0/(c_cap+b_cap)) + (1.0/(c_cap+d_cap+b_cap+1)) +(1.0/(c_cap+1)))
    d_cap_1 = 1.0/ ((1.0/(d_cap+b_cap+1)) + (1.0/(c_cap+d_cap+b_cap+1)))
 
    if np.abs(((b_cap-b_cap_1)/b_cap)+((c_cap-c_cap_1)/c_cap)+((d_cap-d_cap_1)/d_cap))<0.01:
        break

    b_cap = b_cap_1
    c_cap = c_cap_1
    d_cap = d_cap_1 

print("a_cap, b_cap, c_cap, d_cap = ",a_cap,b_cap,c_cap,d_cap,"\n")

#respective capacity parameter value initialization
a_cap = 1 #fixed
b_cap = np.random.uniform(0,1)
c_cap = np.random.uniform(0,1)
d_cap = np.random.uniform(0,1)

print("\nOur Approach")

#MM algorithm run until convergence
while 1<2:
    
    b_cap_1 = 3.0/ ((3.0/(b_cap+c_cap)) + (1.0/(d_cap+b_cap)) + (2.0/(b_cap+1)))
    c_cap_1 = 5.0/ ((3.0/(b_cap+c_cap)) + (1.0/(c_cap+d_cap)) + (2.0/(c_cap+1)))
    d_cap_1 = 2.0/ ((1.0/(c_cap+d_cap)) + (1.0/(d_cap+b_cap)) + (1.0/(d_cap+1)))
 
    if np.abs(((b_cap-b_cap_1)/b_cap)+((c_cap-c_cap_1)/c_cap)+((d_cap-d_cap_1)/d_cap))<0.01:
        break

    b_cap = b_cap_1
    c_cap = c_cap_1
    d_cap = d_cap_1 

print("a_cap, b_cap, c_cap, d_cap = ",a_cap,b_cap,c_cap,d_cap,"\n")