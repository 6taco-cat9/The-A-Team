def total_words(file): # number of words
	with open(file, "r") as f:
	    for count, line in enumerate(f):
	        pass
	return count + 1

class word: # record to replace 2 dimensional list
	def __init__(self, name, format):
		self.name = name
		self.format = format

lst = [] # 'database'
f = open("name_lst.txt")
for i in range(total_words("name_lst.txt")):
	line = f.readline()[:-1] # -1 to exclude \n
	format = [len(i) for i in line.split()] # e.g Ba Co N -> [2, 2, 1]
	lst.append(word("".join(line.split()), format))
