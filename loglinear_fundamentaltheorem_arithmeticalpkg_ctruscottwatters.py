import math
import numpy
from matplotlib import pyplot as plot
import os
# Charles Truscott
# Massachusetts Institute of Technology
# April 25, 2026, 6:33 a.m.
# All my own work
# Number system logic in Python, seems to defy integer and float wrapping
# I love you Dad Mark William Watters, big bro Tai William Wedekind Truscott
# ANZAC Day ~ Lest We Forget
import sys
sys.set_int_max_str_digits(9000)
class ArithmeticalOperation(object):
    def __init__(self, p, q, r=0, s=0):
        self.p = p
        self.q = q
        self.r = r
        self.s = s
    def __str__(self):
        return str("<{}, {}>, <{}, {}>".format(p, q, r, s))
    def add(self):
        addend_one = 0
        addend_two = 0
        for x in range(self.p):
            addend_one += 1
        for y in range(self.q):
            addend_two += 1
        for z in range(addend_two):
            addend_one += 1
        return addend_one
    def subtract(self):
        subtrahend_one = 0
        subtrahend_two = 0
        for x in range(self.p):
            subtrahend_one += 1
        for y in range(self.q):
            subtrahend_two += 1
        for z in range(subtrahend_two):
            subtrahend_one -= 1
        return subtrahend_one
    def multiply(self):
        multiplicand = 0
        for x in range(1, 1 + self.q):
            multiplicand += self.p
        return multiplicand
    def divide(self):
        dividend = float(0.0)
        remainder = 0
        number_to_divide = self.p
        number_to_divide_by = self.q
        epsilon = 0.000001
        while(number_to_divide >= number_to_divide_by):
            number_to_divide -= number_to_divide_by
            dividend += 1
        print(number_to_divide)
        L = []
        step = 0.0000001
#        while(number_to_divide >= epsilon):
#            number_to_divide -= step * number_to_divide_by
#            dividend += step
        remainder = float(number_to_divide)
        high = remainder
        low = 0
        guess = (high + low) / 2.0
        while(round(abs((remainder - (((( round(abs(float(guess)) , 12)) * number_to_divide_by))))), 7) >= step):
#           print("guess: {} dividend: {}".format(guess, dividend + guess))
            if (remainder < ((round(abs(float(guess)) , 12)) * number_to_divide_by )):
                high = guess
            elif (remainder > ((round(abs(float(guess)) , 12)) * number_to_divide_by )):
                low = guess
            guess = (high + low) / 2.0
            
        dividend += guess
#        while(x < 100000):
#            dividend += (1/x) * (number_to_divide % (1/x * number_to_divide_by))
#            number_to_divide -=  (1/x) * #(number_to_divide % (1/x * number_to_divide_by))
#           print(number_to_divide)
#            x += 10 * x
           
        # Yay. All my own work. Approximate answer for solving remainder division all my own work by Charles Truscott Watters. I love MIT. Massachusetts Institute of Technology
#       while(x <= number_to_divide):
#            dividend += number_to_divide_by * 1/#10000000
#            x += number_to_divide_by * 1/10000000
        # Exhaustive Enumeration
        return round(dividend, 6)
    def floor_divide(self):
    	return int(self.divide())
    def exponentiate(self, exponent):
        base = self.p
        exponent = exponent
        power = 1
        for x in range(1, 1 + exponent, 1):
            power *= base
        return power
        
class DecimalFraction(ArithmeticalOperation):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    pass
    

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def bisection_factor(n):
	factors = []
	for x in range(1, ArithmeticalOperation(n, 2).floor_divide()):
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
	n = 2083
	x = ArithmeticalOperation(2, None).exponentiate(n) - 1
	print(x)
	factors = bisection_factor(x)
	print(f"Factors of {x} are {factors}")
	for factor in factors:
		print("{} x {} = {}".format(factor[0], factor[1], factor[0] * factor[1]))
	if is_prime(n):
		print(f"{x} is a prime number")
#	
#	n = 2481
#	print(bisection_factor(n))

	
Charles_FundamentalTheorem()
# Charles Thomas Wallace Truscott

""""
1110403873447313761611101062388081739263988052819954348342480374563212256440927438806225671529727607049449017330618864031795311766922368387586560965894877836787667529442754864018327317915650616444052535188724515945624557238858666915828712787445743253171752792258799881311056126871095365511625862822748960454378351625778130839866971525015035249381812130362763951419260703442163797886417845694313973490356957490316018981689421350194415162421275874291089789042481803813559158111316640144843287203034521253922132704134911678674986324186251719477345731112860734048009196429771871548885220360901961441090142953670915757741059141009407

""""