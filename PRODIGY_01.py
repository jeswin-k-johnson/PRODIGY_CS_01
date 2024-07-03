def encrypt(shift, message):
    result = ""
    for letter in message:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def decrypt(shift, message):
    result = ""
    for letter in message:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (E/D): ")
        if choice.upper() == "E":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted = encrypt(shift, message)
            print("Encrypted message:", encrypted)
        elif choice.upper() == "D":
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted = decrypt(shift, message)
            print("Decrypted message:", decrypted)
        else:
            print("Invalid choice. Please try again.")
        cont = input("Do you want to continue? (Y/N): ")
        if cont.upper() != "Y":
            break

if __name__ == "__main__":
    main()
    