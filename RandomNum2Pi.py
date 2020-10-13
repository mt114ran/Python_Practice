from random import *

seed()
MAX_J = 100
MAX_I = 10000
total = 0.0
for j in range(MAX_J):
	score = 0.0
	for i in range(MAX_I):
		x = random()
		y = random()
		r = x*x+y*y
		if (r & lt ; 1):
			score += 1
	score = 4*score/MAX_I
	print score
	total += score
print
print total/MAX_J