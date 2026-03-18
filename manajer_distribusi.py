from user import User


class ManajerDistribusi(User):
    """
    Class ManajerDistribusi sebagai turunan dari User.
    Bertugas melakukan monitoring distribusi dan analisis laporan.
    """

    def __init__(self, id_user: str, nama: str, username: str, password: str):
        super().__init__(id_user, nama, username, password)

    # =========================
    # IMPLEMENTASI ABSTRACT METHOD
    # =========================
    def get_role(self):
        return "Manajer Distribusi"

    def get_permissions(self):
        return [
            "lihat_barang",
            "lihat_transaksi",
            "lihat_distribusi",
            "lihat_laporan"
        ]

    # =========================
    # METHOD KHUSUS MANAJER
    # =========================
    def lihat_laporan(self, laporan):
        return laporan.generate_ringkasan()

    def monitor_distribusi(self, distribusi):
        return distribusi.get_status()

    def analisis_stok(self, gudang):
        return f"Total jenis barang di gudang: {len(gudang.get_daftar_barang())}"

    # =========================
    # POLYMORPHISM (OVERRIDE)
    # =========================
    def tampilkan_info(self):
        base_info = super().tampilkan_info()

        tambahan = (
            f"║ Akses     : MONITORING      ║\n"
        )

        return base_info.replace(
            "╚══════════════════════════════╝",
            "╠══════════════════════════════╣\n"
            f"{tambahan}"
            "╚══════════════════════════════╝"
        )