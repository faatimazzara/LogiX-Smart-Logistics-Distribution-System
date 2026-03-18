from barang_non_elektronik import BarangNonElektronik
from datetime import datetime


class BarangMakanan(BarangNonElektronik):
    """
    Class turunan untuk produk makanan.
    """

    def __init__(self, id_barang: str, nama: str, stok: int, harga: float, kategori,
                 tanggal_kadaluarsa: str, kondisi: str = "baik"):

        super().__init__(id_barang, nama, stok, harga, kategori, kondisi)

        self._tanggal_kadaluarsa = None
        self.set_tanggal_kadaluarsa(tanggal_kadaluarsa)

        self.log(f"Barang Makanan '{self.get_nama()}' dibuat")

    # GETTER
    def get_tanggal_kadaluarsa(self):
        return self._tanggal_kadaluarsa.strftime('%Y-%m-%d')

    # SETTER
    def set_tanggal_kadaluarsa(self, tanggal: str):
        try:
            parsed = datetime.strptime(tanggal, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Format tanggal harus YYYY-MM-DD")

        self._tanggal_kadaluarsa = parsed
        self._update_timestamp()

    # LOGIC
    def is_kadaluarsa(self):
        return datetime.now() > self._tanggal_kadaluarsa

    # OUTPUT
    def tampilkan_info(self):
        base_info = super().tampilkan_info()

        status = "YA" if self.is_kadaluarsa() else "TIDAK"

        tambahan = (
            f"║ Expired   : {self.get_tanggal_kadaluarsa():<15}║\n"
            f"║ Kadaluarsa: {status:<15}║\n"
        )

        return base_info.replace(
            "╚══════════════════════════════╝",
            "╠══════════════════════════════╣\n"
            f"{tambahan}"
            "╚══════════════════════════════╝"
        )