import zlib
import os

message = "signature="
message += "a"*64
message += "b"*64


# for i in  range(0,10):
#     message = chr(ord("z")-i)+chr(ord("a")+i)
#     message = zlib.compress(message)
#     print chr(ord("z")-i)+chr(ord("a")+i)
#     print message.encode("hex")
    
message = zlib.compress(message)
print message.encode('hex')