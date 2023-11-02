#Nama           :Bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5
#Soal           :Deskripsi Pekerjaan: Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.
#Soal 2         :Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jika estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat waktu," jika tidak, program harus mencetak "Terlambat."


from datetime import datetime

# Meminta input estimasi waktu selesai proyek (dalam format tanggal)
estimasi_selesai_str = input("Masukkan estimasi waktu selesai proyek (yyyy-mm-dd): ")

# Meminta input tanggal target selesai (dalam format tanggal)
tanggal_target_str = input("Masukkan tanggal target selesai (yyyy-mm-dd): ")

# Mengubah string input menjadi objek datetime
estimasi_selesai = datetime.strptime(estimasi_selesai_str, '%Y-%m-%d')
tanggal_target = datetime.strptime(tanggal_target_str, '%Y-%m-%d')

# Memeriksa apakah estimasi_selesai lebih awal atau sama dengan tanggal_target
if estimasi_selesai <= tanggal_target:
    print("Tepat waktu")
else:
    print("Terlambat")