from kategori import Kategori
from supplier import Supplier
from gudang import Gudang
from toko import Toko

from barang_elektronik import BarangElektronik
from barang_makanan import BarangMakanan
from barang_minuman import BarangMinuman

from admin import Admin
from staff_gudang import StaffGudang
from manajer_distribusi import ManajerDistribusi

from distribusi_reguler import DistribusiReguler
from distribusi_express import DistribusiExpress

from pengiriman import Pengiriman
from laporan import Laporan
from transaksi import Transaksi
from status_barang import StatusBarang


def main():
    print("\n" + "=" * 60)
    print("🚀 SISTEM LOGISTIK LogiX DIMULAI")
    print("=" * 60)

    # =========================
    # MASTER DATA
    # =========================
    kategori1 = Kategori(1, "Elektronik")
    kategori2 = Kategori(2, "Makanan")

    supplier = Supplier(1, "PT Sumber Jaya", "08123456789", "Pekanbaru")

    gudang = Gudang(1, "Gudang Pusat", "Pekanbaru")
    toko = Toko(1, "Toko Cemerlang", "Siak")

    print("\n📦 MASTER DATA\n")
    print(kategori1.tampilkan_info())
    print(kategori2.tampilkan_info())
    print(supplier.tampilkan_info())
    print(gudang.tampilkan_info())
    print(toko.tampilkan_info())

    # =========================
    # USER
    # =========================
    admin = Admin(1, "Admin Utama", "admin01", "admin123")
    staff = StaffGudang(2, "Staff Gudang", "staff01", "staff123")
    manajer = ManajerDistribusi(3, "Manager Distribusi", "manager01", "manager123")

    print("\n👤 DATA USER\n")
    print(admin.tampilkan_info())
    print(staff.tampilkan_info())
    print(manajer.tampilkan_info())

    # =========================
    # BARANG
    # =========================
    barang1 = BarangElektronik(1, "Laptop", 10, 7000000, kategori1, 220, 24)
    barang2 = BarangMakanan(2, "Roti", 50, 15000, kategori2, "2026-04-01")
    barang3 = BarangMinuman(3, "Air Mineral", 100, 5000, kategori2, "baik", "600ml")

    # relasi ke kategori & supplier
    kategori1.tambah_barang(barang1)
    kategori2.tambah_barang(barang2)
    kategori2.tambah_barang(barang3)

    supplier.tambah_barang(barang1)
    supplier.tambah_barang(barang2)
    supplier.tambah_barang(barang3)

    print("\n📦 DATA BARANG\n")
    print(barang1.tampilkan_info())
    print(barang2.tampilkan_info())
    print(barang3.tampilkan_info())

    # =========================
    # MASUK GUDANG (TRANSAKSI MASUK)
    # =========================
    trx1 = Transaksi(1, "masuk", barang1, 10, None, gudang)
    trx2 = Transaksi(2, "masuk", barang2, 50, None, gudang)
    trx3 = Transaksi(3, "masuk", barang3, 100, None, gudang)

    trx1.proses()
    trx2.proses()
    trx3.proses()

    print("\n📥 TRANSAKSI MASUK\n")
    print(trx1.tampilkan_info())
    print(trx2.tampilkan_info())
    print(trx3.tampilkan_info())

    print("\n🏢 DATA GUDANG SETELAH TRANSAKSI\n")
    print(gudang.tampilkan_info())

    # =========================
    # DISTRIBUSI
    # =========================
    distribusi1 = DistribusiReguler(1, barang1, 5, gudang, toko)
    distribusi2 = DistribusiExpress(2, barang2, 10, gudang, toko)

    print("\n🚚 DATA DISTRIBUSI\n")
    print(distribusi1.tampilkan_info())
    print(distribusi2.tampilkan_info())

    # proses distribusi (versi polymorphism)
    distribusi1.proses()
    distribusi1.kirim()
    distribusi1.selesai()

    distribusi2.proses()
    distribusi2.kirim()
    distribusi2.selesai()

    # barang masuk ke toko
    toko.terima_barang(barang1, 5)
    toko.terima_barang(barang2, 10)

    print("\n🏪 DATA TOKO SETELAH DISTRIBUSI\n")
    print(toko.tampilkan_info())

    # =========================
    # PENGIRIMAN
    # =========================
    pengiriman1 = Pengiriman(1, distribusi1, "Bekasi")
    pengiriman1.kirim()
    pengiriman1.selesai()

    print("\n📦 DATA PENGIRIMAN\n")
    print(pengiriman1.tampilkan_info())

    # =========================
    # STATUS BARANG (CLASS TERPISAH)
    # =========================
    status1 = StatusBarang("tersedia")
    status2 = StatusBarang("rusak")

    print("\n📊 STATUS (CLASS STATUS BARANG)\n")
    print(status1.tampilkan_info())
    print(status2.tampilkan_info())

    # update status di barang
    barang1.ubah_status("dikirim")
    barang2.ubah_status("rusak")

    print("\n📊 STATUS DI OBJECT BARANG\n")
    print(barang1.tampilkan_info())
    print(barang2.tampilkan_info())

    # =========================
    # LAPORAN
    # =========================
    laporan = Laporan("Laporan Harian")

    laporan.tambah_barang(barang1)
    laporan.tambah_barang(barang2)
    laporan.tambah_barang(barang3)

    laporan.tambah_distribusi(distribusi1)
    laporan.tambah_distribusi(distribusi2)

    print("\n📊 LAPORAN SISTEM\n")
    print(laporan.tampilkan_laporan())

    print("\n" + "=" * 60)
    print("🎉 SIMULASI SELESAI")
    print("=" * 60)


if __name__ == "__main__":
    main()