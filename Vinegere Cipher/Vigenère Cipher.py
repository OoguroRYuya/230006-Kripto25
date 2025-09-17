# =========================
# Vigenere Cipher Utility
# =========================
def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_length = len(key)
    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            enc = (ord(char) - ord('A') + shift) % 26
            ciphertext += chr(enc + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    for i, char in enumerate(ciphertext.upper()):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            dec = (ord(char) - ord('A') - shift) % 26
            plaintext += chr(dec + ord('A'))
        else:
            plaintext += char
    return plaintext

# =========================
# Main Program
# =========================
def main():
    while True:
        print("\n" + "="*50)
        print("        🔑 VIGENERE CIPHER PROGRAM 🔑")
        print("="*50)
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Contoh")
        print("4. Keluar")
        print("="*50)

        pilihan = input("Pilih menu [1-4]: ")

        if pilihan == "1":
            plaintext = input("Masukkan plaintext: ").upper()
            key = input("Masukkan key: ").upper()
            ciphertext = vigenere_encrypt(plaintext, key)
            print("👉 Ciphertext:", ciphertext)

        elif pilihan == "2":
            ciphertext = input("Masukkan ciphertext: ").upper()
            key = input("Masukkan key: ").upper()
            plaintext = vigenere_decrypt(ciphertext, key)
            print("👉 Plaintext:", plaintext)

        elif pilihan == "3":
            print("\n=== Contoh Penggunaan ===")
            text = "HELLO WORLD"
            key = "KEY"
            encrypted = vigenere_encrypt(text, key)
            decrypted = vigenere_decrypt(encrypted, key)
            print("Plaintext :", text)
            print("Key       :", key)
            print("Ciphertext:", encrypted)
            print("Dekripsi  :", decrypted)

        elif pilihan == "4":
            print("Keluar... 👋")
            break
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()
