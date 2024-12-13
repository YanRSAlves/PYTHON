s1 = "mano"
s2 = "mano"
s3 = "aura"
 
def val (s1, s2, s3):
    cont =0
    if (s1 == "mano"):
        cont = cont +1
    if (s2 == "mano"):
        cont = cont +1
    if (s3 == "mano"):
        cont = cont +1
    return cont
print(val(s1,s2,s3))