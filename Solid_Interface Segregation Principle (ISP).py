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
            BisaMakan
            if isinstance(hewan, BisaMakan):
                hewan.makan()
            
BisaTerbang
            if isinstance(hewan, BisaTerbang):
                hewan.terbang()

