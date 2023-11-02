#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5

# Input nilai performa karyawan
performa = int(input("Masukkan nilai performa karyawan (1 hingga 5): "))

# Input gaji tahunan karyawan
gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

# Menggunakan percabangan ternary untuk menghitung bonus berdasarkan performa
bonus = (
    0.2 * gaji_tahunan if performa == 5 else
    0.1 * gaji_tahunan if performa == 4 else
    0.05 * gaji_tahunan if performa == 3 else
    0.02 * gaji_tahunan if performa == 2 else
    0  # Performa 1 tidak mendapatkan bonus
)

# Menampilkan hasil perhitungan bonus
if bonus > 0:
    print(f"Bonus tahunan karyawan adalah: ${bonus:.2f}")
else:
    print("Karyawan tidak memenuhi syarat untuk mendapatkan bonus.")