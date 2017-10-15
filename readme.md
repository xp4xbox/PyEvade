# PyEvade
PyEvade is a simple tool to bypass many antivirus solutions on windows for metasploit payloads.

## Installation
PyEvade requires:

* [Python 2.7](https://www.python.org/downloads)
* [Pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/)
* [Py2Exe](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/)

## Usage

1. Generate raw shellcode using metasploit using `-f python` to get the correct output. eg. (eg. xr8\x02...)
2. Generate encoded shellcode using the [encoder](https://github.com/xp4xbox/PyEvade/blob/master/PyEvade/encoder.py). Setting `shellcode` to be to be your raw shellcode (eg. shellcode = buf).
3. Set `encodedShellcode` to be your encoded shellcode in [payload.py](https://github.com/xp4xbox/PyEvade/blob/master/PyEvade/payload.py).
4. Run `python setup.py` to build your program to standalone .exe.

### How It Works

This tool works by encoding the raw metasploit payload to base64. Then decoding it and injecting the raw shellcode into the file itself on execution.
