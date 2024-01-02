from flask import Flask, flash, render_template, request, redirect, url_for
import data as dat  # Mengimpor modul 'data' sebagai 'dat'

class Opname:
    def __init__(self):
        # Inisialisasi atribut-atribut yang digunakan dalam class
        self.barang = dat.barang  # Mengambil data barang dari modul 'data'
        self.css = "animated-element"  # Atribut untuk mengatur tampilan CSS
        self.down = "slide-down"  # Atribut untuk mengatur animasi slide-down

    def Stock_opname(self):
        # Render template 'stock_opname.html' dengan data barang, css, dan down
        return render_template('stock_opname.html', barang=self.barang, css=self.css, down=self.down)

    def So(self):
        # Mendapatkan nilai barcode dan jumlah dari form yang di-submit
        self.barcode = int(request.form['bar'])
        self.jumlah = int(request.form['jml'])

        if self.barcode not in self.barang:
            flash('Barcode tidak ditemukan.')  # Menampilkan pesan flash jika barcode tidak ditemukan
        else:
            if self.jumlah <= 0:
                flash('Penambahan stock anda tidak valid. Silahkan isi nominal > 0')  # Menampilkan pesan flash jika jumlah tidak valid
            else:
                # Melakukan operasi stock opname
                selisih = (self.jumlah - self.barang[self.barcode]['stock']) * self.barang[self.barcode]['harga_per_pcs']
                self.barang[self.barcode]['selisih_stock'] = self.jumlah - self.barang[self.barcode]['stock']
                self.format_selisih = '{:,.0f}'.format(selisih)
                self.barang[self.barcode]['selisih'] = self.format_selisih
                self.css = 'none'  # Mengubah tampilan CSS
                self.down = 'none'  # Mengubah animasi slide-down

                # Render kembali template 'stock_opname.html' dengan perubahan yang dilakukan
                return render_template('stock_opname.html', barang=self.barang, css=self.css, down=self.down)

        return redirect("/stock_opname")  # Redirect ke halaman stock_opname jika tidak ada perubahan
