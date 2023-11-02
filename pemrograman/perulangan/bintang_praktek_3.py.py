#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5

# Mengambil input nilai investasi pada tahun pertama (tahun ke-1)
nilai_investasi_tahun_pertama = float(input("Masukkan nilai investasi pada tahun pertama: "))

# Mengambil input tahun ke-n yang ingin dihitung
n = int(input("Masukkan tahun ke berapa yang ingin dihitung: "))

# Inisialisasi variabel nilai investasi pada tahun ke-n
nilai_investasi_tahun_n = nilai_investasi_tahun_pertama

# Menghitung nilai investasi pada tahun ke-n menggunakan perulangan
for tahun in range(2, n + 1):
    nilai_investasi_tahun_n += 0.06 * nilai_investasi_tahun_n

# Mencetak nilai investasi pada tahun ke-n
print(f"Nilai investasi pada tahun ke-{n} adalah: {nilai_investasi_tahun_n:.2f}")