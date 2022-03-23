# tugas 3
# input 

esa_t = 71.3
esa_p = 68.3
esa2_t = 86.7
esa2_p = 72.0

# kkm

p = 70.0
t = 70.0

#logika 1

if (esa_t>t and esa_p<p):
    print("anda mengulang ujian praktek")  
elif (esa_t<t and esa_p>p):
    print("anda mengulang ujian teori")
elif (esa_t>t and esa_p>p):
    print("selamat anda lulus ujian")
else :
    print("anda mengulang ujian praktek dan teori")

#logika 2

if (esa2_t>t and esa2_p<p):
    print("anda mengulang ujian praktek")  
elif (esa2_t<t and esa2_p>p):
    print("anda mengulang ujian teori")
elif (esa2_t>t and esa2_p>p):
    print("selamat anda lulus ujian")
else :
    print("anda mengulang ujian praktek dan teori")