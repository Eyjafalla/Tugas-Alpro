import program

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
        no = "No"
        Nama = "NAMA"
        Judul = "JUDUL"
        tglpj = "TGL.PINJAM"
        print("="*80)
        print(f"{no:2} | {Nama:30} | {Judul:25} | {tglpj:12} |")
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
        program.menu()

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
        program.menu()

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
        program.menu()