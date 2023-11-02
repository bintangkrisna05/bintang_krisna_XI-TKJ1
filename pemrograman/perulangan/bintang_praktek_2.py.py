#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5

# Mengambil input jarak pada minggu pertama (minggu ke-1)
jarak_minggu_pertama = float(input("Masukkan jarak pada minggu pertama (km): "))

# Mengambil input minggu ke-n yang ingin dihitung
n = int(input("Masukkan minggu ke berapa yang ingin dihitung: "))

# Inisialisasi variabel jarak pada minggu ke-n
jarak_minggu_n = jarak_minggu_pertama

# Menghitung jarak pada minggu ke-n menggunakan perulangan
for minggu in range(2, n + 1):
    jarak_minggu_n += 0.10 * jarak_minggu_n

# Mencetak jarak pada minggu ke-n
print(f"Jarak pada minggu ke-{n} adalah: {jarak_minggu_n:.2f} km")