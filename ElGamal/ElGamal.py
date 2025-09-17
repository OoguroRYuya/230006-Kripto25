# ===============================
# Program ElGamal Encryption/Decryption
# Plaintext: A-Z (0-25)
# ===============================

def mod_inverse(a, m):
    """Cari invers modulo (Extended Euclidean Algorithm)"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def char_to_num(ch):
    """Konversi huruf A-Z ke angka 0-25"""
    return ord(ch) - ord('A')

def num_to_char(num):
    """Konversi angka 0-25 ke huruf A-Z"""
    return chr(num + ord('A'))

def encrypt(p, g, x, k, plaintext):
    # Hitung public key y
    y = pow(g, x, p)

    # Hitung c1
    c1 = pow(g, k, p)

    # Hitung y^k mod p
    s = pow(y, k, p)

    # Ubah plaintext ke angka 0-25
    m_nums = [char_to_num(ch) for ch in plaintext]

    # Hitung c2
    c2 = [(m * s) % p for m in m_nums]

    return y, c1, c2

def decrypt(p, g, x, c1, c2):
    # Hitung shared key s = c1^x mod p
    s = pow(c1, x, p)

    # Cari invers dari s
    s_inv = mod_inverse(s, p)

    # Dekripsi
    m_nums = [(c * s_inv) % p for c in c2]
    plaintext = "".join(num_to_char(m) for m in m_nums)

    return plaintext

def main():
    while True:
        print("\n=== Menu ElGamal ===")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        choice = input("Pilih menu [1-3]: ")

        if choice == "1":
            mode = input("Pilih mode kunci (1=default, 2=manual): ")

            if mode == "1":
                p = 29
                g = 2
                x = 6
                k = 11
            else:
                p = int(input("Masukkan bilangan prima (p): "))
                g = int(input("Masukkan bilangan acak g: "))
                x = int(input("Masukkan private key x: "))
                k = int(input("Masukkan kunci sesi acak k: "))

            plaintext = input("Masukkan plaintext (A-Z): ").upper()

            y, c1, c2 = encrypt(p, g, x, k, plaintext)

            print("\n👉 Public key: (p={}, g={}, y={})".format(p, g, y))
            print("👉 Private key: x =", x)
            print("👉 Kunci sesi acak k:", k)
            print("👉 Hasil Enkripsi:")
            print("   c1 =", c1)
            print("   c2 =", c2)

        elif choice == "2":
            p = int(input("Masukkan bilangan prima (p): "))
            g = int(input("Masukkan bilangan acak g: "))
            x = int(input("Masukkan private key x: "))
            c1 = int(input("Masukkan c1: "))
            c2 = list(map(int, input("Masukkan c2 (pisahkan dengan spasi): ").split()))

            plaintext = decrypt(p, g, x, c1, c2)
            print("\n👉 Hasil Dekripsi:", plaintext)

        elif choice == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
