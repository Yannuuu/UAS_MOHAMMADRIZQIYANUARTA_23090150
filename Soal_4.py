class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def information(self):
        print(f"Nama: {self.nama}")
        print(f"Warna: {self.warna}")
        print(f"Rasa: {self.rasa}")

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        super().information()
        print(f"Vitamin: {self.vitamin}")

mangga = Mangga("Mangga", "Kuning", "Manis", "Vitamin C")

print(mangga.nama)
print(mangga.warna)
print(mangga.rasa)
print(mangga.vitamin)

mangga.setNama("Mangga Matang")
print(mangga.nama)

mangga.setVitamin("Vitamin A")
print(mangga.vitamin)

mangga.information()