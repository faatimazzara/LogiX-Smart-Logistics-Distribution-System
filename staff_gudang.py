from user import User


class StaffGudang(User):
    """
    Class StaffGudang sebagai turunan dari User.
    Bertugas mengelola stok barang dan distribusi.
    """

    def __init__(self, id_user: str, nama: str, username: str, password: str):
        super().__init__(id_user, nama, username, password)

    # =========================
    # IMPLEMENTASI ABSTRACT METHOD
    # =========================
    def get_role(self):
        return "Staff Gudang"

    def get_permissions(self):
        return [
            "lihat_barang",
            "update_stok",
            "kelola_transaksi",
            "proses_distribusi"
        ]

    # =========================
    # METHOD KHUSUS STAFF
    # =========================
    def tambah_stok(self, barang, jumlah):
        barang.tambah_stok(jumlah)
        return f"Stok {barang.get_nama()} ditambah {jumlah}"

    def kurangi_stok(self, barang, jumlah):
        barang.kurangi_stok(jumlah)
        return f"Stok {barang.get_nama()} dikurangi {jumlah}"

    def cek_stok(self, barang):
        return f"Stok {barang.get_nama()} saat ini: {barang.get_stok()}"

    # =========================
    # POLYMORPHISM (OVERRIDE)
    # =========================
    def tampilkan_info(self):
        base_info = super().tampilkan_info()

        tambahan = (
            f"║ Akses     : TERBATAS        ║\n"
        )

        return base_info.replace(
            "╚══════════════════════════════╝",
            "╠══════════════════════════════╣\n"
            f"{tambahan}"
            "╚══════════════════════════════╝"
        )