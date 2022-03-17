from hashlib import shake_128


s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))

if s2 + s3 > s1 and s3 + s1 > s2 and s2 + s1 > s3:
    print("Pode formar um triângulo!")
else:
    print("Não pode formar um triângulo")