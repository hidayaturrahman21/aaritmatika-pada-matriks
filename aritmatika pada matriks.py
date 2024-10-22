# Input ukuran matriks
baris = int(input("Masukkan jumlah baris matriks: "))
kolom = int(input("Masukkan jumlah kolom matriks: "))

# Input matriks A
print("Masukkan elemen matriks A:")
matriks_A = []
for i in range(baris):
    row = []
    for j in range(kolom):
        elemen = float(input(f"Elemen A[{i + 1}][{j + 1}]: "))
        row.append(elemen)
    matriks_A.append(row)

# Input matriks B
print("Masukkan elemen matriks B:")
matriks_B = []
for i in range(baris):
    row = []
    for j in range(kolom):
        elemen = float(input(f"Elemen B[{i + 1}][{j + 1}]: "))
        row.append(elemen)
    matriks_B.append(row)

# Penjumlahan matriks
print("\nHasil Penjumlahan Matriks A dan B:")
matriks_tambah = []
for i in range(baris):
    row = []
    for j in range(kolom):
        row.append(matriks_A[i][j] + matriks_B[i][j])
    matriks_tambah.append(row)
print(matriks_tambah)

# Pengurangan matriks
print("\nHasil Pengurangan Matriks A dan B:")
matriks_kurang = []
for i in range(baris):
    row = []
    for j in range(kolom):
        row.append(matriks_A[i][j] - matriks_B[i][j])
    matriks_kurang.append(row)
print(matriks_kurang)

# Perkalian matriks (pastikan ukuran sesuai)
if kolom == baris:  # Cek jika bisa dikalikan
    print("\nHasil Perkalian Matriks A dan B:")
    matriks_kali = []
    for i in range(baris):
        row = []
        for j in range(baris):
            elemen = 0
            for k in range(kolom):
                elemen += matriks_A[i][k] * matriks_B[k][j]
            row.append(elemen)
        matriks_kali.append(row)
    print(matriks_kali)
else:
    print("\nMatriks A dan B tidak dapat dikalikan.")

# Transpos matriks A
print("\nTranspos Matriks A:")
matriks_transpos = []
for j in range(kolom):
    row = []
    for i in range(baris):
        row.append(matriks_A[i][j])
    matriks_transpos.append(row)
print(matriks_transpos)
