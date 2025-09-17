# 🔐 ElGamal Cipher Program

## 📌 Deskripsi
Program ini mengimplementasikan algoritma **ElGamal** menggunakan Python.  
Fitur-fitur utama:  
1. **Enkripsi** plaintext menggunakan public key.  
2. **Dekripsi** ciphertext menggunakan private key.  
3. **Pilihan mode kunci**: default atau manual.  

---

## 📌 Alur Program
Saat dijalankan, user akan melihat menu utama:

=== ElGamal Cipher ===

1. Enkripsi  
2. Dekripsi  
3. Keluar  

### 1. Enkripsi
- Input mode kunci:  
  - **Default**: `p=29`, `g=2`, `x=6`, `k=11`.  
  - **Manual**: user memasukkan `p` (bilangan prima), `g` (generator), `x` (private key), dan `k` (kunci sesi acak).  
- Input plaintext (misalnya `HALO`).  
- Program akan:  
  - Konversi huruf → angka (A=0, B=1, ..., Z=25).  
  - Hitung public key:  
    ```
    y = g^x mod p
    ```
  - Hitung ciphertext:  
    ```
    c1 = g^k mod p
    c2 = (m * (y^k)) mod p
    ```
- Output: nilai `c1` dan daftar `c2`.

---

### 2. Dekripsi
- Input kunci privat (`p`, `g`, `x`) dan hasil enkripsi (`c1`, `c2`).  
- Program akan:  
  - Hitung shared key:  
    ```
    s = c1^x mod p
    ```
  - Hitung invers:  
    ```
    s_inv = s^(-1) mod p
    ```
  - Hitung plaintext:  
    ```
    m = c2 * s_inv mod p
    ```
  - Konversi angka → huruf.  
- Output: plaintext asli.

---

### 3. Keluar
Mengakhiri program dengan pesan perpisahan.

---

## 📌 Syarat Validitas Kunci
- `p` **harus bilangan prima**.  
- `g` dipilih sebagai generator mod `p`.  
- `x` (private key) < `p`.  
- `k` (kunci sesi acak) dipilih acak < `p`.  

Jika `p` bukan prima, sistem enkripsi tidak valid.

---

## 📌 Contoh Pemakaian

### Enkripsi
- Pilih menu [1-3]: 1
- Pilih mode kunci (1=default, 2=manual): 2
- Masukkan bilangan prima (p): 29
- Masukkan bilangan acak g: 2
- Masukkan private key x: 6
- Masukkan kunci sesi acak k: 11
- Masukkan plaintext (A-Z): HALO

- 👉 Public key: (p=29, g=2, y=6)
- 👉 Private key: x = 6
- 👉 Kunci sesi acak k: 11
- 👉 Hasil Enkripsi:
- c1 = 18
- c2 = [5, 0, 12, 10]

### Dekripsi

- Pilih menu [1-3]: 2
- Masukkan bilangan prima (p): 29
- Masukkan bilangan acak g: 2
- Masukkan private key x: 6
- Masukkan c1: 18
- Masukkan c2 (pisahkan dengan spasi): 5 0 12 10

- 👉 Hasil Dekripsi: HALO
---

## 📌 Catatan
- Plaintext hanya bisa berupa huruf A–Z.  
- Spasi dan karakter lain tidak didukung (hanya A=0 s/d Z=25).  
- Jika hasil dekripsi tidak sesuai, kemungkinan input `p`, `g`, `x`, atau `k` tidak benar.  

---

## 📌 Bukti Screenshoot
![Enkripsi](Screenshots\enkripsi.png)  
![Dekripsi](Screenshots\dekripsi.png) 
