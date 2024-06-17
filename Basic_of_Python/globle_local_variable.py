a=True
b=7  # a and b are the globel variable

def my_function(x):
    
    a=6 # This a is local variable only use of this defined function

    if x==a:
        print("hello")
    else:
        print("HELLO")


print(a) #This will Print the globle variable

# To change  the globle varila from the defined function you have to use globel keyword

def my_func2(x):
    global a
    a = 2

print(a)