# Dependency Inversion Principle (DIP)
# Analisis oleh: Adibah

# =========================================
# ANALISIS DEPENDENCY INVERSION PRINCIPLE
# =========================================

# Definisi DIP:
# Modul tingkat tinggi tidak boleh bergantung
# langsung pada modul tingkat rendah.
# Keduanya harus bergantung pada abstraksi.

# -----------------------------------------
# PELANGGARAN PADA KODE
# -----------------------------------------

# Pada kode awal, class KebunBinatang
# membuat object Kandang secara langsung.

# Contoh:
# self.kandang = Kandang()

# Hal ini menyebabkan:
# 1. KebunBinatang terlalu bergantung pada Kandang
# 2. Program sulit dikembangkan
# 3. Jika class Kandang berubah,
#    maka KebunBinatang juga ikut berubah
# 4. Coupling antar class menjadi tinggi
# 5. Kode menjadi kurang fleksibel karena
#    hanya dapat menggunakan satu jenis kandang

# -----------------------------------------
# SOLUSI PERBAIKAN
# -----------------------------------------

# Solusi yang dilakukan:
# 1. Membuat abstraksi bernama TempatHewan
# 2. Object kandang dikirim dari luar class
# 3. KebunBinatang hanya menggunakan abstraksi
# 4. KebunBinatang tidak lagi membuat object sendiri,
#    tetapi menerima object dari luar agar sesuai
#    dengan prinsip DIP
# 5. Class Kandang sekarang mengimplementasikan
#    abstraksi TempatHewan sehingga lebih fleksibel
# 6. Jika nanti ada jenis kandang lain,
#    class KebunBinatang tidak perlu diubah lagi

# Penjelasan:
# Pada perbaikan kode ini, class KebunBinatang
# tidak lagi bergantung langsung pada class Kandang,
# tetapi menggunakan abstraksi TempatHewan.
# Dengan cara ini, hubungan antar class menjadi
# lebih fleksibel, mudah dikembangkan,
# dan sesuai dengan prinsip Dependency
# Inversion Principle (DIP).

# Penjelasan Class Kandang:
# Pada perbaikan ini, class Kandang tidak lagi
# digunakan secara langsung oleh KebunBinatang,
# tetapi melalui abstraksi TempatHewan.
# Class Kandang sekarang berperan sebagai
# implementasi konkret dari abstraksi tersebut.
# Dengan begitu, jika nanti ada jenis kandang lain,
# program tidak perlu mengubah class KebunBinatang.
# Hal ini membuat program lebih fleksibel
# dan sesuai dengan prinsip DIP.

# ======= KODE PERBAIKAN  Dengan Menggunakan PRINSIP DIP =======

from abc import ABC, abstractmethod

# Abstraksi
class TempatHewan(ABC):

    @abstractmethod
    def simpan_hewan(self, hewan):
        pass

    @abstractmethod
    def tampilkan_hewan(self):
        pass

class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} sedang makan.")

class Elang(Hewan):

    def terbang(self):
        print(f"{self.nama} sedang terbang di udara.")

class Singa(Hewan):

    def mengaum(self):
        print(f"{self.nama} sedang mengaum.")

# Implementasi konkret
class Kandang(TempatHewan):

    def __init__(self):
        self.daftar_hewan = []

    def simpan_hewan(self, hewan):
        self.daftar_hewan.append(hewan)

    def tampilkan_hewan(self):
        return self.daftar_hewan

# High-level modulenya
class KebunBinatang:

    def __init__(self, tempat_hewan: TempatHewan):
        self.tempat_hewan = tempat_hewan

    def rawat_hewan(self):

        for hewan in self.tempat_hewan.tampilkan_hewan():

            hewan.makan()

            if hasattr(hewan, "terbang"):
                hewan.terbang()

            if hasattr(hewan, "mengaum"):
                hewan.mengaum()

# ======= TEST PROGRAM =======

if __name__ == "__main__":

    print("=== Program Kebun Binatang ===")

    kandang_hewan = Kandang()

    burung = Elang("Rajawali")
    singa = Singa("Simba")

    kandang_hewan.simpan_hewan(burung)
    kandang_hewan.simpan_hewan(singa)

    kebun = KebunBinatang(kandang_hewan)

    kebun.rawat_hewan()
