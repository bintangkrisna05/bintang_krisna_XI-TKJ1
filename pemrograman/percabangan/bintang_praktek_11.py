#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5

# Mengambil input nilai performa karyawan (1-5)
performa = int(input("Masukkan nilai performa karyawan (1-5): "))

# Mengambil input gaji tahunan karyawan
gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

# Menghitung bonus tahunan berdasarkan nilai performa
if performa == 5:
    bonus = 0.20 * gaji_tahunan
elif performa == 4:
    bonus = 0.10 * gaji_tahunan
elif performa == 3:
    bonus = 0.05 * gaji_tahunan
elif performa == 2:
    bonus = 0.02 * gaji_tahunan
elif performa == 1:
    bonus = 0  # Tidak ada bonus untuk performa 1
else:
    print("Nilai performa tidak valid. Masukkan nilai dari 1 hingga 5.")
    bonus = 0

# Mencetak jumlah bonus
if bonus > 0:
    print(f"Bonus tahunan karyawan adalah: ${bonus:.2f}")
else:
    print("Karyawan tidak memenuhi syarat untuk bonus tahunan.")