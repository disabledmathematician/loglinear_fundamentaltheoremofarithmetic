import math
def bisection_factor(n):
	factors = []
	for x in range(0, n):
		high = n
		low = 0
		guess = (high + low) / 2.0
		while (((int(guess) * x) - n) > 0.000001):
#			print(guess, x)
			if ((guess * x) > n):
				high = guess
			if ((guess * x) < n):
				low = guess
			guess = (high + low) / 2.0
			if (int(guess) * x) == n:
				factors.append((int(guess), x))
		high, low, guess = 0, 0, 0
	return factors
	
def Charles_FundamentalTheorem():
	for n in range(2, 100):
		factors = bisection_factor(n)
		print(f"Factors of {n} are {factors}")
#	
#	n = 2481
#	print(bisection_factor(n))
	
Charles_FundamentalTheorem()
