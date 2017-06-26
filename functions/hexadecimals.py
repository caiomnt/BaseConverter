#-*- coding: utf-8 -*-

# Converte o hexdecimal em binario
def hex2bin(hexadecimal):
    return bin(int(hexadecimal, 16))


# Converte o hexdecimal em octal
def hex2octal(hexadecimal):
    return oct(int(hexadecimal, 16))


# Converte o hexdecimal em decimal
def hex2dec(hexadecimal):
    return str(int(hexadecimal, 16))
