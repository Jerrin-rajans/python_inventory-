# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:52:43 2018

@author: jerrin rajan
"""

def vegetable(veg,n):
    p1,p2,p3 = 20,30,40
    if veg =='bringal':
        return p1*n
    elif veg =='potato':
        return p2*n
    elif veg == 'ladysfinger':
        return p3*n
    elif veg == 'no_item':
        return "no item"
    else:
        return 0
        print("not available")
def fruit(fruits,n1):
    p1,p2,p3=50,100,150
    if fruits == 'banana':
        return p1*n1
    elif fruits=='apple':
        return p2*n1
    elif fruits=='kiwi':
        return p3*n1
    elif fruits == 'no_item':
        return 'no_item'
    else:
        return 0
        print("not available")
def details(username):
    username = input("enter the user name")
    print(username)
def total_cost(veg,n,fruits,n1,username):
    username = input("enter the user name")
    print(username)
    total =  (int(vegetable(veg,n)) + int(fruit(fruits,n1)))
    return str(total)




























import veg_book as vb
username = input("enter the name")
veg = input("enter the vegetable")
n = int(input("enter the quantity"))
fruits= input("enter the fruits")
n1 = int(input("enter the quantity"))
with open("output.txt","a") as myfile:
    myfile.write((vb.total_cost(veg,n,fruits,n1,username)))
    myfile.writelines(["name\n|",username])
    myfile.writelines(["\nvegetable|",veg])
    myfile.writelines(["\nquantity|",str(n)])
    myfile.writelines(["\nfruits|",fruits])
    myfile.writelines(["\nquantity|",str(n1)])

    