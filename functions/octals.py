#-*- coding: utf-8 -*-

# Converte o octal em binario
def octal2bin(octal):
    return bin(int(octal, 8))


# Converte o octal em decimal
def octal2dec(octal):
    return str(int(octal, 8))


# Converte o octal em hexadecimal
def octal2hex(octal):
    return hex(int(octal, 8))
