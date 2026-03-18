from abc import ABC, abstractmethod
from datetime import datetime


class DistribusiBase(ABC):
    """
    Abstract Base Class untuk sistem distribusi.
    Menjadi template untuk DistribusiReguler dan DistribusiExpress.
    """

    def __init__(self, id_distribusi: str, barang, jumlah: int, gudang_asal, toko_tujuan):
        self._id_distribusi = id_distribusi
        self._barang = barang
        self._jumlah = jumlah
        self._gudang_asal = gudang_asal
        self._toko_tujuan = toko_tujuan
        self._tanggal = datetime.now()
        self._status = "diproses"

    # =========================
    # GETTER
    # =========================
    def get_id_distribusi(self):
        return self._id_distribusi

    def get_barang(self):
        return self._barang

    def get_jumlah(self):
        return self._jumlah

    def get_status(self):
        return self._status

    def get_tanggal(self):
        return self._tanggal.strftime("%Y-%m-%d %H:%M:%S")

    # =========================
    # SETTER TERBATAS
    # =========================
    def set_status(self, status: str):
        if status.lower() not in ["diproses", "dikirim", "selesai"]:
            raise ValueError("Status tidak valid")
        self._status = status.lower()

    # =========================
    # ABSTRACT METHOD
    # =========================
    @abstractmethod
    def hitung_biaya(self):
        pass

    @abstractmethod
    def estimasi_waktu(self):
        pass

    # =========================
    # METHOD UMUM
    # =========================
    def proses_distribusi(self):
        """
        Mengurangi stok dari gudang
        """
        if self._barang.get_stok() < self._jumlah:
            raise ValueError("Stok tidak mencukupi")

        self._barang.kurangi_stok(self._jumlah)
        self._status = "dikirim"

    def selesaikan_distribusi(self):
        self._status = "selesai"

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

        title = "INFORMASI DISTRIBUSI".center(WIDTH)

        return (
            border("╔", "═", "╗")
            + f"║ {title} ║\n"
            + border("╠", "═", "╣")
            + row("ID", self._id_distribusi)
            + row("Barang", self._barang.get_nama())
            + row("Jumlah", self._jumlah)
            + row("Status", self._status)
            + row("Tanggal", self.get_tanggal())
            + border("╚", "═", "╝")
        )