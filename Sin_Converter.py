#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
n = int(input("Enter the value of the sin Function :"))
out = 1

if n < 90 :

    if n == 0 :
        out = 0 
    elif n == 30 :
        out = 1 / 2
    elif n == 45 :
        out = "1 / root2"
    elif n == 60 :
        out = "root3 / 2"
    elif n == 90 :
        out = "ND"

else:
    r = (n % 90)
    q = n // 90 
    
    if q % 2 == 0 :
        
        if r == 0 :
            out  = (0)
        elif r == 30 :
            out = (0.5)
        elif r == 45 :
            out = ("1 / root2")
        elif r == 60 :
            out = ("root3 / 2 ")
        elif r == 90 :
            out = ("ND")
            
    else:
        if r == 90 :
            out = (0)
        elif r == 60 :
            out = (0.5)
        elif r == 45 :
            out =("1 / root2")
        elif r == 30 :
            out = ("root3 / 2 ")
        elif r == 0 :
            out = ("ND")

if n > 180 and n < 360 :
    print("The Value is : -",out)
else:
    print("The Value is : +",out)


# In[ ]:




