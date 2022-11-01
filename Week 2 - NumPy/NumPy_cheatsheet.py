# -*- coding: utf-8 -*-

"""
NumPy is a library for the Python programming language. It is the core library 
for scientific computing and provides support for large, multi-dimensional 
arrays and matrices. It also contains a large collection of high-level 
mathematical functions to operate on these arrays such as transformations.
"""

"""
It is recommented to run these commands line by line and check your variable 
explorer to see what type of object each command generates. 
"""

# Import convention
import numpy as np


# Create an array (1-D)
#This is a list: [1,2,3]
my1dArray = np.array([1,2,3])

# Create an array (2-D)
#This is a list containing two lists:
#  [ [1,2,3]
#    [4,5,6] ]
my2dArray = np.array([[1,2,3], [4,5,6]])

# An array can have any data type which can also be specified
my2dArrayFloat = np.array([[1,2,3], [4,5,6]], dtype = 'float')
my2dArrayFloat32 = np.array([[1,2,3], [4,5,6]], dtype = np.float32)

# Parenthesis may also be used instead of brackets to specify the array. The
# following commands result to the same arrays as a1 and b1
my2dArray2 = np.array([(1,2,3), (4,5,6)])
my2dArray3 = np.array(((1,2,3), (4,5,6)))

# What would happen if a list contains characters? In such case all the numeric
# values would be turn into characters. The dtype of the array will then be U# 
# (U = unicode, # = number of elements it can hold depending on the OS).
charArray1 = np.array([(1,'a',3), (4,5,'zzz')])
charArray2 = np.array([('1','a','3'), ('4','5','zzz')])
charArray3 = np.array([(1,'a',3), (4,5,'zzz')], dtype = 'U11')
charArray4 = np.array([(1,'a',3), (4,5,'zzz')], dtype = 'U21')
# Why this is the case? Because integer type has less priority than Unicode.



"""
--------------------
Array Initialisation
--------------------
"""

number_rows = 2
number_columns = 3

"""
The following commands are commonly used to initialise arrays.
"""
array0s = np.zeros( (number_rows, number_columns) )
array1s = np.ones( (number_rows, number_columns) )
array5s = 5 * np.ones( (number_rows, number_columns) )
array7s = np.full( (number_rows, number_columns), 7 )
# By default these arrays would be of type float one could specify integer type
array0s_int = np.zeros( (number_rows, number_columns), dtype='int' )       #default integer based on OS
array0s_int16 = np.zeros( (number_rows, number_columns), dtype='int16' )   #16-bitinteger
array0s_int16b = np.zeros( (number_rows, number_columns), dtype=np.int16 ) #16-bitinteger

"""
Evenly spaced values
"""
# Create array of evenly spaced values
start = 10
end = 25

step = 3
evenlyStep = np.arange(start,end,step) #this results to: array([10, 13, 16, 19, 22])

number_samples = 3
evenlySample = np.linspace(start,end,number_samples) #this results to: array([10, 17.5, 25])

"""
Other commands to initialised arrays.
"""
identity = np.eye(2)               #creates a 2x2 identity matrix
random01 = np.random.random((2,3)) #creates a 2x3 array of random values [0.0, 1.0)
randomIntRange = np.random.randint(0, 10, (2,3)) #creates a 2x3 array of random values [0, 10)



"""
-----------------------------------------------
Array Inspection, Subsetting, Slicing, Indexing
-----------------------------------------------
"""
a = np.array([[5,6,3],[2,5,1]])
print("Let array a = ")
print(a)
print("a has ndims: ",  a.ndim)
print("a has shape:",   a.shape)
print("a has size: ",   a.size)
print("a if of type: ", a.dtype)

print("Element at position (0,1): ", a[0,1])
print("Second row of a", a[1:])
print("Second column of a, first and second elements", a[0:2,1])
print("Elements of a smaller than 3", a[a<3])

b = np.array([[5,6,3],[2,5,1],[4,4,4]])
print("Let array b = ")
print(b)
print("Diagonal of b is", np.diag(b))



"""
-----------------------------------------------
Array Arithmetics
-----------------------------------------------
"""
a = np.array([[1,2,5],[7,1,3]])
b = np.array([[4,6,9],[2,5,1]])

# Addition
add1 = a + b
add2 = np.add(a,b)

# Subtraction
sub1 = a - b
sub2 = np.subtract(a,b)

# Multiplication (element-wise)
mul1 = a * b
mul2 = np.multiply(a,b)

# Division (element-wise)
div1 = a / b
div2 = np.divide(a,b)

# Other (element wise) operations
exp = np.exp(a)     #exponential
sqroot = np.sqrt(a) #square root
sin = np.sin(a)     #sine
cos = np.cos(a)     #cosine
log = np.log(a)     #natural logarithm

# Dot product
b = np.array([[4,6],[2,5],[9,1]])
dotp = a.dot(b) # a is 2x3 and b is 3x2, expected dotp to be 2x2



"""
-----------------------------------------------
Array Statistics
-----------------------------------------------
"""
a = np.array([[1,2,5],[7,1,3]])

# Summation (overall)
summ1 = a.sum()
summ2 = np.sum(a)

# Summation (column-wise)
summ1row = a.sum(axis=0)
summ2row = np.sum(a, axis=0)

# Maximum (overall)
maxi = a.max()
# Maximum (row-wise)
maxiCol = a.max(axis=1)

# Mean (column-wise)
average = np.mean(a, axis=0)

# Standard deviation (overall)
std = np.std(a)



"""
-----------------------------------------------
Array Manipulation
-----------------------------------------------
"""
a = np.array([[1,2,5],[7,1,3]])

# Transpose
aTr1 = np.transpose(a)
aTr2 = a.T

# Reshape
reshape1 = np.reshape(a,(3,2))
reshape2 = a.reshape(3,2)
reshapeToRow = a.reshape(6)

# Combine arrays row-wise
b = np.array([3,4,1])
c = np.array([[4,4,4],[7,7,7]])
bac = np.vstack([b,a,c])

# Combine arrays column-wise
b = np.array([[7,8],[4,1]])
c = np.array([[9],[9]])
abc = np.hstack([a,b,c])

# Combine arrays either way
b = np.array([[7,8],[4,1]])
c = np.array([[4,4,4],[7,7,7]])
ab = np.concatenate((a,b),axis=1)
ac = np.concatenate((a,c),axis=0)



"""
-----------------------------------------------
Array I/O
-----------------------------------------------
"""
a = np.array([[1,2,5],[7,1,3]])
b = np.array([[7,8],[4,1]])

# Save an array to binary file (default extension .npy)
np.save('array_a', a)
# Save several arrays to file (default extension .npz)
np.savez('arrays_ab', arr1=a, arr2=b)
# Save an array to text file (extension .txt should be specified)
np.savetxt("array_a.txt", a)
# Save an array to text file specifying the separator "," and numbers as integers
np.savetxt("array_a2.txt", a, delimiter=',', fmt='%d')
# Save an array to a Comma Separated Values file (.csv). 
# For such files delimiter must always be set to ',' or else all the array will
# be written inside the same cell.
np.savetxt("array_a2.csv", a, delimiter=',', fmt='%d')

# Load the .npy file
Anpy = np.load("array_a.npy")
# Load the arrays inside the .npz file
contents = np.load("arrays_ab.npz")
Anpz = contents["arr1"]
Bnpz = contents["arr2"]

# Import the .txt files
Atxt1 = np.loadtxt("array_a.txt")
Atxt2 = np.loadtxt("array_a2.txt", delimiter=',')
# Import the .csv file
Acsv = np.loadtxt("array_a2.csv", delimiter=',')



"""
-----------------------------------------------
Task 1
-----------------------------------------------
"""
# Generate NumPy array
arr = np.array([0,2,4,5,3,7,8,9,5,1])
# Find and replace odd numbers with their negative value
arr[arr % 2 == 1] = -1*arr[arr % 2 == 1]



"""
-----------------------------------------------
Task 2
-----------------------------------------------
"""
A = np.array([0,0])
B = np.array([0,3])
C = np.array([1.5,0])
# Compute AB
AB_diffSquared = np.power(A-B, 2)
AB_squared = np.sum(AB_diffSquared)
AB = np.sqrt(AB_squared)
# Compute AC
AC = np.sqrt(np.sum(np.power(A-C,2)))
# Compute BC
BC = np.sqrt(AB**2 + AC**2)

# Alternative
from numpy import linalg as la
AB2 = la.norm(A-B)
AC2 = la.norm(A-C)
BC2 = la.norm(B-C)



"""
-----------------------------------------------
Short Project
-----------------------------------------------
"""
# Get the Iris dataset
dataRaw = np.loadtxt("iris-head-num.txt", delimiter=',', dtype='object')
# Get the header (first row)
header = dataRaw[0,:]
# Get the data (second row till end; 1-4th columns). Convert them to float
data = dataRaw[1:,:4]
data = np.vstack(data.astype(np.float32))
# Get the labels (second row; 4th columns)
labels = np.vstack(dataRaw[1:,4].astype(np.int32))

# Find unique labels and frequency
labelsUn, labelsCounts = np.unique(labels, return_counts=True)

# Find average, maximum, minimum and stand deviation of each column per category
nrows,ncols = np.shape(data) #number of rows (observations) and columns (attributes or features)
nclasses = len(labelsUn)     #number of unique categories
#Initialise an nclasses-by-ncols per statistic
average = np.zeros((nclasses,ncols))
maxi = np.zeros((nclasses,ncols))
mini = np.zeros((nclasses,ncols))
sd = np.zeros((nclasses,ncols))
for i in labelsUn:
    indexes = np.reshape(labels==i,nrows)
    average[i-1,:] = np.mean(data[indexes,:],axis=0)
    maxi[i-1,:] = np.max(data[indexes,:],axis=0)
    mini[i-1,:] = np.min(data[indexes,:],axis=0)
    sd[i-1,:] = np.std(data[indexes,:],axis=0)

# Find outliers per class and feature based on the formula mean+-2*sd
#More optimal ways are available but let's do it with nested for loops for revision
outliers2sd = np.zeros((nclasses,ncols))
for i in labelsUn:
    indexes = np.reshape(labels==i,nrows)
    classData = data[indexes,:]
    for j in range(ncols):
        thresholdLow = average[i-1,j]-2*sd[i-1,j]
        thresholdHigh = average[i-1,j]+2*sd[i-1,j]
        remain = [x for x in classData[:,j] if(x > thresholdLow)]
        remain = [x for x in classData[:,j] if(x < thresholdHigh)]
        outliers2sd[i-1,j] = 100 * (labelsCounts[i-1] - len(remain)) / labelsCounts[i-1]

# Export to .csv file
decimals = 2
fmt = "%.2f"
formatf = ".csv"
species = np.array(['setosa','versicolor','virginica'])
for i in range(len(labelsUn)):
    temp = np.vstack( [average[i,:], mini[i,:], maxi[i,:], sd[i,:], outliers2sd[i,:]] ).T
    temp = np.around(temp,decimals)
    temp_str = np.char.mod(fmt, temp)
    rows = np.array(header[:-1].astype("U"))[:, np.newaxis]
    rowsf = np.hstack((rows, temp_str))
    headerf = [species[i],'mean','min','max','std','outliers2sd%']
    np.savetxt(species[i]+formatf, np.vstack((headerf, rowsf)), delimiter=',', fmt='%s')



        