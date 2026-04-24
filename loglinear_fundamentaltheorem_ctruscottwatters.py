def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def bisection_factor(n):
	factors = []
	for x in range(1, n // 2):
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
	for n in range(100000, 1000000):
		factors = bisection_factor(n)
		print(f"Factors of {n} are {factors}")
		if is_prime(n):
			print(f"{n} is a prime number")
#	
#	n = 2481
#	print(bisection_factor(n))
	
Charles_FundamentalTheorem()

# Seems fruitful

"""
Factors of 100000 are [(25000, 4), (20000, 5), (12500, 8), (10000, 10), (6250, 16), (5000, 20), (4000, 25), (3125, 32), (2500, 40), (2000, 50), (1250, 80), (1000, 100), (800, 125), (625, 160), (500, 200), (400, 250), (250, 400), (200, 500), (160, 625), (125, 800), (100, 1000), (80, 1250), (50, 2000), (40, 2500), (32, 3125), (25, 4000), (20, 5000), (16, 6250), (10, 10000), (8, 12500), (5, 20000), (4, 25000)]
Factors of 100001 are [(9091, 11), (11, 9091)]
Factors of 100002 are [(33334, 3), (16667, 6), (14286, 7), (7143, 14), (4762, 21), (2381, 42), (42, 2381), (21, 4762), (14, 7143), (7, 14286), (6, 16667), (3, 33334)]
Factors of 100003 are []
100003 is a prime number
Factors of 100004 are [(25001, 4), (4348, 23), (2174, 46), (1087, 92), (92, 1087), (46, 2174), (23, 4348), (4, 25001)]
Factors of 100005 are [(33335, 3), (20001, 5), (6667, 15), (1695, 59), (885, 113), (565, 177), (339, 295), (295, 339), (177, 565), (113, 885), (59, 1695), (15, 6667), (5, 20001), (3, 33335)]
Factors of 100006 are [(3226, 31), (1613, 62), (62, 1613), (31, 3226)]
Factors of 100007 are [(1031, 97), (97, 1031)]

"""

# Charles Thomas Wallace Truscott

