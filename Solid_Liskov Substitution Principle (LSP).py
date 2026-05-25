from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    @abstractmethod
    def makan(self):
        pass

class BisaTerbang:
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class BisaBerenang:
    def berenang(self):
        print(f"{self.nama} sedang berenang.")


class Burung(Hewan, BisaTerbang):
    """Burung bisa makan DAN terbang — valid."""
    def makan(self):
        print(f"{self.nama} sedang makan biji-bijian.")

class Anjing(Hewan):
    """Anjing hanya bisa makan — tidak perlu terbang."""
    def makan(self):
        print(f"{self.nama} sedang makan daging.")

class Bebek(Hewan, BisaTerbang, BisaBerenang):
    """Bebek bisa makan, terbang, dan berenang."""
    def makan(self):
        print(f"{self.nama} sedang makan cacing.")


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

    def terbangkan_hewan(self):
        for hewan in self.kandang.hewan_list:
            if isinstance(hewan, BisaTerbang):  
                hewan.terbang()


if __name__ == "__main__":
    kebun = KebunBinatang()
    kebun.kandang.tambah_hewan(Burung("Kakak Tua", "Burung"))
    kebun.kandang.tambah_hewan(Anjing("Rex", "Mamalia"))
    kebun.kandang.tambah_hewan(Bebek("Donald", "Unggas"))

    print("=== Makan ===")
    kebun.rawat_semua_hewan()

    print("\n=== Terbang ===")
    kebun.terbangkan_hewan()
