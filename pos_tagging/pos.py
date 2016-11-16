from train import *
import matplotlib.pyplot as plt
import numpy as np
import sys
import json

observation = []
time = len(observation)

def trans(i, j):
	if (i, j) not in transition:
		return 0
	else:
		return transition[i, j] / float(context[i])

def emit(i, j):
	if (i, j) not in emission:
		return 0
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
			lst = [t1[k, t-1] * trans(k, i) for k in tags]
			t2[i, t] = max(list(list(zip(*t1.keys()))[0]), key=lambda k: t1[k, t-1] * trans(k, i))
			#print ("t1[%s, %d]" % (i, t), t1[i, t], " t2[%s, %d]" % (i, t), t2[i, t])

	x[time-1] = max(t1.keys(), key=lambda k: t1[k])[0]

	for t in range(time-1, 0, -1):
		x[t-1] = t2[x[t], t]

	print (observation, ":")
	
	ret = ""
	for k in x.keys():
		if x[k] == "JJ":
			ret = ret + " " + observation[k]
	#	print (k, "(%s): " % (observation[k]), x[k])

	return ret
	
def observe(text):
	global observation
	global time
	observation = text.split(" ")
	time = len(observation)

def main():
	f = open(sys.argv[1], "r")
	g = open(sys.argv[2], "w")
	for line in f:
		j = json.loads(line)
		observe(j["text"])
		ret = viterbi()
		j["text"] = ret
		g.write(json.dumps(j))

	f.close()
	g.close()

if __name__ == "__main__":
	main()
