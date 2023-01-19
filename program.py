def menu():
    import os
    os.system ("CLS")
    print ("\n<=============== SELAMAT DATANG DI PROGRAM PERDIG ===============>")
    print ("\nPilih daftar menu untuk mengakses program :\n")
    print("""
            ======================================
            | Nomer | Menu                       |
            ======================================
            |   1   | Lihat Daftar Buku          |
            |   2   | Cari Buku                  |
            |   3   | Tambahkan Data Buku        |
            |   4   | Ubah Data Buku             |
            |   5   | Hapus Data Buku            |
            |   6   | Lihat Daftar Peminjam Buku |
            |   7   | Tambah Peminjam Buku       |
            |   8   | Hapus Data Peminjaman Buku |
            |   11  | Urutkan dari A-Z           |
            |   9   | Keluar                     |
            ======================================
            """)
 
    kode = int(input("\nMasukkan kode menu yang ingin diakses : "))
    pilihmenu(kode)

def pilihmenu(p):
    if p==1:
        daftarbuku()
    elif p==2:
        caridata()
    elif p==3:
        tambahdata()
    elif p==4:
        ubahdata()
    elif p==5:
        hapusdata()
    elif p==6:
        daftarpeminjam()
    elif p==7:
        tambahpeminjam()
    elif p==8:
        hapuspeminjam()
    elif p==11:
        sorting()
    elif p==9:
        print("\n[Anda telah keluar dari program]")
    else:
        print("\n[Masukkan Input Yang telah disediakan!]")

def daftarbuku():
    import os
    os.system("CLS")
    print("\nHasil dari Sorting dari A-Z : ")
    bukadata = open("daftarbuku.txt","r")
    isi = bukadata.readlines()
    #isi.sort()
    if len(isi) == 0:
        print("\n[Data tidak tersedia]")
    else :
        no = "No"
        Judul = "Judul"
        Pengarang = "Pengarang"
        terbit = "Tahun Terbit"
        print("="*61)
        print(f"{no:2} | {Judul:10} | {Pengarang:15} | {terbit:23} |")
        print("="*61)
        
        for index,content in enumerate(isi):
            pecah = content.split(",")
            A = pecah[0]
            B = pecah[1]
            C = pecah[2].replace("\n","")
            print(f"{index+1:2} | {A:10} | {B:15} | {C:20}\n", end="")  
            
        print("="*61)
    print("\nTekan [ENTER] untuk kembali ke menu.")
    bukadata.close()
    input()
    menu()

def caridata():
    import os
    os.system("CLS")
    print("\n           - Pencarian Buku -")
    cari = input("\nMasukkan Judul buku yang ingin dicari : ")
    bukadata = open("daftarbuku.txt","r")
    isi = bukadata.readlines()
    isi.sort()

    print("\n======================================")
    print(" NAMA | JUDUL BUKU | Tahun Terbit    |")
    print("======================================")
    i=1
    for data_buku in isi:
            pecah = data_buku.split(",")
            if pecah[0] == cari:
                print ("\n"+pecah[0]+" | "+ pecah [1]+" | "+ pecah[2], end=" ")
                i += 1
    print("\n======================================")

    print("\n\nTekan [ENTER] untuk kembali ke menu.")
    bukadata.close()
    input()
    menu()

def tambahdata():
    import os
    os.system("CLS")
    print("\n    - Tambah Buku -")
    print("\nMasukkan data buku baru")
    judul = input("Judul Buku : ")
    penulis = input("Penulis Buku : ")
    tahun = input("Tahun Terbit : ")
    bukadata = open("daftarbuku.txt","a")
    bukadata.writelines([judul+","+penulis+","+tahun+ "\n"])
    bukadata.close()

    print("\nIngin menambahkan buku lagi? (Y/N)", end=" ")
    tmbhdata = input(" : ")
    if tmbhdata == "y" or tmbhdata == "Y":
        tambahdata()
    else :
        print("\nTekan [ENTER] Untuk kembali ke menu")
        input()
        menu()

def ubahdata():
    import os
    os.system("CLS")
    print("\n           - Ubah Data Buku -")
    baru = input("\nMasukkan Judul buku yang ingin diperbarui : ")
    print("\nMasukkan data baru")
    judulbr = input("judul Buku : ")
    penulisbr = input("Penulis Buku : ")
    tahunbr = input("Tahun terbit : ")
    bukadata = open("daftarbuku.txt")
    isi = bukadata.readlines()

    i=0
    for data_buku in isi:
            pecah = data_buku.split(",")
            if pecah[0] == baru:
                pecah[0] = judulbr
                pecah[1] = penulisbr
                pecah[2] = tahunbr+"\n"
                xg = ",".join(pecah)
                isi[1]=xg
            i += 1

    bukadata = open("daftarbuku.txt","w")
    isi = bukadata.writelines(isi)
    print("\n[Data Buku Berhasil Diubah]")
    bukadata.close()
    print("\nIngin mengubah data buku lagi? (Y/N)", end=" ")
    ubhdata = input(" : ")
    if ubhdata == "y" or ubhdata == "Y":
        ubahdata()
    else :
        print("\nTekan [ENTER] untuk kembali ke menu")
        input()
        menu()

def hapusdata() :
    import os
    os.system("CLS")
    print("\n           -Hapus Data Buku -")
    bukadata = open("daftarbuku.txt")
    output = []
    str = input("\nMasukkan judul buku yang di hapus : ")
    for hps in bukadata:
        if not hps.startswith(str):
            output.append(hps)
    
    bukadata = open("daftarbuku.txt.","w")
    bukadata.writelines(output)
    print("\n[Data Buku Telah Terhapus!]")
    bukadata.close()
    print("\nIngin menghapus data buku lagi? (Y/N)", end=" ")
    hpsdata = input(" : ")
    if hpsdata == "y" or hpsdata == "Y":
        hapusdata
    else :
        print("\nTekan [ENTER] untuk kembali ke menu")
        input()
        menu()

def daftarpeminjam():
    import os
    os.system("CLS")
    print("\n\t- Daftar peminjam buku -")
    bukadata = open("daftarpeminjam.txt","r")
    isi = bukadata.readlines()
    isi.sort()
    if len(isi) == 0:
        print("\n[Data Tidak Tersedia]")
    else :
        print("\n==========================================")
        print("NO | NAMA | JUDUL BUKU | TGL.PEMINAJAMAN |")
        print("==========================================")
        i=1
        for data_buku in isi:
            pecah = data_buku.split(",")
            print("\n" + str(i) + ".",end=" ")
            print("| "+pecah[0]+" | "+ pecah[1]+" | "+ pecah[2])
            i += 1
        print("\nTekan [ENTER] untuk kembali ke menu")
        bukadata.close()
        input()
        menu()

def tambahpeminjam():
    import os
    os.system("CLS")
    print("\n   - Tambah Peminjam Buku -")
    print("\nMasukkan data peminjam buku")
    nama = input("Nama         :")
    judul = input("Judul Buku     :")
    tanggal = input("Tanggal Peminjaman : ")
    bukadata = open("daftarpeminjam.txt","a")
    bukadata.writelines([nama+","+judul+","+tanggal+ "\n"])
    bukadata.close()

    print("\nIngin menambahkan data peminjam lagi? (Y/N", end=" ")
    tmbhpeminjam = input(" : ")
    if tmbhpeminjam == "y" or tmbhpeminjam == "Y":
        tambahpeminjam()
    else : 
        print("\nTekan [ENTER] untuk kembali ke menu")
        input()
        menu()

def hapuspeminjam():
    import os
    os.system("CLS")
    print("\n          - Hapus Data Peminjam Buku -")
    bukadata = open("daftarpeminjam.txt")
    output = []
    str = input("\nMasukkan Nama Peminjam yang Ingin Dihapus : ")
    for hps in bukadata:
        if not hps.startswith(str):
            output.append(hps)

    bukadata = open("daftarpeminjam.txt.","w")
    bukadata.writelines(output)
    print("\n[Data Peminjam Telah Terhapus")
    bukadata.close()
    print("\nIngin menghapus data peminjam lagi (Y/N)", end=" ")
    hpspeminjam = input(" : ")
    if hpspeminjam == "y" or hpspeminjam == "Y":
        hapuspeminjam()
    else :
        print("\nTekan [ENTER] untuk kembali ke menu")
        input()
        menu()

def sorting():
    import os
    os.system("CLS")
    print("\nHasil dari Sorting dari A-Z : ")
    bukadata = open("daftarbuku.txt","r")
    isi = bukadata.readlines()
    isi.sort()
    if len(isi) == 0:
        print("\n[Data tidak tersedia]")
    else :
        no = "No"
        Judul = "Judul"
        Pengarang = "Pengarang"
        terbit = "Tahun Terbit"
        print("="*61)
        print(f"{no:2} | {Judul:10} | {Pengarang:15} | {terbit:23} |")
        print("="*61)
        
        for index,content in enumerate(isi):
            pecah = content.split(",")
            A = pecah[0]
            B = pecah[1]
            C = pecah[2].replace("\n","")
            print(f"{index+1:2} | {A:10} | {B:15} | {C:20}\n", end="")  
            
        print("="*61)
    print("\nTekan [ENTER] untuk kembali ke menu.")
    bukadata.close()
    input()
    menu()
    