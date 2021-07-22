import numpy as np
import matplotlib.pyplot as plt
import random

p=0.3 #probability of A
q=0.3 #probability of B
r=0.4 #probability of O

cum_A = (p*p)+(2*p*r) #cumulative probability of phenotype A (AA + AO + OA)
cum_B = (q*q)+(2*q*r)+cum_A #cumulative probability of phenotype B (BB + BO + OB)
cum_AB = (2*p*q)+cum_B #cumulative probability of phenotype AB (AB + BA)
cum_O = (r*r)+cum_AB #cumulative probability of phenotype O (OO)

n = 1000 #total number of samples
nA = 0 #number of samples having blood group A
nB = 0 #number of samples having blood group B
nAB = 0 #number of samples having blood group AB
nO = 0 #number of samples having blood group O

for i in range(n):
    var = np.random.uniform(0,1)
    if var<=cum_A:
        nA=nA+1
    elif var<=cum_B:
        nB=nB+1
    elif var<=cum_AB:
        nAB=nAB+1
    else:
        nO=nO+1

nAA , nAO , nBB, nBO = 0.0, 0.0, 0.0, 0.0 #the missing data which will be estimated using the E step

p_cap = np.random.uniform(0,0.8) #initial estimates of p,q,r
q_cap = np.random.uniform(0,1-p_cap)
r_cap = 1 - p_cap - q_cap
print("\nSolution using EM algorithm run for 100 iterations\n")
print("initial estimates of p,q,r = ",p_cap,q_cap,r_cap)

for i in range(1000):
    nAA = (nA * p_cap * p_cap)/((p_cap * p_cap)+(2.0 * p_cap * r_cap))
    nAO = nA - nAA
    nBB = (nB * q_cap * q_cap)/((q_cap * q_cap)+(2.0 * q_cap * r_cap))
    nBO = nB - nBB

    p_cap = (nAA + nA + nAB)/(2*n)
    q_cap = (nBB + nB + nAB)/(2*n)
    r_cap = (nAO + nBO + nO + nO)/(2*n)

print("final estimates of p,q,r = ",p_cap,q_cap,r_cap)
print("nA,nB,nAB,nO,n = ", nA, nB, nAB, nO, n)
print("actual values of p,q,r = ",p,q,r,"\n")
