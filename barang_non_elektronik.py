from barang import Barang


class BarangNonElektronik(Barang):
    """
    Class turunan dari Barang untuk kategori non-elektronik.
    """

    def __init__(self, id_barang: str, nama: str, stok: int, harga: float, kategori,
                 kondisi: str = "baik"):

        super().__init__(id_barang, nama, stok, harga, kategori)

        self._kondisi = None
        self.set_kondisi(kondisi)

        self.log(f"Barang Non-Elektronik '{self.get_nama()}' dibuat")

    # GETTER
    def get_kondisi(self):
        return self._kondisi

    # SETTER
    def set_kondisi(self, kondisi: str):
        if not isinstance(kondisi, str):
            raise TypeError("Kondisi harus berupa string")

        if kondisi.lower() not in ["baik", "rusak"]:
            raise ValueError("Kondisi harus 'baik' atau 'rusak'")

        self._kondisi = kondisi.lower()
        self._update_timestamp()

    # OUTPUT
    def tampilkan_info(self):
        base_info = super().tampilkan_info()

        tambahan = f"║ Kondisi   : {self._kondisi:<15}║\n"

        return base_info.replace(
            "╚══════════════════════════════╝",
            "╠══════════════════════════════╣\n"
            f"{tambahan}"
            "╚══════════════════════════════╝"
        )