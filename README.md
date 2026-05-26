# Latihan Analisis & Penerapan Prinsip SOLID
### Studi Kasus: Sistem Pengelolaan Kebun Binatang (Python)

Tugas kelompok ini dibuat untuk memenuhi mata kuliah **Pemrograman Berorientasi Objek**. Repositori ini berisi analisis kerusakan kode awal (pelanggaran prinsip SOLID) beserta solusi implementasinya menggunakan bahasa pemrograman Python yang dipecah per komponen prinsip.

---

## Anggota Kelompok

| No | Nama | NIM | Prinsip yang Dikerjakan | File |
| :---: | :--- | :---: | :--- | :--- |
| 1 | **Sulthan Hafizh Putra Agung** | **K3525013** | Single Responsibility Principle (SRP) | `srp.py` |
| 2 | **Zahra Faizza Kuncoroningrum** | **K3525017** | Open/Closed Principle (OCP) | `ocp.py` |
| 3 | **⁠Adibah Ruhil** | **K3525044** | Dependency Inversion Principle (DIP) | `dip.py` | 
| 4 | **Aksya Nayla** | **K3525047** | Liskov Substitution Principle (LSP) | `lsp.py` |
| 5 | **Allicya Nailah Fairuza** | **K3525048** |  Interface Segregation Principle (ISP) | `isp.py` |
| 6 | **Faris Rafiuddin Hannan** | **K3525058** |  Integrasi & Dokumentasi | `main.py` |

---

## Struktur Repository

```text
solid-kebunbinatang/
├── srp.py         # Implementasi Single Responsibility Principle
├── ocp.py         # Implementasi Open/Closed Principle
├── lsp.py         # Implementasi Liskov Substitution Principle
├── isp.py         # Implementasi Interface Segregation Principle
├── dip.py         # Implementasi Dependency Inversion Principle
├── main.py        # Integrasi dan pengujian semua prinsip SOLID
└── README.md      # Dokumentasi proyek

```

---

## Kode Awal (Bermasalah)

Berikut adalah kode dasar sebelum diterapkan prinsip SOLID. Kode ini memiliki tingkat ketergantungan yang tinggi dan desain objek yang kaku:

```python
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()

```

---

## Tabel Analisis Pelanggaran Prinsip SOLID

| Prinsip | Status | Detail Pelanggaran pada Kode Awal |
| --- | --- | --- |
| **SRP** | Dilanggar | `Hewan` menyimpan data sekaligus mendefinisikan perilaku spesifik. `Kandang` mengelola daftar hewan sekaligus bertanggung jawab atas aksi kebersihan (`bersihkan_kandang`). |
| **OCP** | Dilanggar | Method `terbang()` dikodekan secara kaku (*hardcoded*) di dalam kelas `Hewan`. Menambahkan perilaku bergerak baru memaksa modifikasi pada kelas yang sudah stabil. |
| **LSP** | Dilanggar | Subclass seperti `Anjing` atau `Ikan` yang mewarisi kelas `Hewan` dipaksa membawa fungsi `terbang()`, yang secara logis merusak kebenaran program saat dieksekusi. |
| **ISP** | Dilanggar | Semua jenis hewan dipaksa bergantung pada method `terbang()` meskipun hewan tersebut tidak memiliki kapabilitas fisik untuk terbang. |
| **DIP** | Dilanggar | Kelas tingkat tinggi `KebunBinatang` bergantung secara langsung (*tight coupling*) pada kelas konkret tingkat rendah `Kandang`, bukan pada sebuah abstraksi/interface. |

---

## Penjelasan & Solusi Perbaikan

### 1. Single Responsibility Principle (SRP)

> *"Setiap class harus memiliki satu, dan hanya satu, alasan untuk berubah."*

**Solusi:** Memisahkan tanggung jawab yang menumpuk menjadi kelas-kelas khusus yang fokus pada satu tugas:

* `Hewan`: Hanya bertanggung jawab menyimpan entitas data nama dan jenis.
* `AktivitasHewan`: Menangani perilaku fungsional hewan (seperti makan).
* `Kandang`: Khusus untuk manajemen struktur data daftar hewan.
* `PerawatanKandang`: Menangani logika kebersihan lingkungan kandang.
* `KebunBinatang`: Berperan murni sebagai koordinator alur perawatan.
*Lihat implementasi:* [`srp.py`](https://www.google.com/search?q=srp.py)

### 2. Open/Closed Principle (OCP)

> *"Class harus terbuka untuk ekstensi, tetapi tertutup untuk modifikasi."*

**Solusi:** Mengubah kelas `Hewan` menjadi sebuah *abstract base class* dengan method umum bernama `bergerak()`. Jika ingin menambah jenis hewan baru, kita hanya perlu mengekstensi kelas tersebut tanpa mengubah kode yang lama:

* `Burung` $\rightarrow$ implementasi `bergerak()` khusus untuk terbang.
* `Anjing` $\rightarrow$ implementasi `bergerak()` khusus untuk berlari.
* `Ikan`   $\rightarrow$ implementasi `bergerak()` khusus untuk berenang.
*Lihat implementasi:* [`ocp.py`](https://www.google.com/search?q=ocp.py)

### 3. Liskov Substitution Principle (LSP)

> *"Objek dari subclass harus dapat menggantikan superclass-nya tanpa merubah kebenaran dari program tersebut."*

**Solusi:** Memisahkan hierarki kelas berdasarkan kapabilitas riil dari objek hewan tersebut:

* `HewanDarat`: Memiliki method spesifik `berlari()`.
* `HewanTerbang`: Memiliki method spesifik `terbang()`.

Dengan demikian, tidak akan ada objek ikan atau anjing yang dipaksa mengeksekusi fungsi terbang.
*Lihat implementasi:* [`lsp.py`](https://www.google.com/search?q=lsp.py)

### 4. Interface Segregation Principle (ISP)

> *"Class tidak boleh dipaksa mengimplementasikan interface yang tidak digunakannya."*

**Solusi:** Memecah interface yang gemuk (*fat interface*) menjadi beberapa interface abstrak yang lebih kecil, modular, dan spesifik sesuai kebutuhan:

* `IBisaMakan`: Kontrak umum untuk semua makhluk hidup.
* `IBisaTerbang`: Kontrak khusus hanya untuk kelompok hewan udara.
* `IBisaBerenang`: Kontrak khusus hanya untuk kelompok hewan air.
*Lihat implementasi:* [`isp.py`](https://www.google.com/search?q=isp.py)

### 5. Dependency Inversion Principle (DIP)

> *"Modul tingkat tinggi tidak boleh bergantung pada modul tingkat rendah. Keduanya harus bergantung pada abstraksi."*

**Solusi:** Memutus ketergantungan langsung dengan mengintroduksi komponen abstraksi baru berupa interface `IKandang`:

* Kelas `KebunBinatang` kini hanya berinteraksi melalui interface `IKandang` (abstraksi).
* Kelas konkret `Kandang` mengimplementasikan cetak biru dari `IKandang`.

Fleksibilitas ini memungkinkan kita mengubah jenis implementasi kandang di masa depan tanpa merusak sistem di `KebunBinatang`.
*Lihat implementasi:* [`dip.py`](https://www.google.com/search?q=dip.py)

---

## Cara Menjalankan Program

### Prasyarat

* Python versi `3.7` ke atas.

### Langkah Eksekusi

```bash
# 1. Clone repositori ke komputer lokal
git clone [https://github.com/](https://github.com/)[username]/solid-kebunbinatang.git
cd solid-kebunbinatang

# 2. Jalankan berkas integrasi utama (Gabungan semua prinsip)
python main.py

# 3. Atau jalankan demonstrasi per berkas prinsip spesifik
python srp.py
python ocp.py
python lsp.py
python isp.py
python dip.py

```

---

## Alur Kerja Git Kelompok

Untuk menjaga kebersihan *history* commit, pengerjaan dilakukan menggunakan strategi *feature-branchinging*:

```bash
# 1. Pastikan repositori lokal sudah sinkron
git clone [https://github.com/](https://github.com/)[username]/solid-kebunbinatang.git
cd solid-kebunbinatang

# 2. Buat branch baru sesuai dengan bagian tugas masing-masing
git checkout -b fitur/srp         # Untuk Anggota 1
git checkout -b fitur/ocp         # Untuk Anggota 2 
git checkout -b fitur/lsp         # Untuk Anggota 3
git checkout -b fitur/isp         # Untuk Anggota 4
git checkout -b fitur/dip         # Untuk Anggota 5
git checkout -b fitur/main        # Untuk Anggota 6

# 3. Lakukan proses coding, simpan, dan commit perubahan Anda
git add .
git commit -m "Add [PRINSIP] implementation and fix violations"

# 4. Push branch fitur Anda ke GitHub remote
git push origin fitur/[nama-fitur-anda]

# 5. Buka repositori di browser dan buat Pull Request (PR) ke branch 'main'

```

```

```
