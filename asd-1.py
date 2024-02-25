import os
os.system("cls")

class Majalah:

    def __init__ (self,id,jenis,harga,tahun_terbit,penerbit):
        self.id = id
        self.jenis = jenis
        self.harga = harga
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit

datamajalah = []

datamajalah.append(Majalah(1,"Kesehatan",20000,2022,"Sparkle Media"))
datamajalah.append(Majalah(2,"Teknologi",20000,2024,"Green Planet"))
datamajalah.append(Majalah(3,"Travel",20000,2024,"Travelogue Ltd"))
datamajalah.append(Majalah(4,"Lingkungan",20000,2023,"Green Planet"))

def display():
    for obj in datamajalah:
        print("Nomor:", obj.id, '| Jenis:', obj.jenis, '| Harga:', obj.harga, '| Tahun Terbit:', obj.tahun_terbit, "| Penerbit:", obj.penerbit)
    pilihan_menu()

def displayonly():
    for obj in datamajalah:
        print("Nomor:", obj.id, '| Jenis:', obj.jenis, '| Harga:', obj.harga, '| Tahun Terbit:', obj.tahun_terbit, "| Penerbit:", obj.penerbit)

def additem():
    input_id = int(input('MASUKKAN NOMOR MAJALAH (NOMOR TIDAK BOLEH SAMA): '))
    input_jenis = str(input('\nMASUKKAN JENIS/NAMA MAJALAH (JENIS/NAMA TIDAK BOLEH SAMA): '))
    input_harga = int(input('\nMASUKKAN HARGA MAJALAH: '))
    input_tahun_terbit = int(input('\nMASUKKAN TAHUN TERBIT MAJALAH: '))
    input_penerbit = str(input('\nMASUKKAN PENERBIT MAJALAH: '))
    
    for obj in datamajalah:
            if input_id == (obj.id):
                print('\nNomor yang dimasukkan sudah digunakan silahkan ulangi lagi\n')
                pilihan_menu()  
                
            elif input_jenis == (obj.jenis):
                print('JENIS/NAMA yang dimasukkan sudah digunakan silahkan ulangi lagi\n')
                pilihan_menu()  

            else:
                datamajalah.append(Majalah(input_id,input_jenis,input_harga,input_tahun_terbit,input_penerbit))
                print('\nPRODUK BERHASIL DITAMBAHKAN')
                pilihan_menu()  

def deleteitem():
    for obj in datamajalah:
        displayonly()
        print('')
        input_id = int(input('MASUKKAN NOMOR MAJALAH: '))
        if input_id == (obj.id):
            final_id = input_id - 1
            datamajalah.pop(final_id)
        else:
            print('\nMAJALAH DENGAN NOMOR YANG DIMASUKKAN TIDAK DITEMUKAN, SILAHKAH COBA LAGI')
            pilihan_menu()
        print('')
        print('MAJALAH BERHASIL DIHAPUS')
        pilihan_menu()

def updateitem():
    for obj in datamajalah:
        displayonly()
        print('')
        input_nomor = int(input('MASUKKAN NOMOR MAJALAH: '))
        final_nomor = input_nomor - 1
        if input_nomor == (obj.id):
            datamajalah.pop(final_nomor)
            input_nomor = final_nomor + 1
            input_jenis = str(input('\nMASUKKAN JENIS/NAMA MAJALAH YANG BARU: '))
            input_harga = int(input('\nMASUKKAN HARGA MAJALAH YANG BARU: '))
            input_tahun_terbit = int(input('\nMASUKKAN TAHUN TERBIT MAJALAH YANG BARU: '))
            input_penerbit = str(input('\nMASUKKAN PENERBIT MAJALAH YANG BARU: '))
            datamajalah.insert(final_nomor, Majalah(input_nomor,input_jenis,input_harga,input_tahun_terbit,input_penerbit))
        else:
            print('\nMAJALAH DENGAN NOMOR YANG DIMASUKKAN TIDAK DITEMUKAN, SILAHKAH COBA LAGI')
            pilihan_menu()

        print('\nPRODUK BERHASIL DIPERBARUI')
        pilihan_menu()   

def pilihan_menu():
        
        print('')
        print("PILIHAN MENU : ")
        print('')
        print("1. LIST PRODUK")
        print("2. TAMBAH PRODUK")
        print("3. HAPUS PRODUK")
        print("4. UBAH PRODUK")
        print("5. KELUAR")
        print('')
        pilihan_menu = int(input("PILIHAN MENU (1/2/3/4) : "))

        if pilihan_menu == 1:
            print('')
            print('LIST PRODUK KAMI ADALAH: \n')
            display()
        elif pilihan_menu == 2:
            print('')
            additem()
        elif pilihan_menu == 3:
            print('')
            deleteitem()
        elif pilihan_menu == 4:
            print('')
            updateitem()
        elif pilihan_menu == 5:
            raise SystemExit
        
print('')
print("=" * 31)
print("SELAMAT DATANG DI MAGAZINE ZONE")
print("=" * 31)

pilihan_menu()
            