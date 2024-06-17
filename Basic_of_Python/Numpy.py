import numpy as np # we can use "np" when ever we want

my_list=[1,2,3,4]

a=np.array(my_list) # a is an one dimentional array """ Defining an Array"""

print(type(a))

print(a.shape)# array_name.shape gives us the number of rows and colums in the array and tell us the dimentions of the array


print(a)

my_list2=[4,5,6,7]
my_list3=[4,9,7,3]

b=np.array([my_list,my_list2,my_list3])# This is an 2 dimentional array

print(b)
print(b.shape)# array_name.shape gives use the number of rows and colums in the array and tell us the dimentions of the array

print(b.reshape(4,3)) #  array_name.reshape use to reshape the array ""THe number of element before and after the reshaping should be same


### Indexing###

arr=np.array([1,2,3,4,5,6,7,8,9])


print(arr)

print(arr[2])# this is one dimenstional indexing

ar=np.array([[1,2,3,4,5,6,7,8,9],
            [2,4,6,7,7,3,2,3,2],
            [3,4,5,3,4,5,4,2,4]])

print(ar)


print(ar[1:4,2:3]) # THis is two dimentional indexting '''[includs:includes+1,include,include+1]'''



###  Arrange  ###

ap=np.arange(0,10, step=2) #Its an inbuild  function in numpy that create an array with specific progration
print(ap)



###  linspace  ###

app=np.linspace(1,10,10)# this in-build funtion create an array from start point to an end point and and divide it into equally space points
print(app)


### Copy funtion and Broadcasting function ###

app[3:]=2 # This will replace the items from the array

print(app)
 
new=app.copy()# by copying  by copy function the old array will not be affacted by changing the new array

new[0:]=5 #Know by changing in this array the old array will not be affacted

print(new)

### Some condtion very usful in exploratory data analysis ###

var=2
print(new>2)# This compair each element of new with var


###  Creating array and reshaping it  ###

new_array=np.arange(0,20,2).reshape(5,2)

print(new_array)

###  ones Function  ###

new_2=np.ones((4,5),dtype=int) #this create arrays of "1" in any shape
print(new_2)

### Random function ###

new_3=np.random.rand(2,3) #this create arrays of random integers in any shape
print(new_3)

### Specific Random function ###

new_4=np.random.randint(0,100,10)#this create arrays of random integers between any interval and number of intergers are also given in any shape

print(new_4)

































