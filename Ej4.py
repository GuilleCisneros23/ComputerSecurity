import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_decode(encoded):
    dec = ""
    i = 0
    while i < len(encoded):
        first_char = encoded[i]
        second_char = encoded[i + 1]

        first_binary = format(ALPHABET.index(first_char), '04b')
        second_binary = format(ALPHABET.index(second_char), '04b')
        
        binary = first_binary + second_binary
        dec += chr(int(binary, 2))
        
        i += 2
    
    return dec


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


flag = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"
key = "c"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

print("Mensaje cifrado:", flag)

dec = ""
for i, c in enumerate(flag):
    dec += shift(c, key[i % len(key)])
plain_text = b16_decode(dec)
print("Mensaje descifrado: picoCTF{{{}}}".format(plain_text))

