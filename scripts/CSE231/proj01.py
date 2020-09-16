#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:13:41 2019

@author: ks.mammie
"""
##############################################################################
# Programming Project #1
#
# Canoe Measurement
#     prompt for a floating-point value
#         representing a distance in rods
#         input a number in string
#         convert the number into a float
#         do the conversions 
#         round the results of the conversions 
#             to 3 decimal places and display the calculations    
##############################################################################

# Take an input and convert it into a float    
num_str = input( "Input rods: " ) # get a distance in rods
num_float = float( num_str ) # convert the distance "num_str" into a float

# Display an input in float
print( "You input ", num_float, "rods." ) # print the distance in float 

# Do the conversions of units
meters = num_float * 5.0292 # calculate meters
furlongs = num_float / 40   # calculate furlongs
miles = meters / 1609.34    # calculate miles
feet = meters / 0.3048      # calculate feet
walking_minutes = ( miles / 3.1 ) * 60  # calculate minutes taken to walk

# Round all the conversions to 3 decimal places and display the results 
print("\nConversions")              # introduce the results 
print("Meters:", round(meters,3) )  # display meters
print("Feet:", round(feet,3) )      # display feet 
print("Miles:", round(miles,3) )    # display miles
print("Furlongs:", round(furlongs,3) ) # display furlongs 
print("Minutes to walk", num_float, "rods:", round(walking_minutes,3) ) # display minute taken to walk


