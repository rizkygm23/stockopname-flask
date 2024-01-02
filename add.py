from flask import Flask, flash, render_template, request, redirect
import data as dat

class Tambah:
    def __init__(self):
        # Inisialisasi atribut-atribut yang digunakan dalam class
        self.barang = dat.barang  # Mengambil data barang dari modul 'data'
        self.css = "animated-element"  # Atribut untuk mengatur tampilan CSS
        self.barcode = 0  # Atribut untuk menyimpan nilai barcode
        self.jumlah = 0  # Atribut untuk menyimpan nilai jumlah
        self.down = "slide-down"  # Atribut untuk mengatur animasi slide-down

    def Viewstock(self):
        # Render template 'viewstock.html' dengan data barang, css, dan down
        return render_template('viewstock.html', barang=self.barang, css=self.css, down=self.down)

    def add(self):
        # Mendapatkan nilai barcode dan jumlah dari form yang di-submit
        self.barcode = int(request.form['barcode'])
        self.jumlah = int(request.form['jumlah'])

        if self.barcode not in self.barang:
            flash('Barcode tidak ditemukan.')  # Menampilkan pesan flash jika barcode tidak ditemukan
        else:
            if self.jumlah <= 0:
                flash('Penambahan stock anda tidak valid. Silahkan isi nominal > 0')  # Menampilkan pesan flash jika jumlah tidak valid
            else:
                # Menambah jumlah barang jika barcode ditemukan dan jumlah valid
                self.barang[self.barcode]['stock'] += self.jumlah
                self.css = 'none'  # Mengubah tampilan CSS
                self.down = 'none'  # Mengubah animasi slide-down

                # Render kembali template 'viewstock.html' dengan perubahan yang dilakukan
                return render_template('viewstock.html', barang=self.barang, css=self.css, down=self.down)

        return redirect("/View_Stock")  # Redirect ke halaman View_Stock jika tidak ada perubahan
