from datetime import datetime


class LogMixin:
    """
    Mixin untuk logging aktivitas sistem.
    Digunakan di berbagai class tanpa duplikasi kode.
    """
    def log(self, message: str):
        print(f"[LOG] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {message}")


class TimestampMixin:
    """
    Mixin untuk mencatat waktu pembuatan dan update data.
    """
    def __init__(self):
        self._created_at = datetime.now()
        self._updated_at = datetime.now()

    def _update_timestamp(self):
        self._updated_at = datetime.now()

    def get_created_at(self):
        return self._created_at.strftime('%Y-%m-%d %H:%M:%S')

    def get_updated_at(self):
        return self._updated_at.strftime('%Y-%m-%d %H:%M:%S')