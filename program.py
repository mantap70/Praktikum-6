# Program untuk mengelola daftar nilai mahasiswa

data_mahasiswa = {}

def tambah(nama, nilai):
    """Menambah data mahasiswa."""
    if nama in data_mahasiswa:
        print(f"Data mahasiswa dengan nama {nama} sudah ada!")
    else:
        data_mahasiswa[nama] = nilai
        print(f"Data mahasiswa {nama} berhasil ditambahkan.")

def tampilkan():
    """Menampilkan semua data mahasiswa."""
    if data_mahasiswa:
        print("\nDaftar Nilai Mahasiswa:")
        for nama, nilai in data_mahasiswa.items():
            print(f"Nama: {nama}, Nilai: {nilai}")
    else:
        print("\nTidak ada data mahasiswa.")

def hapus(nama):
    """Menghapus data mahasiswa berdasarkan nama."""
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data mahasiswa {nama} berhasil dihapus.")
    else:
        print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

def ubah(nama, nilai_baru):
    """Mengubah nilai mahasiswa berdasarkan nama."""
    if nama in data_mahasiswa:
        data_mahasiswa[nama] = nilai_baru
        print(f"Data mahasiswa {nama} berhasil diubah.")
    else:
        print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

# Menu interaktif
while True:
    print("\nPilih opsi:")
    print("1. Tambah data mahasiswa")
    print("2. Tampilkan data mahasiswa")
    print("3. Hapus data mahasiswa")
    print("4. Ubah data mahasiswa")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        nilai = input("Masukkan nilai mahasiswa: ")
        tambah(nama, nilai)
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        nilai_baru = input("Masukkan nilai baru: ")
        ubah(nama, nilai_baru)
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")