def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    choice = input("Type 'encrypt' to encode or 'decrypt' to decode: ").strip().lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid option. Please type 'encrypt' or 'decrypt'.")
    else:
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter shift number: "))
        except ValueError:
            print("Shift must be a number.")
            exit()

        if choice == 'encrypt':
            print("Encrypted:", encrypt(message, shift))
        else:
            print("Decrypted:", decrypt(message, shift))
