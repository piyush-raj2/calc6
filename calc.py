def divide(x,y):
	if y == 0:
		print("Not defined...")
		return None
	return (x/y)

def add(x,y):
	return (x+y)

def subtract(x,y):
	return(x-y)

def main():
	a = 7, b = 8
	print("Add operation for a = ", a, " and b = ", b, " is ", add(a,b))
	print("Divide operation for a = ", a, " and b = ", b," is ", divide(a,b))



if __name__ == '__main__':
	main()
	
