# ============================================================
# BAGIAN 4 – Class Kandang
# Anggota  : Adibah
# Prinsip  : Single Responsibility Principle (SRP), Encapsulation
# ============================================================

from bagian1_hewan import Hewan

class Kandang:
    """
    Bertanggung jawab HANYA untuk mengelola koleksi hewan.
    SRP: satu kelas, satu tanggung jawab.
    """

    def _init_(self, nama_kandang: str, kapasitas: int):
        self.__nama_kandang = nama_kandang
        self.__kapasitas = kapasitas
        self.__hewan_list: list[Hewan] = []
        self.__sudah_bersih = True

    # --- Properties ---
    @property
    def nama_kandang(self) -> str:
        return self.__nama_kandang
@property
    def kapasitas(self) -> int:
        return self.__kapasitas

    @property
    def hewan_list(self) -> list:
        return list(self.__hewan_list)  # return salinan agar list asli aman

    @property
    def jumlah_hewan(self) -> int:
        return len(self.__hewan_list)

    # --- Method ---
    def tambah_hewan(self, hewan: Hewan) -> bool:
        """Menambahkan hewan ke kandang jika kapasitas masih tersedia."""
        if len(self._hewan_list) >= self._kapasitas:
            print(f"  ⚠️  Kandang '{self._nama_kandang}' sudah penuh! Kapasitas: {self._kapasitas}")
            return False
        self.__hewan_list.append(hewan)
        self.__sudah_bersih = False
        print(f"  ✅ {hewan.nama} berhasil masuk kandang '{self.__nama_kandang}'.")
        return True

    def keluarkan_hewan(self, nama_hewan: str) -> bool:
        """Mengeluarkan hewan dari kandang berdasarkan nama."""
        for hewan in self.__hewan_list:
            if hewan.nama.lower() == nama_hewan.lower():
                self.__hewan_list.remove(hewan)
                print(f"  🚪 {hewan.nama} telah dikeluarkan dari kandang '{self.__nama_kandang}'.")
                return True
        print(f"  ❌ Hewan '{nama_hewan}' tidak ditemukan di kandang '{self.__nama_kandang}'.")
        return False

    def bersihkan_kandang(self):
        """Membersihkan kandang (SRP: tugas kandang, bukan kebun binatang)."""
        self.__sudah_bersih = True
        print(f"  🧹 Kandang '{self.__nama_kandang}' telah dibersihkan.")

    def status_kandang(self):
        """Menampilkan status kandang saat ini."""
        kondisi = "Bersih ✨" if self.__sudah_bersih else "Kotor 🪣"
        print(f"\n  📦 Kandang : {self.__nama_kandang}")
        print(f"     Isi     : {self.jumlah_hewan}/{self.__kapasitas} hewan")
        print(f"     Kondisi : {kondisi}")
        if self.__hewan_list:
            print(f"     Penghuni:")
            for h in self.__hewan_list:
                print(f"       - {h}")

    def _str_(self):
        return f"Kandang '{self._nama_kandang}' [{self.jumlah_hewan}/{self._kapasitas}]"
