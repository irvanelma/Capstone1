from tabulate import tabulate

# ========== Database STOCK ==========

data_mobil = {
    'B111ABC' : {'brand': 'toyota', 'namamobil': 'corolla', 'tipe' : 'sedan', 'transmisi' : 'AT', 'nama penyewa' : 'none' },
    'B222ABC' : {'brand': 'Honda', 'namamobil': 'CR-V', 'tipe' : 'sedan', 'transmisi' : 'MT', 'nama penyewa' : 'none' },
    'B333ABC' : {'brand': 'toyota', 'namamobil' : 'fortuner', 'tipe' : 'suv', 'transmisi' : 'AT', 'nama penyewa' : 'none' },
    'B333XYZ' : {'brand': 'BMW', 'namamobil': 'X3', 'tipe' : 'suv', 'transmisi' : 'AT', 'nama penyewa' : 'none' },
}

data_ongoing = {} #dict untuk mobbil yang sedang dipesan

# ========== Function MENU ==========

def menu():
    print('\n======== RENTAL MOBIL IRVAN =========')
    print('_______________________________________')
    print('Pilih Menu: ')
    print('1. Cek Stok Mobil')
    print('2. Tambah Stok mobil')
    print('3. Delete Stok')
    print('4. Pencarian berdasarkan transmisi')
    print('5. Pemesanan Mobil')
    print('6. Pengembalian Mobil')
    print('7. Selesai')
    print('_______________________________________')

# ========== Function PASSWORD ==========

def password():
    password_benar = '123'

    while True:
        password = input('Menu ini hanya untuk karyawan internal, Silahkan masukkan password (atau ketik "menu" untuk kembali): ')

        if password.lower() == 'menu':
            break                # BREAK agar kembali ke menu
        
        elif password == password_benar:
            return True
        
        else:
            print('Password salah. Silahkan masukkan ulang / ketik "menu" untuk kembali: ')

# ========== Function Stock Display ==========

def stock():

    table = []
    for key, value in data_mobil.items():
        row = [key] + [v for v in value.values()] 
        table.append(row)

    headers = ['Nomor Plat', 'Brand', 'Nama Mobil', 'Tipe', 'Transmisi', 'Nama Penyewa']
    print(tabulate(table, headers=headers, tablefmt='github'))

def ongoing():
    table2 = []
    for key2, value2 in data_ongoing.items():
        row2 = [key2] + [b for b in value2.values()]
        table2.append(row2)

    headers = ['Nomor Plat', 'Brand', 'Nama Mobil', 'Tipe', 'Transmisi', 'Nama Penyewa']
    print(tabulate(table2, headers=headers, tablefmt='github'))

# ========== Function TAMBAH STOCK ==========

def tambah():
   
   while True:
    nomor_mobil = input('Masukkan nomor plat mobil baru (ketik "menu" untuk kembali): ')
    if nomor_mobil.upper() in data_mobil or data_ongoing:
        print('Mobil sudah ada didalam stok.')
    elif nomor_mobil == 'menu':
        break
    else:
        brand_baru = input('Masukkan brand mobil baru: ')
        nama_baru  = input('Nama mobil: ')
        tipe_baru  = input('Tipe mobil: ')
        transmisi_baru = input('Transmisi: ')

        data_mobil[nomor_mobil.upper()] = {'brand': brand_baru , 'namamobil' : nama_baru , 'tipe' : tipe_baru, 'transmisi' : transmisi_baru.upper(), 'nama penyewa' : 'none'}
        print(f'\nMobil dengan plat {nomor_mobil} berhasil ditambahkan, berikut stock yang telah di perbarui:')
        stock()
        break
   
# ============ Function Delete Stock ============

def hapus():
    
    while True:
        hapus_mobil = input('Masukkan nomor plat mobil yang ingin di hapus dari stok (ketik "menu" untuk kembali ke menu awal): ')

        if hapus_mobil.upper() in data_mobil:
            del data_mobil[hapus_mobil.upper()]
            print('\nStok berhasil di hapus. Berikut stok yang telah diperbarui:')
            stock()
            break
        elif hapus_mobil.upper() in data_ongoing:
            print('Mobil sedang dipesan, Tidak bisa di hapus')
        elif hapus_mobil.lower() == 'menu':
            break
        else:
            print('Input nomor plat mobil tidak valid')
    
# ============ Function PEMESANAN ============

def pemesanan():
    print('\nHarga sewa: Rp. 300.000 / hari')

    pilih_mobil = input('Pilih nomor plat mobil yang ingin di sewa: ')
    while True:

        if pilih_mobil.upper() in data_mobil:
             #pindah dari stok ke mobil yang sedang dipesa
            data_ongoing[pilih_mobil.upper()] = data_mobil.pop(pilih_mobil.upper())
            
            while True:
                
            #penggantian nama penyewa
                nama        = input('Nama Lengkap: ')
                if nama.isalpha():
                    data_ongoing[pilih_mobil.upper()]['nama penyewa'] = nama
                    break  
                else:
                    print('Nama tidak valid (hanya bisa alphabet). Silahkan input ulang. ')
            
            #perhitungan biaya
            while True:
                try: 
                    lama_sewa = int(input('\nMasukkan lama waktu penyewaan (Hari): '))
                    total = lama_sewa * 300000
                    print(f'Total biaya yang harus anda bayar: {total} ')

                    a = data_ongoing[pilih_mobil.upper()]['namamobil']
                    print(f'Mobil {a} dengan plat nomor {pilih_mobil.upper()} berhasil di sewa')
                    break
                except ValueError:
                    print('input tidak valid (hanya diperbolehkan bilangan bulat).')
            break

        elif pilih_mobil.upper() in data_ongoing:
            print('Mobil sedang dipesan. Silahkan pilih mobil lain!')
            break
        else:
            print('\nNomor plat mobil tidak valid')
            break

# ============== Function SEARCH ==============

def search(jenis_transmisi):

    data_search = [] #list kosong yang nantinya akan diisi dengan mobil dengan transmisi tertentu

    for keys, values in data_mobil.items():
        if values['transmisi'] == jenis_transmisi:
            data_search.append((keys, values))

    if data_search: #mengeCEK apakah data_search mengandung elemen
        print(f'Mobil dengan transmisi {jenis_transmisi}') 
        for keys, values in data_search:
            print(f"Brand: {values ['brand']} | Nama mobil: {values['namamobil']} | Tipe :{values['tipe']} | Transmisi: {values['transmisi']} | Nama penyewa : {values['nama penyewa']}")
    else: 
        print('Mobil tidak ditemukan')


# ============== Function PENGEMBALIAN ==============

def pengembalian():

    print('\n Selamat datang kembali di Rental Mobil IRVAN!')
    
    while True:
        balik_mobil = input('Masukkan nomor plat mobil yang akan dikembalikan (ketik "menu" untuk kembali): ')
        if balik_mobil.upper() in data_ongoing:
            data_mobil[balik_mobil.upper()] = data_ongoing.pop(balik_mobil.upper())  #pindah dari ongoing ke stok
            print('\nMobil berhasil dikembalikan. Terima Kasih!')
            data_mobil[balik_mobil.upper()]['nama penyewa'] = 'none'
            break
        elif balik_mobil.upper() in data_mobil:
            print('\nMobil tidak sedang dipesan.')
        elif balik_mobil.lower() == 'menu':
            break    
        else:
            print('\nnomor mobil tidak valid.')
            
# =================== MAIN =====================

while True:
    try:
        menu()
        pilihan_menu = input('Masukkan nomor pilihan menu (1 - 7): ')

        if pilihan_menu == '1':
            print('\nStock & Availability Rental Mobil IRVAN') #Show stock
            stock()
            print('\nMobil yang sedang dipesan: ')
            ongoing()
        elif pilihan_menu == '2': #Tambah stock
            if password() == True:
                tambah()
        elif pilihan_menu == '3': #Delete stock 
            if password() == True:
                hapus()
        elif pilihan_menu == '4': #pencarian mobil berdasarkan transmisi
            while True:
                jenis_transmisi = input('Cari berdasarkan AT/MT? (ketik "menu" untuk kembali): ')
                if jenis_transmisi.lower() == 'menu':
                    break
                elif jenis_transmisi.upper() == 'AT' or 'MT':
                    search(jenis_transmisi.upper())
        elif pilihan_menu == '5': #Pemesanan
            stock()
            pemesanan()
        elif pilihan_menu == '6': #pengembalian
            pengembalian()
        elif pilihan_menu == '7': # stop program
            print('Terima kasih sudah menggunakan layanan kami!')
            break
        else:
            print('Pilihan menu hanya 1 - 7!')

    except Exception as e:
        print(f'Terjadi kesalahan: {e}')