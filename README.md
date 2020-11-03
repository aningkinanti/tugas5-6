# TUGAS PERTEMUAN 5 DAN 6 BESERTA PENJELASANNYA

**Nama	  : Aning Kinanti** <br>
**Nim	    : 312010364** <br>
**Kelas	  : TI.20.A2** <br>
**Matkul	: Bahasa Pemrograman** <br>

## Tugas Pertemuan 5

![soalBiodata](https://user-images.githubusercontent.com/72775624/97995202-cc442b00-1e18-11eb-9e6c-95133999be3a.PNG)

#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas
 ``` python
#biodata aning kinanti - 312010364

#mengambil input
namaLengkap = input ("nama lengkap:")
namaPendek = input ("nama panggilan:")
nim = input ("nim:")
tempatLahir = input ("tempat lahir:")
umur = input ("umur:")
alamat = input ("alamat:")
noHp = input ("no Hp:")

#menampilkan output
print("", end='\n')
print ("Assalamualaikum")
print ("Let me introduce my self.","My name is",namaLengkap,"but you can call me",namaPendek, ". My NIM is",nim, end='\n')
print ("I was born in",tempatLahir,"and i am",umur,"years old", end='\n')
print ("I am very glad if you want to invite my house in",alamat,".","So don't forget to call me before with the number",noHp)
```

#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![outputBiodata](https://user-images.githubusercontent.com/72775624/97995191-c8b0a400-1e18-11eb-952d-e7daf4ff4d61.PNG)

#### ANALISIS
•	Variabel adalah merupakan tempat untuk menyimpan data yang data-data tersebut dapat diambil/dipanggil kembali apabila dibutuhkan.
Pada syntak diatas namaLengkap, namaPendek, nim, tempatLahir, umur, alamat, dan noHp merupakan variabel. <br>
•	Pada program diatas kita akan menginputkan data yang akan disimpan di variabel pada #mengambil input menggunakan syntax seperti  <br>
``` pyhton
namaLengkap = input (“nama lengkap :”)
```
Pada syntax diatas namaLengkap merupakan variabel, yang isinya akan diinput dengan perintah = input (“nama lengkap: ”) . <br>

•	Pada #menampikan output untuk syntax dibawah ini
``` pyhton
print("", end='\n')
```
Fungsi print digunakan untuk mencetak output. <br>
Fungsi (“”, end =’\n’) digunakan untuk memberi jarak/garis baru/enter. <br>

•	Pada syntax
``` python
print ("Assalamualaikum")
print ("Let me introduce my self.","My name is",namaLengkap,"but you can call me",namaPendek, ". My NIM is",nim, end='\n')
print ("I was born in",tempatLahir,"and i am",umur,"years old", end='\n')
print ("I am very glad if you want to invite my house in",alamat,".","So don't forget to call me before with the number",noHp)
```
Bagian yang berada didalam tanda kutip seperti “My name is” akan ditampilkan/dicetak sama seperti statement tersebut, sedangkan pada ,namaLengkap, digunakan untuk memanggil data dari variabel namaLengkap yang telah diinputkan.

## Tugas Pertemuan 6
#### Mempraktekan program pada Lab1 dan Lab2

### Pertemuan 6 Lab 1

![Syntaxlab1](https://user-images.githubusercontent.com/72775624/97995262-dcf4a100-1e18-11eb-86ce-194b86aacc27.PNG)

### PENGGUNAAN END
#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas
``` python
#penggunaan end
print ('A', end='')
print ('B', end='')
print ('C', end='')
print ( )
print ('X')
print ('Y')
print ('Z')
```

#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![ouputend](https://user-images.githubusercontent.com/72775624/97995241-d8c88380-1e18-11eb-8ecd-7205a65a4c94.PNG)

#### ANALISIS
•	Perintah end berguna untuk memberi garis baru/newline namun apabila value dari end maka statement yang dicetak tidak akan memberi garis baru seperti output diatas.

### PENGGUNAAN SEPARATOR
#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas
``` python
#penggunaan separator
w, x, y, z = 10, 15, 20, 25
print (w, x, y, z)
print (w, x, y, z, sep=',')
print (w, x, y, z, sep='')
print (w, x, y, z, sep=':')
print (w, x, y, z, sep='------')
```

#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![outputseparator](https://user-images.githubusercontent.com/72775624/97995251-dbc37400-1e18-11eb-9616-a46356eed1dd.PNG)

#### ANALISIS
•	Perintah separator berfungsi untuk memberi pemisah seperti koma( , ), titik dua( : )dan lain sebagainya seperti pada syntax diatas.

### PENGGUNAAN STRING
#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas
``` python
#penggunaan string 
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**6)
print(7, 10**7)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)
```

#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![ouputstring](https://user-images.githubusercontent.com/72775624/97995245-d9f9b080-1e18-11eb-96ce-772df1558661.PNG)

#### ANALISIS
•	Penggunaan string ** pada syntax diatas berfungsi untuk mencetak hasil pangkat, mulai dari 10 pangkat 0 sampai 10 pangkat 10

### PENGGUNAAN STRING FORMAT
#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas
``` python
#string format
print ('{0:>3} {1:>16}'.format(0, 10**0))
print ('{0:>3} {1:>16}'.format(1, 10**1))
print ('{0:>3} {1:>16}'.format(2, 10**2))
print ('{0:>3} {1:>16}'.format(3, 10**3))
print ('{0:>3} {1:>16}'.format(4, 10**4))
print ('{0:>3} {1:>16}'.format(5, 10**5))
print ('{0:>3} {1:>16}'.format(6, 10**6))
print ('{0:>3} {1:>16}'.format(7, 10**7))
print ('{0:>3} {1:>16}'.format(8, 10**8))
print ('{0:>3} {1:>16}'.format(9, 10**9))
print ('{0:>3} {1:>16}'.format(10, 10**10))
```

#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![outputstringformat](https://user-images.githubusercontent.com/72775624/97995257-dc5c0a80-1e18-11eb-8cad-f927711e8afb.PNG)

#### ANALISIS
•	BELUM TAU

### Pertemuan 6 Lab 2

![Syntaxlab2](https://user-images.githubusercontent.com/72775624/97995267-df56fb00-1e18-11eb-9428-6f3bcaaba557.PNG)

#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas
``` python
a = eval (input("masukan nilai a: "))
b = eval (input("masukan nilai b: "))
hasil = a+b
print ("variable a = ",a)
print ("variable b = ",b)
print ("hasil penggabungan %d & %d = %d" % (a, b, hasil))

#konversi nilai variable

print ("KONVERSI NILAI VARIABLE")
a = int(a)
b = int(b)
print("hasil penjumlahan {1}+{0}=%d".format(a,b) % (a+b))
print("hasil penjumlahan {1}/{0}=%d".format(a,b) % (a/b))
```

#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![outputlab2](https://user-images.githubusercontent.com/72775624/97995248-da924700-1e18-11eb-9a69-c7cee0798eaa.PNG)

#### ANALISIS
•	BELUM TAU






