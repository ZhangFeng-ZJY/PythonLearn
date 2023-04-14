s = str(input())
s = s + 'l'
s1 = ''
for i in range(0, len(s) - 1):
	if s[i].isdigit() == False:
		continue
	if s[i].isdigit() == True:
		s1 = s1 + s[i]
	if s[i + 1].isdigit() == False:
		s1 = s1 + ','

print(s1)
