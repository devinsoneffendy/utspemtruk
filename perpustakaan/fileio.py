"""Fungsi untuk operasi file data buku."""
from pathlib import Path


def buat_file_awal(nama_file):
    """Buat file baru tanpa menimpa file yang sudah ada (mode x)."""
    path = Path(nama_file)
    path.parent.mkdir(exist_ok=True)
    try:
        with open(path, "x", encoding="utf-8") as file:
            file.write("kode;judul;penulis;halaman\n")
    except FileExistsError:
        # File sudah ada; jangan timpa data lama.
        pass


def baca_buku(nama_file):
    """Baca data per baris dan kembalikan list of dictionary."""
    data = []
    with open(nama_file, "r", encoding="utf-8") as file:
        for nomor, baris in enumerate(file, start=1):
            if nomor == 1 and baris.startswith("kode;"):
                continue
            try:
                kode, judul, penulis, halaman = baris.strip().split(";")
                data.append({
                    "kode": kode,
                    "judul": judul,
                    "penulis": penulis,
                    "halaman": int(halaman),
                })
            except (ValueError, TypeError):
                # TODO: tampilkan pesan dengan nomor baris yang dilewati.
                continue
    return data


def tambah_buku(nama_file, **data_buku):
    """Tambahkan satu data buku dengan mode a."""
    # TODO: pastikan urutan kolom sesuai format file.
    # TODO: tulis satu baris menggunakan with open(..., 'a').
    raise NotImplementedError("Lengkapi fungsi tambah_buku().")


def tulis_laporan(nama_file, isi):
    """Tulis laporan baru dengan mode w."""
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(isi)
