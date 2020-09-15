array = [1,2] # here is the initial array, because the series needs to start somewhere

currentindex = 2

while currentindex < 5:
	array.append(3*(array[currentindex-1])+(array[currentindex-2])) #here is the statement for the nth value in series
	currentindex = currentindex + 1
print(array)
