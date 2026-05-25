from abc import ABC, abstractmethod

class BisaMakan(ABC):
    @abstractmethod
    def makan(self):
        pass

class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class Kucing(BisaMakan):  
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"Kucing {self.nama} sedang makan ikan.")

class Burung(BisaMakan, BisaTerbang): 
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"Burung {self.nama} sedang mematuk biji.")

    def terbang(self):
        print(f"Burung {self.nama} sedang terbang di langit.")

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
        
            if isinstance(hewan, BisaMakan):
                hewan.makan()
            
            if isinstance(hewan, BisaTerbang):
                hewan.terbang()


if __name__ == "__main__":
    gembiraloka = KebunBinatang()
    
    kucing_oren = Kucing("Oren")
    burung_elang = Burung("Elang")
    
    gembiraloka.kandang.tambah_hewan(kucing_oren)
    gembiraloka.kandang.tambah_hewan(burung_elang)
    
    print("--- Memulai Perawatan Hewan (Versi SOLID - ISP) ---")
    gembiraloka.rawat_semua_hewan()
