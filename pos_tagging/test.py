import sys

observation = []
punctuations = [",", "?", "!", "''", "%", "&", "$", ";", "'s", "'"]
exceptions = ["HUGO'S", "Shi'ite", "we're-all-in-this-together", "UAL'S", "O'Rourke", "'90s", "O'Connell", "D'Agosto", "D'Arcy", "N'T", "O'Donnell", "NATION'S", "women's-rights", "I'm-coming-down-your-throat", "n't", "O'Connor", "DARMAN'S", "MAITRE'D", "ain't-it-great-to-be-a-Texan", "l'Ouest", "D'Amico", 'US$', 'M$', 'C$', 'S$', '60%-held', '49%-owned', '80%-owned', '20%-a-year', '62%-owned', '8%-10', '71%-owned', '20%-plus', '16%-owned', '81%-owned', 'P&G', 'A&W', 'A&P', 'A&M', 'AT&T', 'S&P', 'S&L', 'H&R', 'D&B', 'AC&R', '-LCB-', '-LRB-', '-RCB-', '-RRB-']

txt = sys.argv[1]
lst = txt.split(" ")

for i in range(len(lst)):
	if "." in lst[i]:
		idx = lst[i].index(".")
		if idx > 0 and lst[i][idx-1].isdigit() and lst[i][idx+1].isdigit():
			pass
		elif lst[i][0].isupper():
			lst[i] = lst[i].replace(".", ". ")
		else:
			lst[i] = lst[i].replace(".", " . ")

	for p in punctuations:
		if (p in lst[i]) and (lst[i] not in exceptions):
			lst[i] = lst[i].replace(p, " " + p)

s = ' '.join(lst).strip()
print (s)
print (s.split(" "))
