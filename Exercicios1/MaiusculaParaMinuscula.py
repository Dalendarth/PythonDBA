# Converter uma letra maiúscula em minúscula


uppercase_letter = 'A'
ascii_code = ord(uppercase_letter)
if 65 <= ascii_code <= 90: # verifica se é uma letra maiúscula
    lowercase_letter = chr(ascii_code + 32)
    print("A letra maiúscula", uppercase_letter, "é convertida em minúscula:", lowercase_letter)
else:
    print(uppercase_letter, "não é uma letra maiúscula")