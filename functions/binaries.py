#-*- coding: utf-8 -*-

# Converte o binario em decimal
def bin2dec(binary):
    return int(binary, 2)


# Converte o binario em octal
def bin2octal(binary):
    return oct(int(binary, 2))


# Converte o binario em hexadecimal
def bin2hex(binary):
    return hex(int(binary, 2))
