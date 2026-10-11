"""Pengujian fungsi analisis suhu (minimal 3 test)."""
import unittest
from analisis_suhu import rata_suhu, kategori, analisis_suhu


class TestSuhu(unittest.TestCase):

    def test_rata_suhu(self):
        """Rata-rata dari beberapa angka."""
        self.assertAlmostEqual(rata_suhu(30, 32, 34), 32.0)
        self.assertAlmostEqual(rata_suhu(28, 30), 29.0)

    def test_kategori(self):
        """Suhu >= 32 dianggap Panas, selain itu Normal."""
        self.assertEqual(kategori(33), "Panas")
        self.assertEqual(kategori(32), "Panas")
        self.assertEqual(kategori(31), "Normal")

    def test_analisis_tertinggi_terendah(self):
        """Analisis tertinggi, terendah, dan jumlah hari Panas."""
        data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Selasa", "suhu": 35},
            {"hari": "Rabu", "suhu": 28},
            {"hari": "Kamis", "suhu": 33},
        ]
        hasil = analisis_suhu(data)
        self.assertEqual(hasil["tertinggi"]["hari"], "Selasa")
        self.assertEqual(hasil["terendah"]["hari"], "Rabu")
        self.assertEqual(hasil["jumlah_panas"], 2)

    def test_tanpa_data(self):
        """Data kosong harus mengembalikan dict kosong."""
        self.assertEqual(analisis_suhu([]), {})


if __name__ == "__main__":
    unittest.main()
