# ============================================================
# BAGIAN 6 – Main Program (Runner)
# Anggota  : [Zahra Faizza Kuncoroningrum]
# NIM      : K3525017
# Fungsi   : Menggabungkan semua bagian & menjalankan program
# ============================================================

from bagian3_jenis_hewan import Singa, Gajah, Elang, BurungKakatua
from bagian4_kandang import Kandang
from bagian5_kebun_binatang import KebunBinatang


def main():
    print("=" * 55)
    print("  🦁 SIMULASI KEBUN BINATANG – OOP PYTHON")
    print("=" * 55)

    # ── 1. Buat Kebun Binatang ────────────────────────────────
    kebun = KebunBinatang(nama="Ragunan Jaya", kota="Jakarta")

    # ── 2. Buat Kandang ───────────────────────────────────────
    kandang_darat  = Kandang(nama_kandang="Zona Darat",   kapasitas=3)
    kandang_udara  = Kandang(nama_kandang="Zona Terbang", kapasitas=3)

    # Tambah kandang ke kebun binatang
    print("\n📌 Menambahkan kandang...")
    kebun.tambah_kandang(kandang_darat)
    kebun.tambah_kandang(kandang_udara)

    # ── 3. Buat Hewan (Polymorphism: tiap objek punya perilaku sendiri) ──
    singa1   = Singa(nama="Simba",   umur=5)
    singa2   = Singa(nama="Nala",    umur=4)
    gajah1   = Gajah(nama="Dumbo",   umur=10)
    elang1   = Elang(nama="Garuda",  umur=3)
    kakatua1 = BurungKakatua(nama="Polly",  umur=2, kata_favorit="Polly mau makan!")
    kakatua2 = BurungKakatua(nama="Rio",    umur=1, kata_favorit="Halo semuanya!")

    # ── 4. Masukkan Hewan ke Kandang ─────────────────────────
    print("\n📌 Memasukkan hewan ke kandang...")
    kandang_darat.tambah_hewan(singa1)
    kandang_darat.tambah_hewan(singa2)
    kandang_darat.tambah_hewan(gajah1)

    kandang_udara.tambah_hewan(elang1)
    kandang_udara.tambah_hewan(kakatua1)
    kandang_udara.tambah_hewan(kakatua2)

    # Uji kapasitas penuh (SRP Kandang)
    singa_extra = Singa(nama="Mufasa", umur=8)
    kandang_darat.tambah_hewan(singa_extra)

    # ── 5. Tampilkan Info Semua Hewan ────────────────────────
    kebun.tampilkan_semua_info_hewan()

    # ── 6. Rawat Semua Hewan (Polymorphism beraksi) ──────────
    kebun.rawat_semua_hewan()

    # ── 7. Bersihkan Kandang ─────────────────────────────────
    kebun.bersihkan_semua_kandang()

    # ── 8. Laporan Akhir ─────────────────────────────────────
    kebun.laporan()


if __name__ == "__main__":
    main()
