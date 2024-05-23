import modulHW8 as modul

while True:
    print('='*25) 
    print("SELAMAT DATANG DI PROGRAM MANAJEMEN STOK BARANG")
    print('='*25) 
    modul.menu()
    pilihan = int(input('Masukan Pilihan : '))

    if pilihan == 1:
        modul.tambah()
    if pilihan == 2:
        modul.edit()
    if pilihan == 3:
        modul.hapus()
    if pilihan == 4:
        modul.cari_data()
    if pilihan == 5:
        modul.data_barang()
    if pilihan == 6:
        modul.jumlah_data_barang()
    if pilihan == 7:
        print('='*25)  
        print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI")  
        print('='*25)
        exit()  