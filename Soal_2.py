import pandas as pd

data = {
    "Nama": ["Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"],
    "Algoritma dan Struktur Data 2": [90, 50, 65],
    "Matematika Numerik": [80, 60, 70]
}
df = pd.DataFrame(data)

print("Rata-rata nilai untuk setiap mata kuliah:")
print(df[['Algoritma dan Struktur Data 2', 'Matematika Numerik']].mean())

print("\nRata-rata nilai untuk setiap mahasiswa:")
print(df[['Algoritma dan Struktur Data 2', 'Matematika Numerik']].mean(axis=1))