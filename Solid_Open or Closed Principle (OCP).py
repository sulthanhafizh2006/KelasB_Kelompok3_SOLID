from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    
    @abstractmethod
    def bergerak(self):
        pass
    
    @abstractmethod
    def makan(self):
        pass

class Burung(Hewan):
    def bergerak(self):
        print(f"{self.nama} sedang terbang.")
    
    def makan(self):
        print(f"{self.nama} makan biji-bijian.")

class Anjing(Hewan):
    def bergerak(self):
        print(f"{self.nama} sedang berlari.")
    
    def makan(self):
        print(f"{self.nama} makan daging.")

class Ikan(Hewan):
    def bergerak(self):
        print(f"{self.nama} sedang berenang.")
    
    def makan(self):
        print(f"{self.nama} makan plankton.")
