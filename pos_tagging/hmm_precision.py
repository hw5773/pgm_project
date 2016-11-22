import sys
from pos_test import *

sentences = []
sentence_tags = []

def make_sentence(f):
	sentence = ""
	tag_lst = []
	for line in f:
		if len(line) <= 1:
			sentences.append(sentence[0:-2].strip())
			sentence = ""
			sentence_tags.append(tag_lst[0:-1])
			tag_lst = []
			continue

		lst = line.split(" ")
		sentence = sentence + lst[0] + " "
		tag_lst.append(lst[1])
		

def main():
	f = open(sys.argv[1], "r")
	make_sentence(f)
	for s in sentences:
		count = 0
		compare = []

		idx = sentences.index(s)
		tag_lst = sentence_tags[idx]
		observe(s)
		x = viterbi()	
		x_lst = [v for (k, v) in sorted(x.items())]

		compare = [(i, j) for i, j in zip(tag_lst, x_lst) if i == j]
		difference = [(i, j) for i, j in zip(tag_lst, x_lst) if i != j]
		accuracy = len(compare) / len(x_lst)
		if accuracy < 1 and len(difference) > 1:
			print ("\naccuracy: ", len(compare) / len(x_lst))	
			print ("s: ", s)
			print ("t: ", tag_lst)
			print ("x: ", x_lst)
			print ("d: ", difference)
			

if __name__ == "__main__":
	main()
