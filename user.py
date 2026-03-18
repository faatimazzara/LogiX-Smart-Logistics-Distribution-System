from abc import ABC, abstractmethod
from datetime import datetime


class User(ABC):

    def __init__(self, id_user: str, nama: str, username: str, password: str):
        self._id_user = id_user
        self._nama = nama
        self._username = username
        self._password = None
        self._created_at = datetime.now()

        self.set_password(password)

    # =========================
    # GETTER
    # =========================
    def get_id_user(self):
        return self._id_user

    def get_nama(self):
        return self._nama

    def get_username(self):
        return self._username

    def get_created_at(self):
        return self._created_at.strftime("%Y-%m-%d %H:%M:%S")

    # =========================
    # SETTER
    # =========================
    def set_nama(self, nama: str):
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nama

    def set_password(self, password: str):
        if len(password) < 6:
            raise ValueError("Password minimal 6 karakter")
        self._password = password

    # =========================
    # METHOD
    # =========================
    def login(self, username: str, password: str):
        return self._username == username and self._password == password

    # =========================
    # ABSTRACT
    # =========================
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_permissions(self):
        pass

    # =========================
    # OUTPUT
    # =========================
    def tampilkan_info(self):

        WIDTH = 40

        def border(l, m, r):
            return f"{l}{m * (WIDTH + 2)}{r}\n"

        def row(label, value):
            text = f"{label:<12}: {value}"
            return f"║ {text.ljust(WIDTH)} ║\n"

        title = "INFORMASI USER".center(WIDTH)

        akses = self.get_permissions()
        akses = akses[0] if isinstance(akses, list) else akses

        return (
            "\n"
            + border("╔", "═", "╗")
            + f"║ {title} ║\n"
            + border("╠", "═", "╣")
            + row("ID", self._id_user)
            + row("Nama", self._nama)
            + row("Username", self._username)
            + row("Role", self.get_role())
            + row("Akses", akses)
            + border("╠", "═", "╣")
            + row("Dibuat", self.get_created_at())
            + border("╚", "═", "╝")
        )