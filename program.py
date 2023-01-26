import peminjaman
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
            |   9   | Urutkan dari A-z           |
            |   10  | Keluar                     |
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
        peminjaman.daftarpeminjam()
    elif p==7:
        peminjaman.tambahpeminjam()
    elif p==8:
        peminjaman.hapuspeminjam()
    elif p==9:
        sorting()
    elif p==10:
        print("\n[Anda telah keluar dari program]")
    else:
        print("\n[Masukkan Input Yang telah disediakan!]")

def daftarbuku():
    import os
    os.system("CLS")
    print("\nDaftar Buku yang Tersedia : ")
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
        print("="*80)
        print(f"{no:2} | {Judul:30} | {Pengarang:25} | {terbit:12} |")
        print("="*80)
        
        for index,content in enumerate(isi):
            pecah = content.split(",")
            A = pecah[0]
            B = pecah[1]
            C = pecah[2].replace("\n","")
            print(f"{index+1:2} | {A:30} | {B:25} | {C:12} |\n", end="")  
            
        print("="*80)
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

    no = "No"
    Judul = "Judul"
    Pengarang = "Pengarang"
    terbit = "Tahun Terbit"
    print("="*80)
    print(f"{no:2} | {Judul:30} | {Pengarang:25} | {terbit:12} |")
    print("="*80)
    i=1
    for index,data_buku in enumerate (isi):
            pecah = data_buku.split(",")
            if pecah[0] == cari:
                A = pecah[0]
                B = pecah[1]
                C = pecah[2].replace("\n","")
                print(f"{index+1:2} | {A:30} | {B:25} | {C:12} |\n", end="")   
                print("="*80)
                print("\nIngin Mencari Buku Lagi? (Y/N)", end=" ")
                crdt = input(" : ")
                if crdt == "y" or crdt == "Y":
                    caridata()
                else :
                    print("\nTekan [ENTER] Untuk kembali ke menu")
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
                isi[i]= xg
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

def sorting():
    import os
    os.system("CLS")
    print("\nHasil dari Pengurutan dari A-Z : ")
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
        print("="*80)
        print(f"{no:2} | {Judul:30} | {Pengarang:25} | {terbit:12} |")
        print("="*80)
        
        for index,content in enumerate(isi):
            pecah = content.split(",")
            A = pecah[0]
            B = pecah[1]
            C = pecah[2].replace("\n","")
            print(f"{index+1:2} | {A:30} | {B:25} | {C:12} | \n", end="")  
            
        print("="*80)
    print("\nTekan [ENTER] untuk kembali ke menu.")
    bukadata.close()
    input()
    menu()
    #Akhir Dari Program