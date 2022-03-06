#add implementation
def add(x,y):
   
     return x+y
    
 
#subtract implementation 
def subtract(x,y):
    return x-y       #on master branch
    
    #multi implementation
def multiply(x,y):
    return x*y  #implemented bug 456 multipy function
    
    #div implementation
def divide(x,y):
    if y==0:             #Implementation for master branch
        return DIVIDE_BY_0_ERROR
    else:
        return x/y

#square implementation 
def square(x):
    return x*x
    
    