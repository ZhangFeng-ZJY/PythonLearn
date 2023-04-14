s = str(input())
s1 = ''
for i in range(0, len(s)):
	if s[0].isdigit() == False:
		continue
	if s[0].isdigit() == True:
		s1 = s1 + s[i]
	if s[0].isdigit() == False:
		s1 = s1 + ','

print(s1)
