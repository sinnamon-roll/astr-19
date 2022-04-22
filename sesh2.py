# This one will math it up a little
def addFloats():
	x = float(3)
	y = float(9)
	z = x + y
	print(z, "of", type(z))

def diffInt():
	a = int(2)
	b = int(7)
	c = b - a
	print(c, "of", type(c))

def prodMix():
	l = int(6)
	m = float(3)
	n = l * m
	print(n, "of", type(n))

def main():
	addFloats()
	diffInt()
	prodMix()

if __name__ == '__main__':
	main()