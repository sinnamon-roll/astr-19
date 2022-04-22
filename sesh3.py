# Basic formulas, algorithms ahoy
# Not really, no recursion needed here

def f(x):
	y = x**3 + 8
	return(y)

def main():
	x = 9
	z = f(x)
	print(z)
	if z > 27:
		print("YAY!")

if __name__ == '__main__':
	main()