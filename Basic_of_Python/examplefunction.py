# Write a Python function that takes two lists and returns True if they have at least one common member.

def same_list(list_1,list_2):

	for x in list_1:
		for y in list_2:
			if x==y:
				result=True
				return result

print(same_list([1,2,3,4,5],[7,8,9,0,2])) 


