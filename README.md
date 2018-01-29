# BaseConverter
Conversor bem simples de bases com python.

- Como usar
``` HTML
Usage:
        python bc.py <cmd> <arg>
        <cmd>:                      
                -b (binary)       
                -d (decimal)      
                -o (octal)        
                -h (hexadecimal)  
Examples:                         
        python bc.py -b 1111      
        python bc.py -d 15        
        python bc.py -o 17        
        python bc.py -h F
```

</pre>

- Exemplo de execução
<pre>
python bc.py -h FF
[+] Binary: 0b11111111
[+] Octal: 0377
[+] Decimal: 255
</pre>

obs.: Os números possuem representações de bases, iniciados com (0, 0x e 0b)
que são respectivamente octal, hexadecimal e binário.


TODO:
- Input/Output de arquivos para realizar a conversão
- criar portabilidade py2/py3
- Permitir um output mais puro
- Incluir conversão de ASCII
- Incluir conversão com base64/32 e similares
