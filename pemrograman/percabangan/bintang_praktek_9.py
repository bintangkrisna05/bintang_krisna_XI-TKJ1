#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5
#soal :Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek
tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek
diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."

# Mengambil input status persiapan proyek dari pengguna
status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ")

# Mengecek status persiapan proyek dan mencetak hasil sesuai dengan kondisi
if status_persiapan == "Siap":
    print("Proyek diluncurkan.")
elif status_persiapan == "Tunda":
    print("Proyek ditunda.")
else:
    print("Status persiapan tidak valid. Masukkan 'Siap' atau 'Tunda'.")