import Soal_3 

def main():
    antrian = Soal_3.AntrianRestoran()

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

if __name__ == "__main__":
    main()