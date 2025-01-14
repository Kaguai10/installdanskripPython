#install terlebih dahulu progressbar karena skrip ini juga menjalan ekstensi progresbar
#pip install progressbar2  
import time
import progressbar
import subprocess 

class hero:
    @staticmethod
    def loading_with_progressbar2(package_name):
        """Melakukan apt update, apt upgrade, dan apt install berdasarkan input pengguna."""
        try:
            # Menjalankan apt update
            print("Updating packages...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            
            # Menjalankan apt upgrade
            print("Upgrading packages...")
            subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)

            # Menjalankan apt install
            if package_name:
                print(f"Installing package: {package_name}...")
                subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)
            else:
                print("No package specified for installation.")

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return  # Keluar dari fungsi jika ada kesalahan

        # Menampilkan progress bar
        bar = progressbar.ProgressBar(widgets=[
            ' [', progressbar.Percentage(), '] ',
            progressbar.Bar()], maxval=100).start()

        for i in range(100):
            time.sleep(0.1)  # Simulasi proses
            bar.update(i + 1)

        bar.finish()  # Menyelesaikan progress bar
        print("\rProcess completed successfully!")

def main():
    """Fungsi utama untuk menjalankan program."""
    # Input dari pengguna
    package_name = input("Enter the package name to install: ").strip()
    
    # Jika input kosong
    if not package_name:
        print("No package name entered. Exiting...")
        return

    # Menjalankan proses instalasi
    hero.loading_with_progressbar2(package_name)

if __name__ == '__main__':
    main()
