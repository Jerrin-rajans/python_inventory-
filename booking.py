# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:06:58 2018

@author: jerrin rajan
"""

def plane_ride_cost(city):
    if city =='goa':
        return 1200
    elif city=='america':
        return 5000
    elif city=='australia':
        return 6000
    elif city=='delhi':
        return 9000
    else:
        return 0
        print("not available")

        
        
def hotel_cost(night):
    if night == 1 :
        return night*1000
    elif night==2 :
        return night*9000
    elif night==3:
        return night*5000
    elif night==4 :
        return night*9000
    elif night==5:
        return night*9000
    else:
        return 0
        print("charges will be taken extra")
        
def rental_car_cost(days):
    if days <=2:
        return 400*1
    elif days>=3 and days < 7:
        return 400*days-200
    elif days>=7:
        return 400*days-500
    else:
        return 0
        print("select the above package")

def total_trip_cost(city,night,days):
   total_cost = (plane_ride_cost(city) + hotel_cost(night) + rental_car_cost(days))
   return total_cost
#night =int(input("enter the number of nights"))
#type_=input("enter the type of rooms")
#days = int(input("enter the days"))
#city = input("enter the city")
#total_trip_cost(city,night,days)
   





