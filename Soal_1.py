data_mahasiswa =[]

def tambah_data():
    nim = input("Masukan NIM: ")
    nama = input("Masukan Nama: ")
    data_mahasiswa.append({"NIM": nim, "Nama": nama})
    tambah = input("Ingin tambah lagi? (ya/tidak): ")
    if tambah.lower() == "ya":
        tambah_data()
    else:
        tampilkan_data()

def tampilkan_data():
    print("data mahasiswa: ")
    for i, data in enumerate(data_mahasiswa):
        print(f"{i+1}. NIM: {data['NIM']}, Nama: {data['Nama']}")

def start():
    print()
    tambah_data()

start()