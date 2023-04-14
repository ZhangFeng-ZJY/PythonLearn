ftp = "http://www.cucn.edu.cn"
n = ftp[:-1].count("e")
print("e出现了:", n, "次", sep = '')

print(ftp.find('edu'))
print(ftp.upper())
t = ftp.find('cucn')
print(ftp[t : t + 4])
