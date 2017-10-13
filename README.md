# PyEvade
PyEvade is a simple tool to bypass many antivirus solutions on windows for metasploit payloads.

# Installation
PyEvade requires:

* [Python 2.7](https://www.python.org/downloads)
* [Pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/)
* [Py2Exe](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/)

# Usage

1. Generate raw shellcode using metasploit using `-f python` to get the correct output. eg. (eg. xr8\x02...)
2. Generate encrypted shellcode using the [encrypter](https://github.com/xp4xbox/PyEvade/blob/master/encrypter.py). Setting `shellcode` to be your raw shellcode as one line.
3. Set `encryptedShellcode` to be your encrypted shellcode in [payload.py](https://github.com/xp4xbox/PyEvade/blob/master/payload.py).
4. Run `python setup.py` to build your program to standalone .exe.

# How It Works

This tool works by encrypting the raw metasploit payload to base64. Then decoding it and injecting the raw shellcode into the file itself on execution.
