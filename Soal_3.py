class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print(f" Pesanan {pesanan} telah ditambahkan ke antrian.")

    def dequeue(self):
        if len(self.antrian) == 0:
            print("Antrian kosong!")
        else:
            pesanan = self.antrian.pop(0)
            print(f" Pesanan {pesanan} telah diambil dari antrian.")

    def display_antrian(self):
        print("Antrian saat ini:")
        for i, pesanan in enumerate(self.antrian):
            print(f"{i+1}. {pesanan}")


if __name__ == "__main__":
    antrian = AntrianRestoran()

    while True:
        print("\nMenu:")
        print("1. Tambahkan pesanan baru")
        print("2. Ambil pesanan dari antrian")
        print("3. Tampilkan antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            pesanan = input("Masukkan pesanan baru: ")
            antrian.enqueue(pesanan)
        elif pilihan == "2":
            antrian.dequeue()
        elif pilihan == "3":
            antrian.display_antrian()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")