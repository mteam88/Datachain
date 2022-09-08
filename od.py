from timeit import default_timer as timer
from datachain import main
import random
import numpy as np

TARGET_TIME = 0.3
INITIAL_WEIGHT = 2
DIFF_SIZE = 60
MAX_GEN_SIZE = 4
CHILDREN = 3

weight = INITIAL_WEIGHT

def timesolve(dif):
	start = timer()  
	main.solve(dif, b"hi")
	end = timer()
	return end-start

def rungen(diff, gensize):
	avggentime = 0
	for i in range(gensize):
		avggentime += timesolve(diff)
	avggentime = avggentime / gensize
	print(avggentime)
	return avggentime

def dispdiffs(diffs):
	print('---' *10)
	for diff in diffs:
		print(diff, '\n')

diffs = [[1.3973196499071137e+85, None]]

while True:
	nextdiffs = []
	for diff in diffs:
		diff[1] = rungen(diff[0], DIFF_SIZE)
		diff[1] = TARGET_TIME - diff[1]
	diffs = sorted(diffs, key=lambda diff: abs(diff[1]))[:MAX_GEN_SIZE]
	dispdiffs(diffs)
	for diff in diffs:
		#print(diff)
		for i in range(CHILDREN): # add mutation
			nextdiffs.append([diff[0]*(1+random.randint(-200,200)/1000), None])
		#print(diff, '\n')

	
	diffs.extend(nextdiffs)