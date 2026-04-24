def bisection_factor(n):
	factors = []
	for x in range(1, n):
		high = n
		low = 0
		guess = (high + low) // 2
		while((guess * x)  -  n > 0.0000001):
			print(high, low, guess)
			if ((guess * x) > n):
				high = guess
			if ((guess * x) < n):
				low = guess
			guess = (high + low) // 2
		if guess * x == n:
			factors.append((guess, x))
	return factors
	
def Charles_FundamentalTheorem():
	n = 1992
	print(bisection_factor(n))
	
Charles_FundamentalTheorem()