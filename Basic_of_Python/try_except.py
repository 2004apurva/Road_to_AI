text = input("Username:")
# number=int(text) >>> This will turns into an error if the input is not integer

try:
    number=int(text)
    print(number)
except:
    print("Invalid Usernamer")

#By using try and except method we can handel the error