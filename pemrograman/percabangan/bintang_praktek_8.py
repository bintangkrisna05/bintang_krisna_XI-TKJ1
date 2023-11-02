#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5

# Input status persiapan proyek
status_persiapan = input("Status persiapan proyek (Siap/Tunda): ")

# Memeriksa status persiapan proyek
if status_persiapan.lower() == "siap":
    print("Proyek diluncurkan.")
elif status_persiapan.lower() == "tunda":
    print("Proyek ditunda.")
else:
    print("Status persiapan tidak valid. Harap masukkan 'Siap' atau 'Tunda'.")