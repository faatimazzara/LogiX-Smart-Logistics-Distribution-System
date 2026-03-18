from mixins import LogMixin, TimestampMixin


class Barang(LogMixin, TimestampMixin):

    def __init__(self, id_barang: str, nama: str, stok: int, harga: float, kategori):
        super().__init__()

        self._id_barang = id_barang
        self._nama = None
        self._stok = 0
        self._harga = 0.0
        self._kategori = kategori
        self._status = "tersedia"

        self.set_nama(nama)
        self.set_stok(stok)
        self.set_harga(harga)

        self.log(f"Barang '{self._nama}' berhasil dibuat")

    # =========================
    # GETTER
    # =========================
    def get_id_barang(self): return self._id_barang
    def get_nama(self): return self._nama
    def get_stok(self): return self._stok
    def get_harga(self): return self._harga
    def get_kategori(self): return self._kategori
    def get_status(self): return self._status

    # =========================
    # SETTER
    # =========================
    def set_nama(self, nama: str):
        if not nama:
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nama
        self._update_timestamp()

    def set_stok(self, stok: int):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        self._stok = stok
        self._update_timestamp()

    def set_harga(self, harga: float):
        if harga <= 0:
            raise ValueError("Harga harus lebih dari 0")
        self._harga = harga
        self._update_timestamp()

    def set_kategori(self, kategori):
        self._kategori = kategori
        self._update_timestamp()

    # =========================
    # METHOD
    # =========================
    def tambah_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self.set_stok(self._stok + jumlah)
        self.log(f"Stok '{self._nama}' bertambah {jumlah}")

    def kurangi_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        if jumlah > self._stok:
            raise ValueError("Stok tidak mencukupi")
        self.set_stok(self._stok - jumlah)
        self.log(f"Stok '{self._nama}' berkurang {jumlah}")

    def ubah_status(self, status: str):
        self._status = status
        self._update_timestamp()
        self.log(f"Status '{self._nama}' menjadi {status}")

    # =========================
    # OUTPUT 
    # =========================
    def tampilkan_info(self):
        kategori_nama = (
            self._kategori.get_nama()
            if hasattr(self._kategori, "get_nama")
            else str(self._kategori)
        )

        harga_format = f"{self._harga:,.0f}"

        # =========================
        # TABEL 
        # =========================
        WIDTH = 40

        def border(char_left, char_mid, char_right):
            return f"{char_left}{char_mid * (WIDTH + 2)}{char_right}\n"

        def row(label, value):
            text = f"{label:<12}: {value}"
            return f"║ {text.ljust(WIDTH)} ║\n"

        title = "INFORMASI BARANG".center(WIDTH)

        return (
            "\n"
            + border("╔", "═", "╗")
            + f"║ {title} ║\n"
            + border("╠", "═", "╣")
            + row("ID", self._id_barang)
            + row("Nama", self._nama)
            + row("Kategori", kategori_nama)
            + row("Stok", self._stok)
            + row("Harga", f"Rp {harga_format}")
            + row("Status", self._status)
            + border("╠", "═", "╣")
            + row("Dibuat", self.get_created_at())
            + row("Update", self.get_updated_at())
            + border("╚", "═", "╝")
        )