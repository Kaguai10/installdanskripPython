#Sebelum Menggunakannya install googlesearch.python
#pip install googlesearch-python

from googlesearch import search
import webbrowser

def google_search(query, num_results=5):
    """
    Fungsi untuk melakukan pencarian di Google dan mengembalikan hasil.

    Parameters:
    - query: Kata kunci pencarian.
    - num_results: Jumlah hasil yang ingin ditampilkan.
    """
    print(f"\nMencari '{query}' di Google...\n")
    try:
        results = list(search(query, num_results=num_results))
        for i, result in enumerate(results, 1):
            print(f"{i}. {result}")
        return results
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

def main():
    print("=== Pencarian Google via Terminal ===")
    while True:
        print("Selamat Datang di BrowsePython :)")
        query = input("Masukkan kata kunci pencarian (atau ketik 'exit' untuk keluar): ")
        if query.lower() == 'exit':
            print("Keluar dari program. Sampai jumpa!")
            break
        
        # Lakukan pencarian Google
        results = google_search(query, num_results=5)
        if not results:
            continue

        # Memilih tautan untuk dibuka
        while True:
            choice = input("\nKetik nomor tautan untuk membukanya, atau 'back' untuk kembali: ")
            if choice.lower() == 'back':
                break
            if choice.isdigit():
                num = int(choice)
                if 1 <= num <= len(results):
                    print(f"Membuka tautan: {results[num - 1]}")
                    webbrowser.open(results[num - 1])
                else:
                    print("Nomor tidak valid. Silakan pilih nomor dari daftar.")
            else:
                print("Masukkan nomor atau 'back'.")

if __name__ == "__main__":
    main()
