class Hewan:
    def __init__(self, nama):
        self.nama = nama

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
        print(f"{hewan.nama} ditambahkan ke kandang.")

    def tampilkan_hewan(self):
        print("Daftar hewan di kandang:")
        for hewan in self.hewan_list:
            print("-", hewan.nama)

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

# Program utama
kandang = Kandang()

hewan1 = Hewan("Singa")
hewan2 = Hewan("Gajah")

kandang.tambah_hewan(hewan1)
kandang.tambah_hewan(hewan2)

kandang.tampilkan_hewan()

kandang.bersihkan_kandang()
