# Classes this time around
# yay

class koala:
	def __init__(animal, armlen, leglen, eyenum, tail, fur):
		animal.armlen = float(armlen)
		animal.leglen = float(leglen)
		animal.eyenum = int(eyenum)
		animal.tail = bool(tail)
		animal.fur = bool(fur)


	def printDesc(animal):
		print("My favorite animal is the Koala.")
		print("Their arms are about", animal.armlen, "cm long.")
		print("Their legs are about", animal.leglen, "cm long.")
		print("They have", animal.eyenum, "eyes.")
		if animal.tail == True:
			print("They have a tail.")
		elif animal.tail == False:
			print("They don't have a tail.")
		if animal.fur == True:
			print("They are furry.")
		elif animal.tail == False:
			print("They are not furry.")

def main():
	animal = koala(14, 12, 2, False, True)
	animal.printDesc()

if __name__ == '__main__':
	main()