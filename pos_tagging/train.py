f = open("train.txt", "r")

emission = {}
transition = {}
context = {}
prev = "S"

for line in f:
	if prev not in context:
		context[prev] = 1
	else:
		context[prev] = context[prev] + 1

	if len(line) < 5:
		prev = "S"
		continue
	lst = line.split(" ")
	word = lst[0]
	tag = lst[1]

	if (prev, tag) not in transition:
		transition[prev, tag] = 1
	else:
		transition[prev, tag] = transition[prev, tag] + 1

	if tag not in context:
		context[tag] = 1
	else:
		context[tag] = context[tag] + 1

	if (tag, word) not in emission:
		emission[tag, word] = 1
	else:	
		emission[tag, word] = emission[tag, word] + 1

	prev = tag

for k1, k2 in transition:
	print ("T", k1, k2, ": ", transition[k1, k2]/context[k1])

for k1, k2 in emission:
	print ("E", k1, k2, ": ", emission[k1, k2]/context[k1])
