from mixins import LogMixin, TimestampMixin


class Supplier(LogMixin, TimestampMixin):
    """
    Class Supplier merepresentasikan pemasok barang ke dalam sistem.
    """

    BOX_WIDTH = 60  

    def __init__(self, id_supplier: str, nama: str, kontak: str, alamat: str):
        super().__init__()

        # atribut private
        self._id_supplier = id_supplier
        self._nama = None
        self._kontak = None
        self._alamat = alamat

        # relasi ke barang
        self._daftar_barang = []

        # gunakan setter (hindari duplikasi validasi)
        self.set_nama(nama)
        self.set_kontak(kontak)

        self.log(f"Supplier '{self._nama}' berhasil dibuat")

    # =========================
    # GETTER
    # =========================
    def get_id_supplier(self):
        return self._id_supplier

    def get_nama(self):
        return self._nama

    def get_kontak(self):
        return self._kontak

    def get_alamat(self):
        return self._alamat

    def get_daftar_barang(self):
        return self._daftar_barang

    # =========================
    # SETTER
    # =========================
    def set_nama(self, nama: str):
        if not nama:
            raise ValueError("Nama supplier tidak boleh kosong")
        self._nama = nama
        self._update_timestamp()

    def set_kontak(self, kontak: str):
        if not kontak:
            raise ValueError("Kontak tidak boleh kosong")
        self._kontak = kontak
        self._update_timestamp()

    def set_alamat(self, alamat: str):
        self._alamat = alamat
        self._update_timestamp()

    # =========================
    # RELASI DENGAN BARANG
    # =========================
    def tambah_barang(self, barang):
        if barang not in self._daftar_barang:
            self._daftar_barang.append(barang)
            self._update_timestamp()
            self.log(
                f"Barang '{barang.get_nama()}' ditambahkan ke supplier '{self._nama}'"
            )

    def hapus_barang(self, barang):
        if barang in self._daftar_barang:
            self._daftar_barang.remove(barang)
            self._update_timestamp()
            self.log(
                f"Barang '{barang.get_nama()}' dihapus dari supplier '{self._nama}'"
            )

    # =========================
    # FORMAT HELPER
    # =========================
    def _line(self, label, value):
        content_width = self.BOX_WIDTH - 4
        text = f"{label:<12}: {str(value)}"
        return f"║ {text:<{content_width}} ║\n"

    # =========================
    # OUTPUT TERMINAL 
    # =========================
    def tampilkan_info(self):
        jumlah_barang = len(self._daftar_barang)

        top = "╔" + "═" * (self.BOX_WIDTH - 2) + "╗\n"
        mid = "╠" + "═" * (self.BOX_WIDTH - 2) + "╣\n"
        bot = "╚" + "═" * (self.BOX_WIDTH - 2) + "╝\n"

        title = "INFORMASI SUPPLIER"
        title_line = f"║ {title:^{self.BOX_WIDTH-4}} ║\n"

        return (
            "\n"
            + top
            + title_line
            + mid
            + self._line("ID", self._id_supplier)
            + self._line("Nama", self._nama)
            + self._line("Kontak", self._kontak)
            + self._line("Alamat", self._alamat)
            + self._line("Barang", jumlah_barang)
            + mid
            + self._line("Dibuat", self.get_created_at())
            + self._line("Update", self.get_updated_at())
            + bot
        )