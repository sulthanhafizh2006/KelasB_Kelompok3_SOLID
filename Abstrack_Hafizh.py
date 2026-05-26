# ============================================================
# BAGIAN 1 – Abstract Base Class: Hewan
# Anggota  : [Nama Anggota 1]
# Prinsip  : Abstraction, Encapsulation
# ============================================================

from abc import ABC, abstractmethod


class Hewan(ABC):
    """
    Kelas abstrak sebagai blueprint semua hewan.
    Menerapkan Abstraction dan Encapsulation.
    """

    def __init__(self, nama: str, jenis: str, umur: int):
        # Encapsulation: atribut privat, hanya bisa diakses via property
        self.__nama = nama
        self.__jenis = jenis
        self.__umur = umur

    # --- Properties (Encapsulation) ---
    @property
    def nama(self) -> str:
        return self.__nama

    @property
    def jenis(self) -> str:
        return self.__jenis

    @property
    def umur(self) -> int:
        return self.__umur

    # --- Method Konkret (perilaku umum semua hewan) ---
    def makan(self):
        print(f"  🍖 {self.__nama} ({self.__jenis}) sedang makan.")

    def tidur(self):
        print(f"  💤 {self.__nama} ({self.__jenis}) sedang tidur.")

    def info(self):
        print(f"  📋 Nama: {self.__nama} | Jenis: {self.__jenis} | Umur: {self.__umur} tahun")

    # --- Method Abstrak (wajib di-override subclass) ---
    @abstractmethod
    def bergerak(self):
        """Setiap hewan bergerak dengan cara berbeda (Polymorphism)."""
        pass

    @abstractmethod
    def bersuara(self):
        """Setiap hewan bersuara dengan cara berbeda (Polymorphism)."""
        pass

    def __str__(self):
        return f"{self.__jenis}: {self.__nama} (umur {self.__umur} tahun)"
