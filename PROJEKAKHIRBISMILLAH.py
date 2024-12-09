import csv
import os

# File paths
USERS_FILE = 'users.csv'
PRODUCTS_FILE = 'products.csv'  # Nama file sudah sesuai dengan permintaan
TRANSACTIONS_FILE = 'transactions.csv'
# Voucher data
VOUCHERS = {
    "akumahasigma": 0.1,  # Diskon 10%
    "kapallawd": 0.2  # Diskon 20%
}

# ========================== Fungsi untuk Inisialisasi ==========================

def initialize_files():
    """Inisialisasi file CSV yang dibutuhkan jika file belum ada."""
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password', 'role'])

    if not os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'category', 'price', 'stock'])
            # Tambahkan daftar produk awal
            products = [
                ["Pupuk Kandang", "Organik", 40000, 100],
                ["Pupuk Kompos", "Organik", 25000, 100],
                ["Pupuk Hijau", "Organik", 35000, 100],
                ["Pupuk Hayati", "Organik", 75000, 100],
                ["Pupuk Organik Cair", "Organik", 50000, 100],
                ["Pupuk Urea", "Anorganik", 30000, 100],
                ["Pupuk Kapur Tohor", "Anorganik", 20000, 100],
                ["Pupuk ZA", "Anorganik", 10000, 100],
                ["Pupuk NPK Phonska", "Anorganik", 40000, 100],
                ["Pupuk Kalium Sulfat", "Anorganik", 30000, 100],
            ]
            writer.writerows(products)

    if not os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'product', 'quantity', 'total_price', 'voucher', 'final_price'])

# ========================== Fungsi untuk Registrasi ============================

def register():
    """Fungsi untuk registrasi pengguna baru."""
    print("\n-+-+-+-+-+-+-=== Registrasi Pengguna Baru -+-+-+-+-+-+-===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    role = input("Masukkan role (penjual/pembeli): ").lower()
    
    # Validasi role
    if role not in ['penjual', 'pembeli']:
        print("Role tidak valid. Gunakan 'penjual' atau 'pembeli'.")
        return

    with open(USERS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, role])
        print(f"Registrasi berhasil. Anda terdaftar sebagai {role}.")

# ========================== Fungsi untuk Login ================================

def login():
    """Fungsi untuk login pengguna."""
    print("\n=== Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    with open(USERS_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print(f"Login berhasil! Selamat datang, {username}.")
                return username, row[2]  # Mengembalikan username dan role
    print("Username atau password salah.")
    return None, None

# ========================== Fungsi untuk Melihat Produk =======================

def view_products():
    """Melihat daftar produk yang tersedia."""
    print("\n=== Daftar Produk ===")
    try:
        with open(PRODUCTS_FILE, 'r') as file:
            reader = csv.reader(file)
            products = list(reader)

            if len(products) <= 1:
                print("Belum ada produk yang tersedia.")
                return

            # Tampilkan daftar produk dalam format tabel
            print(f"{'No':<5} {'Nama Produk':<20} {'Kategori':<10} {'Harga':<10} {'Stok':<10}")
            print("="*50)
            for i, product in enumerate(products[1:], 1):  # Skip header
                print(f"{i:<5} {product[0]:<20} {product[1]:<10} {product[2]:<10} {product[3]:<10}")
            print("="*50)
    except FileNotFoundError:
        print("File produk tidak ditemukan. Pastikan file sudah diinisialisasi.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# ========================== Fungsi untuk Menambah Produk =======================

def add_product():
    """Fungsi untuk penjual menambah produk baru."""
    print("\n=== Menambah Produk Baru ===")
    print("Masukkan 0 jika tidak ingin menambah produk.")

    name = input("Masukkan nama produk (atau ketik 0 untuk batal): ")
    if name == "0":
        print("Proses penambahan produk dibatalkan.")
        return
    
    category = input("Masukkan kategori (Organik/Anorganik): ").lower()
    if category not in ["organik", "anorganik"]:
        print("Kategori tidak valid. Pilih 'Organik' atau 'Anorganik'.")
        return
    price = int(input("Masukkan harga produk (Rp): "))
    stock = int(input("Masukkan jumlah stok produk: "))

    # Menyimpan produk baru ke dalam CSV
    with open(PRODUCTS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, category.capitalize(), price, stock])
        print(f"Produk '{name}' berhasil ditambahkan.")

# ========================== Fungsi untuk Mengedit Produk =======================

def edit_product():
    """Fungsi untuk penjual mengedit produk yang sudah ada."""
    print("\n=== Edit Produk ===")
    view_products()  # Menampilkan daftar produk
    product_index = input("Pilih nomor produk yang ingin diedit (ketik 0 untuk batal): ")

    if product_index == '0':
        print("Proses edit produk dibatalkan.")
        return
    
    try:
        product_index = int(product_index) - 1
    except:
        print("Input harus berupa angka.")
        return
    # Memastikan produk yang dipilih valid
    with open(PRODUCTS_FILE, 'r') as file:
        reader = csv.reader(file)
        products = list(reader)

    if product_index < 0 or product_index >= len(products) - 1:  # -1 karena header
        print("Pilihan produk tidak valid.")
        return
    
    selected_product = products[product_index + 1]  # Skip header
    print(f"Produk yang dipilih: {selected_product[0]}")

    # Mengedit nama produk
    name = input(f"Nama produk (sekarang: {selected_product[0]}): ")
    if name == "0":
        print("Proses edit produk dibatalkan.")
        return

    category = input(f"Kategori produk (sekarang: {selected_product[1]}): ").lower()
    if category not in ["organik", "anorganik"]:
        print("Kategori tidak valid. Pilih 'Organik' atau 'Anorganik'.")
        return
    price = int(input(f"Harga produk (sekarang: Rp {selected_product[2]}): "))
    stock = int(input(f"Stok produk (sekarang: {selected_product[3]}): "))

    # Update data produk
    products[product_index + 1] = [name, category.capitalize(), price, stock]
    
    # Menyimpan perubahan produk ke dalam CSV
    with open(PRODUCTS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(products)
    
    print(f"Produk '{name}' berhasil diedit.")

# ========================== Fungsi untuk Menghapus Produk ======================

def delete_product():
    """Fungsi untuk penjual menghapus produk yang sudah ada."""
    print("\n=== Hapus Produk ===")
    view_products()  # Menampilkan daftar produk
    product_index = input("Pilih nomor produk yang ingin dihapus (ketik 0 untuk batal): ")

    if product_index == '0':
        print("Proses penghapusan produk dibatalkan.")
        return
    
    try:
        product_index = int(product_index) - 1
    except:
        print("Input harus berupa angka.")
        return
    # Memastikan produk yang dipilih valid
    with open(PRODUCTS_FILE, 'r') as file:
        reader = csv.reader(file)
        products = list(reader)

    if product_index < 0 or product_index >= len(products) - 1:  # -1 karena header
        print("Pilihan produk tidak valid.")
        return
    
    selected_product = products[product_index + 1]  # Skip header
    print(f"Produk yang dipilih: {selected_product[0]}")
    
    confirm = input(f"Apakah Anda yakin ingin menghapus produk '{selected_product[0]}'? (y/n): ").lower()
    if confirm == 'y':
        del products[product_index + 1]
        
        # Menyimpan perubahan ke dalam file CSV
        with open(PRODUCTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(products)
        
        print(f"Produk '{selected_product[0]}' berhasil dihapus.")
    else:
        print("Penghapusan produk dibatalkan.")

# ========================== Fungsi untuk Pembeli ================================

def make_purchase(username):
    """Fungsi untuk pembeli melakukan pembelian produk."""
    print("\n=== Pembelian Produk ===")
    
    selected_products = []
    while True:
        view_products()
        product_index = int(input("Pilih nomor produk untuk membeli (0 untuk selesai): ")) - 1
        
        if product_index == -1:
            break
        
        # Memastikan produk yang dipilih valid
        with open(PRODUCTS_FILE, 'r') as file:
            reader = csv.reader(file)
            products = list(reader)

        if product_index < 0 or product_index >= len(products) - 1:  # -1 karena header
            print("Pilihan produk tidak valid.")
            continue
        
        product = products[product_index + 1]  # Skip header
        quantity = int(input(f"Masukkan jumlah {product[0]} yang ingin dibeli: "))
        
        if quantity > int(product[3]):
            print(f"Stok tidak mencukupi. Hanya ada {product[3]} produk tersedia.")
            continue
        
        selected_products.append({
            'name': product[0],
            'quantity': quantity,
            'price': int(product[2]),
            'total_price': quantity * int(product[2])
        })
        
        # Update stok produk
        product[3] = str(int(product[3]) - quantity)
    
        # Menulis kembali stok yang diperbarui ke file products.csv
        with open(PRODUCTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in products:
                writer.writerow(row)

        print(f"\nStok produk '{product[0]}' telah masuk ke keranjang.")

    total_price = sum([item['total_price'] for item in selected_products])
    print(f"\nTotal Harga Pembelian: Rp {total_price}")

    # Menu untuk membatalkan produk atau mengubah jumlah produk sebelum pembayaran
    while True:
        print("\n=== Daftar Produk yang Anda Pilih ===")
        for i, item in enumerate(selected_products, 1):
            print(f"{i}. {item['name']} - Jumlah: {item['quantity']} - Harga perbiji : {item['price']} - Total Harga: Rp {item['total_price']}")

        print("0. Selesai")
        print("88. Tambah produk lagi")
        print("99. Hapus beberapa jumlah produk")
        cancel_choice = input("\nMasukkan pilihan: ")

        if cancel_choice == '0':
            break
        elif cancel_choice == '88':
            print("Anda memilih untuk menambah produk lagi.")
            make_purchase(username)  # Memanggil ulang fungsi make_purchase untuk menambah produk
            break

        elif cancel_choice == '99':
            try:
                edit_index = int(input("Masukkan nomor produk yang jumlahnya ingin dikurangi: ")) - 1
                if 0 <= edit_index < len(selected_products):
                    remove_qty = int(input(f"Masukkan jumlah yang ingin dihapus dari {selected_products[edit_index]['name']}: "))
                    if remove_qty > selected_products[edit_index]['quantity']:
                        print(f"Jumlah yang ingin dihapus melebihi jumlah yang dibeli.")
                    else:
                        selected_products[edit_index]['quantity'] -= remove_qty
                        selected_products[edit_index]['total_price'] -= remove_qty * selected_products[edit_index]['price']
                        print(f"{remove_qty} dari {selected_products[edit_index]['name']} berhasil dihapus.")
                        if selected_products[edit_index]['quantity'] == 0:
                            removed_product = selected_products.pop(edit_index)
                            print(f"Produk '{removed_product['name']}' telah dihapus sepenuhnya dari keranjang.")
                else:
                    print("Nomor produk tidak valid.")
            except ValueError:
                print("Masukkan angka yang valid.")

    # Menyimpan perubahan stok produk
    with open(PRODUCTS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow(product)

    # Proses pembayaran
    total_price = sum([item['total_price'] for item in selected_products])
    print(f"\nTotal Harga: Rp {total_price}")
    
    voucher_code = input("Masukkan kode voucher (kosongkan jika tidak ada): ").strip()
    discount = 0
    if voucher_code in VOUCHERS:
        discount = VOUCHERS[voucher_code]
        print(f"Diskon {discount*100}% diterapkan.")
    
    final_price = total_price * (1 - discount)
    print(f"Total setelah diskon: Rp {final_price}")
    
    while True:
        payment = int(input(f"Masukkan jumlah uang yang dibayarkan (Rp {final_price}): "))
        if payment >= final_price:
            change = payment - final_price
            print(f"Kembalian Anda: Rp {change}")
            break
        else:
            print("Uang yang dibayarkan kurang. Coba lagi.")

    # Simpan transaksi ke file CSV
    with open(TRANSACTIONS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        for item in selected_products:
            writer.writerow([username, item['name'], item['quantity'], item['total_price'], voucher_code, final_price])


# ========================== Fungsi Menu Pembeli dan Penjual ===================

def pembeli_menu(username):
    """Menu khusus untuk pembeli setelah login"""
    while True:
        print("\nMenu Pembeli:")
        print("1. Lihat Produk")
        print("2. Membeli Produk")
        print("3. Keluar")
        
        choice = input("Pilih menu (1-3): ")
        
        if choice == '1':
            view_products()
        elif choice == '2':
            make_purchase(username)
        elif choice == '3':
            print(f"Terima kasih {username}, Anda telah keluar.")
            break
        else:
            print("Pilihan tidak valid.")

def penjual_menu(username):
    """Menu khusus untuk penjual setelah login"""
    while True:
        print("\nMenu Penjual:")
        print("1. Tambah Produk")
        print("2. Edit Produk")
        print("3. Hapus Produk")
        print("4. Keluar")
        
        choice = input("Pilih menu (1-4): ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            edit_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            print(f"Terima kasih {username}, Anda telah keluar.")
            break
        else:
            print("Pilihan tidak valid.")

# ========================== Program Utama ===========================

def main():
    """Program utama"""
    initialize_files()

    while True:
        print("███████╗░░░░█████╗░░░░██████╗░    ░██████╗████████╗░█████╗░██████╗░███████╗")
        print("██╔════╝░░░██╔══██╗░░░██╔══██╗    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝")
        print("█████╗░░░░░██║░░██║░░░██████╔╝    ╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░")
        print("██╔══╝░░░░░██║░░██║░░░██╔══██╗    ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░")
        print("██║░░░░░██╗╚█████╔╝██╗██║░░██║    ██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗")
        print("╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝    ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝")
        print("                                                                           ")
        print("|||||||||||||||||||||||||||||||||||||||||")
        print("||   Selamat Datang di F.O.R STORE     ||")
        print("||           1. Login                  ||")
        print("||           2. Register               ||")
        print("||           3. Keluar                 ||")
        print("|||||||||||||||||||||||||||||||||||||||||")
        choice = input("Pilih menu (1-3): ")
        
        if choice == '1':
            username, role = login()
            if username:
                if role == 'penjual':
                    penjual_menu(username)
                elif role == 'pembeli':
                    pembeli_menu(username)
        elif choice == '2':
            register()
        elif choice == '3':
            print("Terima kasih telah menggunakan F.O.R STORE. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()
