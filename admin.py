from user import User


class Admin(User):
    """
    Class Admin sebagai turunan dari User.
    Memiliki akses penuh terhadap seluruh sistem.
    """

    def __init__(self, id_user: str, nama: str, username: str, password: str):
        super().__init__(id_user, nama, username, password)

    # =========================
    # IMPLEMENTASI ABSTRACT METHOD
    # =========================
    def get_role(self):
        return "Admin"

    def get_permissions(self):
        return [
            "kelola_barang",
            "kelola_kategori",
            "kelola_supplier",
            "kelola_gudang",
            "kelola_toko",
            "kelola_transaksi",
            "kelola_distribusi",
            "lihat_laporan"
        ]

    # =========================
    # METHOD KHUSUS ADMIN
    # =========================
    def tambah_user(self, user):
        return f"User {user.get_nama()} berhasil ditambahkan oleh Admin"

    def hapus_user(self, user):
        return f"User {user.get_nama()} berhasil dihapus oleh Admin"

    # =========================
    # POLYMORPHISM (OPTIONAL OVERRIDE)
    # =========================
    def tampilkan_info(self):
        base_info = super().tampilkan_info()

        tambahan = (
            f"║ Akses     : FULL ACCESS     ║\n"
        )

        return base_info.replace(
            "╚══════════════════════════════╝",
            "╠══════════════════════════════╣\n"
            f"{tambahan}"
            "╚══════════════════════════════╝"
        )