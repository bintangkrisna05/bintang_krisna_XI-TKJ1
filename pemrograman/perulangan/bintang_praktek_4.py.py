#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5

# Mengambil input sisa apel pada hari pertama (hari ke-1)
sisa_apel_hari_pertama = float(input("Masukkan sisa apel pada hari pertama: "))

# Mengambil input hari ke-n yang ingin dihitung
n = int(input("Masukkan hari ke berapa yang ingin dihitung: "))

# Inisialisasi variabel sisa apel pada hari ke-n
sisa_apel_hari_n = sisa_apel_hari_pertama

# Menghitung sisa apel pada hari ke-n menggunakan perulangan
for hari in range(2, n + 1):
    sisa_apel_hari_n -= 0.10 * sisa_apel_hari_n

# Mencetak sisa apel pada hari ke-n
print(f"Sisa apel pada hari ke-{n} adalah: {sisa_apel_hari_n:.2f}")