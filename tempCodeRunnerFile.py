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


def main():
    print("\n" + "=" * 50)
    print("🚀 SISTEM LOGISTIK LogiX DIMULAI")
    print("=" * 50)

    # MASTER DATA
    kategori1 = Kategori(1, "Elektronik")
    kategori2 = Kategori(2, "Makanan")

    supplier = Supplier(1, "PT Sumber Jaya", "08123456789", "Jakarta")

    gudang = Gudang(1, "Gudang Pusat", "Jakarta")
    toko = Toko(1, "Toko Cabang A", "Bekasi")

    print("\n📦 MASTER DATA SIAP\n")

    # USER
    admin = Admin(1, "Admin Utama", "admin01", "admin123")
    staff = StaffGudang(2, "Staff Gudang", "staff01", "staff123")
    manajer = ManajerDistribusi(3, "Manager Distribusi", "manager01", "manager123")

    print("👤 USER SYSTEM SIAP\n")

    # BARANG
    barang1 = BarangElektronik(1, "Laptop", 10, 7000000, kategori1, 220, 24)

    barang2 = BarangMakanan(
        2,
        "Roti",
        50,
        15000,
        kategori2,
        "2026-04-01"
    )

    barang3 = BarangMinuman(
        3,
        "Air Mineral",
        100,
        5000,
        kategori2,
        "baik",
        "600ml"
    )

    # =========================
    # MASUK GUDANG 
    # =========================
    gudang.tambah_barang(barang1, barang1.get_stok())
    gudang.tambah_barang(barang2, barang2.get_stok())
    gudang.tambah_barang(barang3, barang3.get_stok())

    print("📦 BARANG MASUK KE GUDANG\n")
    print(barang1.tampilkan_info())
    print(barang2.tampilkan_info())
    print(barang3.tampilkan_info())

    # DISTRIBUSI
    distribusi1 = DistribusiReguler(1, barang1, 5, gudang, toko)
    distribusi2 = DistribusiExpress(2, barang2, 10, gudang, toko)

    print("\n🚚 DISTRIBUSI DIBUAT\n")
    print(distribusi1.tampilkan_info())
    print(distribusi2.tampilkan_info())

    # PROSES
    distribusi1.proses()
    distribusi1.kirim()
    distribusi1.selesai()

    distribusi2.proses()
    distribusi2.kirim()
    distribusi2.selesai()

    print("\n✅ DISTRIBUSI SELESAI\n")

    # PENGIRIMAN
    pengiriman1 = Pengiriman(1, "Bekasi", "2026-03-18")

    print("📦 DATA PENGIRIMAN\n")
    print(pengiriman1.tampilkan_info())

    # STATUS
    barang1.ubah_status("dikirim")
    barang2.ubah_status("rusak")

    print("\n📊 STATUS BARANG\n")
    print(barang1.tampilkan_info())
    print(barang2.tampilkan_info())

    # LAPORAN
    laporan = Laporan("Laporan Harian")

    laporan.tambah_barang(barang1)
    laporan.tambah_barang(barang2)
    laporan.tambah_barang(barang3)

    laporan.tambah_distribusi(distribusi1)
    laporan.tambah_distribusi(distribusi2)

    print("\n📊 LAPORAN SISTEM\n")
    print(laporan.tampilkan_laporan())

    print("\n" + "=" * 50)
    print("🎉 SIMULASI SELESAI")
    print("=" * 50)


if __name__ == "__main__":
    main()