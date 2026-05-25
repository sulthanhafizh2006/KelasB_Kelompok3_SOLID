# Single Responsibility Principle (SRP)
# Analisis oleh:
# Nama : [Nama Anggota 1]
# NIM  : [NIM Anggota 1]

# Analisis Kesalahan
# 1. Class Hewan menanggung terlalu banyak tanggung jawab
#    - Class Hewan menyimpan data (nama, jenis) sekaligus mendefinisikan perilaku (makan, terbang)
#    - Idealnya satu class hanya bertanggung jawab atas satu hal saja
#    - Jika ada perubahan pada perilaku hewan, class data ikut terdampak padahal tidak seharusnya

# 2. Class Kandang menggabungkan dua tanggung jawab sekaligus
#    - Class Kandang bertugas menyimpan daftar hewan (manajemen data)
#      sekaligus membersihkan kandang (operasional/perawatan)
#    - Dua tanggung jawab berbeda ini seharusnya dipisah ke class masing-masing

# 3. Class KebunBinatang terlalu tahu urusan dalam Kandang
#    - KebunBinatang langsung mengakses kandang.hewan_list (atribut internal Kandang)
#    - KebunBinatang seharusnya hanya mengurus koordinasi perawatan,
#      bukan urusan teknis penyimpanan hewan di dalam kandang

# Langkah Perbaikan:
# 1. Pisahkan tanggung jawab data dan perilaku hewan
#    - Class Hewan hanya menyimpan data: nama dan jenis
#    - Class AktivitasHewan khusus menangani perilaku hewan (makan)
#    - Perubahan pada perilaku tidak akan memengaruhi struktur data hewan

# 2. Pisahkan manajemen hewan dan perawatan kandang
#    - Class Kandang hanya bertanggung jawab menyimpan dan mengelola daftar hewan
#    - Class PerawatanKandang khusus menangani operasional kebersihan kandang
#    - Keduanya bisa dikembangkan secara independen tanpa saling mengganggu

# 3. KebunBinatang cukup bertugas sebagai koordinator
#    - KebunBinatang hanya mengkoordinasikan perawatan dengan memanggil
#      AktivitasHewan dan PerawatanKandang
#    - Tidak perlu tahu detail implementasi penyimpanan hewan di Kandang


class Hewan:
    """Hanya bertanggung jawab menyimpan DATA hewan."""
    def __init__(self, nama: str, jenis: str):
        self.nama = nama
        self.jenis = jenis


class AktivitasHewan:
    """Hanya bertanggung jawab mengelola PERILAKU/AKTIVITAS hewan."""
    def makan(self, hewan: Hewan):
        print(f"{hewan.nama} sedang makan.")


class Kandang:
    """Hanya bertanggung jawab MENYIMPAN dan MENGELOLA daftar hewan."""
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan: Hewan):
        self.hewan_list.append(hewan)

    def get_semua_hewan(self):
        return self.hewan_list


class PerawatanKandang:
    """Hanya bertanggung jawab mengelola KEBERSIHAN kandang."""
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")


class KebunBinatang:
    """Hanya bertanggung jawab MENGKOORDINASIKAN perawatan hewan."""
    def __init__(self):
        self.kandang = Kandang()
        self.aktivitas = AktivitasHewan()
        self.perawatan = PerawatanKandang()

    def rawat_semua_hewan(self):
        for hewan in self.kandang.get_semua_hewan():
            self.aktivitas.makan(hewan)
        self.perawatan.bersihkan_kandang()


if __name__ == "__main__":
    kebun = KebunBinatang()
    kebun.kandang.tambah_hewan(Hewan("Kakak Tua", "Burung"))
    kebun.kandang.tambah_hewan(Hewan("Rex", "Anjing"))
    kebun.kandang.tambah_hewan(Hewan("Nemo", "Ikan"))
    kebun.rawat_semua_hewan()
