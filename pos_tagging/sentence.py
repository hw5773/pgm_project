import json
import sys

def make_sentence_list(p):
	p = p.replace("\n", " ")
	p = p.replace("\\\"", "\"")
	p = p.replace("  ", " ")
	lst = p.split(" ")

	sentences = []
	s = ""

	for t in lst:
		t = t.strip()
		s = s + " " + t
		if "." in t:
			if t[-1] == "." and (not t[0].isupper()):
				sentences.append(s.strip())
				s = ""

	return sentences

def main():
	f = open(sys.argv[1], "r")

	for line in f:
		js = json.loads(line)
		p = js["text"]
		sentences = make_sentence_list(p)
		print (sentences)

if __name__ == "__main__":
	main()
