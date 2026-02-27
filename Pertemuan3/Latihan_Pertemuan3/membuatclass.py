class Negara:
    def __init__(self, nama, populasi, luas):
        self.nama = nama
        self.populasi = populasi
        self.luas = luas

    def perluas_negara(self, luasbaru):
        self.luas += luasbaru
        return self.luas

    def perkembangan_populasi(self, populasibaru):
        self.populasi += populasibaru
        return self.populasi

negara1 = Negara("Indonesia", 300000000, 19000000)
negara2 = Negara("ilyasland", 1, 100)
negara3 = Negara("ferelia", 1 , 20)
print(negara1.perluas_negara(50000))
print(negara2.populasi)

