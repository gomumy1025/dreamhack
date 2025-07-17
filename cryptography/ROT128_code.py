# Wargame site URL: https://dreamhack.io/wargame/challenges/852

#!/usr/bin/env python3

# List of two-digit hexadecimal strings from 0 to 255
hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

# reading encfile
with open('encfile.txt', 'r', encoding='utf-8') as f:
    enc_data = f.read().strip()

# split into two digits and turn them into a list
enc_list = [enc_data[i:i+2] for i in range(0, len(enc_data), 2)]

# decryption: index - 128 (modulo 256)
dec_list = []
for hex_b in enc_list:
    index = hex_list.index(hex_b)
    orig_index = (index - 128) % len(hex_list)
    dec_list.append(int(hex_list[orig_index], 16))  # Converting to an integer

# Converting to Byte Objects
dec_bytes = bytes(dec_list)

# Save as a restored image file
with open('flag_restored.png', 'wb') as f:
    f.write(dec_bytes)

print("Decryption commplete: flag_restored.png")
