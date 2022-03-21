# input 
pi= 22/7
print("\u03C0 = 22/7") 
r1 = 15
r2 = 34

# kalkulasi 
l1 = pi * r1**2
l2 = pi * r2**2

# jawaban 
txt1 = "luas lingkaran dengan jari -jari {} cm, adalah {} cm\u00b2". format (r1,l1)
txt2 = "luas lingkaran dengan jari -jari {} cm, adalah {} cm\u00b2". format (r2, l2)
print(txt1)
print(txt2)

# bonus
txt3 = "luas lingkaran dengan jari -jari {} cm, adalah {:.2f} cm\u00b2". format (r1,l1)
txt4 = "luas lingkaran dengan jari -jari {} cm, adalah {:.2f} cm\u00b2". format (r2,l2)
print(txt3)
print(txt4)