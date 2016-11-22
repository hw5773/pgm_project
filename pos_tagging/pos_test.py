from train import *
import matplotlib.pyplot as plt
import numpy as np
import sys
import json

observation = []
time = len(observation)
punctuations = ["?", "!", "%", "&", "$", ";", "'"]
exceptions = ["''", "HUGO'S", "Shi'ite", "we're-all-in-this-together", "UAL'S", "O'Rourke", "'90s", "O'Connell", "D'Agosto", "D'Arcy", "N'T", "O'Donnell", "NATION'S", "women's-rights", "I'm-coming-down-your-throat", "n't", "O'Connor", "DARMAN'S", "MAITRE'D", "ain't-it-great-to-be-a-Texan", "l'Ouest", "D'Amico", 'US$', 'M$', 'C$', 'S$', '60%-held', '49%-owned', '80%-owned', '20%-a-year', '62%-owned', '8%-10', '71%-owned', '20%-plus', '16%-owned', '81%-owned', 'P&G', 'A&W', 'A&P', 'A&M', 'AT&T', 'S&P', 'S&L', 'H&R', 'D&B', 'AC&R', '-LCB-', '-LRB-', '-RCB-', '-RRB-']
default = 0.00001

def trans(i, j):
	if (i, j) not in transition:
		return default
	else:
		return transition[i, j] / float(context[i])

def emit(i, j):
	if (i, j) not in emission:
		return default
	else:
		return emission[i, j] / float(context[i])

def viterbi():
	t1 = {}
	t2 = {}
	x = {}

	for i in tags:
		t1[(i, 0)] = trans("S", i) * emit(i, observation[0])
		t2[(i, 0)] = "S"

	for t in range(1, time):
		for i in tags:
			t1[i, t] = max([t1[k, t-1] * trans(k, i) * emit(i, observation[t]) for k in tags])
			t2[i, t] = max(list(list(zip(*t1))[0]), key=lambda k: t1[k, t-1] * trans(k, i))

	x[time-1] = max(tags, key=lambda k: t1[k, time-1])

	for t in range(time-1, 0, -1):
		x[t-1] = t2[x[t], t]

	ret = x
	for k in x.keys():
		#if x[k] == "JJ":
		#	ret = ret + " " + observation[k]
		print (k, "(%s): " % (observation[k]), x[k])

	return ret
	
def observe(text):
	global observation
	global time
	
	lst = text.split(" ")

	for i in range(len(lst)):
		if "." in lst[i]:
			idx = lst[i].index(".")
			if idx > 0 and lst[i][idx-1].isdigit():
				pass
			elif lst[i][idx-1].isupper():
				pass
			elif "..." in lst[i]:
				lst[i] = lst[i].replace("...", " ...")
			elif lst[i][0].isupper():
				lst[i] = lst[i].replace(".", ". ")
			else:
				lst[i] = lst[i].replace(".", " . ").strip()

		if "," in lst[i]:
			idx = lst[i].index(",")
			if idx > 0 and lst[i][idx-1].isdigit():
				pass
			else:
				lst[i] = lst[i].replace(",", " , ").strip()

		for p in punctuations:
			change = False
			if p in lst[i]:
				change = True
				for e in exceptions:
					if e in lst[i]:
						change = False
						lst[i] = lst[i].replace(e, " " + e).strip()

			if change:
				lst[i] = lst[i].replace(p, " " + p).strip()

	text = ' '.join(lst).strip()
	text = text.replace("  ", " ")

	observation = text.split(" ")
	time = len(observation)
#	print ("o: ", observation)

def main():
	observe(sys.argv[1])
	viterbi()

if __name__ == "__main__":
	main()
