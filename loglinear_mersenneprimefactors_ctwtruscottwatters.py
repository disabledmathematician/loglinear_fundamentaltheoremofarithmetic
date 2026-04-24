from humanize import ordinal
from mpmath import mp
from decimal import Decimal
mp.dps = 100000
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def bisection_factor(n):
#	n = mp.mpf(n)
	factors = []
	for x in range(1, int(n) // 2):
		high = n
		low = 0
		guess = (high + low) / 2.0
#		if n % (guess * x) == 0:
		while abs(round(guess * x, 0)) != abs(round(n, 0)):
#			print(guess, x)
#			print(guess * x - n)
			if guess * x  > n:
				high = guess
			if guess * x < n:
				low = guess
			guess = (high + low) / 2.0
			if int(guess) * x == n:
				if ((int(guess), x)) not in factors:
					factors.append((int(guess), x))
	return factors
	
def Charles_FundamentalTheorem():
	for n in range(2000, 3000):
#		x = ((2 ** (2 ** n)) + 1) Fermat Prime
#		x = mp.power(2, n) - 1
		if is_prime(n):
#			x = 2 ** n - 1#Mersenne Prime
			x = mp.mpf(2 ** n) - 1
			print(f"{x}, the {ordinal(n)} Mersenne Number")
			factors = bisection_factor(x)
			if factors != []:
				print(f"Factors of {x} are {factors}")
			for factor in factors:
				print("{} x {} = {}".format(factor[0], factor[1], factor[0] * factor[1]))
			if factors == []:
				print(f"{x} is a prime number")
#		if is_prime(x):
#			print(f"{x} is a prime number")
#	
	
Charles_FundamentalTheorem()
# Charles Thomas Wallace Truscott Watters



