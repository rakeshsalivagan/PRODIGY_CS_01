def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text


def main():
    while True:
        choice = input("hello am rakesh here \n Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please choose encrypt or decrypt.")
            continue

        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'encrypt':
            result = caesar_cipher_encrypt(message, shift)
            print("Encrypted message:", result)
        elif choice == 'decrypt':
            result = caesar_cipher_decrypt(message, shift)
            print("Decrypted message:", result)

        perform_another = input("Do you want to perform another encryption/decryption? (yes/no): ").lower()
        if perform_another != 'yes':
            break


if __name__ == "__main__":
    main()
