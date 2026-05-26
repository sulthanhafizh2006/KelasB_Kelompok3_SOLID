# Simulasi Kebun Binatang – OOP Python

Proyek tugas kelompok simulasi kebun binatang menggunakan konsep **Object-Oriented Programming (OOP)** dalam Python.

---

## Pembagian Tugas Anggota

| Bagian | File | Tanggung Jawab | Anggota |
|--------|------|----------------|---------|
| 1 | `bagian1_hewan.py` | Abstract Base Class `Hewan` | |
| 2 | `bagian2_kategori_hewan.py` | Subclass `HewanDarat` & `HewanTerbang` | |
| 3 | `bagian3_jenis_hewan.py` | Subclass konkret: Singa, Gajah, Elang, Kakatua |  |
| 4 | `bagian4_kandang.py` | Class `Kandang` |  |
| 5 | `bagian5_kebun_binatang.py` | Class `KebunBinatang` | |
| 6 | `bagian6_main.py` | Main program / Runner | |

---

## Prinsip OOP yang Diterapkan

### 1. Encapsulation
- Semua atribut di setiap kelas bersifat **privat** (`self.__nama`)
- Akses hanya melalui **property** (`@property`)
- Contoh: `Hewan.__nama`, `Kandang.__hewan_list`, `KebunBinatang.__kandang_list`

### 2. Abstraction
- Class `Hewan` bersifat **abstrak** (tidak bisa diinstansiasi langsung)
- Method abstrak `bergerak()` dan `bersuara()` wajib diimplementasikan subclass
- Menggunakan modul `abc` (Abstract Base Class)

### 3. Inheritance (Pewarisan)
- `HewanDarat` dan `HewanTerbang` mewarisi `Hewan`
- `Singa`, `Gajah` mewarisi `HewanDarat`
- `Elang`, `BurungKakatua` mewarisi `HewanTerbang`

```
Hewan (Abstract)
├── HewanDarat
│   ├── Singa
│   └── Gajah
└── HewanTerbang
    ├── Elang
    └── BurungKakatua
```

### 4. Polymorphism
- Setiap subclass mengimplementasikan `bergerak()` dan `bersuara()` secara berbeda
- `KebunBinatang.rawat_semua_hewan()` memanggil method yang sama pada semua objek — hasilnya berbeda sesuai jenisnya

### 5. Single Responsibility Principle (SRP)
- `Hewan` → mendefinisikan perilaku dasar hewan
- `Kandang` → mengelola koleksi hewan & kebersihan
- `KebunBinatang` → mengelola kandang & aktivitas harian

---

## Struktur Proyek

```
kebun_binatang/
├── bagian1_hewan.py             # Abstract base class
├── bagian2_kategori_hewan.py    # HewanDarat & HewanTerbang
├── bagian3_jenis_hewan.py       # Singa, Gajah, Elang, Kakatua
├── bagian4_kandang.py           # Class Kandang
├── bagian5_kebun_binatang.py    # Class KebunBinatang
├── bagian6_main.py              # Main program
└── README.md
```

---

## Cara Menjalankan

```bash
# Clone repository
git clone https://github.com/username/kebun-binatang-oop.git
cd kebun-binatang-oop

# Jalankan program (Python 3.10+)
python bagian6_main.py
```

---

## Cara Upload ke GitHub (per anggota)

```bash
# 1. Clone repo kelompok
git clone https://github.com/username/kebun-binatang-oop.git

# 2. Masuk folder
cd kebun-binatang-oop

# 3. Tambahkan file bagian kamu (misal anggota 3)
git add bagian3_jenis_hewan.py

# 4. Commit
git commit -m "Tambah bagian3: Singa, Gajah, Elang, Kakatua [Anggota 3]"

# 5. Push
git push origin main
```

---

## Perbaikan dari Kode Asli

| Masalah Kode Asli | Solusi |
|-------------------|--------|
| `terbang()` ada di semua hewan | Dipindah ke subclass `HewanTerbang` saja |
| Tidak ada inheritance | Dibuat hierarki: `Hewan → HewanDarat/Terbang → Konkret` |
| Tidak ada abstraksi | `Hewan` dijadikan abstract class dengan `ABC` |
| Tidak ada polymorphism | `bergerak()` & `bersuara()` dioverride tiap subclass |
| Atribut publik semua | Semua atribut dijadikan privat + property |
| SRP dilanggar | Setiap class punya satu tanggung jawab jelas |
