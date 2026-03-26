# 🚀 LogiX: Smart Logistics Distribution System
LogiX adalah aplikasi manajemen logistik berbasis Python yang dirancang untuk mengelola barang, gudang, toko, serta proses distribusi secara terstruktur. Sistem ini dikembangkan menggunakan konsep **Object-Oriented Programming (OOP)** dengan penerapan prinsip seperti enkapsulasi, abstraksi, inheritance, polymorphism, modularitas, dan mixins.

## 📌 Deskripsi Singkat
Aplikasi ini digunakan untuk:
- Mengelola data barang, gudang, dan toko
- Mengatur stok barang di gudang dan toko
- Melakukan distribusi barang dari gudang ke toko
- Mencatat riwayat distribusi
- Menampilkan laporan data secara terstruktur
Seluruh data disimpan dalam file **JSON (db.json)** sehingga dapat digunakan kembali saat program dijalankan ulang.

## 👥 Role Pengguna
Sistem memiliki 3 jenis pengguna:
### 1. Supervisor
- Akses penuh ke seluruh sistem
- Mengelola user, barang, gudang, toko, distribusi, dan laporan

### 2. Staff Gudang
- Mengelola data barang
- Mengelola stok gudang

### 3. Staff Toko
- Mengelola stok toko

## ⚙️ Fitur Utama
- 🔐 Login sistem berdasarkan role
- 👤 Manajemen user
- 📦 Manajemen barang
- 🏭 Manajemen gudang
- 🏪 Manajemen toko
- 📊 Pengelolaan stok (tambah & kurangi)
- 🚚 Distribusi barang gudang → toko
- 🧾 Riwayat distribusi
- 🔄 Update status distribusi
- 📋 Laporan barang, gudang, dan distribusi
- 🗑️ Hapus riwayat distribusi
- 💾 Penyimpanan data menggunakan JSON

## 🧠 Konsep OOP yang Digunakan
### 🔹 Enkapsulasi & Kontrol Akses
- Atribut menggunakan `_private`
- Akses melalui method dan property (getter/setter)
- Validasi data untuk menjaga konsistensi

### 🔹 Abstraksi (Abstract Base Class)
- Class `User` sebagai abstract class
- Method `akses_menu()` wajib diimplementasikan oleh subclass

### 🔹 Inheritance
- `Supervisor`, `StaffGudang`, `StaffToko` mewarisi `User`

### 🔹 Polymorphism
- Method `akses_menu()` memiliki implementasi berbeda di setiap role

### 🔹 Modularitas
- Sistem dipisah ke beberapa file sesuai fungsi (barang, gudang, toko, dll)

### 🔹 Mixins
- `LogMixin` → logging aktivitas
- `TimestampMixin` → pencatatan waktu otomatis

## 🗂️ Struktur Project
├── main.py
├── auth.py
├── database.py
├── config.py
├── barang.py
├── gudang.py
├── toko.py
├── distribusi.py
├── laporan.py
├── user.py
├── admin.py
├── staff_gudang.py
├── staff_toko.py
├── mixins.py
├── db.json

## 👨‍💻 Tim Pengembang
### Dian Fajar
### Fatimah Azzahra
### Ghenia Fadiya Zahra
### R. Daffa