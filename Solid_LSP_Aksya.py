# Liskov Substitution Principle (LSP)
# Analisis oleh:
# Nama : Aksya Nayla Fitriana
# NIM  : K3525047

# ANALISIS KESALAHAN DARI KODE AWAL (PELANGGARAN LSP)
# 1. Method terbang() didefinisikan di class Hewan (base class)
#    - Method terbang() langsung ditulis di class Hewan padahal tidak semua hewan bisa terbang
#    - Anjing, ikan, sapi, dan banyak hewan lain tidak memiliki kemampuan terbang
#    - Menempatkan terbang() di base class memaksa semua subclass "mewarisi" perilaku yang tidak sesuai
# 2. KebunBinatang memanggil terbang() untuk semua hewan tanpa seleksi
#    - rawat_semua_hewan() memanggil hewan.terbang() secara paksa ke semua objek
#    - Hewan seperti anjing atau ikan akan "terbang" yang tidak masuk akal secara logika
#    - Ini melanggar LSP: subclass (Anjing, Ikan) tidak bisa menggantikan base class (Hewan)
#      tanpa mengubah kebenaran program
# 3. Subclass yang dibuat dari Hewan tidak dapat disubstitusi dengan aman
#    - Jika dibuat class Anjing(Hewan), method terbang() yang diwarisi tidak valid
#    - Jika subclass meng-override terbang() dengan raise Exception / pass kosong,
#      perilaku program berubah -> ini pelanggaran LSP
#    - Precondition / postcondition tidak terpenuhi untuk subclass hewan darat / hewan air

# PRINSIP LSP YANG DILANGGAR
# LSP menyatakan: "Objek dari subclass harus bisa menggantikan objek dari superclass
# tanpa mengubah kebenaran/perilaku program."

# LANGKAH PERBAIKAN
# 1. Pisahkan kemampuan terbang ke interface/mixin tersendiri (gunakan ABC)
#    - Buat abstract class / mixin BisaTerbang dengan method terbang()
#    - Hanya subclass yang memang bisa terbang yang mengimplementasikan mixin ini
#    - Class Hewan hanya berisi perilaku yang UNIVERSAL (makan, bergerak generik)
# 2. Buat subclass sesuai kemampuan nyata masing-masing hewan
#    - class Elang(Hewan, BisaTerbang) -> bisa terbang
#    - class Anjing(Hewan)             -> tidak bisa terbang
#    - class Ikan(Hewan)               -> tidak bisa terbang
#    - Setiap subclass hanya mengimplementasikan kemampuan yang relevan
# 3. KebunBinatang hanya memanggil terbang() pada hewan yang memang bisa terbang
#    - Gunakan isinstance(hewan, BisaTerbang) sebelum memanggil terbang()
#    - Dengan begitu, semua subclass bisa menggantikan Hewan tanpa melanggar kontrak LSP

# KODE PERBAIKAN (MEMENUHI LSP)

from abc import ABC, abstractmethod


class Hewan(ABC):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

    @abstractmethod
    def bergerak(self):
        """Setiap hewan bergerak dengan caranya sendiri."""
        pass


class BisaTerbang:
    def terbang(self):
        print(f"{self.nama} sedang terbang.")


class BisaBerenang:
    def berenang(self):
        print(f"{self.nama} sedang berenang.")


class Elang(Hewan, BisaTerbang):
    def bergerak(self):
        self.terbang()


class Anjing(Hewan):
    def bergerak(self):
        print(f"{self.nama} sedang berlari.")


class Ikan(Hewan, BisaBerenang):
    def bergerak(self):
        self.berenang()


class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")


class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.bergerak()            

    def latih_terbang(self):
        for hewan in self.kandang.hewan_list:
            if isinstance(hewan, BisaTerbang):  
                hewan.terbang()

if __name__ == "__main__":
    kebun = KebunBinatang()
    kebun.kandang.tambah_hewan(Elang("Rajawali", "Burung"))
    kebun.kandang.tambah_hewan(Anjing("Buddy", "Mamalia"))
    kebun.kandang.tambah_hewan(Ikan("Nemo", "Ikan"))

    print("=== Merawat Semua Hewan ===")
    kebun.rawat_semua_hewan()

    print("\n=== Latihan Terbang (hanya hewan yang bisa) ===")
    kebun.latih_terbang()
