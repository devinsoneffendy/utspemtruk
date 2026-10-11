"""Program utama proyek perpustakaan."""
from pathlib import Path
from perpustakaan.fileio import baca_buku, tambah_buku, buat_file_awal, tulis_laporan
from perpustakaan.processing import hitung_ringkasan, urutkan_buku
from perpustakaan.validasi import validasi_buku

DATA = Path("data/buku.txt")
LAPORAN = Path("data/laporan_buku.txt")


def tampilkan_menu():
    """Tampilkan pilihan menu kepada pengguna."""
    print("\n=== SISTEM PERPUSTAKAAN ===")
    print("1. Lihat semua buku")
    print("2. Tambah buku")
    print("3. Lihat ringkasan dan buat laporan")
    print("4. Urutkan buku berdasarkan judul")
    print("0. Keluar")


def main():
    """Jalankan menu utama."""
    DATA.parent.mkdir(exist_ok=True)
    # TODO: panggil buat_file_awal(DATA) dan tangani kondisi file sudah ada.
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            try:
                for buku in baca_buku(DATA):
                    print(buku)
            except FileNotFoundError:
                print("File data belum ada. Buat file data terlebih dahulu.")
        elif pilihan == "2":
            # TODO: minta kode, judul, penulis, dan jumlah halaman.
            # TODO: validasi data, lalu panggil tambah_buku().
            print("Lengkapi bagian tambah buku.")
        elif pilihan == "3":
            # TODO: baca data, hitung ringkasan, tulis laporan, lalu tampilkan.
            print("Lengkapi bagian laporan.")
        elif pilihan == "4":
            # TODO: gunakan urutkan_buku() dan tampilkan hasilnya.
            print("Lengkapi bagian pengurutan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
