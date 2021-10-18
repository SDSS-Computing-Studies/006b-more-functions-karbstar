#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is scalene
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 1  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
def triangle(a,u,i):
    lst=[a,u,i]
    x=max(lst)
    y=min(lst)
    z= (sum(lst)-x)-y
    t= (y**2+z**2)*(1/2)
    if t == x:
        return 2
    else:
        if t<z:
            if y+z == t:
                return 1
            else:
                return 0
        else:
           if t>z:
                if y+z == t:
                    return 3
                else:
                   return 0

    