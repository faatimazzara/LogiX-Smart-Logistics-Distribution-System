from datetime import datetime


class Laporan:
    """
    Class untuk menghasilkan laporan sistem:
    - Laporan barang
    - Laporan distribusi
    - Statistik sederhana
    """

    def __init__(self, nama_laporan: str):
        self._nama_laporan = nama_laporan
        self._data_barang = []
        self._data_distribusi = []
        self._dibuat_pada = datetime.now()

    # =========================
    # TAMBAH DATA
    # =========================
    def tambah_barang(self, barang):
        self._data_barang.append(barang)

    def tambah_distribusi(self, distribusi):
        self._data_distribusi.append(distribusi)

    # =========================
    # RINGKASAN DATA
    # =========================
    def generate_ringkasan(self):
        total_barang = len(self._data_barang)
        total_distribusi = len(self._data_distribusi)

        return (
            "===== RINGKASAN LAPORAN =====\n"
            f"Nama Laporan     : {self._nama_laporan}\n"
            f"Tanggal          : {self._dibuat_pada.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Total Barang     : {total_barang}\n"
            f"Total Distribusi : {total_distribusi}\n"
        )

    # =========================
    # STATISTIK BARANG
    # =========================
    def statistik_barang(self):
        tersedia = 0
        rusak = 0

        for barang in self._data_barang:
            if barang.get_status() == "tersedia":
                tersedia += 1
            elif barang.get_status() == "rusak":
                rusak += 1

        return (
            "===== STATISTIK BARANG =====\n"
            f"Tersedia : {tersedia}\n"
            f"Rusak    : {rusak}\n"
        )

    # =========================
    # STATISTIK DISTRIBUSI
    # =========================
    def statistik_distribusi(self):
        diproses = 0
        dikirim = 0
        selesai = 0

        for distribusi in self._data_distribusi:
            status = distribusi.get_status()

            if status == "diproses":
                diproses += 1
            elif status == "dikirim":
                dikirim += 1
            elif status == "selesai":
                selesai += 1

        return (
            "===== STATISTIK DISTRIBUSI =====\n"
            f"Diproses : {diproses}\n"
            f"Dikirim  : {dikirim}\n"
            f"Selesai  : {selesai}\n"
        )

    # =========================
    # OUTPUT UTAMA
    # =========================
    def tampilkan_laporan(self):
        return (
            "\n"
            + self.generate_ringkasan()
            + "\n"
            + self.statistik_barang()
            + "\n"
            + self.statistik_distribusi()
        )