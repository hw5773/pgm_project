from nltk.stem import RSLPStemmer
st = RSLPStemmer()
f = open("training_data/integrate.txt", "r")

emission = {}
transition = {}
context = {}
prev = "S"
tags = []

for line in f:
	if len(line) <= 1:
		continue

	elif len(line) < 7:
		prev = "S"
		continue
	else:
		if prev not in context:
			context[prev] = 1
		else:
			context[prev] = context[prev] + 1

		lst = line.split(" ")
		word = lst[0]
		tag = lst[1]

		if tag not in tags:
			tags.append(tag)

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

f.close()
