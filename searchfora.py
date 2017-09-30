def search(x):
    """
    =============
    Search for A
    =============
    NAME:
    search for a
    
    SYNOPSIS:
    element = search(x)
    
    DESCRIPTION:
    Program to solve a mod 2n congruent to 1 where n is positive integer field
    
    INPUTS:
    x               : List of even numbers to consider searching for bounded by n
    
    OUTPUTS:
    element         : Positive odd integer that satisfies the equation
    
    AUTHOR:
    Rohit Kashyap,2017
    """
    num = max(x)+1
    while(1):
        flag = 0
        for i in range(0,len(x)):
            if(num % x[i]!=1):
                flag = 1
                break
        
        if(flag==1):
            num = num+2
        else:
            return num
        
# Define the number of steps        
steps = 10

# Generate the list of even numbers
genlist = lambda steps:[x for x in range(2,steps*2,2) if x%2 == 0]

#Found List
foundList = [0]*steps

#First element is trivially true
foundList[0] = 1

# Find the numbers
for i in range(1,steps):
    foundList[i]= search(genlist(i+1))
    

