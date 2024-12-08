import csv
import os
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
    
    product_index = int(product_index) - 1
    
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
    
    product_index = int(product_index) - 1
    
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
