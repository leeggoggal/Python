#-- coding:utf-8 --
import sys,struct
with open("#input_file_name","rb") as exe:
    pe_hex = exe.read().encode('hex').upper()

orig_stdout = sys.stdout
f = open("#output_file_name",'w')
sys.stdout = f

hex_array = pe_hex
length = len(pe_hex)
hex_cnt = 0
e_magic_cnt = 0
e_lfanew_cnt = 120
for i in range(length):
    check = hex_array[hex_cnt:hex_cnt+4]
    hex_cnt += 4
    if check == "5045":
        e_magic = hex_array[e_magic_cnt:e_magic_cnt + 4]
        e_ifanew = struct.pack('<L', int("0x"+hex_array[e_lfanew_cnt:e_lfanew_cnt + 8],0)).encode('hex').upper()
        Machine = struct.pack('<H', int("0x"+hex_array[hex_cnt+4:hex_cnt+8],0)).encode("hex").upper()
        PE_signature = struct.pack('<h', int("0x"+check,0)).encode("hex").upper()
        NumberOfSections = struct.pack('<H', int("0x"+hex_array[hex_cnt+8:hex_cnt+12],0)).encode("hex").upper()
        SizeOfOptionalHeader = struct.pack('<H', int("0x"+hex_array[hex_cnt+36:hex_cnt+40],0)).encode("hex").upper()
        AddressOfEntryPoint =  struct.pack('<L', int("0x"+hex_array[hex_cnt+76:hex_cnt+84],0)).encode("hex").upper()
        ImageBase = struct.pack('<L', int("0x"+ hex_array[hex_cnt+100:hex_cnt+108],0)).encode("hex").upper()
        print "[IMAGE_DOS_HEADER]\n" + "e_magic : "+e_magic.decode("hex")
        print "e_ifanew : " + "0x" + e_ifanew + "\n"
        print "[IMAGE_FILE_HEADER]\n" +"PE_signature : 0x"+PE_signature
        if Machine == "014C":
            print "Machine : intel_i386 " + " (0x" + Machine+")"
        elif Machine == "8664":
            print "Machine : AMD_64 " + " (0x" + Machine + ")"
        elif Machine == "0200":
            print "Machine : IA_64 " + " (0x" + Machine + ")"
        print "NumberOfSections : "+ str(int(NumberOfSections,16))+ " (0x"+NumberOfSections+")"
        print "SizeOfOptionalHeader : "+str(int(SizeOfOptionalHeader,16))+" bytes"+" (0x"+SizeOfOptionalHeader+")\n"
        print "[IMAGE_OPTIONAL_HEADER]\n"+"AddressOfEntryPoint : 0x" + AddressOfEntryPoint
        print "ImageBase : 0x"+ImageBase+"\n"
        hex_cnt = hex_cnt - 4
        length = (length - hex_cnt)/16
        for i in range(length):
            hex_cnt += 16
            check = hex_array[hex_cnt:hex_cnt+16]
            if check == "434F444500000000" or check == "2E74657874000000":
                print "[SectionTable]"
                for i in range(int(NumberOfSections,16)):
                    print "name : "+hex_array[hex_cnt:hex_cnt+16].decode("hex")
                    VirtualSize = (struct.pack('<L', int("0x"+hex_array[hex_cnt+16:hex_cnt+24],0)).encode("hex"))
                    print "VirtualSize : "+ str(int(VirtualSize,16))+" bytes (0x"+VirtualSize+")"
                    VirtualAddress = (struct.pack('<L', int("0x"+hex_array[hex_cnt+24:hex_cnt+32],0)).encode("hex"))
                    print "VirtualAddress : 0x"+VirtualAddress
                    hex_cnt += 80
                break
        sys.exit()

sys.stdout = orig_stdout
f.close()

