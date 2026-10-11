"""Kerangka unit test. Lengkapi minimal lima fungsi pengujian."""
import unittest
from perpustakaan.processing import hitung_ringkasan, urutkan_buku
from perpustakaan.validasi import validasi_buku, DataBukuTidakValid


class TestPerpustakaan(unittest.TestCase):
    def test_total_halaman(self):
        # TODO: uji total untuk beberapa angka halaman.
        self.fail("Lengkapi pengujian ini.")

    def test_tanpa_data(self):
        # TODO: tetapkan dan uji hasil saat tidak ada angka.
        self.fail("Lengkapi pengujian ini.")

    def test_urut_judul(self):
        # TODO: pastikan buku terurut berdasarkan judul.
        self.fail("Lengkapi pengujian ini.")

    def test_judul_kosong(self):
        # TODO: gunakan assertRaises untuk exception validasi.
        self.fail("Lengkapi pengujian ini.")

    def test_halaman_negatif(self):
        # TODO: uji penolakan jumlah halaman negatif atau nol.
        self.fail("Lengkapi pengujian ini.")


if __name__ == "__main__":
    unittest.main()
