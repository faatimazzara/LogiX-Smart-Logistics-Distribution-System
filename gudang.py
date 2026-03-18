from mixins import LogMixin, TimestampMixin


class Gudang(LogMixin, TimestampMixin):
    """
    Class Gudang merepresentasikan tempat penyimpanan barang.
    Mengelola stok barang secara terpusat.
    """

    def __init__(self, id_gudang: str, nama: str, lokasi: str):
        super().__init__()

        self._id_gudang = id_gudang
        self._nama = None
        self._lokasi = lokasi

        # dictionary barang -> jumlah
        self._stok_barang = {}

        self.set_nama(nama)

        self.log(f"Gudang '{self._nama}' berhasil dibuat")

    # =========================
    # GETTER
    # =========================
    def get_id_gudang(self):
        return self._id_gudang

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
            raise ValueError("Nama gudang tidak boleh kosong")
        self._nama = nama
        self._update_timestamp()

    def set_lokasi(self, lokasi: str):
        self._lokasi = lokasi
        self._update_timestamp()

    # =========================
    # MANAJEMEN STOK
    # =========================
    def tambah_barang(self, barang, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")

        if barang in self._stok_barang:
            self._stok_barang[barang] += jumlah
        else:
            self._stok_barang[barang] = jumlah

        barang.tambah_stok(jumlah)
        self._update_timestamp()
        self.log(f"Tambah {jumlah} '{barang.get_nama()}' ke gudang '{self._nama}'")

    def kurangi_barang(self, barang, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")

        if barang not in self._stok_barang:
            raise ValueError("Barang tidak ditemukan di gudang")

        if jumlah > self._stok_barang[barang]:
            raise ValueError("Stok gudang tidak mencukupi")

        self._stok_barang[barang] -= jumlah

        if self._stok_barang[barang] == 0:
            del self._stok_barang[barang]

        barang.kurangi_stok(jumlah)
        self._update_timestamp()
        self.log(f"Kurangi {jumlah} '{barang.get_nama()}' dari gudang '{self._nama}'")

    def cek_stok(self, barang):
        return self._stok_barang.get(barang, 0)

    # =========================
    # OUTPUT 
    # =========================
    def tampilkan_info(self):

        WIDTH = 40

        def border(left, mid, right):
            return f"{left}{mid * (WIDTH + 2)}{right}\n"

        def row(label, value):
            text = f"{label:<12}: {value}"
            return f"║ {text.ljust(WIDTH)} ║\n"

        def row_text(text):
            return f"║ {text.ljust(WIDTH)} ║\n"

        title = "INFORMASI GUDANG".center(WIDTH)

        total_item = len(self._stok_barang)

        # =========================
        # DAFTAR BARANG
        # =========================
        barang_rows = ""

        if not self._stok_barang:
            barang_rows += row_text("(Belum ada barang)")
        else:
            for barang, jumlah in self._stok_barang.items():
                teks = f"- {barang.get_nama()} ({jumlah})"
                barang_rows += row_text(teks)

        return (
            "\n"
            + border("╔", "═", "╗")
            + f"║ {title} ║\n"
            + border("╠", "═", "╣")
            + row("ID", self._id_gudang)
            + row("Nama", self._nama)
            + row("Lokasi", self._lokasi)
            + row("Total Item", total_item)
            + border("╠", "═", "╣")
            + row_text("Daftar Barang:")
            + barang_rows
            + border("╠", "═", "╣")
            + row("Dibuat", self.get_created_at())
            + row("Update", self.get_updated_at())
            + border("╚", "═", "╝")
        )