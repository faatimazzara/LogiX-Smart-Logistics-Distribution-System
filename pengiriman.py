from datetime import datetime


class Pengiriman:
    """
    Class untuk menangani detail pengiriman barang.
    """

    BOX_WIDTH = 50 

    def __init__(self, id_pengiriman: str, distribusi=None, alamat_tujuan: str = "-"):
        self._id_pengiriman = id_pengiriman
        self._distribusi = distribusi
        self._alamat_tujuan = alamat_tujuan
        self._waktu_kirim = None
        self._waktu_sampai = None
        self._status = "menunggu"

    # =========================
    # GETTER
    # =========================
    def get_id_pengiriman(self):
        return self._id_pengiriman

    def get_status(self):
        return self._status

    def get_alamat(self):
        return self._alamat_tujuan

    # =========================
    # PROSES PENGIRIMAN
    # =========================
    def kirim(self):
        if self._status != "menunggu":
            raise ValueError("Pengiriman sudah diproses")

        self._waktu_kirim = datetime.now()
        self._status = "dikirim"

        if self._distribusi and hasattr(self._distribusi, "set_status"):
            self._distribusi.set_status("dikirim")

    def selesai(self):
        if self._status != "dikirim":
            raise ValueError("Pengiriman belum dikirim")

        self._waktu_sampai = datetime.now()
        self._status = "sampai"

        if self._distribusi and hasattr(self._distribusi, "set_status"):
            self._distribusi.set_status("selesai")

    # =========================
    # HELPER AMAN
    # =========================
    def _get_nama_barang(self):
        """
        Mengambil nama barang secara aman.
        """
        if self._distribusi and hasattr(self._distribusi, "get_barang"):
            barang = self._distribusi.get_barang()
            if hasattr(barang, "get_nama"):
                return barang.get_nama()

        return "-"

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

        waktu_kirim = (
            self._waktu_kirim.strftime("%Y-%m-%d %H:%M:%S")
            if self._waktu_kirim else "-"
        )

        waktu_sampai = (
            self._waktu_sampai.strftime("%Y-%m-%d %H:%M:%S")
            if self._waktu_sampai else "-"
        )

        nama_barang = self._get_nama_barang()

        top = "╔" + "═" * (self.BOX_WIDTH - 2) + "╗\n"
        mid = "╠" + "═" * (self.BOX_WIDTH - 2) + "╣\n"
        bot = "╚" + "═" * (self.BOX_WIDTH - 2) + "╝\n"

        title = "INFORMASI PENGIRIMAN"
        title_line = f"║ {title:^{self.BOX_WIDTH-4}} ║\n"

        return (
            top
            + title_line
            + mid
            + self._line("ID", self._id_pengiriman)
            + self._line("Barang", nama_barang)
            + self._line("Tujuan", self._alamat_tujuan)
            + self._line("Status", self._status)
            + self._line("Kirim", waktu_kirim)
            + self._line("Sampai", waktu_sampai)
            + bot
        )