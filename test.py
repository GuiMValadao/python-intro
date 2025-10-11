def print_formatted(number):
    length = len(str(bin(number)))
    for i in range(1, number):
        print(str(i).rjust(length, ' '), 
              oct(i).rjust(length, ' ').replace('0o', ''),
              hex(i).rjust(length, ' ').replace('0x', ''), 
              bin(i).rjust(length, ' ').replace('0b', ''))

n = int(input())
print_formatted(n)
