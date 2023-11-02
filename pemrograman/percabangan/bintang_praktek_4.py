#Nama           :Bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5

# Input total belanjaan dan status anggota
total_belanjaan = float(input("Masukkan total belanjaan: "))
status_anggota = input("Apakah Anda anggota biasa (B) atau anggota premium (P)? ").upper()

# Inisialisasi variabel diskon
diskon = 0

# Hitung diskon berdasarkan aturan
if status_anggota == "P":
    if total_belanjaan > 500000:
        diskon = total_belanjaan * 0.15
    else:
        diskon = total_belanjaan * 0.10
elif status_anggota == "B":
    if total_belanjaan > 300000:
        diskon = total_belanjaan * 0.07

# Cetak jumlah diskon
print(f"Jumlah diskon yang Anda dapatkan: Rp {diskon:.2f}")