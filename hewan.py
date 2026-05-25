# OCP: Terbuka untuk ekstensi, tertutup untuk modifikasi
from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    @abstractmethod
    def bergerak(self):
        pass

    def makan(self):
        print(f"{self.nama} sedang makan.")

class Burung(Hewan):
    def bergerak(self):
        print(f"{self.nama} sedang terbang.")

class Anjing(Hewan):
    def bergerak(self):
        print(f"{self.nama} sedang berlari.")

class Ikan(Hewan):
    def bergerak(self):
        print(f"{self.nama} sedang berenang.")
