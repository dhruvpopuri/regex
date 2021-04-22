import re
BITS_IDs = '''
njjnsadadsdw
F2020B5PS0930P
msnddod
12012089B3291p
H201646930G
F2020A5PS0933D
F2039029A50930D
ghjkajhs



'''

#For first degree folks 

patterns = re.compile(r'F\d{4}(A1|A2|A3|A4|A5|A7|A8|A9|AA|AB|B1|B2|B3|B4|B5|C2|C5|C6|C7)PS\d{3,4}(P|G|H|D)')

#For second degree folks
h_patterns = re.compile(r'H\d{4}(29|01|45|43|30|44|24|03|41|31|40|42|06|23|12|08|46|47|49|37|36)\d{3,4}(P|G|H|D)')

f_matches = patterns.finditer(BITS_IDs)

h_matches = h_patterns.finditer(BITS_IDs)


for match in f_matches:
	print(match)

for match in h_matches:
	print(match)
