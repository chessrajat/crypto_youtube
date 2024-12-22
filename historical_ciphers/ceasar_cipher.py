
def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        character = text[i]
        if (character == " "):
            result += " "
            continue
        if (character.isupper()):
            # encodeing upper charcter
            character_code = ((ord(character) + (shift-65)) % 26) + 65
            result += chr(character_code)
        else:
            # encode lower character
            character_code = ((ord(character) + (shift-97)) % 26) + 97
            result += chr(character_code)

    return result

result = encrypt("code with rajat", 3)
print(result)
