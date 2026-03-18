from barang_non_elektronik import BarangNonElektronik


class BarangMinuman(BarangNonElektronik):
    """
    Class turunan untuk produk minuman.
    """

    def __init__(self, id_barang: str, nama: str, stok: int, harga: float, kategori,
                 kondisi: str, volume):
        super().__init__(id_barang, nama, stok, harga, kategori, kondisi)

        self._volume = None
        self.set_volume(volume)

        self.log(f"Barang Minuman '{self.get_nama()}' dibuat")

    # =========================
    # GETTER
    # =========================
    def get_volume(self):
        return self._volume

    # =========================
    # SETTER
    # =========================
    def set_volume(self, volume):
        # kalau string: "600ml" / "1.5L"
        if isinstance(volume, str):
            volume = volume.lower().replace(" ", "")

            if "ml" in volume:
                volume = float(volume.replace("ml", ""))
            elif "l" in volume:
                volume = float(volume.replace("l", "")) * 1000
            else:
                raise ValueError("Format volume tidak dikenali (gunakan ml atau L)")

        # validasi
        if volume <= 0:
            raise ValueError("Volume harus lebih dari 0")

        self._volume = float(volume)
        self._update_timestamp()

    # =========================
    # FORMAT OUTPUT
    # =========================
    def get_satuan_volume(self):
        if self._volume >= 1000:
            return f"{self._volume / 1000:.2f} L"
        return f"{int(self._volume)} ml"

    # =========================
    # OUTPUT
    # =========================
    def tampilkan_info(self):
        base_info = super().tampilkan_info()

        tambahan = f"║ Volume    : {self.get_satuan_volume():<15}║\n"

        return base_info.replace(
            "╚══════════════════════════════╝",
            "╠══════════════════════════════╣\n"
            f"{tambahan}"
            "╚══════════════════════════════╝"
        )