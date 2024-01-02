# Mengimpor modul dan kelas yang diperlukan dari file terpisah
from login import *
from add import *
from opname import *

# Mengimpor modul Flask dan beberapa fungsi yang diperlukan
from flask import Flask, flash, render_template, request, redirect, url_for

# Membuat objek dari setiap kelas yang telah diimpor sebelumnya
tambah = Tambah()
logCard = LoginCard()
opname = Opname()

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi kunci rahasia untuk sesi
app.secret_key = 'stock'

# Menetapkan folder statis untuk file CSS, JavaScript, dll.
app.static_folder = 'static'

# Mendefinisikan rute-rute aplikasi Flask
@app.route('/')
def loginPages():
    return logCard.login_page()

@app.route('/login', methods=['POST', 'GET'])
def loginNext():
    return logCard.login()
# def sembunyipasss():
#     return logCard.sembunyipass()

@app.route('/Homepage',  methods=['POST', 'GET'])
def home():
    return logCard.Home()

@app.route('/View_Stock', methods=['POST', 'GET'])
def viewstock():    
    return tambah.Viewstock()

@app.route('/tambah_stok', methods=['POST'])
def tambah_stok_barang():
    return tambah.add()

@app.route('/stock_opname', methods=['POST', 'GET'])
def stock_opname():    
    return opname.Stock_opname()

@app.route('/Mulai_so', methods=['POST'])
def so():
    return opname.So()

# Menjalankan aplikasi Flask pada port 5100 dalam mode debug jika file ini dijalankan langsung
if __name__ == "__main__":
    app.run(debug=True, port=5100)
