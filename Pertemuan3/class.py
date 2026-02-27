# uji coba class simple

class kucing:
    def __init__(self, nama, warna): #konstruktor/init method
        self.nama = nama
        self.warna = warna

    def meong(self):
        return f"{self.nama} mengeong!"
    
kucing1 = kucing("Mimi", "Putih")
print(kucing1.meong())  # Output: Mimi mengeong!
print(f"Warna kucing {kucing1.nama} adalah {kucing1.warna}.")  # Output: Warna kucing Mimi adalah Putih.
