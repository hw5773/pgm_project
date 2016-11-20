import sys

sentences = []

def make_sentence(f):
	sentence = ""
	for line in f:
		if len(line) <= 1:
			sentences.append(sentence.strip())
			sentence = ""
			continue

		lst = line.split(" ")
		sentence = sentence + lst[0] + " "

def main():
	f = open(sys.argv[1], "r")
	make_sentence(f)
	print ("sentences: ", sentences)

if __name__ == "__main__":
	main()
