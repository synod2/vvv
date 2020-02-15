
d = "UGFyc2Vje3BAZGQxbmdfMXNfbmVjZSQkYXJ5IX0="
c = "VjZSQkYXJ5IX0=UGFyc2Vje3BAZGQxbmdfMXNfbm"
r = ""
for j in range(-30,30) : 
    r = ""
    for i in range(0,len(c)) : 
        r += chr(ord(c[i])+j)
    print r