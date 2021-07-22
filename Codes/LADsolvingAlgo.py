import numpy as np
import matplotlib.pyplot as plt
import random

print(" ")
print("______________________________________")
print("Step-Wise Algorithm")
print(" ")

#creating datapoints
X = np.ones((100,2))  # we are working in a 2d plane with 100 datapoints
for i in range(100): #x[:,0] is going to be =1 thrughout as this will accomodate the intercept c
    X[i,1] = random.randint(0,100)

y = np.ones((100,1))
for i in range(100):
    y[i,0] = ( i*0.01*X[i,1] ) + (10*random.random())

plt.plot(X[:,1], y, 'yo',label="sample points") #plotting the points on a graph
plt.xlabel("x values->")
plt.ylabel("y values ->")
plt.legend()
plt.title("Graph containing the sample points")
plt.show()


#initializing the feature vector
theta = np.ones((2,1)) # we are only working with two variables that is slope m and y-intercept c

abs_vector = np.abs ( y - np.matmul(X, theta))  # stores |yi-mxi-c|
print("sum of absolute differences before minimization = ", np.sum(abs_vector))

#running the itrative step wise algorithm
for i in range(250):
    k = theta[1,0] #storing the previous value of m
    temp = np.ones((100,1)) #creating a temporary array to find the weighted median
    for j in range(100):
        temp[j,0]= y[j,0] - (k*X[j,1])    
    temp = np.sort(temp,axis=0) #sorting to find median
    medi = (temp[49,0]+temp[50,0])/2.0 #finding median
    theta[0,0]=medi #updating the value of c

    k = theta[0,0] #storing the previous value of c
    X_abs = np.abs (X[:,1]) #storing the absolute value X values to create the weighted array
    num = np.sum(X_abs) #counting the length of the weighted array
    temp = np.ones((int(num),1)) #creating a temporary array to find the weighted median
    count = 0 

    for j in range(100):  #updating temp array with weighted values
        for l in range(int(X_abs[j])):
            temp[int(count),0] = (y[j,0] - k)/X[j,1]
            count = count + 1        
    
    temp = np.sort(temp,axis=0) #sorting to find median
    length=np.shape(temp)[0] 

    if length%2 == 0: #finding the median of temp when the lenth is even
        medi = (temp[int((length/2))-1,0]+temp[int(length/2),0])/2.0
    else: #finding the median of temp when the lenth is odd
        medi =temp[int(length/2),0]
    
    theta[1,0]=medi#updating the value of m

plt.plot(X[:,1], y, 'yo',label="sample points") #plotting the points on a graph
plt.plot(X[:,1], np.matmul(X, theta),'r',label="LAD regression line generated using step wise algorithm") #plotting the LAD regression line generated using step wise algorithm
plt.xlabel("x values->")
plt.ylabel("y values ->")
plt.legend()
plt.title("Graph containing the sample points along with the LAD regression line generated using step wise algorithm")
plt.show()

X_prev=np.matmul(X, theta)

abs_vector = np.abs ( y - np.matmul(X, theta))  # stores |yi-mxi-c|
print("sum of absolute differences after minimization = ", np.sum(abs_vector))
print("estimated c, m values = ", theta[0,0], theta[1,0])

print(" ")
print("______________________________________")
print("Iteratively Re-Weighted Least Squares")
print(" ")

theta = np.ones((2,1)) # we are only working wit two variables that is slope m and y-intercept c
weight = np.zeros((100,100)) # weight matrix is a square diagonal matrix with diagonal elements as 1/|yi-mxi-c|
abs_vector = np.abs ( y - np.matmul(X, theta))  # stores |yi-mxi-c|
delta = 0.01 # to avoid division by 0

for j in range(100): #ceating the initial weight matrix
    weight[j,j] = 1/(max(delta, abs_vector[j,0]))

print("sum of absolute differences before minimization = ", np.sum(abs_vector))

#irwls iterative code
for i in range(250):
    #updating theta after every run with (X(transpose)*weight(previous)*X)(inverse)*(X(transpose)*weight(previous)*y)
    theta = np.matmul(np.linalg.pinv(np.matmul(np.transpose(X), np.matmul(weight,X))),np.matmul(np.transpose(X), np.matmul(weight,y))) 
    abs_vector = np.abs ( y - np.matmul(X, theta)) 
    for j in range(100): #updating the weight vector
        weight[j,j] = 1/max(delta, abs_vector[j,0])

plt.plot(X[:,1], y, 'yo',label="sample points") #plotting the points on a graph
plt.plot(X[:,1], np.matmul(X, theta),label="LAD regression line generated using Iteratively Re-Weighted Least Squares") #plotting the LAD regression line generated using Iteratively Re-Weighted Least Squares
plt.title("Graph containing the sample points along with the LAD regression line generated using Iteratively Re-Weighted Least Squares")
plt.xlabel("x values->")
plt.ylabel("y values ->")
plt.legend()
plt.show()


print("sum of absolute differences after minimization = ", np.sum(abs_vector))
print("estimated c, m values = ", theta[0,0], theta[1,0])


print("______________________________________")
print("")
    
plt.plot(X[:,1], y, 'yo',label="sample points") #plotting the points on a graph
plt.plot(X[:,1], X_prev,'r',label="LAD regression line generated using step-wise algorithm") #plotting the LAD regression line generated using step-wise algorithm
plt.plot(X[:,1], np.matmul(X, theta),label="LAD regression line generated using Iteratively Re-Weighted Least Squares") #plotting the LAD regression line generated using Iteratively Re-Weighted Least Squares
plt.title("Graph containing the sample points along with the LAD regression line generated using step-wise algorithm and Iteratively Re-Weighted Least Squares")
plt.xlabel("x values->")
plt.ylabel("y values ->")
plt.legend()
plt.show()