# program menghitung gaji karyawan

def informasi_karyawan(nama, nim, jabatan):
    print(f"\nSelamat Datang,{nama}")
    print(f"Nim     : {nim}")
    print(f"jabatan : {jabatan
                       if jabatan 
                       else "karyawan"}")
    print("\n")
# saya membuat jabatan kata "karyawan" sebagai kata default

def login():
    print("==== LOGIN KARYAWAN ====")
    nama = input("Masukkan Nama :")
    nim = input("Masukkan Nim :")
    jabatan = input("Masukkan Jabatan :")
    print("========================")
    return nama, nim, jabatan

def input_angka(pesan):
    while True:
        input_data = input(pesan)
        return float (input_data)
    
def hitung_gaji(jam_kerja, tarif_kerja):
    gaji = jam_kerja * tarif_kerja
    if jam_kerja > 160:
        bonus = 0.1 * gaji
        total_gaji = gaji + bonus
        print("Anda mendapatkan bonus")
    else:
        total_gaji = gaji
    return total_gaji

nama, nim, jabatan = login()
informasi_karyawan(nama, nim, jabatan)

while True:
    print("==== Menghitung Gaji ====")

    jam_kerja = input_angka("masukkan jumlah jam kerja:")
    tarif_kerja = input_angka("masukkan tarif kerja:")

    total_gaji = hitung_gaji(jam_kerja, tarif_kerja)
    print(f"total gaji yang diterima: Rp{total_gaji}")  

    pilihan = input("Apakah anda ingin menghitung gaji lagi? (y/t): ").lower()
    if pilihan != 'y':
        print("Program selesai.")
        break
