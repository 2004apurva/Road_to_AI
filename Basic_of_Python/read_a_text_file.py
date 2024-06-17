# This is to read  from a text file in the same directry 

file = open('text.txt','r')


f = file.readlines()

#print(f)
newlist=[]
for i in f:
	if i[-1]=="\n":
		newlist.append(i[:-1]) #This will add the appended items in the new list
	else:
		newlist.append(i)

print(newlist)

file.close()