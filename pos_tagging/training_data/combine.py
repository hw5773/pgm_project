import sys

f = open(sys.argv[1], "r")
g = open(sys.argv[2], "r")
h = open("integrate.txt", "w")

for line in f:
	h.write(line)
f.close()

for line in g:
	h.write(line)
g.close()

h.close()
