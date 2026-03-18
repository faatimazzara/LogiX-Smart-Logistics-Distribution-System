from mixins import LogMixin, TimestampMixin


class Kategori(LogMixin, TimestampMixin):
    """
    Class Kategori digunakan untuk mengelompokkan barang berdasarkan jenisnya.
    """

    BOX_WIDTH = 50  

    def __init__(self, id_kategori: str, nama: str, deskripsi: str = ""):
        super().__init__()

        # atribut private
        self._id_kategori = id_kategori
        self._nama = None
        self._deskripsi = deskripsi

        # gunakan setter (hindari duplikasi validasi)
        self.set_nama(nama)

        # relasi ke barang (aggregation)
        self._daftar_barang = []

        self.log(f"Kategori '{self._nama}' berhasil dibuat")

    # =========================
    # GETTER
    # =========================
    def get_id_kategori(self):
        return self._id_kategori

    def get_nama(self):
        return self._nama

    def get_deskripsi(self):
        return self._deskripsi

    def get_daftar_barang(self):
        return self._daftar_barang

    # =========================
    # SETTER
    # =========================
    def set_nama(self, nama: str):
        if not nama:
            raise ValueError("Nama kategori tidak boleh kosong")
        self._nama = nama
        self._update_timestamp()

    def set_deskripsi(self, deskripsi: str):
        self._deskripsi = deskripsi
        self._update_timestamp()

    # =========================
    # RELASI DENGAN BARANG
    # =========================
    def tambah_barang(self, barang):
        if barang not in self._daftar_barang:
            self._daftar_barang.append(barang)
            self._update_timestamp()
            self.log(
                f"Barang '{barang.get_nama()}' ditambahkan ke kategori '{self._nama}'"
            )

    def hapus_barang(self, barang):
        if barang in self._daftar_barang:
            self._daftar_barang.remove(barang)
            self._update_timestamp()
            self.log(
                f"Barang '{barang.get_nama()}' dihapus dari kategori '{self._nama}'"
            )

    # =========================
    # FORMAT HELPER
    # =========================
    def _line(self, label, value):
        content_width = self.BOX_WIDTH - 4
        text = f"{label:<10}: {str(value)}"
        return f"║ {text:<{content_width}} ║\n"

    # =========================
    # OUTPUT TERMINAL
    # =========================
    def tampilkan_info(self):
        jumlah_barang = len(self._daftar_barang)

        top = "╔" + "═" * (self.BOX_WIDTH - 2) + "╗\n"
        mid = "╠" + "═" * (self.BOX_WIDTH - 2) + "╣\n"
        bot = "╚" + "═" * (self.BOX_WIDTH - 2) + "╝\n"

        title = "INFORMASI KATEGORI"
        title_line = f"║ {title:^{self.BOX_WIDTH-4}} ║\n"

        return (
            "\n"
            + top
            + title_line
            + mid
            + self._line("ID", self._id_kategori)
            + self._line("Nama", self._nama)
            + self._line("Deskripsi", self._deskripsi)
            + self._line("Jumlah", jumlah_barang)
            + mid
            + self._line("Dibuat", self.get_created_at())
            + self._line("Update", self.get_updated_at())
            + bot
        )