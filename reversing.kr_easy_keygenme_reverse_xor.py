key = [hex(0x10),hex(0x20),hex(0x30)]
Serial= "5B134977135E7D13"
index = 0
k = 0
for i in range((len(Serial)/2)):
    print hex(int(Serial[index:index+2],16) ^ int(key[k],16)).split("0x")[1].decode("hex"),
    index += 2
    k += 1
    if k > 2:
        k = 0
