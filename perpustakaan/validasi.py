"""Validasi data dan exception buatan sendiri."""


class DataBukuTidakValid(Exception):
    """Exception untuk data buku yang tidak memenuhi aturan."""


def validasi_buku(**data):
    """Periksa field wajib dan nilai halaman."""
    # TODO: pastikan kode, judul, dan penulis tidak kosong.
    # TODO: pastikan halaman dapat dikonversi ke integer positif.
    # TODO: gunakan raise DataBukuTidakValid(...) untuk data yang salah.
    raise NotImplementedError("Lengkapi fungsi validasi_buku().")
