import numpy as np
import matplotlib.pyplot as plt
import random

a=0.2 #probability of A
b=0.3 #probability of B
c=0.5 #probability of C
nAB=nBA=nBC=nCB=0

for i in range(100):
    var = np.random.uniform(0,1)
    if var<(a/(a+b)):
        nAB=nAB+1
    elif var>(a/(a+b)):
        nBA=nBA+1

for i in range(200):
    var = np.random.uniform(0,1)
    if var<(b/(c+b)):
        nBC=nBC+1
    elif var>(b/(c+b)):
        nCB=nCB+1

nAC=nCA=0

a_cap = 1 #fixed
b_cap = np.random.uniform(0,0.5)
c_cap = 1-b_cap

while 1<2:
    
    b_cap_1 = (nBA+nBC) / ( ((nAB+nBA)/(b_cap+1)) + ((nBC+nCB)/(b_cap+c_cap)) )
    c_cap_1 = (nCA+nCB) / ( ((nAC+nCA)/(1+c_cap)) + ((nBC+nCB)/(b_cap+c_cap)) )
 
    if np.abs(((b_cap-b_cap_1)/b_cap)+((c_cap-c_cap_1)/c_cap))<0.0001:
        break

    b_cap = b_cap_1
    c_cap = c_cap_1


print("\nFinal estimates of a, b, c = ",a_cap,b_cap,c_cap)
print("Final relative estimates of a, b, c = ",a_cap/(a_cap+b_cap+c_cap),b_cap/(a_cap+b_cap+c_cap),c_cap/(a_cap+b_cap+c_cap))
print("Actual values of a, b, c = ",a,b,c)
print("nAB, nBA, nAC, nCA, nBC, nCB = ",nAB,nBA,nAC,nCA,nBC,nCB)
print(" ")