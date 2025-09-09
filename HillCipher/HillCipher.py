import numpy as np

# =========================
# Utility Functions
# =========================
def mod_inverse(a, m):
    """Cari invers modulo a (mod m)"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inverse(matrix, modulus):
    """Cari invers matriks mod m"""
    det = int(round(np.linalg.det(matrix)))  # determinan
    det = det % modulus
    det_inv = mod_inverse(det, modulus)
    if det_inv is None:
        return None
    
    matrix_adj = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (det_inv * matrix_adj) % modulus

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper().replace(" ", "")]

def numbers_to_text(numbers):
    return ''.join(chr(int(n) + ord('A')) for n in numbers)

# =========================
# Hill Cipher Core
# =========================
def encrypt(plaintext, key):
    numbers = text_to_numbers(plaintext)
    n = key.shape[0]
    if len(numbers) % n != 0:
        numbers += [ord('X') - ord('A')] * (n - len(numbers) % n)
    ciphertext = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        enc = np.dot(key, block) % 26
        ciphertext.extend(enc)
    return numbers_to_text(ciphertext)

def decrypt(ciphertext, key):
    key_inv = matrix_mod_inverse(key, 26)
    if key_inv is None:
        return None
    numbers = text_to_numbers(ciphertext)
    n = key.shape[0]
    plaintext = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        dec = np.dot(key_inv, block) % 26
        plaintext.extend(dec)
    return numbers_to_text(plaintext)

def find_key(plaintext, ciphertext, n):
    P = np.array(text_to_numbers(plaintext)).reshape(-1, n).T
    C = np.array(text_to_numbers(ciphertext)).reshape(-1, n).T
    P_inv = matrix_mod_inverse(P, 26)
    if P_inv is None:
        return None
    return (C.dot(P_inv)) % 26

# =========================
# Main Program
# =========================
def main():
    while True:
        print("\n" + "="*50)
        print("           🔑 HILL CIPHER PROGRAM 🔑")
        print("="*50)
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Cari Kunci (Known Plaintext Attack)")
        print("4. Contoh")
        print("5. Keluar")
        print("="*50)

        pilihan = input("Pilih menu [1-5]: ")

        if pilihan == "1":
            n = int(input("Ukuran matriks kunci (contoh: 2): "))
            key = []
            print("Masukkan elemen matriks kunci (baris per baris):")
            for i in range(n):
                row = list(map(int, input(f"Baris {i+1}: ").split()))
                key.append(row)
            key = np.array(key)

            plaintext = input("Masukkan plaintext: ").upper()
            ciphertext = encrypt(plaintext, key)
            print("👉 Ciphertext:", ciphertext)

        elif pilihan == "2":
            n = int(input("Ukuran matriks kunci (contoh: 2): "))
            key = []
            print("Masukkan elemen matriks kunci (baris per baris):")
            for i in range(n):
                row = list(map(int, input(f"Baris {i+1}: ").split()))
                key.append(row)
            key = np.array(key)

            ciphertext = input("Masukkan ciphertext: ").upper()
            plaintext = decrypt(ciphertext, key)
            if plaintext is None:
                print("❌ Matriks kunci tidak invertibel modulo 26. Gunakan kunci lain!")
            else:
                print("👉 Plaintext:", plaintext)

        elif pilihan == "3":
            n = int(input("Ukuran matriks kunci (contoh: 2): "))
            plaintext = input("Masukkan plaintext (panjang kelipatan n): ").upper()
            ciphertext = input("Masukkan ciphertext: ").upper()
            key = find_key(plaintext, ciphertext, n)
            if key is None:
                print("❌ Matriks plaintext tidak invertibel modulo 26.")
            else:
                print("👉 Kunci ditemukan:")
                print(key)

        elif pilihan == "4":
            print("\n=== Contoh Penggunaan ===")
            key = np.array([[3, 3],
                            [2, 5]])
            plaintext = "HELLO"
            ciphertext = encrypt(plaintext, key)
            decrypted = decrypt(ciphertext, key)
            print("Kunci:\n", key)
            print("Plaintext :", plaintext)
            print("Ciphertext:", ciphertext)
            print("Dekripsi  :", decrypted)

        elif pilihan == "5":
            print("Keluar... 👋")
            break
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()
