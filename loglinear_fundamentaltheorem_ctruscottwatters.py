def bisection_factor(n):
	factors = []
	for x in range(0, n):
		high = n
		low = 0
		guess = (high + low) / 2.0
		while (((int(round(guess, 1)) * x) - n) > 0.000001):
#			print(guess, x)
			if ((int(round(guess, 1)) * x) > n):
				high = guess
			if ((int(round(guess, 1)) * x) < n):
				low = guess
			guess = (high + low) / 2.0
		if (int(round(guess, 1)) * x) == n:
			factors.append((int(round(guess, 0)), x))
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

"""
Factors of 2 are []
Factors of 3 are []
Factors of 4 are [(2, 2)]
Factors of 5 are []
Factors of 6 are [(3, 2)]
Factors of 7 are []
Factors of 8 are [(4, 2), (2, 4)]
Factors of 9 are []
Factors of 10 are [(5, 2), (2, 5)]
Factors of 11 are []
Factors of 12 are [(6, 2), (3, 4)]
Factors of 13 are []
Factors of 14 are [(7, 2)]
Factors of 15 are [(4, 5)]
Factors of 16 are [(8, 2), (4, 4), (2, 8)]
Factors of 17 are []
Factors of 18 are [(9, 2), (2, 9)]
Factors of 19 are []
Factors of 20 are [(10, 2), (5, 4), (2, 10)]
Factors of 21 are []
Factors of 22 are [(11, 2), (3, 11)]
Factors of 23 are []
Factors of 24 are [(12, 2), (6, 4), (3, 8)]
Factors of 25 are []
Factors of 26 are [(13, 2)]
Factors of 27 are [(3, 9)]
Factors of 28 are [(14, 2), (7, 4)]
Factors of 29 are []
Factors of 30 are [(15, 2), (4, 10)]
Factors of 31 are []
Factors of 32 are [(16, 2), (8, 4), (4, 8), (2, 16)]
Factors of 33 are []
Factors of 34 are [(17, 2), (2, 17)]
Factors of 35 are []
Factors of 36 are [(18, 2), (9, 4), (4, 9), (2, 18)]
Factors of 37 are []
Factors of 38 are [(19, 2), (2, 19)]
Factors of 39 are []
Factors of 40 are [(20, 2), (10, 4), (5, 8), (2, 20)]
Factors of 41 are []
Factors of 42 are [(21, 2), (3, 21)]
Factors of 43 are []
Factors of 44 are [(22, 2), (11, 4), (3, 22)]
Factors of 45 are [(6, 9)]
Factors of 46 are [(23, 2), (3, 23)]
Factors of 47 are []
Factors of 48 are [(24, 2), (12, 4), (6, 8), (3, 16)]
Factors of 49 are []
Factors of 50 are [(25, 2)]
Factors of 51 are [(3, 17)]
Factors of 52 are [(26, 2), (13, 4)]
Factors of 53 are []
Factors of 54 are [(27, 2), (7, 9), (3, 18)]
Factors of 55 are []
Factors of 56 are [(28, 2), (14, 4), (7, 8)]
Factors of 57 are [(4, 19)]
Factors of 58 are [(29, 2)]
Factors of 59 are []
Factors of 60 are [(30, 2), (15, 4), (4, 20)]
Factors of 61 are []
Factors of 62 are [(31, 2)]
Factors of 63 are [(8, 9), (4, 21)]
Factors of 64 are [(32, 2), (16, 4), (8, 8), (4, 16), (2, 32)]
Factors of 65 are []
Factors of 66 are [(33, 2), (2, 33)]
Factors of 67 are []
Factors of 68 are [(34, 2), (17, 4), (4, 17), (2, 34)]
Factors of 69 are []
Factors of 70 are [(35, 2), (2, 35)]
Factors of 71 are []
Factors of 72 are [(36, 2), (18, 4), (9, 8), (4, 18), (2, 36)]
Factors of 73 are []
Factors of 74 are [(37, 2), (2, 37)]
Factors of 75 are []
Factors of 76 are [(38, 2), (19, 4), (5, 19), (2, 38)]
Factors of 77 are []
Factors of 78 are [(39, 2), (2, 39)]
Factors of 79 are []
Factors of 80 are [(40, 2), (20, 4), (10, 8), (5, 16), (2, 40)]
Factors of 81 are []
Factors of 82 are [(41, 2), (3, 41)]
Factors of 83 are []
Factors of 84 are [(42, 2), (21, 4), (3, 42)]
Factors of 85 are [(5, 17)]
Factors of 86 are [(43, 2), (3, 43)]
Factors of 87 are []
Factors of 88 are [(44, 2), (22, 4), (11, 8), (3, 44)]
Factors of 89 are []
Factors of 90 are [(45, 2), (6, 18), (3, 45)]
Factors of 91 are []
Factors of 92 are [(46, 2), (23, 4), (3, 46)]
Factors of 93 are []
Factors of 94 are [(47, 2), (3, 47)]
Factors of 95 are [(6, 19)]
Factors of 96 are [(48, 2), (24, 4), (12, 8), (6, 16), (3, 32)]
Factors of 97 are []
Factors of 98 are [(49, 2)]
Factors of 99 are [(3, 33)]

[Program finished]

"""

# Charles Thomas Wallace Truscott
# Byron Bay. Australia
