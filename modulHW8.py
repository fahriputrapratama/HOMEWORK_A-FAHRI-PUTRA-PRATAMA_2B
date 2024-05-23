def menu ():
    print('='*25)
    print ('1. Tambah Data Barang')
    print ('2. Edit Data')
    print ('3. Hapus Data Barang')
    print ('4. Cari Barang')
    print ('5. Tampilkan Data Barang')
    print ('6. Tampilkan Jumlah Data')
    print ('7. Keluar')
    print('='*25)


inventory = []
def tambah ():
    nama = input('Masukan Nama Barang : ')
    stok = input('Masukan Stok Barang : ')
    data_baru = {'barang':nama,'stok':stok}
    inventory.append(data_baru)
    print('='*25) 

def edit():
    nomor_barang = int(input("Edit Data Index ke : "))
    if 1 <= nomor_barang <= len(inventory):
        nomor_index = nomor_barang - 1
        barang = inventory[nomor_index]
        barang['barang'] = input("Masukkan nama : ")
        barang['stok'] = int(input("Masukkan stok : "))
        print("Data barang berhasil diubah.")
        print('='*25) 
    else:
        print("Index barang tidak ditemukan.")
        print('='*25) 


def hapus():
    hapus = int(input('Hapus Data Index Ke : '))
    if inventory:
        if 1 <= hapus <= len(inventory):
            del inventory[hapus - 1]
            print('='*25) 
            print("Data barang berhasil dihapus.")
            print('='*25) 
        else:
            print("Index barang tidak ditemukan.")
            print('='*25) 
    else:
        print('Data barang kosong.')
        print('='*25) 

def cari_data():
    kata = input("Cari Nama Barang: ")
    if inventory:
        ditemukan = False
        for barang in inventory:
            if kata.lower() in barang['barang'].lower():
                print("=== HASIL PENCARIAN ===")
                print(f"- {barang['barang']} stock {barang['stok']}")
                ditemukan = True
        if not ditemukan:
            print("Barang tidak ditemukan.")
    else:
        print("Barang tidak ditemukan.")

def data_barang():
    print("=== Toko Elektronik ===")
    if inventory:
        print("=== DATA BARANG ==")
        for item in inventory:
            print(f"- {item['barang']} stock {item['stok']}")
    else:
        print("=== DATA BARANG KOSONG ===")

def jumlah_data_barang():
    print(f"Jumlah Data Tersimpan: {len(inventory)} Barang")

