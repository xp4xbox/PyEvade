import base64, os

# shellcode (eg. xr8\x02... or shellcode = buf)
shellcode = ""

encodedshellcode = base64.b64encode(shellcode)

os.system("echo " + encodedshellcode + "|clip")

print "encoded shellcode copied to clipboard"
