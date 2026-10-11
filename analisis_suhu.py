"""Program analisis suhu harian selama satu minggu."""


def baca_suhu(nama_file):
    """Baca file suhu baris demi baris jadi list of dictionary."""
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                try:
                    hari, suhu = baris.strip().split(";")
                    data.append({
                        "hari": hari.strip(),
                        "suhu": int(suhu.strip()),
                    })
                except ValueError:
                    print(f"Baris {nomor} dilewati (format tidak valid).")
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
    return data


def rata_suhu(*daftar_suhu):
    """Hitung rata-rata suhu (contoh penggunaan *args)."""
    if not daftar_suhu:
        return 0.0
    return sum(daftar_suhu) / len(daftar_suhu)


def kategori(suhu, batas_panas=32):
    """Tentukan kategori suhu (contoh keyword argument)."""
    return "Panas" if suhu >= batas_panas else "Normal"


def analisis_suhu(data):
    """Analisis lengkap: rata, tertinggi, terendah, kategori, jumlah panas."""
    if not data:
        return {}

    suhu_list = [d["suhu"] for d in data]

    # Rata-rata pakai *args
    rata = rata_suhu(*suhu_list)

    # Tertinggi & terendah pakai lambda sebagai key
    tertinggi = max(data, key=lambda d: d["suhu"])
    terendah = min(data, key=lambda d: d["suhu"])

    # Tentukan kategori tiap hari
    for d in data:
        d["kategori"] = kategori(d["suhu"])

    # Hitung jumlah hari Panas
    jumlah_panas = len([d for d in data if d["kategori"] == "Panas"])

    return {
        "rata": rata,
        "tertinggi": tertinggi,
        "terendah": terendah,
        "jumlah_panas": jumlah_panas,
        "data": data,
    }


def buat_teks_laporan(hasil):
    """Susun hasil analisis jadi teks laporan."""
    lines = [
        "=== LAPORAN SUHU MINGGUAN ===",
        f"Rata-rata suhu     : {hasil['rata']:.2f}",
        f"Suhu tertinggi     : {hasil['tertinggi']['suhu']} "
        f"({hasil['tertinggi']['hari']})",
        f"Suhu terendah      : {hasil['terendah']['suhu']} "
        f"({hasil['terendah']['hari']})",
        f"Jumlah hari Panas  : {hasil['jumlah_panas']}",
        "",
        "Detail harian:",
    ]
    for d in hasil["data"]:
        lines.append(f"- {d['hari']}: {d['suhu']} ({d['kategori']})")
    return "\n".join(lines) + "\n"


def tulis_laporan(nama_file, isi):
    """Tulis laporan ke file dengan mode w."""
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(isi)


if __name__ == "__main__":
    # Tahap 1: baca data
    data = baca_suhu("suhu.txt")

    if not data:
        print("Tidak ada data suhu yang bisa dianalisis.")
    else:
        # Tahap 2: analisis
        hasil = analisis_suhu(data)

        # Tahap 3: tulis & tampilkan laporan
        teks = buat_teks_laporan(hasil)
        tulis_laporan("laporan_suhu.txt", teks)
        print(teks)
        print("Laporan disimpan di: laporan_suhu.txt")
