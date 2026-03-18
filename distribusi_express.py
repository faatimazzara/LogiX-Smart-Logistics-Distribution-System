from distribusi_base import DistribusiBase


class DistribusiExpress(DistribusiBase):
    """
    Distribusi cepat:
    - Biaya lebih mahal
    - Waktu lebih singkat
    """

    def __init__(self, id_distribusi: str, barang, jumlah: int, gudang_asal, toko_tujuan):
        super().__init__(id_distribusi, barang, jumlah, gudang_asal, toko_tujuan)

    # =========================
    # LOGGER 
    # =========================
    def log(self, pesan: str):
        print(f"[LOG] {pesan}")

    # =========================
    # FLOW DISTRIBUSI
    # =========================
    def proses(self):
        self._status = "diproses"
        self.log(f"Distribusi EXPRESS {self._id_distribusi} sedang diproses")

    def kirim(self):
        self._status = "dikirim"
        self.log(f"Distribusi EXPRESS {self._id_distribusi} sedang dikirim")

    def selesai(self):
        self._status = "selesai"
        self.log(f"Distribusi EXPRESS {self._id_distribusi} selesai")

    # =========================
    # IMPLEMENTASI ABSTRACT METHOD
    # =========================
    def hitung_biaya(self):
        """
        Biaya express:
        Rp 2.500 per item
        """
        return self._jumlah * 2500

    def estimasi_waktu(self):
        """
        Estimasi waktu express:
        1 hari (same day / next day)
        """
        return "1 hari"

    # =========================
    # METHOD TAMBAHAN (VALUE EXTRA)
    # =========================
    def prioritas_pengiriman(self):
        return "PRIORITAS TINGGI"

    # =========================
    # POLYMORPHISM (OVERRIDE)
    # =========================
    def tampilkan_info(self):
        base_info = super().tampilkan_info()

        biaya_format = f"{self.hitung_biaya():,}"

        tambahan = (
            f"║ Jenis     : Express         ║\n"
            f"║ Biaya     : Rp {biaya_format:<10}║\n"
            f"║ Estimasi  : {self.estimasi_waktu():<15}║\n"
            f"║ Prioritas : {self.prioritas_pengiriman():<15}║\n"
        )

        return base_info.replace(
            "╚══════════════════════════════╝",
            "╠══════════════════════════════╣\n"
            f"{tambahan}"
            "╚══════════════════════════════╝"
        )