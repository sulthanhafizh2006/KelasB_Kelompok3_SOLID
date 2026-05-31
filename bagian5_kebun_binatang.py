# ============================================================
# BAGIAN 5 – Class KebunBinatang
# Anggota  : [Faris Rafiuddin Hannan]
# NIM      : [K3525058]
# Prinsip  : SRP, Encapsulation, menggunakan Polymorphism
# ============================================================

from bagian4_kandang import Kandang
from bagian1_hewan import Hewan


class KebunBinatang:
    """
    Mengelola seluruh operasional kebun binatang.
    SRP: bertanggung jawab pada manajemen kandang & aktivitas hewan.
    """

    def __init__(self, nama: str, kota: str):
        self.__nama = nama
        self.__kota = kota
        self.__kandang_list: list[Kandang] = []

    # --- Properties ---
    @property
    def nama(self) -> str:
        return self.__nama

    @property
    def kota(self) -> str:
        return self.__kota

    @property
    def total_kandang(self) -> int:
        return len(self.__kandang_list)

    @property
    def total_hewan(self) -> int:
        return sum(k.jumlah_hewan for k in self.__kandang_list)

    # --- Manajemen Kandang ---
    def tambah_kandang(self, kandang: Kandang):
        self.__kandang_list.append(kandang)
        print(f"  🏠 Kandang '{kandang.nama_kandang}' ditambahkan ke {self.__nama}.")

    def cari_kandang(self, nama_kandang: str) -> Kandang | None:
        for k in self.__kandang_list:
            if k.nama_kandang.lower() == nama_kandang.lower():
                return k
        return None

    # --- Aktivitas Hewan (memanfaatkan Polymorphism) ---
    def rawat_semua_hewan(self):
        """Merawat semua hewan di seluruh kandang dengan Polymorphism."""
        print(f"\n{'='*55}")
        print(f"  🌿 SESI PERAWATAN HEWAN – {self.__nama.upper()}")
        print(f"{'='*55}")
        for kandang in self.__kandang_list:
            print(f"\n  [ Kandang: {kandang.nama_kandang} ]")
            for hewan in kandang.hewan_list:
                hewan.makan()       # method konkret dari Hewan
                hewan.bergerak()    # Polymorphism: tiap hewan bergerak beda
                hewan.bersuara()    # Polymorphism: tiap hewan bersuara beda
                hewan.tidur()

    def bersihkan_semua_kandang(self):
        """Membersihkan seluruh kandang."""
        print(f"\n{'='*55}")
        print(f"  🧹 PEMBERSIHAN KANDANG – {self.__nama.upper()}")
        print(f"{'='*55}")
        for kandang in self.__kandang_list:
            kandang.bersihkan_kandang()

    def tampilkan_semua_info_hewan(self):
        """Menampilkan info seluruh hewan di kebun binatang."""
        print(f"\n{'='*55}")
        print(f"  📋 DAFTAR HEWAN – {self.__nama.upper()}, {self.__kota.upper()}")
        print(f"{'='*55}")
        for kandang in self.__kandang_list:
            kandang.status_kandang()

    def laporan(self):
        """Menampilkan laporan singkat kebun binatang."""
        print(f"\n{'='*55}")
        print(f"  📊 LAPORAN KEBUN BINATANG")
        print(f"{'='*55}")
        print(f"  Nama   : {self.__nama}")
        print(f"  Kota   : {self.__kota}")
        print(f"  Kandang: {self.total_kandang}")
        print(f"  Hewan  : {self.total_hewan} ekor")
        print(f"{'='*55}\n")

    def __str__(self):
        return f"KebunBinatang '{self.__nama}' di {self.__kota}"
