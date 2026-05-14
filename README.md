# Sistem Autentikasi User (SHA-256 Secure Hashing)
Repositori ini berisi implementasi sistem registrasi dan login sederhana menggunakan bahasa pemrograman Python. Fokus utama dari program ini adalah keamanan data, di mana password pengguna tidak disimpan dalam bentuk teks asli, melainkan diubah menjadi format hash menggunakan algoritma **SHA-256**.

## Fitur Utama
* **Registrasi User**: Membuat akun baru dengan username unik.
* **Secure Hashing**: Mengubah password menjadi hash SHA-256 sebelum disimpan ke database.
* **Penyimpanan Aman**: Menyimpan data dalam struktur dictionary (simulasi database).
* **Verifikasi Login**: Memeriksa kecocokan password saat login dengan membandingkan nilai hash.
* **Status Login**: Menampilkan feedback visual apakah login berhasil atau gagal.

## Cara Kerja
Sistem ini mengikuti prinsip *One-Way Hashing*:
1. Saat registrasi, password `rahasia123` diubah menjadi `ef2d127de37b94...` dan disimpan.
2. Saat login, password yang diinput user kembali di-hash.
3. Jika hash hasil input **sama** dengan hash yang disimpan di database, maka login diizinkan.

## Cara Menjalankan
1. Buka terminal atau command prompt.
2. Jalankan perintah:
   ```bash
   python Tugas.py
