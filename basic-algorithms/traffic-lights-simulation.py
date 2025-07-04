#traffic-lights-simulation

"""
This script simulates a vehicle traveling along a straight road with traffic lights.
The user inputs the number of traffic lights and the total length of the road.
For each traffic light, the script takes the position, red light duration, and green light duration.
The vehicle travels at a constant speed of 1 unit distance per second.
At each traffic light, if the vehicle arrives during the red phase, it waits until the green light.
The goal is to compute the total time taken to travel from the start point to the end point of the road.
"""

#prompt user to enter number of traffic lights
traffic_lights = int(input("enter number of traffic lights: "))

#prompt user to input  distance of starting and end points
length = int(input("enter distance of starting and end points: "))

#create a variable to store overall time
time = 0

#create a variable to store distance between two light 
distance_lights = 0

#create variables for distance of each traffic light and its red and green light time
distance = 0
red_time = 0
green_time = 0

#use this for loop logic to calculate times
for count in range(traffic_lights):

    #input distance,green and red time of each traffic light
    distance = int(input("enter distance of traffic light: "))
    red_time = int(input("enter time of red light: "))
    green_time = int(input("enter time of green light: "))

    #add distance to overall distance and time
    distance_lights = distance - distance_lights
    time += distance_lights

    #check if we encounter red light
    if time % (red_time + green_time) < red_time:
       
       #if we encounter red light,we should add red light remaining time to overall time
       time += red_time - (time % (red_time + green_time))
    
    #store the latest distance to distance_lights to use in next iteration of loop
    distance_lights = distance
    
#calculate and add the diffrence between distance of start and end points and farthest light(last one)
time += (length - distance)

#print the time taken to go from begin point to end point
print("time taken from start to end points is:",time)