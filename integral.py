from math import e

def integral(f, a, b, n):
	x = []
	h = (b-a)/n
	result = f(a) + f(b)

	for i in range(0, n+1):
		x.append(a+i*h)
	print(x)

	for i in range(1, len(x)-1):
		if i%2 != 0:
			result += 4*f(x[i])
		else:
			result += 2*f(x[i])
	return 1/3 * h * (result)



def f(x):
	return x**2 + 1 - 20*x
#	return e**x

a=4
b=19
n=6

print(integral(f, a,b,n))




