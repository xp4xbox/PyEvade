import base64, os

# shellcode (eg. xr8\x02...)
shellcode = ""

encryptedshellcode = base64.b64encode(shellcode)

os.system("echo " + encryptedshellcode + "|clip")

print "encoded shellcode copied to clipboard"
