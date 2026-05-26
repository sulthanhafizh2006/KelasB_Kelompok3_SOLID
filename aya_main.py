# ============================================================
# BAGIAN 3 – Subclass Konkret: Singa, Gajah, Elang, Burung
# Anggota  : [Allicya Nailah Fairuza]
# Prinsip  : Polymorphism, Inheritance
# ============================================================

from bagian2_kategori_hewan import HewanDarat, HewanTerbang


# ── Hewan Darat ──────────────────────────────────────────────

class Singa(HewanDarat):
    """Polymorphism: mengoverride bersuara() sesuai karakteristik singa."""

    def __init__(self, nama: str, umur: int):
        super().__init__(nama, jenis="Singa", umur=umur, kecepatan_lari=80.0)

    def bersuara(self):
        print(f"  🦁 {self.nama} mengaum: ROAARR!!!")


class Gajah(HewanDarat):
    """Polymorphism: mengoverride bersuara() sesuai karakteristik gajah."""

    def __init__(self, nama: str, umur: int):
        super().__init__(nama, jenis="Gajah", umur=umur, kecepatan_lari=40.0)

    def bergerak(self):
        # Override tambahan: gajah berjalan pelan, bukan berlari
        print(f"  🐘 {self.nama} berjalan lamban namun kuat di savana.")

    def bersuara(self):
        print(f"  🐘 {self.nama} berbunyi: BRRUUMMM!!!")


# ── Hewan Terbang ─────────────────────────────────────────────

class Elang(HewanTerbang):
    """Polymorphism: mengoverride bersuara() sesuai karakteristik elang."""

    def __init__(self, nama: str, umur: int):
        super().__init__(nama, jenis="Elang", umur=umur, tinggi_terbang=3000.0)

    def bersuara(self):
        print(f"  🦅 {self.nama} berteriak: KIIIAAK!!!")


class BurungKakatua(HewanTerbang):
    """Polymorphism: mengoverride bersuara() sesuai karakteristik kakatua."""

    def __init__(self, nama: str, umur: int, kata_favorit: str = "Halo!"):
        super().__init__(nama, jenis="Kakatua", umur=umur, tinggi_terbang=200.0)
        self.__kata_favorit = kata_favorit

    def bersuara(self):
        print(f"  🦜 {self.nama} berkata: '{self.__kata_favorit}'")
