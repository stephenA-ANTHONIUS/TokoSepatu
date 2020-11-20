from os import system
from time import sleep

def print_menu():
	system("cls")
	print("""
	[1]. Lihat Semua Sepatu
	[2]. Tambah Stok Sepatu
	[3]. Cari Sepatu
	[4]. Hapus Data Sepatu
	[5]. Perbarui Merek Sepatu
	[Q]. Keluar
		""")

def print_header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(sepatu=None, ukuran=True, warna=True, harga=True, all_data=False):
	if sepatu != None and all_data == False:
		print(f"UKURAN : {sepatu}")
		print(f"WARNA : {shoestore[sepatu]['warna']}")
		print(f"HARGA : {shoestore[sepatu]['harga']}")
	elif harga == False and all_data == False:
		print(f"UKURAN : {shoes}")
		print(f"WARNA : {shoestore[sepatu]['warna']}")
	elif all_data == True:
		for every_shoes in shoestore: # lists, string, dict
			ukuran = every_shoes # ukuran = key dari dict-nya
			warna = shoestore[every_shoes]["warna"]
			harga = shoestore[every_shoes]["harga"]
			print(f"UKURAN : {ukuran} - WARNA : {warna} - HARGA : {harga}")

def view_shoestore():
	print_header("DAFTAR SEPATU TERSIMPAN")
	if not_empty(shoestore):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA SEPATU TERSIMPAN")
	input("Tekan ENTER untuk kembali ke MENU")

def add_shoes():
	print_header("MENAMBAHKAN SEPATU BARU")
	merek = input("MEREK SEPATU : ")
	ukuran = input("UKURAN \t: ")
	warna = input("WARNA \t: ")
	harga = input("HARGA \t: ")
	respon = input(f"Apakah yakin ingin menyimpan sepatu : {merek} ? (Y/N) ")
	if verify_ans(respon):
		shoestore[merek] = {
			"ukuran" :ukuran,
			"warna" : warna,
			"harga" : harga
		}
		print("Data Kontak Tersimpan.")
	else:
		print("Data Batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching(sepatu):
	if sepatu in tokosepatu:
		return True
	else:
		return False

def find_shoes():
	print_header("MENCARI SEPATU")
	merek = input("Nama Ukuran yang Dicari : ")
	exists = searching(merek)
	if exists:
		print("Data Ditemukan")
		print_data(sepatu=merek)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def delete_shoes():
	print_header("MENGHAPUS SEPATU")
	ukuran = input("Nama Sepatu yang akan Dihapus : ")
	exists = searching(ukuran)
	if exists:
		print_data(sepatu=ukuran)
		respon = input(f"Yakin ingin menghapus {ukuran} ? (Y/N) ")
		if verify_ans(respon):
			del shoestore[ukuran]
			print("Data Kontak Telah Dihapus")
		else:
			print("Data Kontak Batal Dihapus")
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")
	
def update_shoes_ukuran(shoes):
	print(f"Ukuran Lama : {shoes}")
	new_size = input("Masukan Ukuran baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		shoestore[new_size] = shoestore[shoes]
		del shoestore[shoes]
		print("Data Telah di simpan")
		print_data(new_size)
	else:
		print("Data Batal diubah")

def update_shoes_warna(shoes):
	print(f"Warna Lama : {shoestore[shoes]['warna']}")
	new_color = input("Masukan Warna Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result : 
		shoestore[shoes]['warna'] = new_color
		print("Data Telah di simpan")
		print_data(shoes)
	else:
		print("Data Telah diubah")

def update_shoes_harga(shoes):
	print(f"Harga Lama : {shoestore[shoes]['harga']}")
	new_price = input("Masukan Harga Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result : 
		shoestore[shoes]['Harga'] = new_price
		print("Data Telah di simpan")
		print_data(shoes)
	else:
		print("Data Telah diubah")

def update_shoes():
	print_header("MENGUPDATE INFO SEPATU")
	merek = input("Merek Sepatu yang akan di-update : ")
	exists = searching(merek)
	if exists:
		print_data(merek)
		print("EDIT FIELD [1] UKURAN - [2] WARNA - [3] HARGA")
		respon = input("MASUKAN PILIHAN (1/2/3) : ")
		if respon == "1":
			update_shoes_ukuran(merek)
		elif respon == "2":
			update_shoes_warna(Merek)
		elif respon == "3":
			update_shoes_harga(harga)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")


def check_user_input(char):
	char = char.upper()
	if char == "Q":
		print("BYE!!!")
		return True
	elif char == "1":
		view_shoestore()
	elif char == "2":
		add_shoes()
	elif char == "3":
		find_shoes()
	elif char == "4":
		delete_shoes()
	elif char == "5":
		update_shoes()

shoestore = {
	"addidas" : {
		"ukuran": "40",
		"warna" : "biru",
		"harga" : "200000"
	},
	"nike" : {
		"ukuran" : "30",
		"warna" : "merah",
		"harga" : "100000"
	}
}
#flag/sign/tanda menyimpan sebuah kondisi
stop = False

while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)

