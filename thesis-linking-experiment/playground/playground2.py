import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

a = ['452f 99be sig bp ab9122090312 ff33bdc0 profile a5a3 thread flash', 'ext4 partition format', '472009 facebook report']
b = ['ab9122090312 a5a3 thread', 'riyadh chennai', 'partition 472009']

for x in range(len(a)):
	for y in range(len(b)):
		z = fuzz.token_set_ratio(a[x], b[y])
		print('\n')
		print(a[x])
		print(b[y])
		print(z)