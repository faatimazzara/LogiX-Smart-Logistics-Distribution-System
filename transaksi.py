from mixins import LogMixin, TimestampMixin
from datetime import datetime


class Transaksi(LogMixin, TimestampMixin):
    """
    Class Transaksi mencatat aktivitas keluar/masuk barang.
    """

    BOX_WIDTH = 60  

    def __init__(self, id_transaksi: str, jenis: str, barang, jumlah: int, sumber=None, tujuan=None):
        super().__init__()

        # atribut private
        self._id_transaksi = id_transaksi
        self._jenis = None
        self._barang = barang
        self._jumlah = 0
        self._sumber = sumber
        self._tujuan = tujuan
        self._tanggal = datetime.now()

        self.set_jenis(jenis)
        self.set_jumlah(jumlah)

        self.log(f"Transaksi '{self._id_transaksi}' dibuat")

    # =========================
    # GETTER
    # =========================
    def get_id_transaksi(self):
        return self._id_transaksi

    def get_jenis(self):
        return self._jenis

    def get_barang(self):
        return self._barang

    def get_jumlah(self):
        return self._jumlah

    def get_sumber(self):
        return self._sumber

    def get_tujuan(self):
        return self._tujuan

    def get_tanggal(self):
        return self._tanggal.strftime('%Y-%m-%d %H:%M:%S')

    # =========================
    # SETTER
    # =========================
    def set_jenis(self, jenis: str):
        if jenis not in ["masuk", "keluar"]:
            raise ValueError("Jenis transaksi harus 'masuk' atau 'keluar'")
        self._jenis = jenis
        self._update_timestamp()

    def set_jumlah(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self._jumlah = jumlah
        self._update_timestamp()

    # =========================
    # PROSES TRANSAKSI
    # =========================
    def proses(self):

        if self._jenis == "masuk":
            if self._tujuan:
                self._tujuan.tambah_barang(self._barang, self._jumlah)
                self.log(f"Transaksi MASUK: {self._jumlah} '{self._barang.get_nama()}' ke tujuan")

        elif self._jenis == "keluar":
            if self._sumber and self._tujuan:
                self._sumber.kurangi_barang(self._barang, self._jumlah)
                self._tujuan.terima_barang(self._barang, self._jumlah)
                self.log(f"Transaksi KELUAR: {self._jumlah} '{self._barang.get_nama()}' dikirim")

        self._update_timestamp()

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

        top = "╔" + "═" * (self.BOX_WIDTH - 2) + "╗\n"
        mid = "╠" + "═" * (self.BOX_WIDTH - 2) + "╣\n"
        bot = "╚" + "═" * (self.BOX_WIDTH - 2) + "╝\n"

        title = "DATA TRANSAKSI"
        title_line = f"║ {title:^{self.BOX_WIDTH-4}} ║\n"

        sumber = getattr(self._sumber, "get_nama", lambda: "-")()
        tujuan = getattr(self._tujuan, "get_nama", lambda: "-")()

        return (
            "\n"
            + top
            + title_line
            + mid
            + self._line("ID", self._id_transaksi)
            + self._line("Jenis", self._jenis)
            + self._line("Barang", self._barang.get_nama())
            + self._line("Jumlah", self._jumlah)
            + self._line("Tanggal", self.get_tanggal())
            + mid
            + self._line("Sumber", sumber)
            + self._line("Tujuan", tujuan)
            + mid
            + self._line("Dibuat", self.get_created_at())
            + self._line("Update", self.get_updated_at())
            + bot
        )