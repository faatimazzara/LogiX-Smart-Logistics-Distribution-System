from distribusi_base import DistribusiBase


class DistribusiReguler(DistribusiBase):
    """
    Distribusi standar:
    - Biaya lebih murah
    - Waktu lebih lama
    """

    def __init__(self, id_distribusi: str, barang, jumlah: int, gudang_asal, toko_tujuan):
        super().__init__(id_distribusi, barang, jumlah, gudang_asal, toko_tujuan)

    # =========================
    # LOGGER 
    # =========================
    def log(self, pesan: str):
        """
        Method log sederhana agar tidak error.
        Bisa dioverride nanti jika ada sistem logging.
        """
        print(f"[LOG] {pesan}")

    # =========================
    # FLOW DISTRIBUSI
    # =========================
    def proses(self):
        self._status = "diproses"
        self.log(f"Distribusi {self._id_distribusi} sedang diproses")

    def kirim(self):
        self._status = "dikirim"
        self.log(f"Distribusi {self._id_distribusi} sedang dikirim")

    def selesai(self):
        self._status = "selesai"
        self.log(f"Distribusi {self._id_distribusi} selesai")

    # =========================
    # IMPLEMENTASI ABSTRACT METHOD
    # =========================
    def hitung_biaya(self):
        return self._jumlah * 1000

    def estimasi_waktu(self):
        return "2-4 hari"

    # =========================
    # POLYMORPHISM (OVERRIDE)
    # =========================
    def tampilkan_info(self):
        base_info = super().tampilkan_info()

        biaya_format = f"{self.hitung_biaya():,}"

        tambahan = (
            f"║ Jenis     : Reguler         ║\n"
            f"║ Biaya     : Rp {biaya_format:<10}║\n"
            f"║ Estimasi  : {self.estimasi_waktu():<15}║\n"
        )

        return base_info.replace(
            "╚══════════════════════════════╝",
            "╠══════════════════════════════╣\n"
            f"{tambahan}"
            "╚══════════════════════════════╝"
        )