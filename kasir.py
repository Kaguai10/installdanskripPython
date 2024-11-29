from prettytable import PrettyTable
import time

# mengimport Time dan Tabel(prettytable)
print("Selamat Datang Di Kasir TeKaJe22, Perkenalkan Saya BisenBot\nSaya disini untuk membantu anda")
print("adakah yang bisa saya bantu?")
class Item:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_tabel():
        tabel = PrettyTable()
        tabel.field_names = ["No", "Barang", "Harga", ]
        tabel.add_row([1, 'SUSU', "12.000"])
        tabel.add_row([2, 'ROTI', "10.000"])
        tabel.add_row([3, "WAFER", "5.000"])
        tabel.add_row([4, "KOPI", "15.000"])
        tabel.add_row([5, "KEJU", "8.500"])
        print(tabel)

class Kasir:
    def __init__(self):
        self.items = []
        self.cart = []
        self.total = 0
        self.uang_dibayar = 0
        self.kembalian = 0

    def tambah_item(self, item):
        self.items.append(item)

    def tampilkan_items(self):
        print("\nDaftar Barang:")
        for index, item in enumerate(self.items):
            print(f"{index + 1}. {item.nama} - Rp {item.harga}")

    def tambah_ke_keranjang(self, item_index, jumlah):
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            self.cart.append((item, jumlah))
            print(f"{jumlah} x {item.nama} telah ditambahkan ke keranjang.")
        else:
            print("Item tidak valid.")

    def hitung_total(self):
        self.total = sum(item.harga * jumlah for item, jumlah in self.cart)
        return self.total

    def menu_bayar(self):
        total = self.hitung_total()
        if total == 0:
            print("Keranjang masih kosong. Silakan tambahkan barang terlebih dahulu.")
            return
        
        print(f"\nTotal yang harus dibayar: Rp {total}")
        try:
            self.uang_dibayar = float(input("Masukkan jumlah uang yang dibayarkan: "))
            if self.uang_dibayar < total:
                print("Uang yang dibayarkan tidak cukup.")
            else:
                self.kembalian = self.uang_dibayar - total
                print("Pembayaran berhasil. Silakan pilih opsi untuk mencetak struk.")
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")

    def cetak_struk(self):
        print("\nStruk Pembelian:")
        for item, jumlah in self.cart:
            print(f"{item.nama} (x{jumlah}): Rp {item.harga * jumlah}")
        print(f"Total: Rp {self.total}")
        print(f"Uang Dibayar: Rp {self.uang_dibayar}")
        print(f"Kembalian: Rp {self.kembalian}")

def menu():
    print("\nPilihan")
    print("1. tampilkan Tabel")
    print("2. Pilih Barang")
    print("3. Bayar Pembelanjaan")
    print("4. Struk Belanja")
    print("5. Exit")

def loading():
    print("Logout From Program", end="", flush=True)
    for _ in range(13):  
        print(".", end="", flush=True)
        time.sleep(0.5) 
    print("\rBye bye  ", end="", flush=True)  
    time.sleep(1)  

def main():
    kasir = Kasir()
    kasir.tambah_item(Item("SUSU", 12000))
    kasir.tambah_item(Item("ROTI", 10000))
    kasir.tambah_item(Item("WAFER", 5000))
    kasir.tambah_item(Item("KOPI", 15000))
    kasir.tambah_item(Item("KEJU", 8500))

    while True:
        menu()
        pilihan = input("silahkan memilih untuk melanjutkan: ")
        
        if pilihan == '1':
            Item.tampilkan_tabel()
        elif pilihan == '2':
            arif = input("Silahkan Pilih Barang Sesuai Nomor: ")
            item_index = int(arif) - 1
            jumlah = int(input(f"Masukkan jumlah {kasir.items[item_index].nama} yang ingin dibeli: "))
            kasir.tambah_ke_keranjang(item_index, jumlah)
        elif pilihan == '3':
            kasir.menu_bayar()
        elif pilihan == '4':
            if kasir.total > 0:
                    kasir.cetak_struk()
                    kasir.cart.clear()
        elif pilihan == '5':
            print("Terima kasih! Semoga Harimu Menyenangkan")
            loading()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()