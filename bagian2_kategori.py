# ============================================================
# BAGIAN 2 – Subclass Intermediate: HewanDarat & HewanTerbang
# Anggota  : [Aksya Nayla Fitriana]
# BIM      : [K3525047]
# Prinsip  : Inheritance, Abstraction
# ============================================================

from bagian1_hewan import Hewan
from abc import abstractmethod


class HewanDarat(Hewan):
    """
    Kelas turunan untuk hewan yang hidup di darat.
    Menerapkan Inheritance dari Hewan.
    """

    def __init__(self, nama: str, jenis: str, umur: int, kecepatan_lari: float):
        super().__init__(nama, jenis, umur)
        self.__kecepatan_lari = kecepatan_lari 

    @property
    def kecepatan_lari(self) -> float:
        return self.__kecepatan_lari

    def bergerak(self):
        print(f"  🏃 {self.nama} berlari di darat dengan kecepatan {self.__kecepatan_lari} km/jam.")

    @abstractmethod
    def bersuara(self):
        pass


class HewanTerbang(Hewan):
    """
    Kelas turunan untuk hewan yang bisa terbang.
    Menerapkan Inheritance dari Hewan.
    """

    def __init__(self, nama: str, jenis: str, umur: int, tinggi_terbang: float):
        super().__init__(nama, jenis, umur)
        self.__tinggi_terbang = tinggi_terbang  # meter

    @property
    def tinggi_terbang(self) -> float:
        return self.__tinggi_terbang

    def bergerak(self):
        print(f"  🦅 {self.nama} terbang di ketinggian hingga {self.__tinggi_terbang} meter.")

    @abstractmethod
    def bersuara(self):
        pass
