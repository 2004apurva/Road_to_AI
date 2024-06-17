# Function is a machine that that a input and  produace a result

def hello_func(greating , name="You"):
    return '{} {}'.format(greating,name)

#print(hello_func("Good Morning" , name="Apurva"))

   
def student_list(*args,**kwargs):
    print(args)
    print(kwargs)
     
#student_list("maths","science", name="Apurva",classes="4th year")



name=("apurva","sachin","Krunal")
Ranks={"Apurva":1,"Sachin":2,"Krunal":3}

student_list(*name,**Ranks)
 

#OPTIONAL PARAMETER

def new_funct(x="1",y="2"):
    print(x)
    
    if y==3:
        print('Not right')
    else:
        print("All right") #If you have optional-parameter/multipal-paramerter then you can't second element directly you have to change first element first 

new_funct( "6","3")

  








