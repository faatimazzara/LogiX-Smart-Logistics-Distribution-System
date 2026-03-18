from mixins import LogMixin, TimestampMixin


class Toko(LogMixin, TimestampMixin):
    """
    Class Toko merepresentasikan cabang atau tujuan distribusi barang.
    """

    BOX_WIDTH = 60 

    def __init__(self, id_toko: str, nama: str, lokasi: str):
        super().__init__()

        # atribut private
        self._id_toko = id_toko
        self._nama = None
        self._lokasi = lokasi

        # stok barang di toko
        self._stok_barang = {}

        # setter untuk validasi
        self.set_nama(nama)

        self.log(f"Toko '{self._nama}' berhasil dibuat")

    # =========================
    # GETTER
    # =========================
    def get_id_toko(self):
        return self._id_toko

    def get_nama(self):
        return self._nama

    def get_lokasi(self):
        return self._lokasi

    def get_stok_barang(self):
        return self._stok_barang

    # =========================
    # SETTER
    # =========================
    def set_nama(self, nama: str):
        if not nama:
            raise ValueError("Nama toko tidak boleh kosong")
        self._nama = nama
        self._update_timestamp()

    def set_lokasi(self, lokasi: str):
        self._lokasi = lokasi
        self._update_timestamp()

    # =========================
    # MANAJEMEN STOK TOKO
    # =========================
    def terima_barang(self, barang, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")

        if barang in self._stok_barang:
            self._stok_barang[barang] += jumlah
        else:
            self._stok_barang[barang] = jumlah

        barang.tambah_stok(jumlah)
        self._update_timestamp()
        self.log(f"Toko '{self._nama}' menerima {jumlah} '{barang.get_nama()}'")

    def jual_barang(self, barang, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")

        if barang not in self._stok_barang:
            raise ValueError("Barang tidak tersedia di toko")

        if jumlah > self._stok_barang[barang]:
            raise ValueError("Stok tidak mencukupi")

        self._stok_barang[barang] -= jumlah

        if self._stok_barang[barang] == 0:
            del self._stok_barang[barang]

        barang.kurangi_stok(jumlah)
        self._update_timestamp()
        self.log(f"Toko '{self._nama}' menjual {jumlah} '{barang.get_nama()}'")

    def cek_stok(self, barang):
        return self._stok_barang.get(barang, 0)

    # =========================
    # FORMAT HELPER
    # =========================
    def _line(self, label, value):
        content_width = self.BOX_WIDTH - 4
        text = f"{label:<12}: {str(value)}"
        return f"║ {text:<{content_width}} ║\n"

    def _barang_line(self, text):
        content_width = self.BOX_WIDTH - 4
        return f"║ {text:<{content_width}} ║\n"

    # =========================
    # OUTPUT TERMINAL 
    # =========================
    def tampilkan_info(self):
        total_item = len(self._stok_barang)

        top = "╔" + "═" * (self.BOX_WIDTH - 2) + "╗\n"
        mid = "╠" + "═" * (self.BOX_WIDTH - 2) + "╣\n"
        bot = "╚" + "═" * (self.BOX_WIDTH - 2) + "╝\n"

        title = "INFORMASI TOKO"
        title_line = f"║ {title:^{self.BOX_WIDTH-4}} ║\n"

        # daftar barang rapi di dalam box
        detail_barang = ""
        if self._stok_barang:
            for barang, jumlah in self._stok_barang.items():
                detail_barang += self._barang_line(
                    f"- {barang.get_nama()} ({jumlah})"
                )
        else:
            detail_barang += self._barang_line("(Belum ada barang)")

        return (
            "\n"
            + top
            + title_line
            + mid
            + self._line("ID", self._id_toko)
            + self._line("Nama", self._nama)
            + self._line("Lokasi", self._lokasi)
            + self._line("Total Item", total_item)
            + mid
            + self._barang_line("Stok Barang:")
            + detail_barang
            + mid
            + self._line("Dibuat", self.get_created_at())
            + self._line("Update", self.get_updated_at())
            + bot
        )