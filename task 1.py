import getpass

inp_str = getpass.getpass("Enter the message: ")
shift = int(input("Enter the shift value: "))
dirr = int(input("Enter 1 for encryption or 0 for decryption: "))
out_str = ""

for i in inp_str:
    if i.isalpha():
        base = ord('A') if i.isupper() else ord('a')
        out_str += chr((ord(i) - base + shift * (2 * dirr - 1)) % 26 + base)
    else:
        out_str += i

print("Result:", out_str)
