def count_dict(texto):
	dicio = dict()
	atual = ""
	for letra in texto:
		if letra in dicio.keys():
			dicio[letra] = dicio[letra]+1
		else:
			dicio[letra] = 1
	return dicio


print(count_dict("leonardo"))
