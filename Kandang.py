class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def tampilkan_hewan(self):
        print("Daftar hewan di kandang:")
        for hewan in self.hewan_list:
            print("-", hewan.nama)

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")
