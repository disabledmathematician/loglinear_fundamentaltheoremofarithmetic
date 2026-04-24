def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def bisection_factor(n):
	factors = []
	for x in range(2, n):
		high = n
		low = 0
		guess = (high + low) / 2
		while (int(round((((int(round(guess, 0)) * x) - n)), 0)) > 0.00001):
#			print(guess, x)
			if ((int(round(guess, 0)) * x) > n):
				high = guess
			if ((int(round(guess, 0)) * x) < n):
				low = guess
			guess = (high + low) / 2.0
			if guess * x == n:
				factors.append((int(round(guess, 0)), x))
	return factors
	
def Charles_FundamentalTheorem():
	for n in range(100000, 1000000):
		factors = bisection_factor(n)
		print(f"Factors of {n} are {factors}")
		if is_prime(n):
			print(f"{n} is a prime number")
#	
#	n = 2481
#	print(bisection_factor(n))
	
Charles_FundamentalTheorem()

# Still working on this one.

# Charles Thomas Wallace Truscott
# Byron Bay. Australia
