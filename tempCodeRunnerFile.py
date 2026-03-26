import os
from config import Config, Theme
from database import Database
from auth import Auth
from barang import Barang
from gudang import Gudang
from admin import Supervisor
from staff_gudang import StaffGudang
from staff_toko import StaffToko
from toko import Toko
from distribusi import Distribusi
from laporan import Laporan

# Inisialisasi Database Global
db = Database()

def konversi_ke_pcs(jumlah, satuan, kategori):
    if satuan == "dus":
        if kategori == "makanan":
            return jumlah * 20
        elif kategori == "minuman":
            return jumlah * 24  # opsional (kalau beda)
    return jumlah

# ================= VALIDASI INPUT =================

def input_angka(prompt):
    while True:
        try:
            return int(input(f"{Theme.ICON_INFO} {prompt}"))
        except ValueError:
            print(f"{Theme.FAIL}❌ Harus berupa angka!{Theme.ENDC}")

def input_tidak_kosong(prompt):
    while True:
        data = input(f"{Theme.ICON_INFO} {prompt}").strip()
        if data:
            return data
        print(f"{Theme.FAIL}❌ Input tidak boleh kosong!{Theme.ENDC}")

# ================= FUNGSI OPERASIONAL =================

def tambah_user():
    print(f"\n{Theme.OKCYAN}--- FORM TAMBAH USER BARU ---{Theme.ENDC}")
    username = input_tidak_kosong("Username Baru: ").lower().strip()
    
    if username.lower() in [u.lower() for u in db.data.get("users", {})]:
        print(f"{Theme.FAIL}❌ Username sudah terdaftar!{Theme.ENDC}")
        input("Enter...")
        return

    
    password = input_tidak_kosong("Password: ")


    nama = input_tidak_kosong("Nama Lengkap: ")
    
    print(f"\nPilih Role:")
    print("1. Supervisor")
    print("2. Staff Gudang")
    print("3. Staff Toko")

    # 🔥 VALIDASI INPUT
    while True:
        pilihan = input("Pilih (1/2/3): ").strip()
        if pilihan in ["1", "2", "3"]:
            break
        print("❌ Pilihan hanya boleh 1, 2, atau 3!")

    role_map = {
        "1": "supervisor",
        "2": "staff_gudang",
        "3": "staff_toko"
    }

    role = role_map[pilihan]

    db.data["users"][username] = {
        "password": password,
        "role": role,
        "nama": nama
    }

    db.save()
    print(f"{Theme.OKGREEN}✅ User {nama} berhasil didaftarkan!{Theme.ENDC}")
    input("\nTekan Enter...")

def input_kategori():
    while True:
        kategori = input("Kategori (makanan/minuman): ").lower().strip()
        if kategori in ["makanan", "minuman"]:
            return kategori
        print("❌ Kategori hanya boleh 'makanan' atau 'minuman'!")

def tambah_barang():
    print(f"\n{Theme.OKCYAN}--- FORM TAMBAH BARANG BARU ---{Theme.ENDC}")
    print("Satuan:")
    print("1. Pcs")
    print("2. Dus")
    print("0. Batal / Keluar")

    while True:
        pilih_satuan = input("Pilih (1/2/0): ")

        if pilih_satuan == "0":
            print("❌ Input barang dibatalkan")
            return

        if pilih_satuan in ["1", "2"]:
            break

        print("❌ Pilihan tidak valid!")

    satuan = "pcs" if pilih_satuan == "1" else "dus"
    id_b = input_tidak_kosong("ID Barang: ")

    if id_b in db.data.get("barang", {}):
            print(f"{Theme.FAIL}❌ ID sudah digunakan!{Theme.ENDC}")
            return

    nama = input_tidak_kosong("Nama Barang: ")

    # 🔥 INPUT KATEGORI (VALIDASI)
    kategori = input_kategori()

    harga = input_angka("Harga Satuan: ")

    id_g = input_tidak_kosong("Masukkan ID Gudang Penempatan: ")

    if id_g not in db.data["gudang"]:
        print(f"{Theme.FAIL}❌ Gudang tidak ditemukan!{Theme.ENDC}")
        return

    jumlah_input = input_angka("Jumlah: ")
    if jumlah_input <= 0:
        print("❌ Jumlah harus lebih dari 0!")
        return
    jumlah = konversi_ke_pcs(jumlah_input, satuan, kategori)

    if jumlah <= 0 or harga <= 0:
        print(f"{Theme.FAIL}❌ Input tidak valid!{Theme.ENDC}")
        return

    try:
        barang = Barang(id_b, nama, harga, kategori)
        db.data["barang"][id_b] = barang.to_dict()

    except Exception as e:
        print(f"{Theme.FAIL}❌ Gagal menambahkan barang: {e}{Theme.ENDC}")
        input("Enter...")
        return

    gudang_data = db.data["gudang"][id_g]
    gudang_data["stok"][id_b] = gudang_data["stok"].get(id_b, 0) + jumlah

    db.save()
    print(f"{Theme.OKGREEN}✅ Barang berhasil didaftarkan ke Gudang {id_g}!{Theme.ENDC}")
    input("\nTekan Enter...")

def tambah_gudang():
    print(f"\n{Theme.OKCYAN}--- REGISTRASI GUDANG BARU ---{Theme.ENDC}")

    

    while True:
        konfirmasi = input("Yakin ingin menambahkan gudang? (y/n): ").lower()

        if konfirmasi in ["y", "n"]:
            break
        print("❌ Input harus y atau n!")

    if konfirmasi == "n":
        print("❌ Dibatalkan")
        return  # 🔥 kembali ke menu utama

    id_g = input_tidak_kosong("ID Gudang: ")

    if id_g in db.data["gudang"]:
        print(f"{Theme.FAIL}❌ ID Gudang sudah ada!{Theme.ENDC}")
        input("Enter...")
        return
        
    nama = input_tidak_kosong("Nama Lokasi Gudang: ")

    db.data["gudang"][id_g] = {
        "nama": nama,
        "stok": {}
    }

    db.save()
    print(f"{Theme.OKGREEN}✅ Gudang berhasil ditambahkan!{Theme.ENDC}")
    input("\nTekan Enter...")

def tambah_toko():
    print(f"\n{Theme.OKCYAN}--- TAMBAH TOKO ---{Theme.ENDC}")

    while True:
        konfirmasi = input("Yakin ingin menambahkan gudang? (y/n): ").lower()

        if konfirmasi in ["y", "n"]:
            break
        print("❌ Input harus y atau n!")

    if konfirmasi == "n":
        print("❌ Dibatalkan")
        return  # 🔥 kembali ke menu utama

    id_t = input_tidak_kosong("ID Toko: ")

    if id_t in db.data["toko"]:
        print(f"{Theme.FAIL}❌ ID sudah ada!{Theme.ENDC}")
        input("Enter...")
        return

    nama = input_tidak_kosong("Nama Toko: ")

    db.data["toko"][id_t] = {
        "nama": nama,
        "stok": {}
    }

    db.save()
    print(f"{Theme.OKGREEN}✅ Toko berhasil ditambahkan!{Theme.ENDC}")
    input("\nEnter...")
    
def manajemen_stok():
    print(f"\n{Theme.OKCYAN}--- MANAJEMEN STOK ---{Theme.ENDC}")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    print("3. Hapus barang dari gudang")
    print("0. Kembali")

    # VALIDASI MENU
    while True:
        pilih = input("Pilih (1/2/3/0): ").strip()
        if pilih in ["1", "2", "3", "0"]:
            break
        print("❌ Pilihan hanya boleh 1, 2, 3, atau 0!")

    if pilih == "0":
        return

    id_g = input_tidak_kosong("ID Gudang: ")
    try:
        # VALIDASI GUDANG
        if id_g not in db.data["gudang"]:
            print("❌ Gudang tidak ditemukan!")
            return

        gudang_data = db.data["gudang"][id_g]
        gudang_obj = Gudang(id_g, gudang_data["nama"])
        gudang_obj._stok = gudang_data["stok"]

        # ================= TAMBAH =================
        if pilih == "1":
            id_b = input_tidak_kosong("ID Barang: ")
            jumlah = input_angka("Jumlah: ")

            if jumlah <= 0:
                print("❌ Jumlah harus lebih dari 0!")
                return

            gudang_obj.tambah_barang(id_b, jumlah)

        # ================= KURANGI =================
        elif pilih == "2":
            id_b = input_tidak_kosong("ID Barang: ")
            jumlah = input_angka("Jumlah: ")

            if id_b not in gudang_obj._stok:
                print("❌ Barang tidak ada di gudang!")
                return

            if jumlah > gudang_obj._stok[id_b]:
                print(f"❌ Stok tidak cukup! Sisa: {gudang_obj._stok[id_b]}")
                return

            gudang_obj.kurangi_barang(id_b, jumlah)

        # ================= HAPUS (INI YANG KAMU MAU) =================
        elif pilih == "3":
            if not gudang_obj._stok:
                print("❌ Gudang kosong!")
                return

            print("\n=== DAFTAR BARANG DI GUDANG ===")
            daftar_barang = list(gudang_obj._stok.items())

            for i, (id_barang, stok) in enumerate(daftar_barang, 1):
                print(f"{i}. {id_barang} | Stok: {stok}")

            try:
                pilih_hapus = int(input("Pilih nomor barang: ")) - 1

                if pilih_hapus < 0 or pilih_hapus >= len(daftar_barang):
                    print("❌ Nomor tidak valid!")
                    return

                id_hapus = daftar_barang[pilih_hapus][0]

                konfirmasi = input(f"Yakin hapus {id_hapus}? (y/n): ").lower()
                if konfirmasi != "y":
                    print("❌ Dibatalkan")
                    return

                del gudang_obj._stok[id_hapus]

                print(f"✅ Barang {id_hapus} berhasil dihapus!")

            except ValueError:
                print("❌ Input harus angka!")
                return

        # SIMPAN
        db.data["gudang"][id_g]["stok"] = gudang_obj._stok
        db.save()

        print("✅ Perubahan berhasil disimpan!")

    except Exception as e:
        print(f"{Theme.FAIL}❌ {e}{Theme.ENDC}")

    input("\nEnter...")

def distribusi():
    while True:  # 🔥 LOOP UTAMA
        print(f"\n{Theme.OKCYAN}--- PROSES KIRIM BARANG ---{Theme.ENDC}")
        print("Satuan distribusi:")
        print("1. Pcs")
        print("2. Dus")
        print("0. Batal / Keluar")

        pilih_satuan = input("Pilih (1/2/0): ")

        if pilih_satuan == "0":
            print("❌ Distribusi dibatalkan")
            return

        if pilih_satuan not in ["1", "2"]:
            print("❌ Pilihan tidak valid!")
            continue  # 🔥 ulang dari awal

        satuan = "pcs" if pilih_satuan == "1" else "dus"

        id_g = input_tidak_kosong("ID Gudang: ")
        if id_g not in db.data["gudang"]:
            print("❌ Gudang tidak ditemukan!")
            input("Enter...")
            continue  # 🔥 bukan return

        id_b = input_tidak_kosong("ID Barang: ")
        if id_b not in db.data["barang"]:
            print("❌ Barang tidak terdaftar!")
            input("Enter...")
            continue

        id_t = input_tidak_kosong("ID Toko: ")
        if id_t not in db.data["toko"]:
            print("❌ Toko tidak ditemukan!")
            input("Enter...")
            continue

        jumlah_input = input_angka("Jumlah: ")

        kategori = db.data["barang"][id_b]["kategori"]
        jumlah = konversi_ke_pcs(jumlah_input, satuan, kategori)

        stok_gudang = db.data["gudang"][id_g]["stok"]

        if id_b not in stok_gudang:
            print("❌ Barang tidak ada di gudang!")
            input("Enter...")
            continue

        stok_tersedia = stok_gudang[id_b]

        if jumlah <= 0:
            print("❌ Jumlah harus lebih dari 0!")
            input("Enter...")
            continue

        if jumlah > stok_tersedia:
            print(f"❌ Stok tidak cukup!")
            print(f"👉 Stok tersedia: {stok_tersedia}")
            input("Enter...")
            continue

        # ================= PROSES =================
        toko_data = db.data["toko"][id_t]
        toko_obj = Toko(id_t, toko_data["nama"])
        toko_obj._stok = toko_data["stok"]

        stok_gudang[id_b] -= jumlah
        toko_obj.terima_barang(id_b, jumlah)

        db.data["toko"][id_t]["stok"] = toko_obj._stok

        dist = Distribusi(id_b, id_t, jumlah, id_g)
        db.data["distribusi"].append(dist.to_dict())

        db.save()

        print("✅ Distribusi berhasil!")
        input("Enter...")
        return  # keluar kalau sukses1
    


def update_status_distribusi():
    if not db.data["distribusi"]:
        print("❌ Belum ada data distribusi!")
        input("Enter...")
        return

    print("\n=== UPDATE STATUS DISTRIBUSI ===")

    distribusi_list = [Distribusi.from_dict(d) for d in db.data["distribusi"]]

    for i, d in enumerate(distribusi_list):
        print(f"{i+1}. Barang: {d.barang} | Gudang: {d.gudang} | Toko: {d.toko}")

    try:
        pilih = int(input("Pilih nomor: ")) - 1

        if pilih < 0 or pilih >= len(distribusi_list):
            print("❌ Pilihan tidak valid!")
            return

        status = input("Status baru (dikirim/sampai/proses/tertunda): ")

        distribusi_list[pilih].update_status(status)

        db.data["distribusi"] = [d.to_dict() for d in distribusi_list]
        db.save()

        print("✅ Status berhasil diupdate!")

    except Exception as e:
        print("❌ Error:", e)

    input("\nEnter...")


def menu_laporan():
    laporan = Laporan(db.data)

    while True:
        print("\n=== MENU LAPORAN ===")
        print("1. Lihat Semua Laporan")
        print("2. Hapus Riwayat Distribusi")
        print("0. Kembali")

        pilih = input("Pilih: ")

        if pilih == "1":
            laporan.tampilkan_semua()
            input("\nEnter...")

        elif pilih == "2":
            laporan.hapus_riwayat()
            db.save()  # 🔥 WAJIB
            input("\nEnter...")

        elif pilih == "0":
            break

        else:
            print("❌ Pilihan tidak valid!")

def cek_stok_gudang():
    Laporan(db.data).tampilkan_gudang()
    input("\nEnter...")

def cek_stok_toko():
    print("\n--- STOK TOKO ---")
    for id_t, t in db.data["toko"].items():
        print(f"{t['nama']} : {t.get('stok', {})}")
    input("\nEnter...")

def jual_barang():
    id_t = input_tidak_kosong("ID Toko: ")
    id_b = input_tidak_kosong("ID Barang: ")
    jumlah = input_angka("Jumlah: ")

    try:
        toko_data = db.data["toko"][id_t]
        toko_obj = Toko(id_t, toko_data["nama"])
        toko_obj._stok = toko_data["stok"]

        toko_obj.jual_barang(id_b, jumlah)

        db.data["toko"][id_t]["stok"] = toko_obj._stok
        db.save()

    except Exception as e:
        print(f"{Theme.FAIL}❌ {e}{Theme.ENDC}")

    input("\nEnter...")

# ================= MAIN =================

def main():
    Config.display_splash()
    auth_system = Auth(db)

    user_aktif = None
    while not user_aktif:
        user_aktif = auth_system.login()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        user_aktif.tampilkan_welcome()

        akses = user_aktif.akses_menu()
        menu_map = {}

        print(f"{Theme.BOLD}MENU UTAMA:{Theme.ENDC}")

        for i, item in enumerate(akses, 1):
            menu_map[str(i)] = item
            print(f"{i}. {item}")

        pilih = input("Pilih: ")

        if pilih in menu_map:
            aksi = menu_map[pilih]

            if aksi == "keluar":
                auth_system.logout(user_aktif.nama)
                break
            elif aksi == "tambah user":
                tambah_user()
            elif aksi == "tambah barang":
                tambah_barang()
            elif aksi == "tambah gudang":
                tambah_gudang()
            elif aksi == "tambah toko":
                tambah_toko()
            elif aksi == "manajemen stok":
                manajemen_stok()
            elif aksi == "distribusi barang":
                distribusi()
            elif aksi == "laporan lengkap":
                menu_laporan()
            elif aksi == "update status distribusi":
                update_status_distribusi()
            elif aksi == "cek stok gudang":
                cek_stok_gudang()
            elif aksi == "cek stok toko":
                cek_stok_toko()
            elif aksi == "jual barang":
                jual_barang()
        else:
            print("Pilihan tidak valid")
            input("Enter...")

if __name__ == "__main__":
    main()