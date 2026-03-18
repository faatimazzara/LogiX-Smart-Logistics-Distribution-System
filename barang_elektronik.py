from barang import Barang


class BarangElektronik(Barang):

    def __init__(self, id_barang: str, nama: str, stok: int, harga: float, kategori,
                 daya: int, garansi: int):

        super().__init__(id_barang, nama, stok, harga, kategori)

        self._daya = 0
        self._garansi = 0

        self.set_daya(daya)
        self.set_garansi(garansi)

        self.log(f"Barang Elektronik '{self.get_nama()}' dibuat")

    def get_daya(self): return self._daya
    def get_garansi(self): return self._garansi

    def set_daya(self, daya: int):
        if daya <= 0:
            raise ValueError("Daya harus lebih dari 0 watt")
        self._daya = daya
        self._update_timestamp()

    def set_garansi(self, garansi: int):
        if garansi < 0:
            raise ValueError("Garansi tidak boleh negatif")
        self._garansi = garansi
        self._update_timestamp()

    def tampilkan_info(self):
        base_info = super().tampilkan_info()

        tambahan = (
            f"║ Daya      : {self._daya:<15}║\n"
            f"║ Garansi   : {str(self._garansi) + ' bulan':<15}║\n"
        )

        return base_info.replace(
            "╚══════════════════════════════╝",
            "╠══════════════════════════════╣\n"
            f"{tambahan}"
            "╚══════════════════════════════╝"
        )