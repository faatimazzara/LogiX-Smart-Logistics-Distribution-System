from datetime import datetime


class StatusBarang:
    """
    Class untuk mengelola status barang.
    Contoh status:
    - tersedia
    - dikirim
    - rusak
    """

    STATUS_VALID = ["tersedia", "dikirim", "rusak"]
    BOX_WIDTH = 50  

    def __init__(self, status: str = "tersedia"):
        self._status = None
        self._updated_at = None

        self.set_status(status)

    # =========================
    # GETTER
    # =========================
    def get_status(self):
        return self._status

    def get_last_update(self):
        return self._updated_at.strftime("%Y-%m-%d %H:%M:%S")

    # =========================
    # SETTER 
    # =========================
    def set_status(self, status: str):
        status = status.lower()

        if status not in self.STATUS_VALID:
            raise ValueError(f"Status harus salah satu dari {self.STATUS_VALID}")

        self._status = status
        self._updated_at = datetime.now()

    # =========================
    # METHOD TAMBAHAN
    # =========================
    def is_tersedia(self):
        return self._status == "tersedia"

    def is_dikirim(self):
        return self._status == "dikirim"

    def is_rusak(self):
        return self._status == "rusak"

    # =========================
    # FORMAT HELPER 
    # =========================
    def _line(self, label, value):
        content_width = self.BOX_WIDTH - 4
        text = f"{label:<10}: {str(value)}"
        return f"║ {text:<{content_width}} ║\n"

    # =========================
    # OUTPUT
    # =========================
    def tampilkan_info(self):

        top = "╔" + "═" * (self.BOX_WIDTH - 2) + "╗\n"
        mid = "╠" + "═" * (self.BOX_WIDTH - 2) + "╣\n"
        bot = "╚" + "═" * (self.BOX_WIDTH - 2) + "╝\n"

        title = "STATUS BARANG"
        title_line = f"║ {title:^{self.BOX_WIDTH-4}} ║\n"

        return (
            top
            + title_line
            + mid
            + self._line("Status", self._status)
            + self._line("Update", self.get_last_update())
            + bot
        )