
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, zscore
from scipy import integrate
from scipy.stats import t, ttest_1samp


"""
    Unnamed: 0  Year  Max Daily Rain        Date
0            0  2003           107.0   27/6/2003
1            1  2004           102.0   25/2/2004
2            2  2005           177.6   30/6/2005
3            3  2006           146.4   16/4/2006
4            4  2007            62.6   26/6/2007
5            5  2008           101.6    4/2/2008
6            6  2009            59.6   14/2/2009
7            7  2010           204.8   4/10/2010
8            8  2011            79.8  27/10/2011
9            9  2012            94.4   26/1/2012
10          10  2013            89.6   28/1/2013
11          11  2014            70.4   28/8/2014
12          12  2015           115.2   20/1/2015
13          13  2016           166.4    5/6/2016
14          14  2017           162.0   16/3/2017
15          15  2018            58.4   29/4/2018
16          16  2019            57.0   26/6/2019
17          17  2020           275.4    7/2/2020
18          18  2021           134.2   22/3/2021
19          19  2022           164.2   30/3/2022
20          20  2023            77.8    1/2/2023
21          21  2024           108.6   16/1/2024
mu: 118.86363636363635, sigma: 54.157325916382014
From 57.0 to 275.4 millilitres in highest volume day's rain, there is a probability of: 0.8714105102631312, with an error of 1.1757892638936556e-11
"""
def NormalD(x, mu, sigma):
	return norm.pdf(x, loc=mu, scale=sigma)
	
def TDistribution(deg, ts):
	return t.pdf(ts, deg)
def CTruscottWatters():
	data = pd.read_csv('byronrain.csv')
	print(data)
	y = data["Max Daily Rain"]
	x2 = data["Year"]
	mu, sigma = np.mean(y), np.std(y)
	print("mu: {}, sigma: {}".format(mu, sigma))
	x = np.linspace(np.min(y), np.max(y), int(np.max(y)) - int(np.min(y)))
	nums = []
	proba = []
	y_dev = TDistribution(len(x2), ttest_1samp(y, y.mean()))
	a = int(np.min(y))
	b = int(np.max(y))
	c = [n for n in range(a, b)]
	
#	integral_result, error_estimate = integrate.quad(NormalD, a, b, args=(mu, sigma))
#	for n in range(int(np.min(y)), int(np.max(y))):
	for n in range(len(x) - 1):
		a = x[n]
		b = x[n + 1]
#		a = n
#		b = n + 0.01
		integral_result, error_estimate = integrate.quad(NormalD, a, b, args=(mu, sigma))
		integral_result *= 100
		nums.append(a)
		proba.append(integral_result)
#		print(f"Between {a} and {b} there is a {integral_result}% probability")
#	total_integral, error_total = integrate.quad(NormalD, np.min(y), np.max(y), args=(mu, sigma))
	total_integral, error_total = integrate.quad(NormalD, np.min(y), np.max(y), args=(mu, sigma))
	print(f"From {np.min(y)} to {np.max(y)} millilitres in highest volume day's rain, there is a probability of: {total_integral}, with an error of {error_total}")
#	total_integral *= 100
#	print(f"From 100 to 160 millilitres in highest volume day's rain, there is a probability of: {total_integral}, with an error of {error_total}")
	plt.figure(0, dpi=120, figsize = [12, 8])
	plt.title("Byron Bay Rainfall as a Bell Curve ~ Charles Truscott Watters")
	plt.xlabel("Highest recorded daily mM of rainfall per year over 11 years")
	plt.ylabel("Probability")
#	plt.plot(x, y_dev)
	plt.bar(nums, proba, edgecolor="black", linewidth=0.22, color="purple")
#	for mM, which_color in zip([100, 120, 130, 140, 150], ["black", "blue", "purple", "green", "gold"]):
#		print(mM, which_color)
#		plt.axvline(mM, color=which_color, label=f"{mM} mM rain")
#		plt.axhline(round(np.interp(mM, nums, proba), 2), color=which_color, label="{} mM rainfall probability: {}".format(mM, round(np.interp(mM, nums, proba), 2)))
#	plt.axvline(np.mean(y), color="r",label="Mean ≈ {}".format(int(np.mean(y))))
#	plt.axvline(mu, color='k', linestyle='dashed', linewidth=2, label='Mean')
#	plt.axvline(mu + sigma, color='r', linestyle='dashed', linewidth=2, label='$\pm1$ Std Dev')
#	plt.axvline(mu - sigma, color='r', linestyle='dashed', linewidth=2)
#	plt.axvline(mu + 2*sigma, color='g', linestyle='dashed', linewidth=2, label='+2 Std Dev')
#	plt.axvline(mu - 2*sigma, color='g', linestyle='dashed', linewidth=2)

#	plt.axhline(np.interp(275, nums, proba), color="r", label="275 mM rainfall probability: {}".format(round(np.interp(275, nums, proba), 2)))

#	print("Interpolated range: 150 - 100 probability {}".format(np.interp(150, nums, proba) - np.interp(100, nums, proba)))

#	plt.axhline(np.interp(57.5, nums, proba), color="g", label="57.5 mM rainfall probability: {}".format(np.interp(57.5, nums, proba)))
#	plt.axvline(140.03, color="b",label="mM Rain March 12 2026 (Flash Flooding ≈ {}".format(int(140)))
#	plt.xticks(np.arange(np.min(y), np.max(y), 25), rotation=45, ha="center")
	plt.legend()
	plt.show()
#	plt.savefig("rain_final.png")
#	plt.figure(0, dpi=100, figsize = [7, 5])
#	plt.title("Byron Rainfall as a Normal Distribution or Probability Density Function")
#	plt.xlabel("mL of rainfall")
#	plt.ylabel("Relative Likelihood")
#	plt.plot(x, y_dev)
#	plt.xticks(np.arange(np.min(y), np.max(y), 25), rotation=45, ha="center")
#	plt.show()
#	plt.savefig("likelihood.png")
#	coefficients = np.polyfit(x, y, 33)
#	polynomial = np.poly1d(coefficients)
#	y_predicted = polynomial(x)
#	y = polynomial(x)
#	plt.figure(0)
#	plt.plot(x, y, color="gold", label="Highest day of rain each year")
#	plt.plot(x, y_predicted, color="red", label="Polynomial fit of the data")
#	plt.legend()
#	plt.savefig("fit.png")

#	plt.figure(1, dpi=120, figsize=[7, 5])
#	plt.title("Charles Truscott Watters. Byron Rainfall")
#	plt.xlabel("Year")
#	plt.ylabel("Highest recorded daily mM rainfull per year")
#	plt.bar(x2, y, color="purple", edgecolor="blue")
#	plt.savefig("Rainfall.png")
	
#	plt.show()
#	pass
CTruscottWatters()