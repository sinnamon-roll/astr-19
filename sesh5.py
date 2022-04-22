# A little more complicated, but not that bad

import numpy as np

def createTable():
	x = np.linspace(0.0, 2*np.pi, 1000)
	y = np.sin(x)
	i = 0
	while i < 1000:
		print(y[i], "|", x[i])
		i = i + 1


def main():
	print("sin(x)", "|", "x")
	createTable()

if __name__ == '__main__':
	main()