def encrypt(msg, shift_val):
    result = ""
    # transverse the plain text
    for i in range(len(msg)):
        char = msg[i]
        # In case of space 
        if char == " ":
            result += result.join(" ")
        # Encrypt uppercase characters in plain text
        elif (char.isupper()):
            result += chr((ord(char) + shift_val - 65) % 26 + 65)
        # Encrypt lowercase characters in plain
        else:
            result += chr((ord(char) + shift_val - 97) % 26 + 97)
    return result[:-1]

# Read files
with open('sample3.txt') as f:
    f = f.readlines()
encrypted_text = []
for i in range(26):
    for j in range(len(f)):
        encrypted_text.append(f'key #{i}: ' + encrypt(f[j], i))
txt_file = open('encrypted with keys.txt', 'w')
for i in range(len(encrypted_text)):
    txt_file.write(encrypted_text[i])
    txt_file.write('\n')
txt_file.close()



"""alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


for i in range(0, len(alphabet)):
    # Create unique dictionary for each round
    my_dict = dict()
    for index, letter in enumerate(alphabet):
        my_dict[letter] = alphabet[index - i]
    # Encrypt message
    for j in range(len(f)):
        f[j] = f[j].lower()
        for key, value in my_dict.items():
            f[j] = f[j].replace(key, value)
           
        print(f"Key{j}: {f[j]}")"""
        
        
