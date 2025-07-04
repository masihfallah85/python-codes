#pythagoras-triples

"""
in this script we want to find all pythagoras triples(integers a, b, c satisfying a^2 + b^2 = c^2) from 1 to n with brute force
"""

#prompt user to enter upper bound of integers to find pythagoras triples
upper_bound  = int(input("enter upper bound of integers to set range to fidn pythagoras triples: "))

#loop through possible values for first edge
for edge_1 in range(1,upper_bound + 1):
    
    #loop through possible values for second edge(greater than first edge)
    for edge_2 in range(edge_1 + 1,upper_bound + 1):
        
        #loop through possible values for hypotenuse(greater than first edge and second edge)
        for  hypotenuse in range(edge_2 +1,upper_bound + 1):
            
            #check pythagoras condition
            if (edge_1 ** 2) + (edge_2 ** 2) == (hypotenuse ** 2):
                
                #print the result
                print(f"edge_1: {edge_1} , edge_2: {edge_2} , hypotenuse: {hypotenuse}")