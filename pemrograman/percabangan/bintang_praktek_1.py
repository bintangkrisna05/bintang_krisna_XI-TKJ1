#Nama           :Bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5
#Soal           :Deskripsi Pekerjaan: Di sebuah toko online, Anda bertanggung jawab untuk menghitung diskon berdasarkan jumlah total belanjaan pelanggan.
#Soal 1         :Buat program Python yang mengambil total belanjaan pelanggan dan memberikan diskon berdasarkan aturan berikut: Jika total belanjaan lebih dari 500.000, berikan diskon 10%. Jika total belanjaan antara 300.000 dan 500.000, berikan diskon 5%. Jika total belanjaan kurang dari 300.000, tidak ada diskon.


# Meminta input total belanjaan dari pelanggan
total_belanjaan = float(input("Masukkan total belanjaan pelanggan: "))

# Inisialisasi variabel diskon
diskon = 0

# Memeriksa aturan diskon
if total_belanjaan > 500000:
    diskon = 0.10  # Diskon 10% untuk total belanjaan lebih dari 500.000
elif 300000 <= total_belanjaan <= 500000:
    diskon = 0.05  # Diskon 5% untuk total belanjaan antara 300.000 dan 500.000

# Menghitung jumlah diskon
jumlah_diskon = total_belanjaan * diskon

# Menghitung total pembayaran setelah diskon
total_pembayaran = total_belanjaan - jumlah_diskon

# Menampilkan hasil
print(f"Total belanjaan: {total_belanjaan} IDR")
print(f"Diskon yang diberikan: {diskon*100}%")
print(f"Jumlah diskon: {jumlah_diskon} IDR")
print(f"Total pembayaran setelah diskon: {total_pembayaran} IDR")