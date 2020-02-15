from pwn import * 

res = []

def enc(msg):
    p = remote("ctf.iitdh.ac.in",2201)
    p.recvuntil("decrypt - decrypt a message")
    p.sendline("encrypt")
    p.sendlineafter("Message: ",msg)
    return p.recvline()
    
def dec(msg):
    p = remote("ctf.iitdh.ac.in",2201)
    p.recvuntil("decrypt - decrypt a message")
    p.sendline("decrypt")
    p.sendlineafter("Message: ",msg)
    return p.recvline()
    
    
for i in range(0,4) : 
    res.append(enc("aaaa"))
    print len(res[i])
    print "nonce : "+res[i][:32]+"\n str : "+res[i][32:64]+"\n str2 : "+res[i][64:96]