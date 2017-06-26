#-*- coding: utf-8 -*-

# Modulos
from functions.decimals import *
from functions.octals import *
from functions.hexadecimals import *
from functions.binaries import *
from sys import argv, exit
from getopt import getopt, GetoptError

# Como usar
def usage():
    print 'Usage:'
    print '\tpython',argv[0],'<cmd> <arg>'
    print '\tcmd: \n\t\t-b (binary)\n\t\t-d (decimal)\n\t\t-o (octal)\n\t\t-h (hexadecimal)'
    print 'Examples:'
    print '\tpython',argv[0],'-b 1111'
    print '\tpython',argv[0],'-d 15'
    print '\tpython',argv[0],'-o 17'
    print '\tpython',argv[0],'-h F'
    exit(1)

# Funcao principal
def main():

    try:

        # Retorna os argumentos via terminal
        opts, args = getopt(argv[1:], "b:o:d:h:")

        # Restringindo a entrada de dados
        if len(opts) >= 2 or len(args) > 1:
            usage()
        else:
            # Analisa os modos passados e executa as conversões devidas
            for cmd, arg in opts:
                if cmd == "-d":
                    print '[+] Octal: ' + dec2octal(arg)
                    print '[+] Binary: ' + dec2bin(arg)
                    print '[+] Hexadecimal: ' + dec2hex(arg)
                elif cmd == "-b":
                    print '[+] Decimal: ' + bin2dec(arg)
                    print '[+] Octal: ' + bin2octal(arg)
                    print '[+] Hexadecimal: ' + bin2hex(arg)
                elif cmd == "-o":
                    print '[+] Binary: ' + octal2bin(arg)
                    print '[+] Decimal: ' + octal2dec(arg)
                    print '[+] Hexadecimal: ' + octal2hex(arg)
                elif cmd == "-h":
                    print '[+] Binary: ' + hex2bin(arg)
                    print '[+] Octal: ' + hex2octal(arg)
                    print '[+] Decimal: ' + hex2dec(arg)
                else:
                    usage()

    # Trata erros de entrada
    except (GetoptError, ValueError):
        usage()


# Executa a funcao principal
if __name__ == "__main__":
    main()
