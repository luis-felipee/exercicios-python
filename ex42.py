# Isósceles: dois lados iguais
# Equilátero: todos os lados iguais
#  Escaleno: todos os lados diferentes

s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))

if s2 + s3 > s1 and s3 + s1 > s2 and s2 + s1 > s3:
    if s1 == s2 and s3 != s1 or s2 == s3 and s3 != s1 or s3 == s1 and s3 != s2:
        print("Triângulo Isósceles")
    elif s1 == s2  == s3:
        print("Triângulo Equilátero")
    elif s1 != s2 != s3 != s1:
        print("Triângulo Escaleno")