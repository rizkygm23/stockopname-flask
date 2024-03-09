from flask import Flask, flash, render_template, request, redirect, url_for
import data as dat  # Mengimpor modul 'data' sebagai 'dat'

class LoginCard:
    def __init__(self):
        # Inisialisasi atribut untuk pesan, aksi, tombol login, dan peringatan
        self.message = ''  # Pesan untuk ditampilkan pada halaman
        self.action = 'login'  # Aksi default
        self.button_login = 'Login'  # Teks tombol login default
        self.alert = ''  # Tipe alert untuk menampilkan pesan
    
    # def sembunyipass(self):
    #     return '*' * len(request.form['pin'])
    
    def login_page(self):
        # Mengembalikan halaman login dalam bentuk template 'login.html' dengan nilai awal untuk pesan, aksi, tombol login, dan peringatan
        return render_template('login.html', message='', action=self.action, button_login=self.button_login, alert=self.alert)
    
    def login(self):
        if request.method == 'POST':
            # Mendapatkan nilai 'nim' dan 'pin' dari form yang di-submit pada halaman HTML
            nim = int(request.form['nim'])
            pin = request.form['pin']

            if nim in dat.data_user and pin == dat.data_user[nim]["PIN"]:
                # Jika nim dan pin cocok dengan data di 'data_user', set pesan selamat datang dan ubah nilai aksi, tombol login, dan peringatan
                self.message = f"Selamat datang, {dat.data_user[nim]['NAMA']}, Silahkan masukkan ulang data anda untuk melanjutkan"  # Update pesan
                self.action = 'Homepage'  # Update aksi
                self.button_login = 'Lanjutkan'  # Update teks tombol login
                self.alert = 'alert alert-primary'  # Update tipe alert
            else:
                # Jika nim dan pin tidak cocok dengan data di 'data_user', set pesan yang menyatakan bahwa nim atau pin tidak valid
                self.message = "NIM atau PIN anda tidak valid. Silahkan coba lagi."  # Update pesan
                self.action = 'login'  # Update aksi
                self.button_login = 'Login'  # Update teks tombol login
                self.alert = 'alert alert-warning'  # Update tipe alert
                # Render ulang halaman login dengan pesan yang telah di-set sebelumnya
                return render_template('login.html', action=self.action, message=self.message, button_login=self.button_login, alert=self.alert)
            
            # Render halaman login dengan pesan dan aksi yang telah di-set sebelumnya setelah validasi
            return render_template('login.html', action=self.action, message=self.message, button_login=self.button_login, alert=self.alert)
        # return redirect('/')
        
        # Render halaman login dengan pesan, aksi, tombol login, dan peringatan yang telah di-set sebelumnya
        return render_template('login.html', action=self.action, message=self.message, button_login=self.button_login, alert=self.alert)

    def Home(self):
        # Mengembalikan halaman index.html
        return render_template('index.html')
    
    
    
    # asasas
