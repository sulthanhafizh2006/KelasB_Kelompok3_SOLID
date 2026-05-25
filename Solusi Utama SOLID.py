from abc import ABC, abstractmethod

# ============================================================
# S - Single Responsibility Principle
# Setiap kelas hanya punya satu tanggung jawab
# ============================================================

# I - Interface Segregation Principle
# Pisahkan interface agar kelas tidak terpaksa implementasi
# metode yang tidak relevan
# ============================================================

class Hewan(ABC):
    """Base class hewan - hanya bertanggung jawab atas data dasar hewan"""
    def __init__(self, nama: str, jenis: str):
        self.nama = nama
        self.jenis = jenis

    @abstractmethod
    def makan(self):
        pass


class BisaTerbang(ABC):
    """Interface terpisah khusus untuk hewan yang bisa terbang"""
    @abstractmethod
    def terbang(self):
        pass


class BisaBerlari(ABC):
    """Interface terpisah khusus untuk hewan yang bisa berlari"""
    @abstractmethod
    def berlari(self):
        pass


# ============================================================
# O - Open/Closed Principle
# Terbuka untuk ekstensi (tambah hewan baru),
# tertutup untuk modifikasi kelas yang sudah ada
# ============================================================

class Elang(Hewan, BisaTerbang, BisaBerlari):
    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")

    def berlari(self):
        print(f"{self.nama} sedang berlari.")


class Kucing(Hewan, BisaBerlari):
    """Kucing tidak bisa terbang, jadi tidak implementasi BisaTerbang"""
    def makan(self):
        print(f"{self.nama} sedang makan.")

    def berlari(self):
        print(f"{self.nama} sedang berlari.")


class Ikan(Hewan):
    """Ikan tidak terbang dan tidak berlari"""
    def makan(self):
        print(f"{self.nama} sedang makan.")


# ============================================================
# L - Liskov Substitution Principle
# Subclass bisa menggantikan superclass tanpa merusak program
# ============================================================

# Semua subclass Hewan bisa dipakai di mana pun Hewan diharapkan,
# karena makan() selalu tersedia. Metode terbang() hanya dipanggil
# setelah pengecekan isinstance, sehingga tidak ada error.


# ============================================================
# D - Dependency Inversion Principle
# Kelas tingkat tinggi bergantung pada abstraksi, bukan konkret
# ============================================================

class KandangInterface(ABC):
    """Abstraksi kandang agar KebunBinatang tidak bergantung langsung
    pada implementasi Kandang"""
    @abstractmethod
    def tambah_hewan(self, hewan: Hewan):
        pass

    @abstractmethod
    def ambil_semua_hewan(self) -> list:
        pass

    @abstractmethod
    def bersihkan(self):
        pass


class Kandang(KandangInterface):
    """Implementasi konkret kandang - tanggung jawab: kelola koleksi hewan"""
    def __init__(self):
        self._hewan_list: list[Hewan] = []

    def tambah_hewan(self, hewan: Hewan):
        self._hewan_list.append(hewan)
        print(f"{hewan.nama} ditambahkan ke kandang.")

    def ambil_semua_hewan(self) -> list:
        return list(self._hewan_list)

    def bersihkan(self):
        print("Kandang sedang dibersihkan.")


class KebunBinatang:
    """Bergantung pada abstraksi KandangInterface, bukan Kandang langsung"""
    def __init__(self, kandang: KandangInterface):
        self._kandang = kandang

    def rawat_semua_hewan(self):
        print("\n--- Merawat semua hewan ---")
        for hewan in self._kandang.ambil_semua_hewan():
            hewan.makan()
            if isinstance(hewan, BisaTerbang):
                hewan.terbang()
            if isinstance(hewan, BisaBerlari):
                hewan.berlari()

    def bersihkan_kandang(self):
        self._kandang.bersihkan()


# ============================================================
# ============================================================

if __name__ == "__main__":
    kandang = Kandang()
    kandang.tambah_hewan(Elang("Elang Jawa", "Burung"))
    kandang.tambah_hewan(Kucing("Kucing Persia", "Mamalia"))
    kandang.tambah_hewan(Ikan("Ikan Mas", "Ikan"))

    kebun_binatang = KebunBinatang(kandang)
    kebun_binatang.rawat_semua_hewan()

    print()
    kebun_binatang.bersihkan_kandang()
