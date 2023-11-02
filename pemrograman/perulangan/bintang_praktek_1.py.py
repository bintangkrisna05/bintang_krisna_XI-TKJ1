#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5

# Mengambil input jumlah ayam bulan pertama (bulan ke-1)
jumlah_ayam_bulan_pertama = int(input("Masukkan jumlah ayam bulan pertama: "))

# Mengambil input bulan ke-n yang ingin dihitung
n = int(input("Masukkan bulan ke berapa yang ingin dihitung: "))

# Inisialisasi variabel jumlah ayam pada bulan ke-n
jumlah_ayam_bulan_n = jumlah_ayam_bulan_pertama

# Menghitung jumlah ayam pada bulan ke-n menggunakan perulangan
for bulan in range(2, n + 1):
    jumlah_ayam_bulan_n += 0.05 * jumlah_ayam_bulan_n

# Mencetak jumlah ayam pada bulan ke-n
print(f"Jumlah ayam pada bulan ke-{n} adalah: {jumlah_ayam_bulan_n:.2f}")