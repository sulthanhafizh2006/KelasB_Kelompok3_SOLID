class KebunBinatang:
    def __init__(self):
        self.kandang = []

    def tambah_hewan(self, hewan):
        self.kandang.append(hewan)

    def rawat_semua_hewan(self):
        for hewan in self.kandang:
            hewan.makan()
