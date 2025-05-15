from tabulate import tabulate

data_mobil = {
    "MB001": {"merk": "Toyota Avanza", "tahun": 2020, "warna": "Hitam", "harga": 350000, "status": "Tersedia"},
    "MB002": {"merk": "Honda Brio", "tahun": 2019, "warna": "Merah", "harga": 300000, "status": "Disewa"},
    "MB003": {"merk": "Suzuki Ertiga", "tahun": 2021, "warna": "Putih", "harga": 320000, "status": "Tersedia"},
    "MB004": {"merk": "Daihatsu Xenia", "tahun": 2022, "warna": "Abu-abu", "harga": 340000, "status": "Tersedia"},
    "MB005": {"merk": "Mitsubishi Xpander", "tahun": 2023, "warna": "Silver", "harga": 400000, "status": "Disewa"},
}

def tampilkan_data():
    print("\n=== DAFTAR MOBIL ===")
    if not data_mobil:
        print("Tidak ada data mobil.")
        return

    table = []
    for kode, m in data_mobil.items():
        table.append([kode, m["merk"], m["tahun"], m["warna"], f"Rp {m['harga']:,}", m["status"]])
    
    headers = ["Kode", "Merk", "Tahun", "Warna", "Harga/Hari", "Status"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

def tambah_data():
    print("\n=== TAMBAH MOBIL ===")
    kode = input("Masukkan kode mobil unik (contoh MB004): ").upper()
    if kode in data_mobil:
        print("Kode sudah ada!")
        return

    try:
        merk = input("Merk Mobil       : ")
        tahun = int(input("Tahun            : "))
        warna = input("Warna            : ")
        harga = int(input("Harga per hari   : "))
        status = input("Status (Tersedia/Disewa): ").capitalize()
        if status not in ['Tersedia', 'Disewa']:
            raise ValueError("Status harus 'Tersedia' atau 'Disewa'")
    except ValueError as e:
        print("Input tidak valid:", e)
        return

    data_mobil[kode] = {
        "merk": merk,
        "tahun": tahun,
        "warna": warna,
        "harga": harga,
        "status": status
    }
    print("Mobil berhasil ditambahkan.")

def ubah_data():
    print("\n=== UBAH DATA MOBIL ===")
    kode = input("Masukkan kode mobil: ").upper()
    if kode not in data_mobil:
        print("Data tidak ditemukan.")
        return

    merk = input("Merk baru (kosongkan jika tidak diubah): ")
    tahun = input("Tahun baru: ")
    warna = input("Warna baru: ")
    harga = input("Harga baru: ")
    status = input("Status baru: ")

    if merk:
        data_mobil[kode]["merk"] = merk
    if tahun:
        data_mobil[kode]["tahun"] = int(tahun)
    if warna:
        data_mobil[kode]["warna"] = warna
    if harga:
        data_mobil[kode]["harga"] = int(harga)
    if status:
        data_mobil[kode]["status"] = status.capitalize()

    print("Data berhasil diperbarui.")

def hapus_data():
    print("\n=== HAPUS MOBIL ===")
    kode = input("Masukkan kode mobil: ").upper()
    if kode in data_mobil:
        konfirmasi = input(f"Yakin ingin menghapus mobil {kode}? (y/n): ").lower()
        if konfirmasi == 'y':
            del data_mobil[kode]
            print("Data mobil berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Kode tidak ditemukan.")

def sewa_mobil():
    print("\n=== SEWA MOBIL ===")
    kode = input("Masukkan kode mobil: ").upper()
    if kode not in data_mobil:
        print("Mobil tidak ditemukan.")
        return
    if data_mobil[kode]["status"].lower() == "disewa":
        print("Mobil sedang disewa.")
        return

    data_mobil[kode]["status"] = "Disewa"
    print("Mobil berhasil disewa.")

def kembalikan_mobil():
    print("\n=== KEMBALIKAN MOBIL ===")
    kode = input("Masukkan kode mobil: ").upper()
    if kode not in data_mobil:
        print("Mobil tidak ditemukan.")
        return
    if data_mobil[kode]["status"].lower() == "tersedia":
        print("Mobil belum disewa.")
        return

    data_mobil[kode]["status"] = "Tersedia"
    print("Mobil berhasil dikembalikan.")

def cari_mobil():
    print("\n=== CARI MOBIL ===")
    keyword = input("Masukkan merk atau tahun mobil: ").lower()
    hasil = {
        kode: mobil for kode, mobil in data_mobil.items()
        if keyword in mobil["merk"].lower() or keyword in str(mobil["tahun"])
    }

    if not hasil:
        print("Tidak ada hasil ditemukan.")
    else:
        table = []
        for kode, m in hasil.items():
            table.append([kode, m["merk"], m["tahun"], m["warna"], f"Rp {m['harga']:,}", m["status"]])
        headers = ["Kode", "Merk", "Tahun", "Warna", "Harga/Hari", "Status"]
        print(tabulate(table, headers=headers, tablefmt="grid"))

def menu_utama():
    while True:
        print("\n=== MENU RENTAL MOBIL ===")
        print("1. Tampilkan Data Mobil")
        print("2. Tambah Mobil")
        print("3. Ubah Data Mobil")
        print("4. Hapus Mobil")
        print("5. Sewa Mobil")
        print("6. Kembalikan Mobil")
        print("7. Cari Mobil")
        print("8. Keluar")

        pilihan = input("Pilih menu (1-8): ")
        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            sewa_mobil()
        elif pilihan == "6":
            kembalikan_mobil()
        elif pilihan == "7":
            cari_mobil()
        elif pilihan == "8":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    menu_utama()
