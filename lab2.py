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
