def flat(lista):
	result = []
	for elem in lista:
		if type(elem) == type([]):
			result += flat(elem)
		else:
			result += [elem]
	return result

a = ["one", "two", ["three", ["four", "five", "six", ["seven", "eight"]], "nine"], "ten"]

print(a)
print(flat(a))

