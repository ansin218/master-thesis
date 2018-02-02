# Similarity comparison done here
# May be use something like Jaccard similarity or Cosine similarity 
import Levenshtein

a = ['452f 99be sig bp ab9122090312 ff33bdc0 profile a5a3 thread flash', 'ext4 partition format', '472009 facebook report']
b = ['ab9122090312 a5a3 thread', 'riyadh chennai', 'partition 472009']

c = Levenshtein.ratio('472009 facebook report', 'partition 472009')
print(c)

for x in range(len(a)):
	for y in range(len(b)):
		c = Levenshtein.ratio(a[x], b[y])
		print('\n')
		print(a[x])
		print(b[y])
		print(c)


# custom method

s = 0

for x in range(len(a)):
	for y in range(len(b)):
		if(a[x] == b[y]):
			print('==> Similar: ', a[x], b[y])
			s += 1

if(s == 0):
	print('Completely Dissimilar')
else:
	if(len(a) == len(b)):
		if(s == len(a)):
			print('Completely Similar: 100%')
		else:
			if(s == 0):
				print('Completely Dissimilar')
			else:
				print('Partially Similar: ', (s * 100) / (len(a) + len(b) - s), '%')
	else:
		print('Partially Similar: ', (s * 100) / (len(a) + len(b) - s), '%')