# 🌟 LogiX: Smart Logistics Distribution System 🌟

## 🚀 Deskripsi
LogiX adalah sistem manajemen **logistik, gudang, dan distribusi** berbasis Python. Sistem ini menggunakan **Object-Oriented Programming (OOP)** secara intensif untuk mengelola:
- **Master data**: Kategori, Supplier, Gudang, Toko  
- **User**: Admin, Staff, Manajer Distribusi  
- **Barang**: Elektronik, Makanan, Minuman, Non-Elektronik  
- **Transaksi**: masuk/keluar  
- **Distribusi**: Reguler & Express  
- **Pengiriman**  
- **Laporan & statistik sistem**  

Aplikasi ini dibuat untuk simulasi proses logistik dari gudang ke toko, lengkap dengan pencatatan stok, status barang, dan laporan harian.

## 🛠 Fitur Utama
### ➡️ Manajemen User
- **Admin**: akses penuh sistem  
- **Staff Gudang**: mengelola stok  
- **Manajer Distribusi**: monitoring distribusi & laporan  

### ➡️ Manajemen Barang
- **Barang Elektronik**: atribut daya & garansi  
- **Barang Makanan**: tanggal kadaluarsa  
- **Barang Minuman**: volume (ml/L)  
- **Barang Non-Elektronik**: kondisi (baik/rusak)  

### ➡️ Distribusi & Pengiriman
- **Distribusi Reguler**: biaya murah, estimasi 2–4 hari  
- **Distribusi Express**: biaya lebih tinggi, estimasi 1 hari  
- **Pengiriman otomatis** mengubah status distribusi  

### ➡️ Laporan & Statistik
- Ringkasan barang & distribusi  
- Statistik stok & status barang  
- Logging & Timestamp: semua aktivitas dicatat otomatis, waktu pembuatan & update data tercatat untuk tracking  

## 🏗 Arsitektur OOP
### ➡️ Inheritance (Pewarisan)
- **Admin, StaffGudang, ManajerDistribusi** mewarisi User  
- **BarangElektronik, BarangMakanan, BarangMinuman** mewarisi Barang / BarangNonElektronik  
- **DistribusiReguler & DistribusiExpress** mewarisi DistribusiBase  
- **Manfaat**: menghindari duplikasi kode, memudahkan extensibility  

### ➡️ Polymorphism (Polimorfisme)
- Method `tampilkan_info()` di-override di semua subclass:  
  - **Admin** menampilkan “FULL ACCESS”  
  - **Barang** menampilkan atribut spesifik (garansi, volume, expired)  
  - **Distribusi** menampilkan jenis & estimasi  
- DistribusiReguler & DistribusiExpress bisa diproses dengan method sama (`proses()`, `kirim()`, `selesai()`) tapi implementasinya berbeda 
- **Manfaat**: memudahkan penggunaan interface yang sama untuk objek berbeda  

### ➡️ Abstraction (Abstraksi)
- **DistribusiBase** adalah abstract base class  
  - Memaksa subclass mengimplementasikan `hitung_biaya()` & `estimasi_waktu()`  
- **User** juga abstract class (tidak bisa instansiasi langsung, harus subclass)  
- **Manfaat**: menegaskan kontrak method yang harus dimiliki subclass  

### ➡️ Encapsulation (Enkapsulasi)
- Semua atribut menggunakan private/protected (`_nama`, `_stok`, `_harga`)  
- Getter & Setter digunakan untuk validasi & update timestamp  

### ➡️ Mixins
- LogMixin: menambahkan logging aktivitas
- TimestampMixin: otomatis mencatat created_at & updated_at
- Digunakan di Barang, Gudang, Kategori, dll
- Manfaat: kode reusable tanpa harus mewarisi class utama

## 📦 Struktur Folder
logix/
│
├─ admin.py
├─ barang.py
├─ barang_elektronik.py
├─ barang_makanan.py
├─ barang_minuman.py
├─ barang_non_elektronik.py
├─ distribusi_base.py
├─ distribusi_reguler.py
├─ distribusi_express.py
├─ gudang.py
├─ kategori.py
├─ laporan.py
├─ pengiriman.py
├─ transaksi.py
├─ status_barang.py
├─ user.py
└─ main.py
