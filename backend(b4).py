def total_words(file): # number of words
	with open(file, "r") as f:
	    for count, line in enumerate(f):
	        pass
	return count + 1

class word: # record to replace 2 dimensional list
	def __init__(self, name, format, format_count, mode):
		self.name = name
		self.format = format
		self.format_count = format_count
		self.mode = mode

lst = [] # 'database'
f = open("name_lst.txt")
for i in range(total_words("name_lst.txt")):
	line = f.readline()[:-1] # -1 to exclude \n
	format = [len(i) for i in line.split()] # e.g Ba Co N -> [2, 2, 1]
	lst.append(word(line, format, 0, 0))


format_lst = [word.format for word in lst]
""" 
unique_format_lst= []
for f in format_lst:
	if f not in unique_format_lst:
		unique_format_lst.append(f)
print("different format -", len(unique_format_lst))

for i in sorted(unique_format_lst):
	print(i, '-', format_lst.count(i))
"""
# to get an idea of whether current lst has enough for wordle

for word in lst:
	word.format_count = format_lst.count(word.format)
	if word.format_count == 1:
		word.mode = "challenge" # only has 1 attempt
	else:
		word.mode = "wordle" # wordle with 2 twists
# print(lst[2].name, lst[2].format, lst[2].format_count, lst[2].mode)


# yellow 1 point
# green 2 point
def compare(cur, tar):
	value = 0
	for i in range(len(cur)):
		if cur[i] in tar: 
			value += 1 # yellow 
		if cur[i] == tar[i]:
			value += 1 # green
	return value
# print(compare("Ge Ni U S".split(), "Fe Ti S H".split()))


# initial and target need to enter in .split() format
# temp represents list of possible words in each step
def steps(ini, tar, temp, count):
	if len(temp) == 1: return count # base case
		
	non = [] # no colour
	yel = []
	gre = []
	for i in range(len(ini)):
		if ini[i] not in tar:
			non.append(ini[i])
		elif ini[i] != tar[i]:
			yel.append([i, ini[i]]) # [index, ele]
		else:
			gre.append([i, ini[i]])

	# no colour case
	for i in range(len(temp) - 1, -1, -1): # rev loop to avoid IndexError
		cur = temp[i].split()
		cur_with_i = [[index, ele] for index, ele in enumerate(cur)]	  		# to compare with yel, gre lst
		if any(item in cur for item in non):
			temp.pop(i)
		elif not all(item in cur for item in [j[1] for j in yel]):
			temp.pop(i)
		elif any(item in cur_with_i for item in yel):
			temp.pop(i)
		elif not all(item in cur_with_i for item in gre):
			temp.pop(i)	

	# change ini to worst case possible
	value_lst = [compare(i.split(), tar) for i in temp]
	ini = temp[value_lst.index(min(value_lst))]
	print(ini)
	count += 1
	return steps(ini.split(), tar, temp, count) 
	# lst is mutable type -> by ref works

# print(steps("Po Li S H".split(), "Fe Ti S H".split(), ["Ge Ni U S", "Po Li S H", "Fe Ti S H", "Ac Ce S S", "Mo Ti O N"], 0))
