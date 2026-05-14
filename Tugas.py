import hashlib

# Database sederhana menggunakan dictionary {username: password_hash}
user_db = {}

def hash_password(password):
    """Mengubah string password menjadi SHA-256 hash."""
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    print("\n--- Menu Registrasi ---")
    username = input("Masukkan username baru: ")
    if username in user_db:
        print("Username sudah terdaftar!")
        return

    password = input("Masukkan password: ")
    
    # Proses Hashing
    hashed_pw = hash_password(password)
    
    # Simpan ke database
    user_db[username] = hashed_pw
    
    print(f"User berhasil didaftarkan!")
    print(f"Hash Password disimpan: {hashed_pw}")

def login():
    print("\n--- Menu Login ---")
    username = input("Username: ")
    password = input("Password: ")

    if username in user_db:
        # Cek apakah hash password yang diinput sama dengan yang di database
        if hash_password(password) == user_db[username]:
            print(">>> LOGIN BERHASIL! Selamat datang.")
        else:
            print(">>> LOGIN GAGAL: Password salah.")
    else:
        print(">>> LOGIN GAGAL: Username tidak ditemukan.")

# Simulasi Berjalan
while True:
    print("\n1. Registrasi\n2. Login\n3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == '1':
        register()
    elif pilihan == '2':
        login()
    elif pilihan == '3':
        break
    else:
        print("Pilihan tidak valid.")