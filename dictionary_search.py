def total_words(file): # number of words
	with open(file, "r") as f:
	    for count, line in enumerate(f):
	        pass
	return count + 1

words = [] # 'database'
f = open("english_words.txt")
for i in range(total_words("english_words.txt")):
	line = f.readline()[:-1] # -1 to exclude \n
	if len(line) > 2:	words.append(line.lower())

form_lst = [] # list of form
for word in words:
	ele_lst = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']
	lst = [i.lower() for i in ele_lst if i.lower() in word] 
	# lst of possible elements
	
	form = []
	while len(word) > 0:
		if word[:2] in lst:
			form.append(word[:2].capitalize() + " ")
			word = word[2:]
		elif word[:1] in lst:
			form.append(word[:1].capitalize() + " ")
			word = word[1:]
		else:
			form.clear()
			break;
	if len(form) > 0:	form_lst.append(form) # add to lst with the format
# print(len(form_lst))
f = open("elemental_words.txt", "a")
for i in form_lst:
	f.write("".join(i) + "\n")
f.close()



