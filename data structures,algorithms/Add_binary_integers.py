#Add_binary_integers

"""
In this script we want to add two n-bit integers and return an n+1 bit integer stored in array wich A[1] is most significant bit and
A[n] is least significant bit.first we have an empty list named C.starting form n and going to 1,we initialize a carry = 0 and find
(A[n] + B[n] + carry) (mod 2) storing it in c[n + 1],then we change carry depending on mod_2 of (A[i] + B[i] + carry) and going to next i
in descending order,when the loop finishes we put the last carry in C[1],terminating the function succesfuly.in floyde_hoare logic
{carry and A[i] and B[i]}C[i + 1] = A[i] + B[i] + carry{carry = 1 if A[i] + B[i] + carry >= 2 else 0}/{i = n}C[i + 1] = A[i] + B[i] + carry{C[1] = carry}
"""

def add_binary(A,B):

    """This function adds two binary integers"""

    C = [0 for i in range(len(A) + 1)] #cost = c1 times = n + 1
    
    carry = 0 #cost = c2 times = 1

    for i in range(len(A) - 1,-1,-1):#cost = c3 times = n + 1

        C[i + 1] = (A[i] + B[i] + carry) % 2 #cost = c4 times = n

        if A[i] + B[i] + carry >= 2:#cost = c5 #times = n

            carry = 1

        else:

            carry = 0

    C[0] = carry #cost = c6 times = 1

    return C

#Create two example binary numbers
A = [0,0,1]

B = [1,1,1]

print(add_binary(A,B))

"""
Worst,best,average case are similar.T(n) = c1 * (n + 1) + c2 * 1 + c3 * (n + 1) + c4 * (n) + c5 * (n)  + c6 = an + b,a linear function

of n,wich makes overall complexity Θ(n).
"""