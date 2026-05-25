# Open/Closed Principle (OCP)
# Analisis oleh:
# Nama : Zahra Faizza Kuncoroningrum
# NIM  : K3525017

# Analisis Kesalahan
# 1. Method terbang() dikodekan keras di class Hewan
#    - Method terbang() langsung ditulis di class Hewan padahal tidak semua hewan bisa terbang
#    - Setiap ada perilaku baru (berenang, berlari, melompat), developer harus membuka dan mengubah class Hewan yang sudah ada
#    - Setiap perubahan berisiko merusak kode lain yang sudah berjalan
# 2. KebunBinatang memanggil terbang() untuk semua hewan
#    - rawat_semua_hewan() memanggil hewan.terbang() secara paksa ke semua objek tanpa membedakan jenisnya
#    - Hewan seperti anjing atau ikan akan ikut "terbang" yang tidak masuk akal secara logika

# Langkah Perbaikan:
# 1. Mengubah Hewan menjadi class abstrak
#    - Mengapus implementasi konkret terbang() dari class Hewan
#    - Mengganti dengan method abstrak generik (bergerak()) yang wajib diimplementasikan oleh setiap subclass
# 2. Membuat subclass untuk setiap jenis hewan
#    - Setiap hewan baru dibuat sebagai subclass terpisah
#    - Masing-masing subclass mengisi sendiri cara bergerak()-nya sesuai kemampuan hewannya
#    - Class Hewan tidak perlu disentuh sama sekali saat menambah hewan baru
# 3. KebunBinatang cukup panggil method generik
#    - Mengganti pemanggilan terbang() dengan bergerak() yang berlaku untuk semua hewan
#    - KebunBinatang tidak perlu tahu jenis hewan apapun, sehingga tidak perlu diubah lagi ke depannya

from abc import ABC, abstractmethod
class Hewan(ABC):
    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass

    @abstractmethod
    def bergerak(self):
        """Tiap hewan punya cara bergerak masing-masing."""
        pass

class Burung(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan biji-bijian.")

    def bergerak(self):
        print(f"{self.nama} sedang terbang.")

class Anjing(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan daging.")

    def bergerak(self):
        print(f"{self.nama} sedang berlari.")

class Ikan(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan plankton.")

    def bergerak(self):
        print(f"{self.nama} sedang berenang.")

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan: Hewan):
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

if __name__ == "__main__":
    kebun = KebunBinatang()
    kebun.kandang.tambah_hewan(Burung("Kakak Tua"))
    kebun.kandang.tambah_hewan(Anjing("Rex"))
    kebun.kandang.tambah_hewan(Ikan("Nemo"))

    kebun.rawat_semua_hewan()
