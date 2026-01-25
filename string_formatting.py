def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:]) # for binary, octal, hexadecimal there is a extra prefix '0b', '0o', '0x', so we slice it off with [2:]
    
    for i in range(1, number + 1 ):
        decemal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(decemal, octal, hexa, binary)
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)