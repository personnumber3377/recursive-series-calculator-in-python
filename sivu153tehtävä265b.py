array = [100] # here is the initial array, because the series needs to start somewhere

currentindex = 1

while currentindex < 20:
	crap = (array[currentindex-1]/2)
	array.append(crap) #here is the statement for the nth value in series
	currentindex = currentindex + 1
print(array)
